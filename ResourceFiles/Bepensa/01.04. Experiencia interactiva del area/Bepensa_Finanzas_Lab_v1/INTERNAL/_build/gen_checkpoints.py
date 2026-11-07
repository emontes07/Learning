"""Checkpoints de Excel con fórmulas: resultado de los ejercicios 2, 3 y 4."""
import os, shutil
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter
import zava_data as Z, answers as A

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_Finanzas_Lab_v1"
F1 = os.path.join(ROOT, "files", "1_Archivos_de_practica")
F2 = os.path.join(ROOT, "files", "2_Checkpoints")
os.makedirs(F2, exist_ok=True)
GREEN = "0F5F4A"
H = Font(bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor=GREEN)
T = Font(bold=True, size=13, color=GREEN); B = Font(bold=True)
MXN = '#,##0.00;[Red]-#,##0.00'; MXN0 = '#,##0;[Red]-#,##0'; PCT = '0.0%;[Red]-0.0%'
OBS, EST = "Observado", "Estimación"


def hdr(ws, row, labels, col=1):
    for j, l in enumerate(labels, col):
        c = ws.cell(row, j, l); c.font = H; c.fill = HF; c.alignment = Alignment(wrap_text=True, vertical="center")


def widths(ws, ws_w):
    for j, w in enumerate(ws_w, 1): ws.column_dimensions[get_column_letter(j)].width = w


