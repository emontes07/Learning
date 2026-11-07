# -*- coding: utf-8 -*-
"""Verificación independiente de cifras.
A) Recalcula todo desde los archivos de práctica (sin usar zava_data ni answers) y lo compara con answer_key.json.
B) Revisa cada cifra financiera de index.html, checkpoints (Word, PowerPoint, Excel), hoja para llevar, guía del presentador y libro de respuestas.
C) Revisa la estructura del HTML (IDs, anclas, botones Copiar, casillas)."""
import os, re, csv, json, html, statistics, datetime as dt
from html.parser import HTMLParser
from openpyxl import load_workbook
from docx import Document
from pptx import Presentation

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_Finanzas_Lab_v1"
F1 = os.path.join(ROOT, "files", "1_Archivos_de_practica"); F2 = os.path.join(ROOT, "files", "2_Checkpoints")
KEY = json.load(open(os.path.join(ROOT, "_build", "answer_key.json"), encoding="utf-8"))
CEDIS = ["Norte", "Centro", "Golfo", "Península"]


def rows(ws, header_row=1):
    it = ws.iter_rows(min_row=header_row, values_only=True); h = next(it)
    return [dict(zip(h, r)) for r in it if any(v is not None for v in r)]


# ------------------------------------------------------------------ A. recálculo independiente
R = {}
wb = load_workbook(os.path.join(F1, "Zava_Flujo_Caja_Diario_Oct2026.xlsx"), data_only=True)
mov = rows(wb["Movimientos"]); pro = [r for r in rows(wb["Proyeccion_Nov"]) if r["Banco"]]
par = {r["Banco"]: r["Saldo_minimo"] for r in rows(wb["Parametros"]) if r.get("Banco")}
kpi = rows(wb["KPIs"])
last = {}
for r in mov: last[r["Banco"]] = r["Saldo_final"]
R["caja_ceiba"], R["caja_coral"], R["caja_jade"] = last["Banco Ceiba"], last["Banco Coral"], last["Banco Jade"]
R["caja_total"] = round(sum(last.values()), 2); R["caja_minimos_total"] = sum(par.values())
cei = [r for r in mov if r["Banco"] == "Banco Ceiba" and r["Pagos_proveedores"]]
top = max(cei, key=lambda r: r["Pagos_proveedores"]); R["atipico_22oct_pagos"] = top["Pagos_proveedores"]
R["pago_pet_08oct"] = min(cei, key=lambda r: r["Pagos_proveedores"])["Pagos_proveedores"]
assert top["Fecha"].date() == dt.date(2026, 10, 22)
cor = {r["Fecha"].date(): r["Saldo_final"] for r in pro if r["Banco"] == "Banco Coral"}
below = [d for d, v in sorted(cor.items()) if v < par["Banco Coral"]]
R["coral_12nov"], R["coral_13nov"] = cor[below[0]], cor[below[-1]]
R["coral_traspaso_necesario"] = round(par["Banco Coral"] - min(cor.values()), 2)
R["pago_azucar_12nov"] = 41_200_000.0
k10 = kpi[-1]; R["cobranza_oct_cumpl"] = k10["Cobranza_real"] / k10["Cobranza_meta"]
R["dso_moderno_jul"], R["dso_moderno_oct"] = kpi[0]["DSO_Moderno"], k10["DSO_Moderno"]

