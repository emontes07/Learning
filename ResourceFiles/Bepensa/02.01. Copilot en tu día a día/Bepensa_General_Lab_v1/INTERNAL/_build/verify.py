# -*- coding: utf-8 -*-
"""Verificación independiente (sesión general): recalcula desde los archivos y revisa cada cifra de los entregables."""
import os, re, json, html, statistics, datetime as dt
from collections import Counter
from html.parser import HTMLParser
from openpyxl import load_workbook
from docx import Document
from pptx import Presentation

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_General_Lab_v1"
F1, F2 = os.path.join(ROOT, "files", "1_Archivos_de_practica"), os.path.join(ROOT, "files", "2_Checkpoints")
KEY = json.load(open(os.path.join(ROOT, "_build", "answer_key.json")))
REG = ["Norte", "Centro", "Golfo", "Península"]


def rows(ws, ncol=None):
    it = ws.iter_rows(values_only=True, max_col=ncol); h = next(it)
    return [dict(zip(h, r)) for r in it if r[0] is not None]


# ---------------- A. recálculo desde los archivos de práctica
R = {}
raw = rows(load_workbook(os.path.join(F1, "Zava_Indicadores_Servicio_2026.xlsx"), data_only=True)["Indicadores"])
metas = {r["Indicador"][:5]: r["Meta"] for r in rows(load_workbook(os.path.join(F1, "Zava_Indicadores_Servicio_2026.xlsx"), data_only=True)["Metas"])}
sig = Counter(tuple(r.values()) for r in raw)
dups = [k for k, n in sig.items() if n > 1]
assert len(dups) == 1
clean, seen = [], set()
for r in raw:
    t = tuple(r.values())
    if t in seen: continue
    seen.add(t); clean.append(r)
med = {g: statistics.median(r["Tiempo_respuesta_horas"] for r in clean if r["Region"] == g) for g in REG}
outl = [r for r in clean if r["Tiempo_respuesta_horas"] > 3 * med[r["Region"]]]
assert len(outl) == 1
months = sorted({r["Mes"] for r in raw})
missing = [(g, m) for g in REG for m in months if not any(r["Region"] == g and r["Mes"] == m for r in clean)]
R["n_filas_raw"], R["n_filas_limpias"] = len(raw), len(clean)
R["dup_atendidas"] = dict(zip(raw[0].keys(), dups[0]))["Solicitudes_atendidas"]; R["atipico"] = outl[0]["Tiempo_respuesta_horas"]
R["atipico_mediana_region"] = statistics.median(r["Tiempo_respuesta_horas"] for r in clean if r["Region"] == outl[0]["Region"] and r is not outl[0])
pen = [r["Tiempo_respuesta_horas"] for r in clean if r["Region"] == outl[0]["Region"] and r is not outl[0]]
R["rango_min_region_atipico"], R["rango_max_region_atipico"] = min(pen), max(pen)
Q = {"3T": ["2026-07", "2026-08", "2026-09"], "2T": ["2026-04", "2026-05", "2026-06"]}
for tag, ms in Q.items():
    rs = [r for r in clean if r["Mes"] in ms]; tr = [r for r in rs if r is not outl[0]]
    R[f"rec_{tag}"] = sum(r["Solicitudes_recibidas"] for r in rs); R[f"ate_{tag}"] = sum(r["Solicitudes_atendidas"] for r in rs)
    R[f"pct_ate_{tag}"] = R[f"ate_{tag}"] / R[f"rec_{tag}"]
    R[f"tiempo_{tag}"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in tr) / sum(r["Solicitudes_atendidas"] for r in tr)
    R[f"sat_{tag}"] = sum(r["Satisfaccion_1a5"] * r["Encuestas_respondidas"] for r in rs) / sum(r["Encuestas_respondidas"] for r in rs)
    R[f"pres_asig_{tag}"] = sum(r["Presupuesto_asignado"] for r in rs); R[f"pres_ej_{tag}"] = sum(r["Presupuesto_ejercido"] for r in rs)
    R[f"pres_pct_{tag}"] = R[f"pres_ej_{tag}"] / R[f"pres_asig_{tag}"]
    for g in REG:
        rg = [r for r in rs if r["Region"] == g]; tg = [r for r in rg if r is not outl[0]]
        R[f"ate_{tag}_{g}"] = sum(r["Solicitudes_atendidas"] for r in rg)
        R[f"tiempo_{tag}_{g}"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in tg) / sum(r["Solicitudes_atendidas"] for r in tg)
        R[f"sat_{tag}_{g}"] = sum(r["Satisfaccion_1a5"] * r["Encuestas_respondidas"] for r in rg) / sum(r["Encuestas_respondidas"] for r in rg)
        R[f"pres_pct_{tag}_{g}"] = sum(r["Presupuesto_ejercido"] for r in rg) / sum(r["Presupuesto_asignado"] for r in rg)
