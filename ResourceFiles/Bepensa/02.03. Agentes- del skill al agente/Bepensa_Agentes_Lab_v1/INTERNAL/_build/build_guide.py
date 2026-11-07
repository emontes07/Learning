# -*- coding: utf-8 -*-
"""Arma index.html de la sesión de agentes."""
import os, html
from zcontent import *

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_Agentes_Lab_v1"
HERE = os.path.dirname(os.path.abspath(__file__))
E = html.escape
CSS = open(os.path.join(HERE, "collab_style.css"), encoding="utf-8").read()
JS = open(os.path.join(HERE, "collab_script.js"), encoding="utf-8").read().replace("bepensa-colaboracion-v1", "zava-agentes-lab-v1").replace("' of '+boxes.length+' casillas completadas'", "' de '+boxes.length+' casillas completadas'")
JS = JS.split("document.querySelectorAll('.fac')")[0]
CSS += """
.lvl{display:inline-block;font-size:.74rem;font-weight:700;border-radius:99px;padding:2px 10px}.lvl-req{background:#4338CA;color:#fff}.lvl-ver{background:#e0e7ff;color:#3730a3}.lvl-demo{background:#fde7d4;color:#9a3412}.lvl-opt{background:#eef2f7;color:#334155}.lvl-reto{background:#1E1B4B;color:#fdba74}.lvl-sum{margin-left:6px}
.legend{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0}.legend div{flex:1 1 200px;background:#f7f9fc;border:1px solid var(--border);border-radius:10px;padding:8px 12px;font-size:.92rem}
.rule{background:linear-gradient(120deg,#1E1B4B,#4338CA);color:#fff;border-radius:14px;padding:14px 20px;margin:12px 0;font-size:1.05rem}.rule b{color:#fdba74}
.ladder{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:12px 0}.ladder div{border-radius:12px;padding:10px 12px;background:#f0f4f9;border-top:5px solid #4338CA}.ladder div:nth-child(4){border-top-color:#7c3aed}.ladder div:nth-child(5){border-top-color:#F97316}
.ladder b{display:block;color:#1E1B4B}.ladder small{color:#5d6b82}@media (max-width:960px){.ladder{grid-template-columns:1fr}}
.nolic{background:#eef2f7;border-color:#64748b}.ok3{color:#166534;font-weight:600}.bad3{color:#b42318;font-weight:600}
"""
LVL = {"Requerido": "lvl-req", "Ver y comparar": "lvl-ver", "Demo": "lvl-demo", "Opcional": "lvl-opt", "Reto": "lvl-reto"}
MODE = {"Agent Builder": "mode-agent", "Copilot Studio": "mode-plan", "Copilot Chat": "mode-teams", "Skill": "mode-edit", "Instrucciones": "mode-plan", "Correo": "mode-outlook", "Plantilla": "mode-chat"}
LIC = '<span class="req req-lic">Licencia de Microsoft 365 Copilot o pago por uso</span>'
STUDIO = '<span class="req req-lic">Copilot Studio · consume Copilot Credits</span>'
NONE = '<span class="req req-m365">Solo observar</span>'
FS = "files/"


def table(head, rows):
    return '<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>"


def dl(path, label=None): return f'<a href="{E(path)}" download>{E(label or path.split("/")[-1])}</a>'


def prompt(pid, label, mode, text):
    return (f'<div class="prompt"><div class="prompt-head"><span class="prompt-label">{E(label)}</span><span class="mode {MODE[mode]}">{mode}</span>'
            f'<button class="copy" type="button" aria-label="Copiar: {E(label)}">Copiar</button></div><pre id="{pid}">{E(text)}</pre></div>')


def lab(id, n, title, level, time, goal, app, inputs, produces, lic=LIC, intro="", prompts=(), expect="", fail="", checks=(), callouts=(), extra=""):
    meta = (f'<div class="meta"><span><b>Tiempo</b> {time}</span><span><b>Objetivo</b> {goal}</span><span><b>App</b> {app}</span><span><b>Requiere</b> {lic}</span></div>'
            f'<div class="chain"><div><span class="chain-k">Usas</span>{inputs}</div><div><span class="chain-k add">Produce para el siguiente paso</span>{produces}</div></div>')
    pr = "".join(prompt(f"p-{id}-{k}", l, m, t) for k, (l, m, t) in enumerate(prompts))
    ex = f'<div class="callout expect"><div class="callout-title">Lo que verás</div><div>{expect}</div></div>' if expect else ""
    co = "".join(f'<div class="callout {c}"><div class="callout-title">{t}</div><div>{b}</div></div>' for c, t, b in callouts)
    fl = f'<div class="callout catchup"><div class="callout-title">Si no te sale</div><div>{fail}</div></div>' if fail else ""
    ck = ('<div class="selfcheck"><div class="callout-title">Para practicar después</div><ul>' + "".join(f'<li><label><input type="checkbox" data-key="{id}-{i}"> {c}</label></li>' for i, c in enumerate(checks)) + "</ul></div>") if checks else ""
    return (f'<details class="lab" id="{id}"><summary><span class="lab-num">{n}</span><span class="lab-title">{title}</span><span class="lvl {LVL[level]} lvl-sum">{level}</span></summary>'
            f'<div class="lab-body">{meta}{"<p>" + intro + "</p>" if intro else ""}{extra}{pr}{ex}{co}{fl}{ck}</div></details>')