# ------------------------------------------------------------------ Ejercicio 2
def ej2():
    src = os.path.join(F1, "Zava_Conciliacion_Banco_Ceiba_Oct2026.xlsx")
    dst = os.path.join(F2, "CHECKPOINT_Ej2_Resultado_Conciliacion.xlsx")
    wb = load_workbook(src)
    nb = wb["Estado_Cuenta"].max_row; nl = wb["Auxiliar_Bancos"].max_row
    BR, LR = f"Estado_Cuenta!$B$2:$B${nb}", f"Auxiliar_Bancos!$B$2:$B${nl}"
    BC, BA = f"Estado_Cuenta!$D$2:$D${nb}", f"Estado_Cuenta!$E$2:$E${nb}"
    LC, LA = f"Auxiliar_Bancos!$D$2:$D${nl}", f"Auxiliar_Bancos!$E$2:$E${nl}"
    for name, n, other, oc, oa, me, mc, ma in (("Cruce_Banco", nb, LR, LC, LA, BR, BC, BA), ("Cruce_Libros", nl, BR, BC, BA, LR, LC, LA)):
        ws = wb.create_sheet(name)
        srcs = "Estado_Cuenta" if name == "Cruce_Banco" else "Auxiliar_Bancos"
        ws["A1"] = f"Cruce de {'estado de cuenta contra auxiliar' if name == 'Cruce_Banco' else 'auxiliar contra estado de cuenta'} (fórmulas)"; ws["A1"].font = T
        hdr(ws, 3, ["Fecha", "Referencia", "Cargo", "Abono", "Veces en este lado", "Veces en el otro lado", "Mismo importe en el otro lado", "Estatus"])
        for i in range(2, n + 1):
            r = i + 2
            ws.cell(r, 1, f"={srcs}!A{i}").number_format = "dd/mm/yyyy"
            ws.cell(r, 2, f"={srcs}!B{i}")
            ws.cell(r, 3, f"={srcs}!D{i}").number_format = MXN
            ws.cell(r, 4, f"={srcs}!E{i}").number_format = MXN
            ws.cell(r, 5, f"=COUNTIF({me},B{r})")
            ws.cell(r, 6, f"=COUNTIF({other},B{r})")
            ws.cell(r, 7, f"=COUNTIFS({other},B{r},{oc},C{r},{oa},D{r})")
            ws.cell(r, 8, f'=IF(F{r}=0,"Sin contrapartida",IF(G{r}=0,"Importe distinto",IF(E{r}>F{r},"Repetido","Conciliado")))')
        widths(ws, [12, 20, 16, 16, 12, 12, 14, 18])
        ws.freeze_panes = "A4"
    # Partidas
    ws = wb.create_sheet("Partidas")
    ws["A1"] = "Partidas sin conciliar al 31 de octubre de 2026"; ws["A1"].font = T
    hdr(ws, 3, ["#", "Tipo", "Referencia", "Fecha", "Importe en banco", "Importe en libros", "Diferencia", "Lado que se ajusta", "Acción"])
    K = A.compute()
    items = [
        (1, "Depósito en tránsito", Z.DEP_TRANSITO["ref"], "Banco", "Ninguna en libros; verificar que el banco lo abone el 2 de noviembre."),
        (2, "Comisión bancaria no registrada", Z.COMISION["ref"], "Libros", "Registrar comisión ($16,000.00) e IVA acreditable ($2,560.00)."),
        (2, "IVA de la comisión no registrado", "IVA-" + Z.COMISION["ref"], "Libros", "Registrar junto con la comisión."),
        (3, "Cargo duplicado del banco", Z.DUPLICADO["ref"], "Banco", "Reclamar al banco el segundo cargo; registrar cuenta por cobrar al banco si no se reembolsa al cierre."),
        (4, "Error de captura (transposición)", Z.ERROR_CAPTURA["ref"], "Libros", "Corregir el registro: 457,320.00 → 475,320.00 (diferencia divisible entre 9)."),
    ]
    for k, (n, tipo, ref, lado, acc) in enumerate(items, 4):
        ws.cell(k, 1, n); ws.cell(k, 2, tipo); ws.cell(k, 3, ref)
        ws.cell(k, 4, f'=IFERROR(INDEX(Estado_Cuenta!$A$2:$A${nb},MATCH(C{k},{BR},0)),INDEX(Auxiliar_Bancos!$A$2:$A${nl},MATCH(C{k},{LR},0)))').number_format = "dd/mm/yyyy"
        ws.cell(k, 5, f"=SUMIFS({BA},{BR},C{k})-SUMIFS({BC},{BR},C{k})").number_format = MXN
        ws.cell(k, 6, f"=SUMIFS({LA},{LR},C{k})-SUMIFS({LC},{LR},C{k})").number_format = MXN
        ws.cell(k, 7, f"=E{k}-F{k}").number_format = MXN
        ws.cell(k, 8, lado); ws.cell(k, 9, acc)
    ws.cell(10, 6, "Suma de diferencias").font = B
    ws.cell(10, 7, "=SUM(G4:G8)").number_format = MXN
    ws.cell(11, 6, "Diferencia de saldos (banco − libros)").font = B
    ws.cell(11, 7, f"=Estado_Cuenta!F{nb}-Auxiliar_Bancos!F{nl}").number_format = MXN
    ws.cell(12, 6, "Comprobación (debe ser 0.00)").font = B
    ws.cell(12, 7, "=ROUND(G10-G11,2)").number_format = MXN
    widths(ws, [4, 34, 20, 12, 18, 18, 18, 16, 70])
    # Conciliacion
    ws = wb["Conciliacion"]
    ws["B3"] = f"=Estado_Cuenta!F{nb}"
    ws["B4"] = "=-Partidas!G4"
    ws["B5"] = "=-Partidas!G7"
    ws["B6"] = "=B3+B4+B5"
    ws["B8"] = f"=Auxiliar_Bancos!F{nl}"
    ws["B9"] = "=Partidas!G8"
    ws["B10"] = "=Partidas!G5+Partidas!G6"
    ws["B11"] = "=B8+B9+B10"
    ws["B13"] = "=ROUND(B6-B11,2)"
    ws["A10"] = "(−) Cargos del banco no registrados (comisión + IVA)"
    ws["A15"] = "Comprobación independiente (Cruce_Banco y Cruce_Libros): renglones que no dicen 'Conciliado'"
    ws["B15"] = '=COUNTIFS(Cruce_Banco!H4:H300,"<>Conciliado",Cruce_Banco!B4:B300,"<>")+COUNTIFS(Cruce_Libros!H4:H300,"<>Conciliado",Cruce_Libros!B4:B300,"<>")'
    for r in (3, 4, 5, 6, 8, 9, 10, 11, 13): ws.cell(r, 2).number_format = MXN
    wb.move_sheet("Conciliacion", offset=-(len(wb.sheetnames) - 2))
    wb.save(dst)
    return dst