R["tiempo_delta"] = R["tiempo_3T"] - R["tiempo_2T"]; R["sat_delta"] = R["sat_3T"] - R["sat_2T"]
r3 = [r for r in raw if r["Mes"] in Q["3T"]]
R["ate_3T_sucio"] = sum(r["Solicitudes_atendidas"] for r in r3)
R["tiempo_3T_sucio"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in r3) / R["ate_3T_sucio"]
co = [r for r in clean if r["Mes"] in Q["3T"]]
R["tiempo_3T_solo_atipico"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in co) / sum(r["Solicitudes_atendidas"] for r in co)
R["meta_tiempo"], R["meta_sat"] = metas["Tiemp"], metas["Satis"]
com = rows(load_workbook(os.path.join(F1, "Zava_Encuesta_Servicio_3T2026.xlsx"), data_only=True)["Comentarios"])
temas = rows(load_workbook(os.path.join(F2, "CHECKPOINT_Ej2_Resultado_Excel.xlsx"), data_only=True)["Comentarios_temas"], 7)
assert [c["Comentario"] for c in com] == [c["Comentario"] for c in temas], "La encuesta y el checkpoint no coinciden"
R["com_total"] = len(com); R["com_cal_prom"] = sum(c["Calificacion_1a5"] for c in com) / len(com)
for t in sorted({c["Tema"] for c in temas}):
    cs = [c for c in temas if c["Tema"] == t]; R[f"tema_n_{t}"] = len(cs); R[f"tema_cal_{t}"] = sum(c["Calificacion_1a5"] for c in cs) / len(cs)
R["tema_pct_tiempo"] = R["tema_n_Tiempo de respuesta"] / R["com_total"]
R["com_con_nombre"] = sum(1 for c in temas if c["Menciona_a_una_persona"] == "Sí")
R["tiempo_norte_jul"] = next(r["Tiempo_respuesta_horas"] for r in clean if r["Region"] == "Norte" and r["Mes"] == "2026-07")
R["tiempo_norte_sep"] = next(r["Tiempo_respuesta_horas"] for r in clean if r["Region"] == "Norte" and r["Mes"] == "2026-09")
checksA = [(k, v, KEY[k], abs(KEY[k] - v) <= max(1e-6, abs(v) * 1e-9)) for k, v in R.items() if k in KEY]
checksA.append(("problemas: mes faltante = Centro 2026-08", str(missing), "[('Centro', '2026-08')]", missing == [("Centro", "2026-08")]))

# ---------------- B. cifras en textos
PARAMS = [24.0, 4.20, 30, 10, 120, 70, 5, 3, 4, 6, 8, 2, 1, 100, 0.0]
ALLOWED = [abs(v) for v in R.values() if isinstance(v, (int, float))] + PARAMS
ALLOWED += [abs(v) * 100 for v in R.values() if isinstance(v, float) and abs(v) < 1.5]
ALLOWED += [R[f"tema_n_{t}"] / R["com_total"] * 100 for t in [k[7:] for k in R if k.startswith("tema_n_")]]
FIN = re.compile(r"[−\-+]?\$\d{1,3}(?:,\d{3})+(?:\.\d+)?|[−\-+]?\d{1,3}(?:,\d{3})+(?:\.\d+)?|[−\-+]?\d+\.\d+\s*(?:%|h\b)?|[−\-+]?\d+\s*(?:%|h\b)")
SKIP = re.compile(r"\d{1,2}:\d{2}|20\d\d-\d\d|\b20\d\d\b|C-\d{3}")