def chapter(id, num_, title, tags, story, body):
    return (f'<section class="module" id="{id}"><div class="module-head"><div class="module-num">{num_}</div><h2>{title}</h2><div class="module-tags">' + "".join(f"<span>{t}</span>" for t in tags) +
            f'</div></div><div class="story"><div class="story-label">La idea</div><p>{story}</p></div>{body}</section>')


AGENDA = [(0, 5, "#ch1", "1. La escalera: de prompt a agente que actúa"), (5, 22, "#ch2", "2. Agente 1 · Agent Builder: Asistente de Estándares de Procedimientos"),
          (22, 25, "#ch3", "3. ¿Agent Builder o Copilot Studio?"), (25, 42, "#ch4", "4. Agente 2 · Copilot Studio: Solicitudes de personal (RH)"),
          (42, 47, "#ch5", "5. Gobierno y licencias"), (47, 50, "#ch6", "6. Caso real: «Andi», el agente de RH de Coca-Cola Andina"),
          (50, 55, "#ch7", "7. Ideas por área y plantilla para tu agente"), (55, 60, "#ch8", "8. Preguntas frecuentes")]
LADDER = [("Prompt", "Lo escribes cada vez.", "«Da formato a este POE…»"), ("Prompt guardado", "Lo guardas y lo reusas tú o tu equipo.", "Guardar mensaje en Copilot Chat"),
          ("Skill", "Un buen prompt escrito una vez, con reglas y plantilla, que un agente usa cuando hace falta.", "formato-estandar-poe"),
          ("Agente", "Instrucciones + skills + conocimiento, compartido con tu equipo.", "Asistente de Estándares de Procedimientos"),
          ("Agente que actúa", "Además usa herramientas: lee correos, crea registros, abre chats (con tu confirmación).", "Solicitudes de personal en Copilot Studio")]

FAQ = [
    ("¿Qué es una skill?", "Un paquete con un archivo SKILL.md: nombre, descripción y las instrucciones para una tarea (por ejemplo, la plantilla de POE). El agente la usa cuando la tarea lo requiere. En Agent Builder un agente puede tener hasta 8 skills; las skills están recién disponibles; puede que todavía no aparezcan en tu organización."),
    ("¿En qué se diferencia un agente de un prompt guardado?", "El prompt guardado es una sola instrucción que tú pegas. El agente junta instrucciones permanentes, skills y conocimiento (por ejemplo, la carpeta de procedimientos), y lo compartes para que tu equipo obtenga respuestas consistentes."),
    ("¿Qué es el «GitHub Copilot harness» de Copilot Studio?", "Es un marco de creación y orquestación de Copilot Studio para agentes que razonan en varios pasos; crea y edita archivos de Word, Excel, PowerPoint y PDF, y admite skills y memoria. No es el servicio GitHub Copilot para programadores: según Microsoft, los datos no se envían a ese servicio. Los agentes de este harness consumen Copilot Credits."),
    ("¿Necesito licencia para crear agentes?", "En Agent Builder puedes crear agentes con instrucciones y conocimiento público. Para skills, y para usar SharePoint, archivos o conectores, necesitas licencia de Microsoft 365 Copilot o pago por uso; correo, personas y Teams requieren la licencia. Copilot Studio consume Copilot Credits. Tu área de TI define qué está habilitado."),
    ("¿El agente puede ver información que yo no puedo ver?", "El conocimiento de Microsoft 365 respeta los permisos de quien usa el agente. Las herramientas de Copilot Studio usan una conexión (por ejemplo, al buzón o a la lista): define con TI con qué cuenta se conectan y quién puede usar el agente."),
    ("¿«Usar solo las fuentes especificadas» bloquea el conocimiento general?", "No. Según la documentación, la opción da prioridad a tus fuentes, pero no bloquea el conocimiento general del modelo. Si necesitas un control más estricto, la recomendación es Copilot Studio."),
    ("¿Un agente de RH puede decidir a quién contratar?", "No debe. El agente registra, ordena y prepara mensajes; la decisión sobre personas es de RH. Por eso las instrucciones lo prohíben y las acciones que salen hacia otras personas piden confirmación."),
    ("¿Cómo comparto un agente con mi equipo?", "En Agent Builder lo compartes con personas o grupos (con permiso de chat o de edición) y, si tu organización lo permite, lo envías al catálogo de la organización. En Copilot Studio lo publicas en Teams y Microsoft 365, y el envío al catálogo requiere la aprobación de un administrador en el Centro de administración de Teams."),
]
IDEAS = [("Recursos Humanos", "Preguntas frecuentes de políticas (vacaciones, trabajo híbrido) con las políticas como conocimiento", "Registro de solicitudes de personal (este ejemplo), con confirmación humana"),
         ("Operaciones", "Asistente de POE y escalamientos (este ejemplo)", "Resumen de bitácoras de turno y pendientes para el relevo"),
         ("Calidad", "Evaluación de vacíos de procedimientos contra la plantilla", "Preparación de evidencias para una auditoría interna"),
         ("Compras", "Comparativo de cotizaciones con criterios fijos", "Preguntas frecuentes de proveedores sobre el proceso de alta"),
         ("Comercial", "Preparación de visitas con el historial del cliente", "Resumen semanal de promociones por región"),
         ("Finanzas", "Respuestas sobre la política de viáticos y gastos", "Primer borrador del análisis de variaciones con reglas de la empresa")]