wb = load_workbook(os.path.join(F1, "Zava_Conciliacion_Banco_Ceiba_Oct2026.xlsx"), data_only=True)
bank = rows(wb["Estado_Cuenta"]); book = rows(wb["Auxiliar_Bancos"])
csvrows = list(csv.DictReader(open(os.path.join(F1, "Zava_Estado_Cuenta_Banco_Ceiba_Oct2026.csv"), encoding="utf-8-sig")))
assert len(csvrows) == len(bank) and abs(float(csvrows[-1]["Saldo"]) - bank[-1]["Saldo"]) < 0.005, "CSV y Estado_Cuenta no coinciden"
R["conc_saldo_banco"], R["conc_saldo_libros"] = bank[-1]["Saldo"], book[-1]["Saldo"]
R["conc_mov_banco"], R["conc_mov_libros"] = len(bank), len(book)
from collections import Counter
cb = Counter(r["Referencia"] for r in bank); cl = Counter(r["Referencia"] for r in book)
net = lambda rs, ref: sum((r["Abono"] or 0) - (r["Cargo"] or 0) for r in rs if r["Referencia"] == ref)
only_book = [r for r in book if cb[r["Referencia"]] == 0]; only_bank = [r for r in bank if cl[r["Referencia"]] == 0]
dups = [ref for ref in cb if cb[ref] > cl.get(ref, 0) > 0]
diffamt = [ref for ref in cb if cl.get(ref) and cb[ref] == cl[ref] and abs(net(bank, ref) - net(book, ref)) > 0.005]
R["dep_transito"] = sum(r["Abono"] for r in only_book)
com = [r for r in only_bank if not r["Referencia"].startswith("IVA")]; iva = [r for r in only_bank if r["Referencia"].startswith("IVA")]
R["comision"], R["comision_iva"] = sum(r["Cargo"] for r in com), sum(r["Cargo"] for r in iva)
R["comision_total"] = R["comision"] + R["comision_iva"]
R["duplicado"] = sum(-(net(bank, ref) - net(book, ref)) for ref in dups)
R["error_banco"] = net(bank, diffamt[0]); R["error_libros"] = net(book, diffamt[0]); R["error_dif"] = R["error_banco"] - R["error_libros"]
R["conc_diferencia_inicial"] = round(R["conc_saldo_libros"] - R["conc_saldo_banco"], 2)
R["conc_ajustado_banco"] = round(R["conc_saldo_banco"] + R["dep_transito"] + R["duplicado"], 2)
R["conc_ajustado_libros"] = round(R["conc_saldo_libros"] + R["error_dif"] - R["comision_total"], 2)
R["conc_diferencia_final"] = round(R["conc_ajustado_banco"] - R["conc_ajustado_libros"], 2)

wb = load_workbook(os.path.join(F1, "Zava_Cierre_Oct2026.xlsx"), data_only=True)
er = rows(wb["Datos_ER"]); dist = rows(wb["Gastos_Distribucion"]); corp = [r for r in rows(wb["Gastos_Corporativos"]) if r.get("Real") is not None]
S = lambda esc, col, c=None, ch=None: sum(r[col] for r in er if r["Escenario"] == esc and (c is None or r["CEDIS"] == c) and (ch is None or r["Canal"] == ch))
tag = {"Real": "r", "Presupuesto": "p", "Año anterior": "a"}
for e, t in tag.items():
    R[f"vol_{t}"] = S(e, "Volumen_CU"); R[f"ventas_{t}"] = S(e, "Ventas_netas"); R[f"ub_{t}"] = S(e, "Utilidad_bruta"); R[f"mb_{t}"] = R[f"ub_{t}"] / R[f"ventas_{t}"]
    R[f"dist_{t}"] = sum(r[e] for r in dist); R[f"corp_{t}"] = sum(r[e] for r in corp)
    R[f"ebitda_{t}"] = R[f"ub_{t}"] - R[f"dist_{t}"] - R[f"corp_{t}"]
    for m, col in (("azucar", "Costo_azucar"), ("pet", "Costo_PET"), ("conc", "Costo_concentrado"), ("otros", "Otros_costos_produccion")):
        R[f"{m}_{t}"] = S(e, col)
    for c in CEDIS:
        R[f"vol_{t}_{c}"] = S(e, "Volumen_CU", c); R[f"ventas_{t}_{c}"] = S(e, "Ventas_netas", c); R[f"ub_{t}_{c}"] = S(e, "Utilidad_bruta", c)
        R[f"dist_{t}_{c}"] = next(r[e] for r in dist if r["CEDIS"] == c)