def parse(tok):
    t = tok.replace("−", "-").replace("$", "").replace(",", "").replace("%", "").replace("h", "").strip()
    dec = len(t.split(".")[1]) if "." in t else 0
    return abs(float(t)), 0.5 * 10 ** (-dec)


def scan(name, text):
    out = []; clean_ = SKIP.sub(" ", text)
    for m in FIN.finditer(clean_):
        tok = m.group(0)
        if re.fullmatch(r"\s*[0-7]\.[0-4]\s*", tok): continue  # número de ejercicio
        if not re.search(r"[$%,.h]", tok): continue  # enteros pequeños sin unidad: estructurales
        v, tol = parse(tok)
        out.append((name, tok.strip(), any(abs(a - v) <= tol + 1e-9 for a in ALLOWED), clean_[max(0, m.start() - 50):m.end() + 30].replace("\n", " ")))
    return out


def htext(p):
    t = open(p, encoding="utf-8").read(); t = re.sub(r"(?s)<style.*?</style>|<script.*?</script>", " ", t)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def dtext(p):
    d = Document(p); parts = [x.text for x in d.paragraphs]
    for t in d.tables:
        for r in t.rows: parts += [c.text for c in r.cells]
    return "\n".join(parts)


def ptext(p):
    pr = Presentation(p); parts = []
    for s in pr.slides:
        for sh in s.shapes:
            if sh.has_text_frame: parts.append(sh.text_frame.text)
        if s.has_notes_slide: parts.append(s.notes_slide.notes_text_frame.text)
    return "\n".join(parts)


DOCS = [("index.html", htext(os.path.join(ROOT, "index.html"))), ("Zava_Notas_y_Politicas_Servicio.docx", dtext(os.path.join(F1, "Zava_Notas_y_Politicas_Servicio.docx"))),
        ("CHECKPOINT_Ej3_Resultado_Reporte.docx", dtext(os.path.join(F2, "CHECKPOINT_Ej3_Resultado_Reporte.docx"))),
        ("CHECKPOINT_Ej4_Resultado_Presentacion.pptx", ptext(os.path.join(F2, "CHECKPOINT_Ej4_Resultado_Presentacion.pptx"))),
        ("CHECKPOINT_Ej5_Resultado_Correos.docx", dtext(os.path.join(F2, "CHECKPOINT_Ej5_Resultado_Correos.docx"))),
        ("Hoja para llevar", dtext(os.path.join(ROOT, "CUSTOMER_FACING", "Copilot_Dia_a_Dia_10_Casos_Hoja_para_llevar.docx"))),
        ("Guia_Presentador_INTERNAL.html", htext(os.path.join(ROOT, "INTERNAL", "Guia_Presentador_INTERNAL.html")))]
checksB = []
for n, t in DOCS: checksB += scan(n, t)

# ---------------- C. celdas de checkpoints y libro de respuestas
checksC = []
wb = load_workbook(os.path.join(F2, "CHECKPOINT_Ej2_Resultado_Excel.xlsx"), data_only=True)
HK = ["rec_3T", "ate_3T", "pct_ate_3T", "tiempo_3T", "tiempo_2T", "tiempo_3T_Golfo", "sat_3T", "sat_2T", "sat_3T_Golfo", "pres_ej_3T", "pres_asig_3T", "pres_pct_3T", "com_total", "tema_n_Tiempo de respuesta", "tiempo_3T_sucio"]
for k, r in zip(HK, [r for r in wb["Hechos"].iter_rows(min_row=5, values_only=True) if r[0]]):
    checksC.append((f"Hechos · {k}", r[2], R[k], r[2] is not None and abs(r[2] - R[k]) <= max(1e-6, abs(R[k]) * 1e-9)))