# ------------------------------------------------------------------ Ejercicio 3
DER = "Datos_ER!${c}$2:${c}$37"
def rng(c): return DER.format(c=c)
COLS = dict(vol="E", ventas="F", azucar="G", pet="H", conc="I", otros="J", cv="K", ub="L")


def sumifs(field, esc, cedis_ref=None, canal_ref=None):
    f = f'SUMIFS({rng(COLS[field])},{rng("B")},"{esc}"'
    if cedis_ref: f += f',{rng("C")},{cedis_ref}'
    if canal_ref: f += f',{rng("D")},{canal_ref}'
    return f + ")"


def add_ej3(wb):
    # Variaciones por CEDIS
    ws = wb.create_sheet("Variaciones")
    ws["A1"] = "Variaciones de octubre 2026 por CEDIS: real contra presupuesto y contra año anterior"; ws["A1"].font = T
    hd = ["CEDIS", "Volumen real", "Volumen ppto", "Var % vol vs ppto", "Volumen AA", "Var % vol vs AA",
          "Ventas real", "Ventas ppto", "Var $ ventas vs ppto", "Var % ventas vs ppto", "Ventas AA", "Var % ventas vs AA",
          "UB real", "UB ppto", "Var $ UB vs ppto", "Margen bruto real", "Margen bruto ppto", "Distribución real", "Distribución ppto", "Var $ distribución"]
    hdr(ws, 3, hd)
    for i, c in enumerate(Z.CEDIS + ["Total"], 4):
        ws.cell(i, 1, c)
        cr = None if c == "Total" else f"$A{i}"
        if c == "Total":
            for col in "BCEGHKMNRS":
                ws[f"{col}{i}"] = f"=SUM({col}4:{col}7)"
        else:
            ws[f"B{i}"] = "=" + sumifs("vol", "Real", cr); ws[f"C{i}"] = "=" + sumifs("vol", "Presupuesto", cr)
            ws[f"E{i}"] = "=" + sumifs("vol", "Año anterior", cr)
            ws[f"G{i}"] = "=" + sumifs("ventas", "Real", cr); ws[f"H{i}"] = "=" + sumifs("ventas", "Presupuesto", cr)
            ws[f"K{i}"] = "=" + sumifs("ventas", "Año anterior", cr)
            ws[f"M{i}"] = "=" + sumifs("ub", "Real", cr); ws[f"N{i}"] = "=" + sumifs("ub", "Presupuesto", cr)
            ws[f"R{i}"] = f"=INDEX(Gastos_Distribucion!$B$2:$B$5,MATCH($A{i},Gastos_Distribucion!$A$2:$A$5,0))"
            ws[f"S{i}"] = f"=INDEX(Gastos_Distribucion!$C$2:$C$5,MATCH($A{i},Gastos_Distribucion!$A$2:$A$5,0))"
        ws[f"D{i}"] = f"=B{i}/C{i}-1"; ws[f"F{i}"] = f"=B{i}/E{i}-1"
        ws[f"I{i}"] = f"=G{i}-H{i}"; ws[f"J{i}"] = f"=G{i}/H{i}-1"; ws[f"L{i}"] = f"=G{i}/K{i}-1"
        ws[f"O{i}"] = f"=M{i}-N{i}"; ws[f"P{i}"] = f"=M{i}/G{i}"; ws[f"Q{i}"] = f"=N{i}/H{i}"; ws[f"T{i}"] = f"=R{i}-S{i}"
        for col in "BCEGHIKMNORST": ws[f"{col}{i}"].number_format = MXN0
        for col in "DFJLPQ": ws[f"{col}{i}"].number_format = PCT
    for col in range(1, 21): ws.cell(8, col).font = B
    widths(ws, [12] + [15] * 19); ws.freeze_panes = "B4"

    # Puente contra presupuesto
    ws = wb.create_sheet("Puente_Ppto")
    ws["A1"] = "Puente de ventas, costos y EBITDA: presupuesto → real (octubre 2026)"; ws["A1"].font = T
    hdr(ws, 3, ["CEDIS", "Canal", "Vol real", "Ventas real", "Vol ppto", "Ventas ppto", "Precio real", "Precio ppto", "Ventas real a precio ppto"])
    r0 = 4
    for c in Z.CEDIS:
        for ch in Z.CANALES:
            r = r0; r0 += 1
            ws.cell(r, 1, c); ws.cell(r, 2, ch)
            ws.cell(r, 3, "=" + sumifs("vol", "Real", f"$A{r}", f"$B{r}")); ws.cell(r, 4, "=" + sumifs("ventas", "Real", f"$A{r}", f"$B{r}"))
            ws.cell(r, 5, "=" + sumifs("vol", "Presupuesto", f"$A{r}", f"$B{r}")); ws.cell(r, 6, "=" + sumifs("ventas", "Presupuesto", f"$A{r}", f"$B{r}"))
            ws.cell(r, 7, f"=D{r}/C{r}"); ws.cell(r, 8, f"=F{r}/E{r}"); ws.cell(r, 9, f"=C{r}*H{r}")
            for j in (3, 4, 5, 6, 9): ws.cell(r, j).number_format = MXN0
            for j in (7, 8): ws.cell(r, j).number_format = "#,##0.00"
    tr = r0  # 16
    ws.cell(tr, 1, "Total").font = B
    for j, col in ((3, "C"), (4, "D"), (5, "E"), (6, "F"), (9, "I")):
        ws.cell(tr, j, f"=SUM({col}4:{col}{tr-1})").number_format = MXN0
    ws.cell(tr, 7, f"=D{tr}/C{tr}").number_format = "#,##0.00"; ws.cell(tr, 8, f"=F{tr}/E{tr}").number_format = "#,##0.00"
    b = tr + 3  # puente
    ws.cell(b - 1, 1, "Puente de ventas netas").font = T
    rows = [("Ventas presupuesto", f"=F{tr}"), ("Efecto volumen", f"=(C{tr}-E{tr})*H{tr}"), ("Efecto mezcla", f"=I{tr}-C{tr}*H{tr}"),
            ("Efecto precio", f"=D{tr}-I{tr}"), ("Ventas real", f"=SUM(B{b}:B{b+3})"), ("Comprobación (real − Datos_ER, debe ser 0)", f"=ROUND(B{b+4}-D{tr},2)")]
    P = {}
    for k, (l, f) in enumerate(rows):
        ws.cell(b + k, 1, l); ws.cell(b + k, 2, f).number_format = MXN0; P[l] = f"Puente_Ppto!B{b+k}"
    c0 = b + 8
    ws.cell(c0 - 1, 1, "Puente de costo de ventas (por insumo)").font = T
    hdr(ws, c0, ["Insumo", "Costo ppto", "Costo real", "Efecto volumen", "Efecto costo unitario", "Var total", "Costo/CU ppto", "Costo/CU real", "Var % costo/CU"])
    for k, (m, name) in enumerate((("azucar", "Azúcar"), ("pet", "PET"), ("conc", "Concentrado"), ("otros", "Otros costos de producción")), c0 + 1):
        ws.cell(k, 1, name)
        ws.cell(k, 2, "=" + sumifs(m, "Presupuesto")); ws.cell(k, 3, "=" + sumifs(m, "Real"))
        ws.cell(k, 4, f"=(C{tr}-E{tr})*B{k}/E{tr}"); ws.cell(k, 5, f"=C{k}-C{tr}*B{k}/E{tr}"); ws.cell(k, 6, f"=C{k}-B{k}")
        ws.cell(k, 7, f"=B{k}/E{tr}"); ws.cell(k, 8, f"=C{k}/C{tr}"); ws.cell(k, 9, f"=H{k}/G{k}-1")
        for j in (2, 3, 4, 5, 6): ws.cell(k, j).number_format = MXN0
        for j in (7, 8): ws.cell(k, j).number_format = "#,##0.00"
        ws.cell(k, 9).number_format = PCT
        P[f"cu_{m}"] = f"Puente_Ppto!I{k}"; P[f"tar_{m}"] = f"Puente_Ppto!E{k}"
    ct = c0 + 5
    ws.cell(ct, 1, "Total").font = B
    for j in (2, 3, 4, 5, 6): ws.cell(ct, j, f"=SUM({get_column_letter(j)}{c0+1}:{get_column_letter(j)}{c0+4})").number_format = MXN0
    P["cost_vol"], P["cost_tar"], P["cost_var"] = f"Puente_Ppto!D{ct}", f"Puente_Ppto!E{ct}", f"Puente_Ppto!F{ct}"
    e0 = ct + 3
    ws.cell(e0 - 1, 1, "Puente de EBITDA: presupuesto → real ajustado").font = T
    erows = [("EBITDA presupuesto", f"=F{tr}-B{c0+5}-SUM(Gastos_Distribucion!C2:C5)-SUM(Gastos_Corporativos!C2:C4)"),
             ("Variación de ventas netas", f"=B{b+4}-B{b}"),
             ("Variación de costo de ventas (más costo = negativo)", f"=-F{ct}"),
             ("Variación de gastos de distribución", "=-(SUM(Gastos_Distribucion!B2:B5)-SUM(Gastos_Distribucion!C2:C5))"),
             ("Variación de gastos corporativos (preliminar)", "=-(SUM(Gastos_Corporativos!B2:B4)-SUM(Gastos_Corporativos!C2:C4))"),
             ("EBITDA real preliminar", f"=SUM(B{e0}:B{e0+4})"),
             ("Ajuste de conciliación: comisión bancaria no registrada", f"=-{Z.COMISION['importe']:.0f}"),
             ("EBITDA real ajustado", f"=B{e0+5}+B{e0+6}"),
             ("Var % EBITDA ajustado vs presupuesto", f"=B{e0+7}/B{e0}-1")]
    for k, (l, f) in enumerate(erows):
        ws.cell(e0 + k, 1, l); ws.cell(e0 + k, 2, f).number_format = PCT if "%" in l else MXN0
        P[l] = f"Puente_Ppto!B{e0+k}"
    widths(ws, [52, 18, 16, 16, 18, 18, 14, 14, 18])
    return P