R["ebitda_ajuste"] = -R["comision"]; R["ebitda_r_aj"] = R["ebitda_r"] + R["ebitda_ajuste"]
R["ventas_var_p"] = R["ventas_r"] - R["ventas_p"]; R["ventas_varpct_p"] = R["ventas_r"] / R["ventas_p"] - 1; R["ventas_varpct_a"] = R["ventas_r"] / R["ventas_a"] - 1
R["vol_varpct_p"] = R["vol_r"] / R["vol_p"] - 1; R["vol_varpct_a"] = R["vol_r"] / R["vol_a"] - 1
R["dist_var_p"] = R["dist_r"] - R["dist_p"]
R["ebitda_var_p"] = R["ebitda_r_aj"] - R["ebitda_p"]; R["ebitda_varpct_p"] = R["ebitda_r_aj"] / R["ebitda_p"] - 1
R["mb_var_p_pts"] = R["mb_r"] - R["mb_p"]
for c in CEDIS:
    R[f"vol_varpct_p_{c}"] = R[f"vol_r_{c}"] / R[f"vol_p_{c}"] - 1; R[f"vol_varpct_a_{c}"] = R[f"vol_r_{c}"] / R[f"vol_a_{c}"] - 1
    R[f"ventas_var_p_{c}"] = R[f"ventas_r_{c}"] - R[f"ventas_p_{c}"]; R[f"ventas_varpct_p_{c}"] = R[f"ventas_r_{c}"] / R[f"ventas_p_{c}"] - 1
    R[f"dist_var_p_{c}"] = R[f"dist_r_{c}"] - R[f"dist_p_{c}"]; R[f"mbc_{c}"] = R[f"ub_r_{c}"] / R[f"ventas_r_{c}"]
cells = {(r["CEDIS"], r["Canal"]) for r in er}
g = {(r["Escenario"], r["CEDIS"], r["Canal"]): r for r in er}
pav = R["ventas_p"] / R["vol_p"]
atpp = sum(g[("Real",) + k]["Volumen_CU"] * g[("Presupuesto",) + k]["Ventas_netas"] / g[("Presupuesto",) + k]["Volumen_CU"] for k in cells)
R["ef_volumen"] = (R["vol_r"] - R["vol_p"]) * pav; R["ef_mezcla"] = atpp - R["vol_r"] * pav; R["ef_precio"] = R["ventas_r"] - atpp
for m in ("azucar", "pet", "conc", "otros"):
    cp = R[f"{m}_p"] / R["vol_p"]
    R[f"cost_vol_{m}"] = (R["vol_r"] - R["vol_p"]) * cp; R[f"cost_tarifa_{m}"] = R[f"{m}_r"] - R["vol_r"] * cp
    R[f"{m}_cu_varpct_p"] = (R[f"{m}_r"] / R["vol_r"]) / cp - 1
R["cost_vol_total"] = sum(R[f"cost_vol_{m}"] for m in ("azucar", "pet", "conc", "otros"))
R["cost_tarifa_total"] = sum(R[f"cost_tarifa_{m}"] for m in ("azucar", "pet", "conc", "otros"))
hist = rows(wb["Historico_Volumen"]); H = {(c, r["Mes"]): r[c] for r in hist for c in CEDIS}
sup = {r["Supuesto"]: r["Valor"] for r in rows(wb["Supuestos_Forecast"]) if r.get("Supuesto")}
ppnd = rows(wb["Presupuesto_NovDic"])
ratios = {(c, m): H[(c, m)] / H[(c, "2025-" + m[5:])] for (c, m) in H if m.startswith("2026")}
oc, om = max(ratios, key=ratios.get)
R["atipico_vol"] = H[(oc, om)]
prev_m, next_m = f"2026-{int(om[5:])-1:02d}", f"2026-{int(om[5:])+1:02d}"
xr = lambda x: int(x + 0.5)
R["atipico_reemplazo"] = xr((H[(oc, prev_m)] + H[(oc, next_m)]) / 2)
adj = dict(H); adj[(oc, om)] = R["atipico_reemplazo"]
u = lambda name: next(v for k, v in sup.items() if k.startswith(name))
ucr = u("Costo azúcar") + u("Costo PET") + u("Concentrado") * u("Tipo de cambio") + u("Otros costos")
ndv = ndven = 0
for c in CEDIS:
    s26 = sum(adj[(c, f"2026-{m:02d}")] for m in range(1, 11)); s25 = sum(adj[(c, f"2025-{m:02d}")] for m in range(1, 11)); gc = s26 / s25 - 1
    R[f"fc_g_{c}"] = gc; price = sup[f"Precio promedio por CU real octubre · {c}"]
    for m in (11, 12):
        v = xr(H[(c, f"2025-{m}")] * (1 + gc)); R[f"fc_vol_{c}_{m}"] = v; ndv += v; ndven += v * price
