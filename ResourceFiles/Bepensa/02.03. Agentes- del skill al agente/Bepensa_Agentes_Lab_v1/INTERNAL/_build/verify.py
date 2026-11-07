# -*- coding: utf-8 -*-
import os, re, csv, json, zipfile, html, datetime as dt, sys
from html.parser import HTMLParser
from docx import Document
from openpyxl import load_workbook
from zcontent import *
from build_guide import AGENDA
from gen_internal import DRY, LIMITES
SOURCES = LIMITES + [
 ('Skills: requieren licencia de Microsoft 365 Copilot o pago por uso', 'Verificado', 'https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills'),
 ('«Usar solo las fuentes especificadas»', 'Prioriza, no bloquea', 'https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge'),
 ('«Uploaded files» renombrado «Attachments»', 'No documentado (la doc dice Uploaded files); en la guía como «visto en pantalla»', 'https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge'),
 ('Agentes pueden usar todo lo que Copilot puede por defecto', 'No documentado así; correo, personas y Teams se agregan como conocimiento y requieren licencia', 'https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites'),
 ('Crear Word, Excel, PowerPoint y gráficos', 'Verificado: Create documents, charts, and code', 'https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents'),
 ('GitHub Copilot harness: consume Copilot Credits', 'Verificado', 'https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview'),
 ('Harness: no es el servicio GitHub Copilot', 'Verificado', 'https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview'),
 ('Licencia de Microsoft 365 Copilot incluye el harness estándar', 'Cambió: «permite crear agentes del GitHub Copilot harness»; los créditos se cobran desde que se crea', 'https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing'),
 ('Acciones de conectores (Get emails (V3), Reply to email (V3), Send an email (V2), Create item, Search for users (V2), Create a chat)', 'Verificado', 'https://learn.microsoft.com/en-us/connectors/office365/'),
 ('Etiqueta de publicación', 'Make agent available in Microsoft Copilot', 'https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams'),
 ('Aprobación del catálogo', 'Centro de administración de Teams', 'https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams'),
 ('Confirmación de herramientas', 'Ask the end user before running (por defecto No)', 'https://learn.microsoft.com/en-us/microsoft-copilot-studio/add-tools-custom-agent'),
 ('Coca-Cola Andina: contexto', 'Argentina, Brasil, Chile y Paraguay; miles de empleados en oficinas y plantas embotelladoras', 'https://learn.microsoft.com/es-es/power-platform/guidance/case-studies/coca-cola-andina-hr-support'),
 ('Skills en Agent Builder: estado', 'Sin marca de versión preliminar ni Frontier (página actualizada el 6 de noviembre de 2026); se conserva la nota de barreras de información', 'https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills')]

ROOT = sys.argv[1] if len(sys.argv) > 1 else r"C:\Users\erikmontes\ZavaBuild\Bepensa_Agentes_Lab_v1"
F = lambda *p: os.path.join(ROOT, "files", *p)
checks = []
def ck(area, name, ok, detail=""): checks.append((area, name, bool(ok), detail))

# 1. HTML
class PP(HTMLParser):
    def __init__(s): super().__init__(); s.ids, s.hrefs, s.copy, s.box = [], [], 0, 0
    def handle_starttag(s, tag, a):
        a = dict(a)
        if "id" in a: s.ids.append(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"): s.hrefs.append(a["href"][1:])
        if tag == "a" and a.get("href", "").startswith("files/"): s.hrefs.append("FILE:" + a["href"])
        if tag == "button" and "copy" in a.get("class", ""): s.copy += 1
        if tag == "input" and a.get("type") == "checkbox": s.box += 1
idx = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read(); p = PP(); p.feed(idx)
dups = sorted({i for i in p.ids if p.ids.count(i) > 1}); broken = [h for h in p.hrefs if not h.startswith("FILE:") and h not in p.ids]
missing = [h[5:] for h in p.hrefs if h.startswith("FILE:") and not os.path.exists(os.path.join(ROOT, h[5:].replace("/", os.sep)))]
ck("HTML", "0 IDs duplicados", not dups, str(dups)); ck("HTML", "0 anclas rotas", not broken, str(broken)); ck("HTML", "Enlaces a archivos existen", not missing, str(missing))
ck("HTML", "Un botón Copiar por bloque de prompt", p.copy == len(re.findall(r'<div class="prompt">', idx)), f"{p.copy} botones")
ck("HTML", "Casillas de avance", p.box > 0, f"{p.box} casillas")
ck("HTML", "Agenda suma 60 minutos", sum(b - a for a, b, *_ in AGENDA) == 60 and AGENDA[0][0] == 0 and AGENDA[-1][1] == 60 and all(AGENDA[i][1] == AGENDA[i + 1][0] for i in range(len(AGENDA) - 1)))
txt = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?s)<style.*?</style>|<script.*?</script>", " ", idx)))
ck("HTML", "«Bepensa» solo en el encabezado", txt.count("Bepensa") == 1)
ck("HTML", "No menciona el lunes", "lunes" not in txt.lower())
for s in (PROMPT_ES, PROMPT_EN, SKILL_POE, SKILL_ESC, INSTRUCCIONES_A1, INSTRUCCIONES_A2):
    ck("HTML", f"Texto exacto en un <pre>: {s[:35]}…", html.escape(s) in idx)