def hechos(wb, P, with_forecast=False, F=None):
    ws = wb.create_sheet("Hechos_del_cierre")
    ws["A1"] = "Hechos del cierre · octubre 2026 · cada cifra con su fuente"; ws["A1"].font = T
    ws["A2"] = "Regla: nada entra a la presentación del Consejo si no está en esta hoja. Observado = sale de los datos; Estimación = pronóstico o escenario."
    hdr(ws, 4, ["#", "Hecho", "Cifra", "Unidad", "Fuente (archivo, hoja y celda o cálculo)", "Tipo", "Revisado por"])
    V = "Variaciones"
    rows = [
        ("Ventas netas reales de octubre", f"={V}!G8", "MXN", "Zava_Cierre_Oct2026 · Variaciones!G8 (suma de Datos_ER)", OBS, MXN0),
        ("Variación de ventas contra presupuesto", f"={V}!I8", "MXN", "Variaciones!I8", OBS, MXN0),
        ("Variación % de ventas contra presupuesto", f"={V}!J8", "%", "Variaciones!J8", OBS, PCT),
        ("Variación % de ventas contra año anterior", f"={V}!L8", "%", "Variaciones!L8", OBS, PCT),
        ("Volumen real de octubre", f"={V}!B8", "CU", "Variaciones!B8", OBS, MXN0),
        ("Variación % de volumen contra presupuesto", f"={V}!D8", "%", "Variaciones!D8", OBS, PCT),
        ("Variación % de volumen contra año anterior", f"={V}!F8", "%", "Variaciones!F8", OBS, PCT),
        ("Efecto volumen en ventas (vs presupuesto)", "=" + P["Efecto volumen"], "MXN", P["Efecto volumen"], OBS, MXN0),
        ("Efecto mezcla en ventas (vs presupuesto)", "=" + P["Efecto mezcla"], "MXN", P["Efecto mezcla"], OBS, MXN0),
        ("Efecto precio en ventas (vs presupuesto)", "=" + P["Efecto precio"], "MXN", P["Efecto precio"], OBS, MXN0),
        ("Variación % del costo de azúcar por CU vs presupuesto", "=" + P["cu_azucar"], "%", P["cu_azucar"], OBS, PCT),
        ("Efecto costo unitario del azúcar en costo de ventas", "=" + P["tar_azucar"], "MXN", P["tar_azucar"], OBS, MXN0),
        ("Margen bruto real", f"={V}!P8", "%", "Variaciones!P8", OBS, PCT),
        ("Margen bruto presupuesto", f"={V}!Q8", "%", "Variaciones!Q8", OBS, PCT),
        ("Volumen Golfo: variación % vs presupuesto", f"={V}!D6", "%", "Variaciones!D6", OBS, PCT),
        ("Distribución Golfo: variación vs presupuesto", f"={V}!T6", "MXN", "Variaciones!T6", OBS, MXN0),
        ("EBITDA real preliminar", "=" + P["EBITDA real preliminar"], "MXN", P["EBITDA real preliminar"], OBS, MXN0),
        ("Ajuste de conciliación (comisión bancaria no registrada)", "=" + P["Ajuste de conciliación: comisión bancaria no registrada"], "MXN", "Conciliación Banco Ceiba · Partidas (Ejercicio 2)", OBS, MXN0),
        ("EBITDA real ajustado", "=" + P["EBITDA real ajustado"], "MXN", P["EBITDA real ajustado"], OBS, MXN0),
        ("EBITDA presupuesto", "=" + P["EBITDA presupuesto"], "MXN", P["EBITDA presupuesto"], OBS, MXN0),
        ("Variación % EBITDA ajustado vs presupuesto", "=" + P["Var % EBITDA ajustado vs presupuesto"], "%", P["Var % EBITDA ajustado vs presupuesto"], OBS, PCT),
        ("Posición de caja al 30 de octubre (3 bancos)", A.compute()["caja_total"], "MXN", "Zava_Flujo_Caja_Diario_Oct2026 · Movimientos (Saldo_final al 30/10)", OBS, MXN),
        ("Cargo duplicado por reclamar a Banco Ceiba", Z.DUPLICADO["importe"], "MXN", "Conciliación Banco Ceiba · Partidas (Ejercicio 2)", OBS, MXN),
        ("Diferencia de conciliación explicada (banco vs libros)", A.compute()["conc_diferencia_inicial"], "MXN", "Conciliación Banco Ceiba · Partidas!G10", OBS, MXN),
    ]
    if with_forecast:
        rows += [
            ("Volumen atípico Golfo julio 2026 (excluido de la tendencia)", "=" + F["atipico"], "CU", F["atipico"], OBS, MXN0),
            ("Crecimiento de volumen ene–oct 2026 vs 2025, sin el atípico", "=" + F["g_total"], "%", F["g_total"], EST, PCT),
            ("Pronóstico de volumen 4T 2026 (oct real + nov y dic estimados)", "=" + F["q4_vol"], "CU", F["q4_vol"], EST, MXN0),
            ("Pronóstico de ventas netas 4T 2026", "=" + F["q4_ventas"], "MXN", F["q4_ventas"], EST, MXN0),
            ("Pronóstico de ventas 4T vs presupuesto 4T", "=" + F["q4_vs_pp"], "%", F["q4_vs_pp"], EST, PCT),
            ("Escenario azúcar +10 %: impacto en utilidad bruta nov–dic", "=" + F["esc_az"], "MXN", F["esc_az"], EST, MXN0),
            ("Escenario tipo de cambio +1.00: impacto en utilidad bruta nov–dic", "=" + F["esc_tc"], "MXN", F["esc_tc"], EST, MXN0),
            ("Escenario combinado: impacto en utilidad bruta nov–dic", "=" + F["esc_comb"], "MXN", F["esc_comb"], EST, MXN0),
        ]
    for k, (h, f, u, src, tipo, nf) in enumerate(rows, 5):
        ws.cell(k, 1, k - 4); ws.cell(k, 2, h); c = ws.cell(k, 3, f); c.number_format = nf
        ws.cell(k, 4, u); ws.cell(k, 5, src); ws.cell(k, 6, tipo)
        if tipo == EST: ws.cell(k, 6).font = Font(bold=True, color="B4530F")
    widths(ws, [4, 62, 18, 8, 62, 12, 14]); ws.freeze_panes = "A5"
    return ws