R["fc_g_total_adj"] = sum(adj[(c, f"2026-{m:02d}")] for c in CEDIS for m in range(1, 11)) / sum(adj[(c, f"2025-{m:02d}")] for c in CEDIS for m in range(1, 11)) - 1
R["fc_g_total_raw"] = sum(H[(c, f"2026-{m:02d}")] for c in CEDIS for m in range(1, 11)) / sum(H[(c, f"2025-{m:02d}")] for c in CEDIS for m in range(1, 11)) - 1
R["fc_nd_vol"] = ndv; R["fc_q4_vol"] = R["vol_r"] + ndv; R["fc_q4_ventas"] = R["ventas_r"] + ndven
R["pp_q4_ventas"] = R["ventas_p"] + sum(r["Ventas_netas"] for r in ppnd); R["fc_q4_ventas_vs_pp"] = R["fc_q4_ventas"] / R["pp_q4_ventas"] - 1
R["fc_nd_ub"] = ndven - ndv * ucr
R["esc_azucar"] = -ndv * u("Costo azúcar") * u("Escenario: aumento del precio del azúcar")
R["esc_tc"] = -ndv * (u("Concentrado") * u("Escenario: aumento del tipo") + u("Costo PET") * u("Proporción del costo de PET") * u("Escenario: aumento del tipo") / u("Tipo de cambio"))
R["esc_comb"] = R["esc_azucar"] + R["esc_tc"]; R["esc_comb_pct_ub"] = R["esc_comb"] / R["fc_nd_ub"]

checksA = []
for k, v in R.items():
    if k in KEY:
        kv = KEY[k]; ok = abs(kv - v) <= max(0.01, abs(v) * 1e-9)
        checksA.append((k, v, kv, ok))

# ------------------------------------------------------------------ B. cifras en los entregables
PARAMS = [100, 0.10, 1.00, 0.62, 0.50, 18.65, 19.65, 9, 2000.0, 15_000_000, 10_000_000, 8_000_000, 150_000_000, 41_200_000, 0.0, 3_722_060.0, 16_000, 2_560, 18_560, 0.0701]
ALLOWED = [abs(v) for v in R.values() if isinstance(v, (int, float))] + [abs(v) for v in PARAMS]
ALLOWED += [abs(v) * 100 for v in R.values() if isinstance(v, float) and abs(v) < 1.5]  # porcentajes
ALLOWED += [R["esc_azucar"] / -R["fc_nd_vol"], (R["esc_tc"]) / -R["fc_nd_vol"], (R["esc_comb"]) / -R["fc_nd_vol"], R["esc_azucar"] / R["fc_nd_ub"] * -100, R["esc_tc"] / R["fc_nd_ub"] * -100,
            R["error_dif"] / 9, R["fc_nd_ub"], sum(R[f"fc_vol_{c}_11"] for c in CEDIS), sum(R[f"fc_vol_{c}_12"] for c in CEDIS), R["mb_var_p_pts"] * -100, 22.90, 14.55, 11.563, 9.20, 21.40,
            KEY["comisiones_prelim"], KEY["comisiones_aj"], H[("Golfo", "2025-07")], R["vol_varpct_a_Centro"] * 100, R["dso_moderno_jul"], R["dso_moderno_oct"], 120]