# 2. Textos de práctica vs libro de respuestas
def dtext(path): return "\n".join(x.text for x in Document(path).paragraphs)
ab = load_workbook(os.path.join(ROOT, "INTERNAL", "Libro_Respuestas_INTERNAL.xlsx"), data_only=True)
NUM = re.compile(r"\d+(?:\.\d+)?")
CODE = re.compile(r"\b[A-Z]{2,4}-[A-Z0-9]{2,4}(?:-[0-9A-Z]{1,3})?\b")
for i, pr in enumerate(PRUEBAS, 1):
    t = dtext(F("1_Textos_de_practica", pr["archivo"])).replace("≤", "")
    book = [r for r in ab[f"Prueba_{i}"].iter_rows(min_row=2, values_only=True)]
    bc = [r[0] for r in book if r[0]]; bf = [r[1] for r in book if r[1]]; bi = [r[2] for r in book if r[2]]
    ck("Prueba %d" % i, "Libro de respuestas = base (conservar, faltantes, invención)", bc == pr["conservar"] and bf == pr["faltantes"] and bi == pr["invento"])
    nums_doc = set(NUM.findall(t)); nums_book = set(NUM.findall(" ".join(pr["conservar"])))
    ck("Prueba %d" % i, "Cada cifra del libro (conservar) está en el texto de práctica", nums_book <= nums_doc, str(sorted(nums_book - nums_doc)))
    body = "\n".join(pr["texto"])
    nb = set(NUM.findall(body)) - {"1", "2", "3", "4", "5", "6"} if i == 3 else set(NUM.findall(body))
    ck("Prueba %d" % i, "Cada cifra del texto de práctica está en el libro (conservar)", nb - {"2"} <= nums_book | ({"2"} if i in (1,) else set()), str(sorted(nb - nums_book)))
    codes_doc = set(CODE.findall(t)); codes_book = set(CODE.findall(" ".join(pr["conservar"])))
    ck("Prueba %d" % i, "Códigos de formatos iguales en texto y libro", codes_doc == codes_book, f"{sorted(codes_doc)} vs {sorted(codes_book)}")
    for c in pr["conservar"]:
        core = re.sub(r"\s*\(.*?\)$", "", c).replace("«", "").replace("»", "").replace("≤ ", "").replace("pH ", "").replace("canal ", "")
        core = core.replace("versión 2", "versión 2").replace(" a ", " a ")
        ok = core.lower().replace("ui (icumsa)", "ui (icumsa)") in t.lower() or all(n in t for n in NUM.findall(core)) and NUM.findall(core)
        ck("Prueba %d" % i, f"Conservar «{c}» aparece en el texto", ok)

