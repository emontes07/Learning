"""Genera los archivos de práctica (files/1_Archivos_de_practica)."""
import os, csv, json, datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
import zava_data as Z, answers as A

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_Finanzas_Lab_v1"
F1 = os.path.join(ROOT, "files", "1_Archivos_de_practica")
os.makedirs(F1, exist_ok=True)
GREEN, LIME = "0F5F4A", "E8F3D6"
HFONT = Font(bold=True, color="FFFFFF"); HFILL = PatternFill("solid", fgColor=GREEN)
NOTE = Font(italic=True, color="555555")
MXN = '#,##0.00;[Red]-#,##0.00'; MXN0 = '#,##0;[Red]-#,##0'; DATE = 'dd/mm/yyyy'


def sheet_table(ws, name, headers, rows, fmts=None, start_row=1, widths=None):
    for j, h in enumerate(headers, 1):
        c = ws.cell(start_row, j, h); c.font = HFONT; c.fill = HFILL; c.alignment = Alignment(wrap_text=True, vertical="center")
    for i, r in enumerate(rows, start_row + 1):
        for j, v in enumerate(r, 1):
            c = ws.cell(i, j, v)
            if fmts and fmts[j - 1]: c.number_format = fmts[j - 1]
    ref = f"A{start_row}:{get_column_letter(len(headers))}{start_row + len(rows)}"
    t = Table(displayName=name, ref=ref); t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium7", showRowStripes=True)
    ws.add_table(t)
    for j, h in enumerate(headers, 1):
        ws.column_dimensions[get_column_letter(j)].width = (widths[j - 1] if widths else max(12, min(40, len(str(h)) + 4)))
    ws.freeze_panes = ws.cell(start_row + 1, 1)


def leeme(ws, title, lines):
    ws["A1"] = title; ws["A1"].font = Font(bold=True, size=14, color=GREEN)
    for i, l in enumerate(lines, 3):
        ws.cell(i, 1, l).alignment = Alignment(wrap_text=True, vertical="top")
    ws.column_dimensions["A"].width = 120


def cash_book(D, path):
    wb = Workbook(); ws = wb.active; ws.title = "Leeme"
    leeme(ws, "Zava Bebidas · Flujo de caja diario · octubre 2026 (datos ficticios)", [
        "Fuente: banca electrónica de los tres bancos. Saldos al cierre de cada día hábil, en pesos (MXN).",
        "Movimientos: un renglón por banco y día hábil del 1 al 30 de octubre de 2026.",
        "Proyeccion_Nov: flujo proyectado del 2 al 13 de noviembre de 2026 (incluye pagos programados y traspasos planeados).",
        "Parametros: saldo mínimo operativo por banco y línea de crédito disponible.",
        "KPIs: cobranza contra meta, DSO por canal, DPO y días de inventario de julio a octubre de 2026.",
        "Banco Ceiba es la cuenta concentradora (cobranza); Banco Coral paga proveedores; Banco Jade paga nómina e impuestos.",
        "Empresa, bancos, proveedores y cifras son ficticios.",
    ])
    ws = wb.create_sheet("Movimientos")
    cols = ["Fecha", "Banco", "Saldo_inicial", "Cobranza", "Traspasos_recibidos", "Otros_ingresos", "Pagos_proveedores", "Nomina", "Impuestos", "Traspasos_enviados", "Comisiones", "Saldo_final"]
    rows = [[r[c] for c in cols] for r in sorted(D["cash"], key=lambda r: (r["Fecha"], Z.BANCOS.index(r["Banco"])))]
    sheet_table(ws, "tblMovimientos", cols, rows, [DATE, None] + [MXN] * 10, widths=[12, 14] + [16] * 10)
    ws = wb.create_sheet("Proyeccion_Nov")
    pc = ["Fecha", "Banco", "Saldo_inicial", "Cobranza_esperada", "Traspasos", "Pagos_programados", "Nomina", "Impuestos", "Saldo_final"]
    rows = [[r[c] for c in pc] for r in sorted(D["proj"], key=lambda r: (r["Fecha"], Z.BANCOS.index(r["Banco"])))]
    sheet_table(ws, "tblProyeccion", pc, rows, [DATE, None] + [MXN] * 7, widths=[12, 14] + [18] * 7)
    ws.cell(len(rows) + 3, 1, "Traspasos: positivo = entra al banco; negativo = sale. El 12 de noviembre Banco Coral paga la quincena de azúcar.").font = NOTE
    ws = wb.create_sheet("Parametros")
    sheet_table(ws, "tblParametros", ["Banco", "Uso", "Saldo_minimo"], [
        ["Banco Ceiba", "Concentradora de cobranza", Z.MINIMO["Banco Ceiba"]],
        ["Banco Coral", "Pagos a proveedores", Z.MINIMO["Banco Coral"]],
        ["Banco Jade", "Nómina e impuestos", Z.MINIMO["Banco Jade"]]], [None, None, MXN0], widths=[16, 30, 18])
    ws["E1"] = "Línea de crédito revolvente disponible (no dispuesta)"; ws["E2"] = Z.LINEA_CREDITO; ws["E2"].number_format = MXN0
    ws.column_dimensions["E"].width = 48
    ws = wb.create_sheet("KPIs")
    K = A.compute(D)
    kr = []
    for m, real, meta, dso, dt_, dm, dc, dpo, inv in Z.KPIS:
        if m == "2026-10": real, meta = K["cobranza_oct_real"], K["cobranza_oct_meta"]
        kr.append([m, real, meta, dso, dt_, dm, dc, dpo, inv])
    sheet_table(ws, "tblKPIs", ["Mes", "Cobranza_real", "Cobranza_meta", "DSO_total", "DSO_Tradicional", "DSO_Moderno", "DSO_Consumo_en_sitio", "DPO", "Dias_inventario"],
                kr, [None, MXN0, MXN0] + ["0.0"] * 6, widths=[10, 18, 18, 12, 16, 14, 22, 10, 16])
    wb.save(path)