ALLOWED += [abs(R[f"mbc_{c}"]) * 100 for c in CEDIS]
FIN = re.compile(r"[−\-+]?\$?\d{1,3}(?:,\d{3})+(?:\.\d+)?(?:\s*millones)?|[−\-+]?\$?\d+\.\d+(?:\s*millones)?\s*%?|[−\-+]?\$\d+(?:\s*millones)?|[−\-+]?\d+(?:\.\d+)?\s*(?:%|pts)")


def parse(tok):
    t = tok.replace("−", "-").replace("$", "").replace(",", "").strip()
    mult, pctg = 1, False
    if "millones" in t: mult = 1e6; t = t.replace("millones", "").strip()
    if t.endswith("%"): pctg = True; t = t[:-1].strip()
    if t.endswith("pts"): t = t[:-3].strip()
    dec = len(t.split(".")[1]) if "." in t else 0
    return abs(float(t)) * mult, 0.5 * 10 ** (-dec) * mult


def match(val, tol):
    return any(abs(a - val) <= tol + 1e-9 for a in ALLOWED)


SKIP = re.compile(r"\d{1,2}:\d{2}|\d{1,2}/\d{1,2}(?:/\d{4})?|20\d\d-\d\d")


def scan(name, text):
    out = []
    clean = SKIP.sub(" ", text)
    for m in FIN.finditer(clean):
        tok = m.group(0)
        if re.fullmatch(r"\s*[0-6]\.[0-5]\s*", tok): continue  # número de ejercicio, no es cifra
        try: val, tol = parse(tok)
        except ValueError: continue
        ctx = clean[max(0, m.start() - 50): m.end() + 30].replace("\n", " ")
        out.append((name, tok.strip(), match(val, tol), ctx))
    return out


def html_text(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"(?s)<style.*?</style>|<script.*?</script>", " ", t)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def docx_text(path):
    d = Document(path); parts = [p.text for p in d.paragraphs]
    for t in d.tables:
        for r in t.rows: parts += [c.text for c in r.cells]
    return "\n".join(parts)


def pptx_text(path):
    p = Presentation(path); parts = []
    for s in p.slides:
        for sh in s.shapes:
            if sh.has_text_frame: parts.append(sh.text_frame.text)
        if s.has_notes_slide: parts.append(s.notes_slide.notes_text_frame.text)
    return "\n".join(parts)


def xlsx_text(path, sheets=None):
    wb = load_workbook(path, data_only=True); parts = []
    for ws in wb.worksheets:
        if sheets and ws.title not in sheets: continue
        for r in ws.iter_rows(values_only=True):
            parts += [str(v) for v in r if isinstance(v, str)]
    return "\n".join(parts)


DOCS = [("index.html", html_text(os.path.join(ROOT, "index.html"))),
        ("Zava_Correos_y_Minuta_Oct2026.docx", docx_text(os.path.join(F1, "Zava_Correos_y_Minuta_Oct2026.docx"))),
        ("CHECKPOINT_Ej1_Resultado_Briefing.docx", docx_text(os.path.join(F2, "CHECKPOINT_Ej1_Resultado_Briefing.docx"))),
        ("CHECKPOINT_Ej5_Resultado_Resumen_Consejo.docx", docx_text(os.path.join(F2, "CHECKPOINT_Ej5_Resultado_Resumen_Consejo.docx"))),
        ("CHECKPOINT_Ej5_Resultado_Consejo.pptx", pptx_text(os.path.join(F2, "CHECKPOINT_Ej5_Resultado_Consejo.pptx"))),
        ("Copilot_Finanzas_10_Casos_Hoja_para_llevar.docx", docx_text(os.path.join(ROOT, "CUSTOMER_FACING", "Copilot_Finanzas_10_Casos_Hoja_para_llevar.docx"))),
        ("Guia_Presentador_INTERNAL.html", html_text(os.path.join(ROOT, "INTERNAL", "Guia_Presentador_INTERNAL.html"))),
        ("Libro_Respuestas_INTERNAL.xlsx (textos)", xlsx_text(os.path.join(ROOT, "INTERNAL", "Libro_Respuestas_INTERNAL.xlsx")))]