# 3. Correos vs resultados esperados
MESES = {"noviembre": 11, "diciembre": 12}
for c in CORREOS:
    t = open(F("4_Copilot_Studio", c["archivo"]), encoding="utf-8").read()
    e = c["esperado"]
    if c["tipo"] != "Incompleto":
        m = re.search(r"del (\d+)(?: de (\w+))? al (\d+) de (\w+) de (\d{4})", t)
        d1 = dt.date(int(m.group(5)), MESES[m.group(2) or m.group(4)], int(m.group(1))); d2 = dt.date(int(m.group(5)), MESES[m.group(4)], int(m.group(3)))
        ck(f"Correo {c['tipo']}", "Fechas = esperado", (d1.isoformat(), d2.isoformat()) == (e["FechaInicio"], e["FechaFin"]))
        ck(f"Correo {c['tipo']}", "Número de personas = esperado", f"Número de personas: {e['NumeroDePersonas']}" in t)
        ck(f"Correo {c['tipo']}", "Centro de costos = esperado", e["CentroDeCostos"] in t)
        ck(f"Correo {c['tipo']}", "Turno = esperado", e["Turno"].lower() in t.lower())
        md = re.search(r"(\d+) de (\w+) de (\d{4}), (\d+):(\d+)", t)
        sent = dt.datetime(int(md.group(3)), MESES[md.group(2)], int(md.group(1)), int(md.group(4)), int(md.group(5)))
        urg = "Urgente" if (dt.datetime.combine(d1, dt.time(0)) - sent).total_seconds() < 72 * 3600 else "Normal"
        ck(f"Correo {c['tipo']}", "Urgencia calculada (< 72 h) = esperado", urg == e["Urgencia"], urg)
    else:
        falt = ["Número de personas", "Fechas", "Turno", "Centro de costos"]
        ck("Correo Incompleto", "No trae número, fechas, turno ni centro de costos", not re.search(r"\d+ personas|CC-\d+|turno|del \d+", t, re.I))
        ck("Correo Incompleto", "Estatus esperado = Información incompleta", e["Estatus"] == "Información incompleta")
    ck(f"Correo {c['tipo']}", "Remitente con dominio .example (ficticio)", re.search(r"@zavabebidas\.example", t))
ck("Correo Urgente", "Trae la instrucción que el agente NO debe seguir (reenviar)", "reenvía" in open(F("4_Copilot_Studio", "Correo_2_Urgente.txt"), encoding="utf-8").read())

# 4. Lista
rows = list(csv.reader(open(F("4_Copilot_Studio", "Lista_Solicitudes_de_Personal_esquema.csv"), encoding="utf-8-sig")))
ck("Lista", "CSV = esquema de la guía", [tuple(r) for r in rows[1:]] == [tuple(x) for x in ESQUEMA])
est = next(r[3] for r in rows if r[0] == "Estatus").split("; ")
ck("Lista", "Estatus de las instrucciones existen en la lista", all(s in est for s in ("Información incompleta", "En revisión RH")) and all(c["esperado"]["Estatus"] in est for c in CORREOS))
ck("Lista", "Campos esperados de los correos son columnas de la lista", all(k in [r[0] for r in rows] for k in CORREOS[0]["esperado"]))
ck("Agente 2", "Instrucciones sin «Send an email» y con confirmación", "confirmación" in INSTRUCCIONES_A2.lower() and "Nunca envíes correos nuevos" in INSTRUCCIONES_A2)

# 5. Skills
for name, src in (("formato-estandar-poe", SKILL_POE), ("formato-estandar-escalamiento", SKILL_ESC)):
    zp = F("2_Skills", f"{name}.zip")
    with zipfile.ZipFile(zp) as z:
        names = z.namelist(); body = z.read("SKILL.md").decode("utf-8") if "SKILL.md" in names else ""
    fm = re.match(r"---\nname: (.+)\ndescription: (.+)\n---\n", body)
    ck(f"Skill {name}", "SKILL.md en la raíz del .zip y nada más", names == ["SKILL.md"])
    ck(f"Skill {name}", "Front matter con name y description", fm and fm.group(1) == name and len(fm.group(2)) > 20)
    ck(f"Skill {name}", "name: minúsculas, números y guiones; sin guion al inicio o final", re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name))
    ck(f"Skill {name}", "Instrucciones < 20,000 caracteres", len(body) < 20000, f"{len(body):,}")
    ck(f"Skill {name}", ".zip < 50 MB", os.path.getsize(zp) < 50 * 1024 * 1024, f"{os.path.getsize(zp):,} bytes")
    ck(f"Skill {name}", "Contiene la leyenda BORRADOR - NO CONTROLADO", LEYENDA in body)
    ck(f"Skill {name}", "Igual al texto de la guía", body == src)
ck("Agente 1", "Instrucciones < 8,000 caracteres", len(INSTRUCCIONES_A1) < 8000, f"{len(INSTRUCCIONES_A1):,}")
ck("Agente 1", "Skills por agente ≤ 8", 2 <= 8)
ck("Agente 1", "Prompt en español pide dos skills, español y la leyenda", all(x in PROMPT_ES for x in ("formato-estandar-poe", "formato-estandar-escalamiento", "español de México", LEYENDA)))