PLANTILLA = """Crea un agente llamado «[nombre]» para [equipo o área] de [empresa].
Su trabajo: [qué tarea repetida resuelve y para quién].
Conocimiento: usa [carpeta de SharePoint, documentos o sitios] como fuente principal y cita el documento.
Reglas:
- [qué debe conservar sin cambios]
- Nunca inventes información; si algo falta, márcalo como [FALTA: ...].
- [qué no debe hacer nunca: decisiones sobre personas, datos sensibles, etc.]
- [formato y leyenda de salida]
- Responde en español de México.
Crea [n] skills reutilizables: «[nombre-skill-1]» para [tarea 1] y «[nombre-skill-2]» para [tarea 2].
Antes de responder, si algo no está claro, haz hasta 3 preguntas."""


def expect_prueba(p):
    return ("<p><b>Debe conservar sin cambios:</b> " + "; ".join(E(x) for x in p["conservar"]) + ".</p>"
            "<p><b>Debe marcar como faltante:</b></p><ol>" + "".join(f"<li>{E(x)}</li>" for x in p["faltantes"]) + "</ol>"
            '<p class="bad3">Señales de que inventó algo:</p><ul>' + "".join(f"<li>{E(x)}</li>" for x in p["invento"]) + "</ul>"
            f"<p>Y siempre la leyenda <b>{LEYENDA}</b> y el recordatorio de revisión y aprobación.</p>")