rs = wb["Resumen_3T"]
for i, g in enumerate(REG, 4):
    for col, k in (("C", f"ate_3T_{g}"), ("E", f"tiempo_3T_{g}"), ("F", f"sat_3T_{g}"), ("I", f"pres_pct_3T_{g}")):
        v = rs[f"{col}{i}"].value; checksC.append((f"Resumen_3T!{col}{i} · {k}", v, R[k], abs(v - R[k]) <= 1e-6))
rv = wb["Revision"]
checksC += [("Revision!D4 (duplicado = 2 renglones)", rv["D4"].value, 2, rv["D4"].value == 2), ("Revision!D5 (máximo Península)", rv["D5"].value, R["atipico"], rv["D5"].value == R["atipico"]),
            ("Revision!D6 (Centro agosto = 0)", rv["D6"].value, 0, rv["D6"].value == 0)]
ct = wb["Comentarios_temas"]
for i in range(2, 7):
    t, n = ct[f"I{i}"].value, ct[f"J{i}"].value; checksC.append((f"Comentarios_temas · {t}", n, R[f"tema_n_{t}"], n == R[f"tema_n_{t}"]))
pr = Presentation(os.path.join(F2, "CHECKPOINT_Ej4_Resultado_Presentacion.pptx"))
for s in pr.slides:
    for sh in s.shapes:
        if sh.has_chart:
            vals = list(sh.chart.plots[0].series[0].values)
            for g, v in zip(REG, vals): checksC.append((f"Gráfica PPT · {g}", v, round(R[f"tiempo_3T_{g}"], 1), v == round(R[f"tiempo_3T_{g}"], 1)))
ab = load_workbook(os.path.join(ROOT, "INTERNAL", "Libro_Respuestas_INTERNAL.xlsx"), data_only=True)
for r in ab["Cifras_clave"].iter_rows(min_row=2, values_only=True):
    if r[0] in R: checksC.append((f"Libro de respuestas · {r[0]}", r[1], R[r[0]], abs(r[1] - R[r[0]]) <= max(1e-6, abs(R[r[0]]) * 1e-9)))