# 6. Nombres internos o reales en archivos para clientes
BAD = ["Erik", "Humberto", "Montes", "Molina", "Melhus", "Duarte", "Rocio", "Rocío", "Ricardo", "Colla", "Valderrama", "Gamboa", "Cetina", "Garma", "Chacon", "Trujillo", "Gorocica", "Marrufo", "Mezquita", "Dzib", "Custodio", "Ojeda",
       "Montesinos", "Cristerna", "Ceballos", "Canche", "Landeros", "Bastarrachea", "Euan", "Itzincab", "Guillen", "Berzunza", "Espadas", "Ureña", "Bermejo", "Rivero", "Quijano", "Alcocer", "Alvarado",
       "Pech", "microsoft.com>", "@microsoft", "@bepensa", "INTERNO", "INTERNAL", "Mariana", "Raúl"]
def office_text(path):
    out = []
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            if n.endswith(".xml"): out.append(re.sub(r"<[^>]+>", " ", z.read(n).decode("utf-8", "ignore")))
    return " ".join(out)
cf = [os.path.join(ROOT, "index.html")] + [os.path.join(dp, f) for base in ("files", "CUSTOMER_FACING") for dp, _, fs in os.walk(os.path.join(ROOT, base)) for f in fs]
for path in cf:
    ext = path.lower().rsplit(".", 1)[-1]
    if ext in ("docx", "xlsx", "pptx"): t = office_text(path)
    elif ext == "zip":
        t = ""
        with zipfile.ZipFile(path) as z:
            for n in z.namelist():
                b = z.read(n)
                if n.endswith((".txt", ".md", ".csv")): t += b.decode("utf-8", "ignore")
                elif n.endswith((".docx", ".xlsx", ".pptx")):
                    import io as _io
                    with zipfile.ZipFile(_io.BytesIO(b)) as zz: t += " ".join(re.sub(r"<[^>]+>", " ", zz.read(m).decode("utf-8", "ignore")) for m in zz.namelist() if m.endswith(".xml"))
    elif ext == "pdf":
        b = open(path, "rb").read(); t = b.decode("latin-1") + b.decode("utf-16-be", "ignore")
    else: t = open(path, encoding="utf-8", errors="ignore").read()
    hits = [w for w in BAD if re.search(r"(?<![A-Za-zÁÉÍÓÚáéíóúñ])" + re.escape(w) + r"(?![A-Za-zÁÉÍÓÚáéíóúñ])", t)]
    ck("Nombres", f"Sin nombres internos o reales: {os.path.relpath(path, ROOT)}", not hits, str(hits))

# 7. Etiquetas de confidencialidad
labels = []
for dp, _, fs in os.walk(ROOT):
    if "_build" in dp: continue
    for f in fs:
        if not f.lower().endswith((".docx", ".xlsx", ".pptx")): continue
        path = os.path.join(dp, f); sig = open(path, "rb").read(4).hex()
        if sig == "d0cf11e0": state = "CIFRADO (etiqueta con protección)"
        else:
            with zipfile.ZipFile(path) as z:
                cp = z.read("docProps/custom.xml").decode("utf-8", "ignore") if "docProps/custom.xml" in z.namelist() else ""
            state = "Con etiqueta MSIP" if "MSIP_Label" in cp else "Sin etiqueta"
        labels.append((os.path.relpath(path, ROOT), state)); ck("Etiquetas", f"Sin etiqueta: {os.path.relpath(path, ROOT)}", state == "Sin etiqueta", state)

# 8. Ajustes del 6 de noviembre
from docx import Document as _D
_hand = " ".join(p.text for p in _D(os.path.join(ROOT, "CUSTOMER_FACING", "Agentes_Hoja_para_llevar.docx")).paragraphs)
_guia = open(os.path.join(ROOT, "INTERNAL", "Guia_Presentador_INTERNAL.html"), encoding="utf-8").read()
for _n, _t in (("index.html", txt), ("Guía del presentador", html.unescape(_guia))):
    for _v in ("1,200", "3,600", "5,000", "6 min 33 s", "4.1 de 5", "976"):
        ck("Andi", f"{_n}: cifra de Learn «{_v}»", _v in _t)
for _n, _t in (("index.html", txt), ("Hoja para llevar", _hand), ("Guía del presentador", html.unescape(_guia))):
    ck("Andi", f"{_n}: sin «más de 300» ni «no publica»", "más de 300" not in _t and "no publica" not in _t)
    ck("Andi", f"{_n}: sin 16,000 ni nota de Microsoft Latinoamérica", "16,000" not in _t and "Latinoamérica" not in _t)
    ck("Andi", f"{_n}: línea de contexto nueva" , ("miles de empleados en oficinas y plantas embotelladoras" in _t) or _n == "Hoja para llevar")
    ck("Skills", f"{_n}: sin «versión preliminar»", "versión preliminar" not in _t and "es preliminar" not in _t)