def ej3():
    src = os.path.join(F1, "Zava_Cierre_Oct2026.xlsx")
    dst = os.path.join(F2, "CHECKPOINT_Ej3_Resultado_Cierre.xlsx")
    wb = load_workbook(src); P = add_ej3(wb); hechos(wb, P); wb.save(dst); return dst


# ------------------------------------------------------------------ Ejercicio 4
def add_ej4(wb):
    ws = wb.create_sheet("Pronostico")
    ws["A1"] = "Pronóstico del 4T 2026 por CEDIS (Estimación, salvo octubre real)"; ws["A1"].font = T
    ws["A2"] = "Método: julio 2026 de Golfo se reemplaza por el promedio de junio y agosto 2026. Crecimiento = ene–oct 2026 / ene–oct 2025 − 1. Nov y dic 2026 = mismo mes 2025 × (1 + crecimiento)."
    HV = "Historico_Volumen"
    hdr(ws, 4, ["CEDIS", "Ene–oct 2025", "Ene–oct 2026 sin ajuste", "Ajuste atípico", "Ene–oct 2026 ajustado", "Crecimiento ajustado", "Nov 2025", "Dic 2025",
                "Nov 2026 (Est.)", "Dic 2026 (Est.)", "Oct 2026 real", "4T volumen (Est.)", "Precio oct real", "Ventas nov–dic (Est.)", "4T ventas (Est.)",
                "4T volumen ppto", "4T ventas ppto"])
    cols = {c: get_column_letter(2 + i) for i, c in enumerate(Z.CEDIS)}
    for i, c in enumerate(Z.CEDIS, 5):
        L = cols[c]
        ws[f"A{i}"] = c
        ws[f"B{i}"] = f"=SUM({HV}!{L}2:{L}11)"
        ws[f"C{i}"] = f"=SUM({HV}!{L}14:{L}23)"
        ws[f"D{i}"] = f"=ROUND(AVERAGE({HV}!{L}19,{HV}!{L}21),0)-{HV}!{L}20" if c == Z.OUTLIER["cedis"] else 0
        ws[f"E{i}"] = f"=C{i}+D{i}"
        ws[f"F{i}"] = f"=E{i}/B{i}-1"
        ws[f"G{i}"] = f"={HV}!{L}12"; ws[f"H{i}"] = f"={HV}!{L}13"
        ws[f"I{i}"] = f"=ROUND(G{i}*(1+F{i}),0)"; ws[f"J{i}"] = f"=ROUND(H{i}*(1+F{i}),0)"
        ws[f"K{i}"] = f"={HV}!{L}23"
        ws[f"L{i}"] = f"=I{i}+J{i}+K{i}"
        ws[f"M{i}"] = f'=INDEX(Supuestos_Forecast!$B$2:$B$13,MATCH("*· {c}",Supuestos_Forecast!$A$2:$A$13,0))'
        ws[f"N{i}"] = f"=(I{i}+J{i})*M{i}"
        ws[f"O{i}"] = f'=N{i}+SUMIFS(Datos_ER!$F$2:$F$37,Datos_ER!$B$2:$B$37,"Real",Datos_ER!$C$2:$C$37,A{i})'
        ws[f"P{i}"] = f'=SUMIFS(Presupuesto_NovDic!$C$2:$C$9,Presupuesto_NovDic!$B$2:$B$9,A{i})+SUMIFS(Datos_ER!$E$2:$E$37,Datos_ER!$B$2:$B$37,"Presupuesto",Datos_ER!$C$2:$C$37,A{i})'
        ws[f"Q{i}"] = f'=SUMIFS(Presupuesto_NovDic!$D$2:$D$9,Presupuesto_NovDic!$B$2:$B$9,A{i})+SUMIFS(Datos_ER!$F$2:$F$37,Datos_ER!$B$2:$B$37,"Presupuesto",Datos_ER!$C$2:$C$37,A{i})'
    ws["A9"] = "Total"; ws["A9"].font = B
    for col in "BCDEGHIJKLNOPQ": ws[f"{col}9"] = f"=SUM({col}5:{col}8)"
    ws["F9"] = "=E9/B9-1"
    for r in range(5, 10):
        for col in "BCDEGHIJKLNOPQ": ws[f"{col}{r}"].number_format = MXN0
        ws[f"F{r}"].number_format = PCT; ws[f"M{r}"].number_format = "#,##0.00"
    ws["A11"] = "Crecimiento ene–oct sin ajustar (con el atípico)"; ws["B11"] = "=C9/B9-1"; ws["B11"].number_format = PCT
    ws["A12"] = "4T ventas pronóstico vs presupuesto"; ws["B12"] = "=O9/Q9-1"; ws["B12"].number_format = PCT
    ws["A13"] = "4T volumen pronóstico vs presupuesto"; ws["B13"] = "=L9/P9-1"; ws["B13"].number_format = PCT
    ws["A14"] = "Volumen atípico Golfo julio 2026"; ws["B14"] = f"={HV}!{cols['Golfo']}20"; ws["B14"].number_format = MXN0
    ws["A15"] = "Utilidad bruta nov–dic (Est., costo/CU real de octubre)"; ws["B15"] = "=N9-(I9+J9)*(Supuestos_Forecast!B2+Supuestos_Forecast!B3+Supuestos_Forecast!B4*Supuestos_Forecast!B5+Supuestos_Forecast!B6)"; ws["B15"].number_format = MXN0
    widths(ws, [12] + [15] * 16); ws.freeze_panes = "B5"
    ws2 = wb.create_sheet("Escenarios")
    ws2["A1"] = "Escenarios sobre la utilidad bruta de noviembre y diciembre 2026 (Estimación)"; ws2["A1"].font = T
    hdr(ws2, 3, ["Escenario", "Cambio en costo por CU", "Volumen nov–dic (Est.)", "Impacto en utilidad bruta", "Utilidad bruta nov–dic resultante", "Impacto %"])
    S = "Supuestos_Forecast"
    sc = [("Base", "=0"), ("Azúcar +10 %", f"={S}!B2*{S}!B8"),
          ("Tipo de cambio +1.00 MXN/USD", f"={S}!B4*{S}!B9+{S}!B3*{S}!B7*{S}!B9/{S}!B5")]
    for k, (n, f) in enumerate(sc, 4):
        ws2.cell(k, 1, n); ws2.cell(k, 2, f).number_format = "#,##0.0000"
        ws2.cell(k, 3, "=Pronostico!I9+Pronostico!J9").number_format = MXN0
        ws2.cell(k, 4, f"=-B{k}*C{k}").number_format = MXN0
        ws2.cell(k, 5, f"=Pronostico!B15+D{k}").number_format = MXN0
        ws2.cell(k, 6, f"=D{k}/Pronostico!B15").number_format = PCT
    ws2.cell(7, 1, "Combinado (azúcar + tipo de cambio)"); ws2.cell(7, 2, "=B5+B6").number_format = "#,##0.0000"
    ws2.cell(7, 3, "=Pronostico!I9+Pronostico!J9").number_format = MXN0
    ws2.cell(7, 4, "=D5+D6").number_format = MXN0; ws2.cell(7, 5, "=Pronostico!B15+D7").number_format = MXN0; ws2.cell(7, 6, "=D7/Pronostico!B15").number_format = PCT
    ws2["A9"] = "PET: sólo la proporción ligada al dólar cambia con el tipo de cambio. Concentrado: 100 % en dólares."
    widths(ws2, [38, 22, 22, 24, 30, 12])
    return dict(atipico="Pronostico!B14", g_total="Pronostico!F9", q4_vol="Pronostico!L9", q4_ventas="Pronostico!O9", q4_vs_pp="Pronostico!B12",
                esc_az="Escenarios!D5", esc_tc="Escenarios!D6", esc_comb="Escenarios!D7")


def ej4():
    src = os.path.join(F1, "Zava_Cierre_Oct2026.xlsx")
    dst = os.path.join(F2, "CHECKPOINT_Ej4_Resultado_Forecast.xlsx")
    wb = load_workbook(src); P = add_ej3(wb); F = add_ej4(wb); hechos(wb, P, True, F); wb.save(dst); return dst


if __name__ == "__main__":
    print(ej2(), ej3(), ej4())