# ---------------- D. HTML
class PP(HTMLParser):
    def __init__(s): super().__init__(); s.ids, s.hrefs, s.copy, s.box = [], [], 0, 0
    def handle_starttag(s, tag, a):
        a = dict(a)
        if "id" in a: s.ids.append(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"): s.hrefs.append(a["href"][1:])
        if tag == "a" and a.get("href", "").startswith("files/"): s.hrefs.append("FILE:" + a["href"])
        if tag == "button" and "copy" in a.get("class", ""): s.copy += 1
        if tag == "input" and a.get("type") == "checkbox": s.box += 1
p = PP(); idx = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read(); p.feed(idx); txt = htext(os.path.join(ROOT, "index.html"))
S = dict(ids=len(p.ids), duplicados=sorted({i for i in p.ids if p.ids.count(i) > 1}), anclas_rotas=[h for h in p.hrefs if not h.startswith("FILE:") and h not in p.ids],
         archivos_faltantes=[h[5:] for h in p.hrefs if h.startswith("FILE:") and not os.path.exists(os.path.join(ROOT, h[5:].replace("/", os.sep)))],
         botones_copiar=p.copy, bloques_prompt=len(re.findall(r'<div class="prompt">', idx)), casillas=p.box, menciones_Bepensa=txt.count("Bepensa"),
         palabras_prohibidas=[w for w in ("Erik", "Humberto", "Montes", "Molina", "INTERNO", "lunes", "Finanzas") if w in txt],
         nombres_de_comentarios=[w for w in ("Mariana", "Raúl") if w in txt])

okA, okB, okC = sum(x[3] for x in checksA), sum(x[2] for x in checksB), sum(x[3] for x in checksC)
tot, ok = len(checksA) + len(checksB) + len(checksC), okA + okB + okC
E = html.escape
fmt = lambda v: f"{v:,.4f}" if isinstance(v, float) else str(v)
tr = lambda cells, o: "<tr" + ("" if o else " style='background:#ffe9e7'") + ">" + "".join(f"<td>{E(str(c))}</td>" for c in cells) + "</tr>"
bad = [x for x in checksB if not x[2]]
by, okf = Counter(x[0] for x in checksB), Counter(x[0] for x in checksB if x[2])
rep = f"""<!DOCTYPE html><html lang="es-MX"><head><meta charset="utf-8"><title>Reporte de verificación</title><style>body{{font-family:Segoe UI,Arial;background:#f5f5fb;margin:0}}.b{{background:#b42318;color:#fff;text-align:center;font-weight:700;padding:6px}}header{{background:linear-gradient(120deg,#1E1B4B,#4338CA 60%,#F97316 140%);color:#fff;padding:22px 30px}}main{{max-width:1200px;margin:auto;padding:18px}}.card{{background:#fff;border:1px solid #d8dee9;border-radius:12px;padding:14px 20px;margin-bottom:14px}}table{{border-collapse:collapse;width:100%;font-size:.84rem}}td,th{{border-bottom:1px solid #d8dee9;padding:5px;text-align:left}}.big{{font-size:2rem;font-weight:800;color:{'#2f7d1f' if ok == tot else '#b42318'}}}</style></head><body>
<div class="b">INTERNO · NO COMPARTIR</div><header><h1>Reporte de verificación de cifras</h1><div>Copilot en tu día a día · generado {dt.datetime.now():%Y-%m-%d %H:%M}</div></header><main>
<div class="card"><div class="big">{ok} de {tot} comprobaciones correctas</div><ul><li>A. Recálculo independiente desde los archivos de práctica vs libro de respuestas: {okA} de {len(checksA)}</li><li>B. Cifras en textos (HTML, Word, PowerPoint, hoja para llevar, guía del presentador): {okB} de {len(checksB)}</li><li>C. Celdas de checkpoints, gráfica y libro de respuestas: {okC} de {len(checksC)}</li></ul>
<p>El recálculo encuentra por su cuenta el duplicado, el atípico (más de 3 veces la mediana de su región) y el mes faltante, limpia los datos y recalcula todo sin usar el código que generó los archivos.</p></div>
<div class="card"><h2>Estructura de index.html</h2><table>{''.join(f'<tr><td>{E(k)}</td><td>{E(str(v))}</td></tr>' for k, v in S.items())}</table></div>
<div class="card"><h2>B. Por archivo</h2><table>{''.join(f'<tr><td>{E(f)}</td><td>{okf[f]} de {n}</td></tr>' for f, n in by.items())}</table>{'<table>' + ''.join(tr([x[0], x[1], x[3]], False) for x in bad) + '</table>' if bad else '<p>Todas coinciden.</p>'}</div>
<div class="card"><h2>A. Recálculo</h2><table>{''.join(tr([k, fmt(v), fmt(kv), 'Sí' if o else 'NO'], o) for k, v, kv, o in checksA)}</table></div>
<div class="card"><h2>C. Celdas</h2><table>{''.join(tr([k, fmt(v), fmt(kv), 'Sí' if o else 'NO'], o) for k, v, kv, o in checksC)}</table></div>
<div class="card"><h2>B. Detalle</h2><table>{''.join(tr([a, b, 'Sí' if c else 'NO', d], c) for a, b, c, d in checksB)}</table></div></main></body></html>"""
open(os.path.join(ROOT, "INTERNAL", "Reporte_Verificacion_Cifras_INTERNAL.html"), "w", encoding="utf-8").write(rep)
print(f"TOTAL {ok}/{tot}  A {okA}/{len(checksA)}  B {okB}/{len(checksB)}  C {okC}/{len(checksC)}"); print(S)
for x in bad[:30]: print("SIN COINCIDENCIA:", x[0], "|", x[1], "|", x[3])
for x in checksA + checksC:
    if not x[3]: print("FALLA:", x)