def build():
    ag = table(["Minuto", "Tema"], [[f"{a}–{b}", f'<a href="{h}">{t}</a>'] for a, b, h, t in AGENDA]) + f"<p class='small muted'>Total: {sum(b - a for a, b, *_ in AGENDA)} minutos.</p>"
    lad = '<div class="ladder">' + "".join(f"<div><b>{i}. {t}</b><span>{d}</span><br><small>Ejemplo: {e}</small></div>" for i, (t, d, e) in enumerate(LADDER, 1)) + "</div>"
    files = table(["Carpeta", "Archivo", "Para qué"],
                  [["1_Textos_de_practica", dl(FS + "1_Textos_de_practica/" + p["archivo"]), f"Prueba {i}"] for i, p in enumerate(PRUEBAS, 1)] +
                  [["2_Skills", dl(FS + "2_Skills/formato-estandar-poe.zip"), "Plan B: subir la skill de POE"], ["2_Skills", dl(FS + "2_Skills/formato-estandar-escalamiento.zip"), "Plan B: subir la skill de escalamiento"],
                   ["2_Skills", dl(FS + "2_Skills/Instrucciones_Asistente_Estandares.txt"), "Instrucciones de referencia del agente 1"],
                   ["3_Conocimiento_SharePoint", "5 procedimientos y plantillas ficticios", "Carpeta de conocimiento del agente 1"],
                   ["4_Copilot_Studio", dl(FS + "4_Copilot_Studio/Lista_Solicitudes_de_Personal_esquema.csv"), "Esquema de la lista de SharePoint"],
                   ["4_Copilot_Studio", "Correo_1_Completo.txt · Correo_2_Urgente.txt · Correo_3_Incompleto.txt", "Correos de prueba del agente 2"],
                   ["4_Copilot_Studio", dl(FS + "4_Copilot_Studio/Instrucciones_Agente_Solicitudes_de_Personal.txt"), "Instrucciones del agente 2"]])
    welcome = f"""<section class="card" id="bienvenida"><h2>Bienvenida</h2>
<blockquote class="quote">Una skill es un buen prompt escrito una vez, así que es el cierre natural del tema. Las guías lo presentan como una escalera: prompt → prompt guardado → skill → agente. Y hay un quinto escalón: el agente que actúa.</blockquote>
{lad}<p class="lead">En 60 minutos vemos en vivo dos agentes para Zava Bebidas, una empresa ficticia (Planta Mérida y CEDIS Península): un agente de Agent Builder que estandariza procedimientos de Operaciones y Calidad, y un agente de Copilot Studio que registra solicitudes de personal temporal para Recursos Humanos. Si tienes licencia, puedes seguir el primero en tu laptop.</p>
<h3>Agenda (60 minutos)</h3>{ag}
<h3>Archivos</h3><p><a class="btn-dl" href="{FS}Zava_Agentes_Archivos.zip" download>Descargar todos los archivos (.zip)</a></p>{files}
<div class="rule"><b>El agente propone, tú decides.</b> Un agente no reemplaza la revisión: los procedimientos salen como borrador y las acciones hacia otras personas piden tu confirmación.</div>
<div class="callout important" id="responsable"><div class="callout-title">Uso responsable</div><div><ul><li>No pongas datos personales sensibles en el conocimiento de un agente ni en las pruebas.</li><li>Un agente no toma decisiones sobre personas (contratar, evaluar, sancionar).</li><li>Comparte el agente solo con quien lo necesita y revisa sus fuentes.</li></ul></div></div>
<div class="callout note"><div class="callout-title">Datos ficticios</div><div>Empresa, procedimientos, valores, correos y direcciones son ficticios. Los nombres de botones pueden variar según la versión y el idioma.</div></div></section>"""

    ch1 = chapter("ch1", "Minutos 0–5", "1. La escalera: de prompt a agente que actúa", ["5 minutos", "Demo"],
                  "Cada escalón guarda más de tu trabajo: el prompt lo escribes cada vez; la skill lo escribes una vez; el agente lo comparte con tu equipo; el agente que actúa, además, hace cosas por ti, con tu confirmación.",
                  '<div class="chapter-inner">' + table(["Escalón", "Dónde vive", "Cuándo subir al siguiente"], [
                      ["1. Prompt", "En tu chat", "Cuando lo escribes por tercera vez"], ["2. Prompt guardado", "Galería de Copilot (Sus mensajes)", "Cuando necesita reglas, plantilla o más de un paso"],
                      ["3. Skill", "Un SKILL.md dentro de un agente", "Cuando varias personas necesitan lo mismo con el mismo conocimiento"],
                      ["4. Agente", "Agent Builder (Microsoft 365 Copilot)", "Cuando hace falta actuar en otros sistemas (correo, listas, Teams)"],
                      ["5. Agente que actúa", "Copilot Studio con herramientas", "Siempre con confirmación humana y gobierno de TI"]]) + "</div>")

    a1 = lab("lab-2-1", "2.1", "Crea el agente con un solo prompt", "Demo", "4 min", "Que Agent Builder genere instrucciones y dos skills", "Agent Builder (Microsoft 365 Copilot)",
             "El prompt de abajo", "El agente con sus instrucciones y skills",
             intro="En la aplicación Microsoft Copilot, en <b>Agentes</b>, selecciona <b>Nuevo agente</b> (en la documentación: <b>Agents &amp; Skills</b> &gt; <b>New agent</b>) y describe el agente en la pestaña <b>Describir</b>. El agente de referencia se creó en inglés; esta es la versión en español.",
             prompts=[("Prompt para crear el agente (español)", "Agent Builder", PROMPT_ES), ("Prompt original en inglés (referencia)", "Agent Builder", PROMPT_EN)],
             expect="Agent Builder propone nombre, descripción e instrucciones, y crea dos skills: <b>formato-estandar-poe</b> y <b>formato-estandar-escalamiento</b>. Revisa que las instrucciones digan que conserve el contenido técnico, que no invente y que use la leyenda «BORRADOR - NO CONTROLADO».",
             fail="Si no crea las skills, súbelas (ejercicio 2.2). Si las instrucciones salen en inglés, pide: «Escribe las instrucciones en español de México».",
             checks=["Creé un agente describiéndolo con un prompt."])
    a2 = lab("lab-2-2", "2.2", "Revisa las instrucciones y las skills (plan B: súbelas)", "Demo", "3 min", "Saber qué quedó escrito y cómo arreglarlo", "Agent Builder",
             "Instrucciones y skills generadas, o los .zip de la carpeta 2_Skills", "El agente con instrucciones revisadas y 2 skills",
             intro="Abre la pestaña <b>Configurar</b>. Revisa las instrucciones (límite de 8,000 caracteres) y despliega <b>Skills</b>. Si una skill no se creó: <b>Configurar</b> &gt; <b>Skills</b> &gt; <b>Agregar</b> y sube el .zip completo (no el SKILL.md solo). Cada .zip trae el SKILL.md en la raíz.",
             prompts=[("Instrucciones de referencia (pégalas si las generadas no sirven)", "Instrucciones", INSTRUCCIONES_A1), ("SKILL.md · formato-estandar-poe", "Skill", SKILL_POE), ("SKILL.md · formato-estandar-escalamiento", "Skill", SKILL_ESC)],
             callouts=[("note", "Límites de las skills", "Hasta 8 skills por agente; .zip de hasta 50 MB (25 MB por archivo); SKILL.md con nombre y descripción en el encabezado y las instrucciones en menos de 20,000 caracteres. Requiere licencia de Microsoft 365 Copilot o pago por uso. Las skills están recién disponibles; puede que todavía no aparezcan en tu organización.")],
             extra=f"<p>Descarga: {dl(FS + '2_Skills/formato-estandar-poe.zip')} · {dl(FS + '2_Skills/formato-estandar-escalamiento.zip')}</p>",
             checks=["Revisé las instrucciones de un agente.", "Subí una skill desde un .zip."])
    a3 = lab("lab-2-3", "2.3", "Agrega conocimiento: la carpeta de procedimientos vigentes", "Demo", "3 min", "Que el agente use la terminología y los formatos de la empresa", "Agent Builder",
             "Una carpeta de SharePoint con los 5 documentos de 3_Conocimiento_SharePoint", "Un agente que cita los procedimientos vigentes",
             intro="En <b>Configurar</b> &gt; <b>Conocimiento</b>, agrega la carpeta de SharePoint con los procedimientos vigentes ficticios (POE-PRO-014, POE-CAL-001, ESC-CAL-002 y las dos plantillas).",
             expect=table(["Fuente", "Límite por agente"], [["Archivos, carpetas o sitios de SharePoint", "100 archivos"], ["Listas de SharePoint", "1 lista"], ["Archivos de OneDrive", "50 archivos"],
                                                        ["Archivos subidos", "20 archivos"], ["Sitios web públicos", "4 URL"], ["Chats de Teams", "5 chats"], ["Reuniones de Teams", "5 reuniones"]]),
             callouts=[("warning", "«Usar solo las fuentes especificadas»", "Esta opción <b>da prioridad</b> a tus fuentes, pero <b>no bloquea</b> el conocimiento general del modelo. Para un control más estricto, la documentación recomienda Copilot Studio."),
                       ("tip", "Visto en pantalla (puede variar)", "En la versión reciente de Agent Builder, los archivos subidos pueden aparecer como «Attachments» (en la documentación todavía dice «Uploaded files»), y el agente puede crear documentos, gráficos y presentaciones con la opción <b>Create documents, charts, and code</b>.")],
             checks=["Agregué una carpeta de SharePoint como conocimiento."])
    pr = "".join(lab(f"lab-2-4-{i}", f"2.{3 + i}", f"Prueba {i}: {t}", "Demo" if i > 1 else "Opcional", m, g, "Agent Builder (pestaña Pruébelo / Try it)",
                     dl(FS + "1_Textos_de_practica/" + p["archivo"]), pr_, prompts=[(f"Prueba {i}", "Agent Builder", p["prompt"])], expect=expect_prueba(p),
                     intro=f"Copia el prompt, abre {dl(FS + '1_Textos_de_practica/' + p['archivo'])} y pega su texto donde dice [pega aquí…].",
                     fail="Si el agente inventa algo, señálalo: «No inventes; marca como [FALTA] lo que no esté en el texto» y vuelve a pedirlo. Es justo lo que queremos detectar.",
                     checks=[f"Hice la prueba {i} y revisé qué conservó, qué marcó y qué inventó."])
                 for i, (p, t, m, g, pr_) in enumerate(zip(PRUEBAS, ["un POE nuevo desde notas sueltas", "reordenar un escalamiento existente", "evaluación de vacíos con entrega en Word"],
                                                            ["3 min", "2 min", "2 min"], ["Un POE en formato estándar sin inventar", "El mismo escalamiento, ordenado y completo", "La lista de vacíos en un documento de Word"],
                                                            ["Un POE borrador con vacíos marcados", "Un escalamiento borrador con vacíos marcados", "Un documento de Word con la evaluación"]), 1))
    ch2 = chapter("ch2", "Minutos 5–22", "2. Agente 1 · Agent Builder: Asistente de Estándares de Procedimientos", ["17 minutos", "Agent Builder", "Operaciones y Calidad"],
                  "Operaciones y Calidad escriben POE y escalamientos con formatos distintos y a veces con huecos. El agente aplica siempre la misma plantilla, conserva los valores técnicos tal cual, marca lo que falta y nunca inventa.", a1 + a2 + a3 + pr)

    comp = table(["Si necesitas…", "Agent Builder", "Copilot Studio"], [
        ["Responder con instrucciones, skills y documentos de Microsoft 365", "Sí: empieza aquí", "Sí"],
        ["Crear documentos, gráficos o presentaciones", "Sí (Create documents, charts, and code)", "Sí (el GitHub Copilot harness crea Word, Excel, PowerPoint y PDF)"],
        ["Actuar en otros sistemas: leer correos, crear registros, abrir chats", "No: Agent Builder no permite crear acciones con servicios externos", "Sí, con herramientas y conectores"],
        ["Flujos, lógica de negocio o ambientes de desarrollo, prueba y producción", "No", "Sí"],
        ["Publicar en un canal externo (por ejemplo, un sitio para clientes)", "No", "Sí"],
        ["Bloquear el conocimiento general del modelo", "No (solo priorizar tus fuentes)", "Sí, con más control"],
        ["Gobierno", "Controles de agentes de Microsoft 365", "Ambientes y políticas de conectores de Power Platform"]])
    ch3 = chapter("ch3", "Minutos 22–25", "3. ¿Agent Builder o Copilot Studio?", ["3 minutos"],
                  "Elige por lo que el agente tiene que hacer, no por cuántas personas lo van a usar. Si con instrucciones, skills y conocimiento de Microsoft 365 basta, empieza en Agent Builder; un agente de Agent Builder se puede copiar después a Copilot Studio (como una copia independiente).",
                  f'<div class="chapter-inner" id="decision">{comp}</div>')

    tools = table(["Herramienta (conector)", "Acción", "¿La usamos?", "Por qué"], [
        ["Office 365 Outlook", "Get emails (V3)", "Sí", "Leer las solicitudes del buzón"], ["Office 365 Outlook", "Reply to email (V3)", "Sí, con confirmación", "Contestar en el mismo hilo con el folio o lo que falta"],
        ["Office 365 Outlook", "Send an email (V2)", "<b>No</b>", E(SEND_EMAIL_DECISION)], ["SharePoint", "Create item", "Sí", "Registrar la solicitud en la lista"],
        ["Office 365 Users", "Search for users (V2)", "Sí", "Completar el nombre y el área del solicitante"], ["Microsoft Teams", "Create a chat", "Sí, con confirmación", "Abrir el chat entre el solicitante y RH"]])
    schema = table(["Columna", "Tipo", "Obligatoria", "Valores o nota"], [[E(c) for c in r] for r in ESQUEMA])
    b1 = lab("lab-4-1", "4.1", "Así está construido (antes de la sesión)", "Demo", "4 min", "Entender las piezas del agente", "Copilot Studio (nueva experiencia)", "El agente ya creado", "El contexto para la demo", lic=STUDIO,
             intro="El agente se preparó antes de la sesión. Pasos del laboratorio original: <b>copilotstudio.microsoft.com</b> &gt; <b>Inicio</b> &gt; mosaico <b>Agent</b> &gt; nombre &gt; <b>Save</b>; después <b>Tools</b> con los conectores de la tabla. Lo adaptamos a RH: «Solicitudes de personal» temporal.",
             extra=f"<h3>Herramientas</h3>{tools}<h3>Lista de SharePoint «{LISTA}»</h3>{schema}<p>Esquema en {dl(FS + '4_Copilot_Studio/Lista_Solicitudes_de_Personal_esquema.csv')}.</p>",
             prompts=[("Instrucciones del agente", "Instrucciones", INSTRUCCIONES_A2)])
    b2 = lab("lab-4-2", "4.2", "En vivo: agrega una herramienta y la confirmación", "Demo", "4 min", "Ver cómo un agente gana una acción", "Copilot Studio", "El agente", "El agente con la herramienta Create a chat", lic=STUDIO,
             intro="En <b>Tools</b> &gt; <b>Add a tool</b>, busca el conector <b>Microsoft Teams</b> y elige <b>Create a chat</b>. En la configuración de la herramienta activa <b>Ask the end user before running</b> (en la documentación en español: «Pregunte al usuario final antes de ejecutar»). Haz lo mismo en <b>Reply to email (V3)</b>.",
             expect="La herramienta aparece en la lista del agente. Al probarla, el agente muestra los participantes y pide confirmación antes de crear el chat.",
             callouts=[("important", "Confirmación humana", "Las acciones que llegan a otras personas (responder correos, abrir chats) siempre piden confirmación. Por defecto la opción está en «No»: hay que activarla.")])
    b3 = lab("lab-4-3", "4.3", "Prueba con 3 correos", "Demo", "6 min", "Ver qué hace con una solicitud completa, una urgente y una incompleta", "Copilot Studio (panel de prueba)",
             "Correo_1_Completo, Correo_2_Urgente y Correo_3_Incompleto", "Tres registros en la lista y respuestas pendientes de confirmar", lic=STUDIO,
             intro="Los tres correos están en el buzón de prueba. Pide al agente en el panel de prueba: «Revisa los correos nuevos del buzón de solicitudes y regístralos».",
             prompts=[(f"Correo {i}: {c['tipo']}", "Correo", f"Asunto: {c['asunto']}\n\n" + "\n".join(c["cuerpo"])) for i, c in enumerate(CORREOS, 1)],
             expect=table(["Campo", "Correo 1 · Completo", "Correo 2 · Urgente", "Correo 3 · Incompleto"],
                          [[k] + [E(str(c["esperado"][k])) for c in CORREOS] for k in CORREOS[0]["esperado"]] + [["Acciones"] + [E(c["acciones"]) for c in CORREOS]]),
             fail="Si el agente no lee el buzón, pega el texto del correo en el panel de prueba y pide: «Registra esta solicitud».")
    b4 = lab("lab-4-4", "4.4", "Publica en Teams y Microsoft 365 (y el catálogo, solo mostrar)", "Demo", "3 min", "Ver cómo llega el agente a los usuarios", "Copilot Studio", "El agente probado", "El agente disponible en Teams y Microsoft Copilot", lic=STUDIO,
             intro="<b>Publish</b> &gt; canal <b>Teams and Microsoft 365 Copilot</b> &gt; activa <b>Make agent available in Microsoft Copilot</b> &gt; <b>Save and publish</b>. Después, en <b>Availability options</b> se elige compartir con compañeros o con toda la organización, y <b>Submit to org catalog</b> envía el agente a aprobación.",
             callouts=[("note", "Solo se muestra", "El envío al catálogo de la organización requiere la aprobación de un administrador en el Centro de administración de Teams. En la sesión solo mostramos el paso."),
                       ("tip", "Etiqueta actual", "En la documentación vigente la opción dice «Make agent available in Microsoft Copilot».")])
    ch4 = chapter("ch4", "Minutos 25–42", "4. Agente 2 · Copilot Studio: Solicitudes de personal (RH)", ["17 minutos", "Copilot Studio", "Recursos Humanos"],
                  "Los gerentes piden personal temporal por correo, cada quien a su manera. El agente lee el buzón, registra cada solicitud en una lista, marca lo que falta y prepara la respuesta y el chat con RH, pero no envía nada sin confirmación y nunca decide a quién contratar.",
                  b1 + b2 + b3 + b4)

    gov = table(["Tema", "Lo que hay que saber"], [
        ["Skills en Agent Builder", "Licencia de Microsoft 365 Copilot o pago por uso; hasta 8 por agente; recién disponibles; puede que todavía no aparezcan en tu organización. Si la organización usa barreras de información, los usuarios no pueden agregar skills."],
        ["Conocimiento sin licencia", "Usuarios de Copilot Chat: instrucciones, búsqueda web, creación de documentos e imágenes. Con pago por uso: SharePoint, archivos, conectores. Correo, personas y Teams: requieren licencia."],
        ["Copilot Studio y el GitHub Copilot harness", "Los agentes de este harness consumen Copilot Credits desde que empiezas a crearlos. La licencia de Microsoft 365 Copilot permite crear agentes del harness en Copilot Studio; confirma con TI cómo se cobran los créditos."],
        ["Compartir", "Agent Builder: con personas o grupos (chat o edición) y, si TI lo permite, catálogo de la organización. Copilot Studio: publicar en Teams y Microsoft 365; el catálogo requiere aprobación de un administrador."],
        ["Controles", "Agent Builder se gobierna con los controles de agentes de Microsoft 365; Copilot Studio, con ambientes y políticas de conectores de Power Platform."],
        ["Buenas prácticas", "Dueño claro de cada agente, fuentes revisadas, confirmación humana en las acciones, sin datos sensibles y revisión periódica."]])
    ch5 = chapter("ch5", "Minutos 42–47", "5. Gobierno y licencias", ["5 minutos"], "Un agente útil es un agente gobernado: quién lo crea, con qué datos, con quién se comparte y cuánto cuesta.", f'<div class="chapter-inner">{gov}</div>')
    andi = ("<ul><li><b>Qué es:</b> «Andi», un agente de Recursos Humanos de Coca-Cola Andina construido con Microsoft Copilot Studio en su operación de Argentina.</li>"
            "<li><b>Cómo funciona:</b> los colaboradores le escriben por WhatsApp; Microsoft Entra ID autentica y aporta los datos del perfil; el contenido de RH vive en SharePoint; y si Andi no puede resolver, crea un ticket a RH con Power Automate, que RH atiende en Power Apps.</li>"
            "<li><b>Resultados:</b> 1,200 de aproximadamente 3,600 empleados activos en Argentina lo usan cada mes; casi 5,000 conversaciones, con una duración promedio de 6 min 33 s; satisfacción (CSAT) de 4.1 de 5, con 976 encuestas. Una parte importante de las preguntas llega fuera del horario de RH, cuando antes había que esperar al día siguiente.</li>"
            "<li><b>Contexto:</b> La empresa opera en Argentina, Brasil, Chile y Paraguay, con miles de empleados en oficinas y plantas embotelladoras (caso de estudio de Microsoft Learn).</li></ul>"
            '<p class="small muted">Fuentes: caso de estudio de Microsoft Learn «Coca-Cola Andina mejora el soporte de RR. HH. para el personal de primera línea con Copilot Studio» (8 de septiembre de 2026) e historia de cliente de Microsoft.</p>')
    ch6 = chapter("ch6", "Minutos 47–50", "6. Caso real: «Andi», el agente de RH de Coca-Cola Andina", ["3 minutos", "Recursos Humanos"], "Un agente de RH en producción, en una embotelladora de la región.", f'<div class="chapter-inner">{andi}</div>')
    ideas = table(["Área", "Agente que responde (Agent Builder)", "Agente que actúa o más estructura"], [list(r) for r in IDEAS])
    tpl = lab("lab-7-1", "7.1", "Plantilla de prompt para crear tu agente", "Reto", "después", "Crear tu primer agente", "Agent Builder", "Tu caso", "Tu agente en borrador",
              prompts=[("Plantilla para crear un agente", "Plantilla", PLANTILLA)], checks=["Escribí el prompt de mi agente con la plantilla.", "Probé mi agente con un caso que tiene faltantes."])
    ch7 = chapter("ch7", "Minutos 50–55", "7. Ideas por área y plantilla para tu agente", ["5 minutos"], "Empieza por una tarea que se repite, con documentos claros y un dueño.", f'<div class="chapter-inner">{ideas}</div>' + tpl)
    faq = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in FAQ)
    ch8 = chapter("ch8", "Minutos 55–60", "8. Preguntas frecuentes", ["5 minutos"], "Las dudas que más salen al empezar con agentes.", f'<div class="chapter-inner faq" id="faq">{faq}</div>')
    refs = ('<section class="card" id="refs"><h2>Referencias</h2><ul>' + "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in [
        ("Agregar skills a un agente (Agent Builder)", "https://learn.microsoft.com/es-es/microsoft-365/copilot/extensibility/agent-builder-add-skills"),
        ("Skills de agentes declarativos", "https://learn.microsoft.com/es-es/microsoft-365/copilot/extensibility/declarative-agent-skills"),
        ("Agregar conocimiento (Agent Builder)", "https://learn.microsoft.com/es-es/microsoft-365/copilot/extensibility/agent-builder-add-knowledge"),
        ("Agent Builder o Copilot Studio", "https://learn.microsoft.com/es-es/microsoft-365/copilot/extensibility/copilot-studio-experience"),
        ("Harnesses de Copilot Studio", "https://learn.microsoft.com/es-es/microsoft-copilot-studio/harnesses-overview"),
        ("Agregar herramientas en Copilot Studio", "https://learn.microsoft.com/es-es/microsoft-copilot-studio/add-tools-custom-agent"),
        ("Publicar en Teams y Microsoft 365", "https://learn.microsoft.com/es-es/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams"),
        ("Caso de estudio en Microsoft Learn: Coca-Cola Andina", "https://learn.microsoft.com/es-es/power-platform/guidance/case-studies/coca-cola-andina-hr-support"),
        ("Historia de cliente: Coca-Cola Andina", "https://www.microsoft.com/en/customers/story/26256-coca-cola-andina-microsoft-copilot-studio")]) + "</ul></section>")
    nav = '<a class="nav-top" href="#bienvenida">Bienvenida</a>' + "".join(
        f'<div class="nav-group"><a class="nav-mod" href="{h}">{t}</a>' + "".join(f'<a class="nav-lab" href="#{a}">{b}</a>' for a, b in labs) + "</div>"
        for h, t, labs in [("#ch1", "1. La escalera", []), ("#ch2", "2. Agent Builder", [("lab-2-1", "2.1 Crear"), ("lab-2-2", "2.2 Instrucciones y skills"), ("lab-2-3", "2.3 Conocimiento"),
                           ("lab-2-4-1", "2.4 Prueba 1"), ("lab-2-4-2", "2.5 Prueba 2"), ("lab-2-4-3", "2.6 Prueba 3")]), ("#ch3", "3. ¿Cuál uso?", []),
                           ("#ch4", "4. Copilot Studio", [("lab-4-1", "4.1 Cómo está hecho"), ("lab-4-2", "4.2 Agregar herramienta"), ("lab-4-3", "4.3 Probar"), ("lab-4-4", "4.4 Publicar")]),
                           ("#ch5", "5. Gobierno y licencias", []), ("#ch6", "6. Caso Andi", []), ("#ch7", "7. Ideas y plantilla", [("lab-7-1", "7.1 Plantilla")]), ("#ch8", "8. Preguntas", [])]) + \
          '<div class="nav-group"><a class="nav-mod" href="#responsable">Uso responsable</a><a class="nav-mod" href="#refs">Referencias</a></div>'
    page = f"""<!DOCTYPE html><html lang="es-MX"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light">
<title>Agentes en Microsoft 365: de la skill al agente que actúa</title><style>{CSS}</style></head><body><a class="skip" href="#bienvenida">Ir al contenido</a>
<header class="hero"><div class="eyebrow">Bootcamp &middot; TDx Bepensa &middot; Martes 10 de noviembre de 2026</div><h1>Agentes en Microsoft 365: de la skill al agente que actúa</h1>
<p>Dos agentes en vivo para Zava Bebidas: uno de Agent Builder que estandariza procedimientos de Operaciones y Calidad, y uno de Copilot Studio que registra solicitudes de personal para Recursos Humanos.</p>
<div class="tags"><span>60 minutos</span><span>Demo guiada</span><span>Agent Builder &middot; Copilot Studio</span><span>Skills</span><span>Operaciones, Calidad y RH</span><span>Datos ficticios</span></div></header>
<div class="shell"><div><button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="sideNav">Menú: secciones</button>
<nav class="side" id="sideNav" aria-label="Navegación"><div class="nav-title">Tu avance</div><div class="progress"><div class="bar"><i id="progBar"></i></div><small id="progTxt"></small></div>
<div class="controls"><button type="button" id="expandAll">Abrir todo</button><button type="button" id="collapseAll">Cerrar todo</button></div>{nav}
<div class="controls" style="margin-top:12px"><button type="button" id="resetProg">Reiniciar casillas</button></div></nav></div>
<main id="main">{welcome}{ch1}{ch2}{ch3}{ch4}{ch5}{ch6}{ch7}{ch8}{refs}<footer>Agentes en Microsoft 365 &middot; v1 &middot; Empresa y datos ficticios con fines de capacitación.</footer></main></div><script>{JS}</script></body></html>"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page)
    return len(page)


if __name__ == "__main__":
    print(build())