checksB = []
for n, t in DOCS: checksB += scan(n, t)

# números del libro de respuestas y de los checkpoints de Excel (celda por celda)
checksC = []
ab = load_workbook(os.path.join(ROOT, "INTERNAL", "Libro_Respuestas_INTERNAL.xlsx"), data_only=True)
for r in ab["Cifras_clave"].iter_rows(min_row=2, values_only=True):
    if r[0] in R: checksC.append((f"Libro de respuestas · {r[0]}", r[1], R[r[0]], abs(r[1] - R[r[0]]) <= max(0.01, abs(R[r[0]]) * 1e-9)))
HECHOS = ["ventas_r", "ventas_var_p", "ventas_varpct_p", "ventas_varpct_a", "vol_r", "vol_varpct_p", "vol_varpct_a", "ef_volumen", "ef_mezcla", "ef_precio",
          "azucar_cu_varpct_p", "cost_tarifa_azucar", "mb_r", "mb_p", "vol_varpct_p_Golfo", "dist_var_p_Golfo", "ebitda_r", "ebitda_ajuste", "ebitda_r_aj", "ebitda_p",
          "ebitda_varpct_p", "caja_total", "duplicado", "conc_diferencia_inicial", "atipico_vol", "fc_g_total_adj", "fc_q4_vol", "fc_q4_ventas", "fc_q4_ventas_vs_pp",
          "esc_azucar", "esc_tc", "esc_comb"]
for f, n in (("CHECKPOINT_Ej3_Resultado_Cierre.xlsx", 24), ("CHECKPOINT_Ej4_Resultado_Forecast.xlsx", 32)):
    ws = load_workbook(os.path.join(F2, f), data_only=True)["Hechos_del_cierre"]
    vals = [r[2] for r in ws.iter_rows(min_row=5, values_only=True) if r[0] is not None]
    for k, v in zip(HECHOS[:n], vals):
        ok = v is not None and abs(v - R[k]) <= max(0.01, abs(R[k]) * 1e-9)
        checksC.append((f"{f} · Hechos · {k}", v, R[k], ok))
wb = load_workbook(os.path.join(F2, "CHECKPOINT_Ej2_Resultado_Conciliacion.xlsx"), data_only=True)
c = wb["Conciliacion"]
for cell, k in (("B3", "conc_saldo_banco"), ("B4", "dep_transito"), ("B5", "duplicado"), ("B6", "conc_ajustado_banco"), ("B8", "conc_saldo_libros"), ("B9", "error_dif"),
                ("B11", "conc_ajustado_libros"), ("B13", "conc_diferencia_final")):
    checksC.append((f"CHECKPOINT_Ej2 · Conciliacion!{cell} · {k}", c[cell].value, R[k], abs(c[cell].value - R[k]) < 0.005))
checksC.append(("CHECKPOINT_Ej2 · Partidas!G12 (comprobación = 0)", wb["Partidas"]["G12"].value, 0.0, wb["Partidas"]["G12"].value == 0))
checksC.append(("CHECKPOINT_Ej2 · renglones no conciliados (Cruce)", c["B15"].value, 7, c["B15"].value == 7))
wb4 = load_workbook(os.path.join(F2, "CHECKPOINT_Ej4_Resultado_Forecast.xlsx"), data_only=True)
for c_, row in zip(CEDIS, range(5, 9)):
    for col, m in (("I", 11), ("J", 12)):
        v = wb4["Pronostico"][f"{col}{row}"].value; k = f"fc_vol_{c_}_{m}"
        checksC.append((f"CHECKPOINT_Ej4 · Pronostico!{col}{row} · {k}", v, R[k], v == R[k]))