def bank_files(D, csv_path, xlsx_path):
    bank = Z.running(D["bank"], Z.SALDO_INICIAL_CEIBA)
    books = Z.running(D["books"], Z.SALDO_INICIAL_CEIBA)
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["Fecha", "Referencia", "Concepto", "Cargo", "Abono", "Saldo"])
        for r in bank:
            w.writerow([r[0].strftime("%d/%m/%Y"), r[1], r[2], f"{r[3]:.2f}", f"{r[4]:.2f}", f"{r[5]:.2f}"])
    wb = Workbook(); ws = wb.active; ws.title = "Leeme"
    leeme(ws, "Zava Bebidas · Conciliación bancaria Banco Ceiba · octubre 2026 (datos ficticios)", [
        "Cuenta: Banco Ceiba, cuenta concentradora de cobranza (terminación 4471, ficticia).",
        f"Saldo inicial al 1 de octubre de 2026 (conciliado en septiembre, sin partidas pendientes): {Z.SALDO_INICIAL_CEIBA:,.2f}.",
        "Estado_Cuenta: movimientos según el banco (misma información que el archivo CSV del banco).",
        "Auxiliar_Bancos: movimientos registrados en contabilidad (libro auxiliar de bancos).",
        "Cada movimiento tiene una Referencia única que usan el banco y contabilidad.",
        "Conciliacion: formato para completar. Las partidas sin conciliar se buscan en el Ejercicio 2.",
    ])
    ws = wb.create_sheet("Estado_Cuenta")
    sheet_table(ws, "tblBanco", ["Fecha", "Referencia", "Concepto", "Cargo", "Abono", "Saldo"],
                [r[:6] for r in bank], [DATE, None, None, MXN, MXN, MXN], widths=[12, 20, 58, 16, 16, 18])
    ws = wb.create_sheet("Auxiliar_Bancos")
    sheet_table(ws, "tblLibros", ["Fecha", "Referencia", "Concepto", "Cargo", "Abono", "Saldo"],
                [r[:6] for r in books], [DATE, None, None, MXN, MXN, MXN], widths=[12, 20, 58, 16, 16, 18])
    ws = wb.create_sheet("Conciliacion")
    ws["A1"] = "Conciliación bancaria Banco Ceiba al 31 de octubre de 2026"; ws["A1"].font = Font(bold=True, size=13, color=GREEN)
    lines = ["Saldo según estado de cuenta", "(+) Depósitos en tránsito", "(+) Cargos del banco por aclarar", "Saldo ajustado según banco", "",
             "Saldo según libros (auxiliar)", "(+) Abonos del banco no registrados / correcciones", "(−) Cargos del banco no registrados", "Saldo ajustado según libros", "", "Diferencia (debe ser 0.00)"]
    for i, l in enumerate(lines, 3):
        ws.cell(i, 1, l); ws.cell(i, 2).number_format = MXN
    ws.column_dimensions["A"].width = 52; ws.column_dimensions["B"].width = 20
    wb.save(xlsx_path)