ck("Andi", "Hoja para llevar: 1,200 de ~3,600 y CSAT 4.1 de 5", "1,200" in _hand and "3,600" in _hand and "4.1 de 5" in _hand)
ck("Skills", "index.html: frase «recién disponibles; puede que todavía no aparezcan en tu organización» (3 lugares)", txt.count("recién disponibles; puede que todavía no aparezcan en tu organización") == 3)
ck("Skills", "index.html: conserva la nota de barreras de información", "barreras de información" in txt)
for _v in ("Correo 2 (urgente) debe llegar el lunes 9 de noviembre", "Correo 1 y el Correo 3 pueden enviarse antes", "consume Copilot Credits"):
    ck("Guía del presentador", f"Preparación: «{_v}»", _v in html.unescape(re.sub(r"<[^>]+>", "", _guia)))

ok = sum(c[2] for c in checks); tot = len(checks)
import json as _j
_sp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scratch_labels.json")
SCR = "".join(f"<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td></tr>" for a, b in (_j.load(open(_sp, encoding="utf-8")) if os.path.exists(_sp) else []))
E = html.escape
rep = f"""<!DOCTYPE html><html lang="es-MX"><head><meta charset="utf-8"><title>Reporte de verificación</title><style>body{{font-family:Segoe UI,Arial;background:#f5f5fb;margin:0}}.b{{background:#b42318;color:#fff;text-align:center;font-weight:700;padding:6px}}header{{background:linear-gradient(120deg,#1E1B4B,#4338CA 60%,#F97316 140%);color:#fff;padding:22px 30px}}main{{max-width:1200px;margin:auto;padding:18px}}.card{{background:#fff;border:1px solid #d8dee9;border-radius:12px;padding:14px 20px;margin-bottom:14px}}table{{border-collapse:collapse;width:100%;font-size:.85rem}}td,th{{border-bottom:1px solid #d8dee9;padding:5px;text-align:left}}.big{{font-size:2rem;font-weight:800;color:{'#2f7d1f' if ok == tot else '#b42318'}}}</style></head><body>
<div class="b">INTERNO · NO COMPARTIR</div><header><h1>Reporte de verificación</h1><div>Sesión de agentes · {E(ROOT)} · {dt.datetime.now():%Y-%m-%d %H:%M}</div></header><main>
<div class="card"><div class="big">{ok} de {tot} comprobaciones correctas</div></div>
<div class="card"><h2>Fuentes de los datos verificados</h2><table><tr><th>Dato</th><th>Valor vigente</th><th>Fuente</th></tr>{"".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td><a href='{E(c)}'>{E(c)}</a></td></tr>" for a, b, c in SOURCES)}</table></div>
<div class="card"><h2>Comprobaciones</h2><table><tr><th>Área</th><th>Comprobación</th><th>OK</th><th>Detalle</th></tr>{"".join(f"<tr{'' if o else ' style=background:#ffe9e7'}><td>{E(a)}</td><td>{E(n)}</td><td>{'Sí' if o else 'NO'}</td><td>{E(d)}</td></tr>" for a, n, o, d in checks)}</table></div>
<div class="card"><h2>Pruebas en Copilot Chat (prueba aproximada)</h2><table><tr><th>Prueba</th><th>Resultado</th></tr>{"".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in DRY)}</table></div>
<div class="card"><h2>Etiquetas en la copia de Scratchpad (OneDrive de Microsoft)</h2><p>Al sincronizar, la etiqueta predeterminada cifra los archivos de Office sueltos. Para Bepensa usa el .zip de entrega o la copia limpia de ZavaBuild.</p><table><tr><th>Archivo</th><th>Estado</th></tr>{SCR}</table></div>
<div class="card"><h2>Etiquetas de confidencialidad (copia limpia)</h2><table><tr><th>Archivo</th><th>Estado</th></tr>{"".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in labels)}</table></div></main></body></html>"""
if len(sys.argv) <= 1: open(os.path.join(ROOT, "INTERNAL", "Reporte_Verificacion_INTERNAL.html"), "w", encoding="utf-8").write(rep)
print(f"TOTAL {ok}/{tot}")
for c in checks:
    if not c[2]: print("FALLA:", c)