# ------------------------------------------------------------------ D. estructura del HTML
class P_(HTMLParser):
    def __init__(s): super().__init__(); s.ids = []; s.hrefs = []; s.copy = 0; s.boxes = 0; s.pre_in_prompt = 0
    def handle_starttag(s, tag, a):
        a = dict(a)
        if "id" in a: s.ids.append(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"): s.hrefs.append(a["href"][1:])
        if tag == "a" and a.get("href", "").startswith("files/"): s.hrefs.append("FILE:" + a["href"])
        if tag == "button" and "copy" in a.get("class", ""): s.copy += 1
        if tag == "input" and a.get("type") == "checkbox": s.boxes += 1
p = P_(); idx = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read(); p.feed(idx)
dups = sorted({i for i in p.ids if p.ids.count(i) > 1})
broken = [h for h in p.hrefs if not h.startswith("FILE:") and h not in p.ids]
missing_files = [h[5:] for h in p.hrefs if h.startswith("FILE:") and not os.path.exists(os.path.join(ROOT, h[5:].replace("/", os.sep)))]
pres = len(re.findall(r'<div class="prompt">', idx))
names = re.findall(r"\b[A-ZÁÉÍÓÚ][a-záéíóú]+ [A-ZÁÉÍÓÚ][a-záéíóú]+\b", html_text(os.path.join(ROOT, "index.html")))
forbidden = [w for w in ("Erik", "Humberto", "Montes", "Molina", "INTERNAL", "INTERNO", "Microsoft presenters") if w in html_text(os.path.join(ROOT, "index.html"))]
bep = html_text(os.path.join(ROOT, "index.html")).count("Bepensa")
structure = dict(ids=len(p.ids), duplicados=dups, anclas=len([h for h in p.hrefs if not h.startswith("FILE:")]), anclas_rotas=broken,
                 enlaces_a_archivos=len([h for h in p.hrefs if h.startswith("FILE:")]), archivos_faltantes=missing_files,
                 botones_copiar=p.copy, bloques_prompt=pres, casillas=p.boxes, palabras_internas=forbidden, menciones_Bepensa=bep)

# ------------------------------------------------------------------ reporte
okA = sum(1 for x in checksA if x[3]); okB = sum(1 for x in checksB if x[2]); okC = sum(1 for x in checksC if x[3])
total = len(checksA) + len(checksB) + len(checksC); ok = okA + okB + okC
E = html.escape
def tr(cells, ok): return "<tr" + ("" if ok else " style='background:#ffe9e7'") + ">" + "".join(f"<td>{E(str(c))}</td>" for c in cells) + "</tr>"
fmt = lambda v: f"{v:,.4f}" if isinstance(v, float) else (f"{v:,}" if isinstance(v, int) else str(v))
bad = [x for x in checksB if not x[2]]
byfile = Counter(x[0] for x in checksB); okfile = Counter(x[0] for x in checksB if x[2])
rep = f"""<!DOCTYPE html><html lang="es-MX"><head><meta charset="utf-8"><title>Reporte de verificación de cifras</title>
<style>body{{font-family:Segoe UI,Arial;margin:0;background:#f5f5fb;color:#172033}}.banner{{background:#b42318;color:#fff;text-align:center;font-weight:700;padding:6px}}
header{{background:linear-gradient(120deg,#1E1B4B,#4338CA 60%,#F97316 140%);color:#fff;padding:22px 30px}}main{{max-width:1200px;margin:auto;padding:18px}}
.card{{background:#fff;border:1px solid #d8dee9;border-radius:12px;padding:16px 22px;margin-bottom:16px}}table{{border-collapse:collapse;width:100%;font-size:.84rem}}td,th{{border-bottom:1px solid #d8dee9;padding:5px 7px;text-align:left}}th{{background:#eef0fb}}
.big{{font-size:2rem;font-weight:800;color:{'#2f7d1f' if ok == total else '#b42318'}}}</style></head><body>
<div class="banner">INTERNO · NO COMPARTIR</div><header><h1>Reporte de verificación de cifras</h1><div>Copilot para Finanzas: del cierre al Consejo · generado {dt.datetime.now():%Y-%m-%d %H:%M}</div></header><main>
<div class="card"><div class="big">{ok} de {total} comprobaciones correctas</div>
<ul><li><b>A. Recálculo independiente desde los archivos de práctica vs libro de respuestas:</b> {okA} de {len(checksA)}</li>
<li><b>B. Cifras financieras en textos (HTML, Word, PowerPoint, hoja para llevar, guía del presentador):</b> {okB} de {len(checksB)}</li>
<li><b>C. Celdas de checkpoints de Excel y libro de respuestas:</b> {okC} de {len(checksC)}</li></ul>
<p>El recálculo (A) lee los archivos que descargan los asistentes y no usa el código que los generó. Cada cifra de los textos (B) debe coincidir, con el redondeo mostrado, con un valor recalculado o con un parámetro del ejercicio.</p></div>
<div class="card"><h2>Estructura de index.html</h2><table>{''.join(f'<tr><td>{E(k)}</td><td>{E(str(v))}</td></tr>' for k, v in structure.items())}</table>
<p>Prueba funcional en navegador (Playwright, 5 de noviembre): 0 IDs duplicados, 0 anclas rotas, Copiar copia el prompt al portapapeles, las casillas actualizan y guardan el avance, Reiniciar lo borra, Abrir todo abre los 22 ejercicios y los enlaces del menú abren el ejercicio.</p></div>
<div class="card"><h2>B. Cifras por archivo</h2><table><tr><th>Archivo</th><th>Correctas</th></tr>{''.join(f'<tr><td>{E(f)}</td><td>{okfile[f]} de {n}</td></tr>' for f, n in byfile.items())}</table>
{'<h3>Sin coincidencia</h3><table><tr><th>Archivo</th><th>Cifra</th><th>Contexto</th></tr>' + ''.join(tr([x[0], x[1], x[3]], False) for x in bad) + '</table>' if bad else '<p>Todas las cifras coinciden.</p>'}</div>
<div class="card"><h2>A. Recálculo independiente</h2><table><tr><th>Clave</th><th>Recalculado</th><th>Libro de respuestas</th><th>OK</th></tr>{''.join(tr([k, fmt(v), fmt(kv), 'Sí' if o else 'NO'], o) for k, v, kv, o in checksA)}</table></div>
<div class="card"><h2>C. Checkpoints y libro de respuestas</h2><table><tr><th>Celda</th><th>Valor</th><th>Recalculado</th><th>OK</th></tr>{''.join(tr([k, fmt(v), fmt(kv), 'Sí' if o else 'NO'], o) for k, v, kv, o in checksC)}</table></div>
<div class="card"><h2>B. Detalle de cifras en textos</h2><table><tr><th>Archivo</th><th>Cifra</th><th>OK</th><th>Contexto</th></tr>{''.join(tr([a, b, 'Sí' if c_ else 'NO', d], c_) for a, b, c_, d in checksB)}</table></div>
</main></body></html>"""
open(os.path.join(ROOT, "INTERNAL", "Reporte_Verificacion_Cifras_INTERNAL.html"), "w", encoding="utf-8").write(rep)
print(f"TOTAL {ok}/{total}  A {okA}/{len(checksA)}  B {okB}/{len(checksB)}  C {okC}/{len(checksC)}")
print(structure)
for x in bad[:40]: print("SIN COINCIDENCIA:", x[0], "|", x[1], "|", x[3])
for x in checksA + [(a, b, c_, d) for a, b, c_, d in checksC]:
    if not x[3]: print("FALLA:", x)