def pl_book(D, path):
    pl = D["pl"]; K = A.compute(D)
    wb = Workbook(); ws = wb.active; ws.title = "Leeme"
    leeme(ws, "Zava Bebidas · Cierre de octubre 2026 y supuestos de forecast (datos ficticios)", [
        "Empresa ficticia: embotelladora regional con 4 CEDIS (Norte, Centro, Golfo, Península) y 3 canales (Tradicional, Moderno, Consumo en sitio).",
        "Volumen en cajas unidad (CU). Importes en pesos mexicanos (MXN).",
        "Datos_ER: un renglón por Escenario (Real, Presupuesto, Año anterior) × CEDIS × Canal. Real y Presupuesto son octubre 2026; Año anterior es octubre 2025.",
        "Costo_ventas = Costo_azucar + Costo_PET + Costo_concentrado + Otros_costos_produccion. Utilidad_bruta = Ventas_netas − Costo_ventas.",
        "Precio promedio por CU = Ventas_netas / Volumen_CU (calcúlalo sobre los totales; no promedies precios).",
        "Gastos_Distribucion: por CEDIS y escenario. Gastos_Corporativos: por concepto y escenario. Las cifras Real son PRELIMINARES: faltan los ajustes de la conciliación bancaria.",
        "EBITDA = Utilidad bruta − Gastos de distribución − Gastos corporativos.",
        "Historico_Volumen: volumen mensual por CEDIS de enero 2025 a octubre 2026 (octubre 2025 y octubre 2026 coinciden con Datos_ER).",
        "Supuestos_Forecast: costos unitarios reales de octubre, tipo de cambio y parámetros de escenarios. Presupuesto_NovDic: presupuesto de volumen y ventas de noviembre y diciembre 2026.",
    ])
    ws = wb.create_sheet("Datos_ER")
    cols = ["Mes", "Escenario", "CEDIS", "Canal", "Volumen_CU", "Ventas_netas", "Costo_azucar", "Costo_PET", "Costo_concentrado", "Otros_costos_produccion", "Costo_ventas", "Utilidad_bruta"]
    sheet_table(ws, "tblDatosER", cols, [[r[c] for c in cols] for r in pl], [None] * 4 + [MXN0] * 8, widths=[10, 14, 12, 18] + [17] * 8)
    ws = wb.create_sheet("Gastos_Distribucion")
    sheet_table(ws, "tblDistribucion", ["CEDIS", "Real", "Presupuesto", "Año anterior"],
                [[c] + [Z.DIST[e][c] for e in Z.ESC] for c in Z.CEDIS], [None, MXN0, MXN0, MXN0], widths=[14, 16, 16, 16])
    ws = wb.create_sheet("Gastos_Corporativos")
    sheet_table(ws, "tblCorporativos", ["Concepto", "Real", "Presupuesto", "Año anterior"],
                [[k] + [v[e] for e in Z.ESC] for k, v in Z.CORP.items()], [None, MXN0, MXN0, MXN0], widths=[36, 16, 16, 16])
    ws.cell(6, 1, "Real = preliminar (antes de ajustes de la conciliación bancaria de octubre).").font = NOTE
    ws = wb.create_sheet("Historico_Volumen")
    meses = [f"2025-{m:02d}" for m in range(1, 13)] + [f"2026-{m:02d}" for m in range(1, 11)]
    sheet_table(ws, "tblHistorico", ["Mes"] + Z.CEDIS, [[m] + [D["hist"][(c, m)] for c in Z.CEDIS] for m in meses], [None] + [MXN0] * 4, widths=[10, 14, 14, 14, 14])
    ws = wb.create_sheet("Supuestos_Forecast")
    u = Z.UC["Real"]
    srows = [
        ["Costo azúcar por CU (real octubre)", u["azucar"], "MXN/CU", "Observado"],
        ["Costo PET por CU (real octubre)", u["pet"], "MXN/CU", "Observado"],
        ["Concentrado por CU", u["conc_usd"], "USD/CU", "Observado"],
        ["Tipo de cambio promedio octubre", u["tc"], "MXN por USD", "Observado"],
        ["Otros costos de producción por CU (real octubre)", u["otros"], "MXN/CU", "Observado"],
        ["Proporción del costo de PET ligada al dólar", Z.PET_USD_SHARE, "proporción", "Supuesto"],
        ["Escenario: aumento del precio del azúcar", Z.ESC_AZUCAR, "proporción", "Supuesto"],
        ["Escenario: aumento del tipo de cambio", Z.TC_SHOCK, "MXN por USD", "Supuesto"],
    ]
    for c in Z.CEDIS:
        srows.append([f"Precio promedio por CU real octubre · {c}", K[f"precio_oct_{c}"], "MXN/CU", "Observado"])
    sheet_table(ws, "tblSupuestos", ["Supuesto", "Valor", "Unidad", "Tipo"], srows, [None, "#,##0.00##", None, None], widths=[52, 14, 14, 12])
    ws.cell(len(srows) + 3, 1, "El concentrado se paga en dólares: costo MXN/CU = USD/CU × tipo de cambio.").font = NOTE
    ws = wb.create_sheet("Presupuesto_NovDic")
    prow = []
    for m in (11, 12):
        for c in Z.CEDIS:
            prow.append([f"2026-{m:02d}", c, K[f"pp_vol_{c}_{m}"], K[f"pp_ventas_{c}_{m}"]])
    sheet_table(ws, "tblPptoNovDic", ["Mes", "CEDIS", "Volumen_CU", "Ventas_netas"], prow, [None, None, MXN0, MXN0], widths=[10, 14, 16, 18])
    wb.save(path)


def main():
    D = Z.build_all(); K = A.compute(D)
    json.dump({k: v for k, v in K.items()}, open(os.path.join(ROOT, "_build", "answer_key.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=str)
    cash_book(D, os.path.join(F1, "Zava_Flujo_Caja_Diario_Oct2026.xlsx"))
    bank_files(D, os.path.join(F1, "Zava_Estado_Cuenta_Banco_Ceiba_Oct2026.csv"), os.path.join(F1, "Zava_Conciliacion_Banco_Ceiba_Oct2026.xlsx"))
    pl_book(D, os.path.join(F1, "Zava_Cierre_Oct2026.xlsx"))
    print("ok")


if __name__ == "__main__":
    main()
