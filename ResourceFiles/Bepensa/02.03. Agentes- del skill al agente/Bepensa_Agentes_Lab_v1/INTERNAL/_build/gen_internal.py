# -*- coding: utf-8 -*-
import os, html
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from zcontent import *
from build_guide import AGENDA, LADDER, FAQ, IDEAS, PLANTILLA

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_Agentes_Lab_v1"
INT, CF = os.path.join(ROOT, "INTERNAL"), os.path.join(ROOT, "CUSTOMER_FACING")
E = html.escape
CSS = """:root{--p:#1E1B4B;--s:#4338CA;--a:#F97316;--b:#d8dee9}body{margin:0;font-family:"Segoe UI",Arial;color:#172033;background:#f5f5fb;line-height:1.5}.banner{background:#b42318;color:#fff;font-weight:700;text-align:center;padding:6px}
.hero{background:linear-gradient(120deg,var(--p),var(--s) 60%,var(--a) 140%);color:#fff;padding:24px 32px}main{max-width:1250px;margin:auto;padding:20px}.card{background:#fff;border:1px solid var(--b);border-radius:14px;padding:16px 24px;margin-bottom:16px}
h2{color:var(--p)}h3{color:var(--s)}table{border-collapse:collapse;width:100%;font-size:.88rem}th,td{border-bottom:1px solid var(--b);padding:6px 8px;text-align:left;vertical-align:top}th{background:#eef0fb}
.callout{border-left:5px solid var(--a);background:#fff4ec;padding:10px 14px;border-radius:0 10px 10px 0;margin:10px 0}.warn{border-left-color:#d97706;background:#fff4df}.imp{border-left-color:#b42318;background:#ffe9e7}
.pill{border-radius:99px;padding:1px 9px;font-size:.78rem;font-weight:600}.e{background:#fde7d4;color:#9a3412}.h{background:#dcfce7;color:#166534}ul.cb{list-style:none;padding-left:4px}ul.cb li:before{content:"\\2610  ";color:var(--s)}"""
ER, HU = '<span class="pill e">Erik</span>', '<span class="pill h">Humberto</span>'


def page(title, sub, body):
    return f'<!DOCTYPE html><html lang="es-MX"><head><meta charset="utf-8"><title>{E(title)}</title><style>{CSS}</style></head><body><div class="banner">INTERNO · SOLO PRESENTADORES DE MICROSOFT · NO COMPARTIR NI PUBLICAR</div><header class="hero"><h1>{E(title)}</h1><div>{sub}</div></header><main>{body}</main></body></html>'


def tbl(h, rows): return "<table><tr>" + "".join(f"<th>{x}</th>" for x in h) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"


MINUTE = [
    ("0–5", "1. La escalera", ER, "Abrir con la frase de la skill. Mostrar los 5 escalones con el ejemplo de cada uno.", "Diapositiva o la sección 1 de la guía."),
    ("5–9", "2.1 Crear el agente con un prompt", ER, "Pegar el prompt en español en Agent Builder (Describir). Leer en voz alta las reglas que generó.", "Si tarda o no responde: abrir el agente que se dejó creado antes (copia de respaldo)."),
    ("9–12", "2.2 Instrucciones y skills", ER, "Configurar: mostrar las instrucciones y las 2 skills. Abrir un SKILL.md.", "Si no creó las skills: Configurar > Skills > Agregar y subir los .zip. Si no hay opción de skills: pegar el SKILL.md en las instrucciones y explicar que las skills están recién disponibles y puede que todavía no aparezcan en la organización."),
    ("12–15", "2.3 Conocimiento", HU, "Agregar la carpeta de SharePoint con los 5 documentos. Explicar los límites y «Usar solo las fuentes especificadas».", "Si la carpeta no aparece: mostrar la tabla de límites y seguir con las pruebas sin conocimiento."),
    ("15–18", "2.4 Prueba 1 (POE nuevo)", ER, "Pegar el prompt y el texto. Señalar en pantalla: valores conservados, [FALTA] y la leyenda.", "Si el agente falla: correr la misma prueba en Copilot Chat pegando instrucciones + SKILL.md (así se probó)."),
    ("18–20", "2.5 Prueba 2 (escalamiento)", ER, "Mostrar que los umbrales quedaron igual y que pide suplentes y aviso al CEDIS.", "Ídem."),
    ("20–22", "2.6 Prueba 3 (Word)", HU, "Mostrar el documento de Word que genera y la lista de vacíos.", "Si no crea el Word: pedir el contenido en el chat y copiarlo a Word."),
    ("22–25", "3. ¿Cuál uso?", HU, "Recorrer la tabla de decisión: «por lo que hace, no por cuántas personas».", "—"),
    ("25–29", "4.1 Cómo está construido", HU, "Agente ya creado en Copilot Studio: instrucciones, herramientas, lista. Explicar por qué no está «Send an email».", "Si el ambiente no carga: capturas de pantalla preparadas."),
    ("29–33", "4.2 Agregar herramienta en vivo", HU, "Tools > agregar Microsoft Teams · Create a chat; activar «Ask the end user before running».", "Si el conector pide conexión y falla: mostrar la herramienta ya agregada en el agente de respaldo."),
    ("33–39", "4.3 Probar con 3 correos", HU, "Correo 1, 2 y 3: mostrar el registro en la lista, la urgencia, lo que falta y la confirmación.", "Si no lee el buzón: pegar el correo en el panel de prueba. Si no crea el elemento: mostrar la tabla de resultados esperados."),
    ("39–42", "4.4 Publicar (catálogo solo mostrar)", HU, "Publish > Teams and Microsoft 365 Copilot > «Make agent available in Microsoft Copilot» > Save and publish. Availability options > Submit to org catalog (sin enviar).", "Si publicar tarda: mostrar el agente ya publicado en Teams."),
    ("42–47", "5. Gobierno y licencias", ER, "Skills: licencia o pago por uso. Créditos del harness. Compartir y catálogo. Confirmación humana.", "—"),
    ("47–50", "6. Caso Andi", ER, "Contar el caso con las cifras de Microsoft Learn: 1,200 de ~3,600 empleados activos en Argentina al mes, casi 5,000 conversaciones (6 min 33 s en promedio), CSAT 4.1 de 5 con 976 encuestas, muchas preguntas fuera del horario de RH. WhatsApp, Entra ID, SharePoint y ticket a RH.", "Fuente: caso de estudio de Microsoft Learn del 8 de septiembre de 2026."),
    ("50–55", "7. Ideas y plantilla", "Ambos", "Pedir a RH una idea y armar el prompt con la plantilla en voz alta.", "—"),
    ("55–60", "8. Preguntas", "Ambos", "Empezar por «¿qué es el GitHub Copilot harness?».", "—"),
]
UI = [("Agent Builder · entrada", "Agentes > Nuevo agente; pestañas Describir / Configurar / Pruébelo", "Doc: «Agents & Skills > New agent»; es-ES: «Agentes & Aptitudes > Nuevo agente». Confirmar en la interfaz en español."),
      ("Agent Builder · skills", "Configurar > Skills > Agregar", "es-ES traduce «Skills» como «Aptitudes». Confirmar."),
      ("Agent Builder · «Attachments»", "Mencionado como «visto en pantalla»", "La doc vigente todavía dice «Uploaded files». No afirmarlo como cambio oficial."),
      ("Agent Builder · usa todo lo que Copilot puede", "No se afirma en la guía", "La doc no lo dice así: correo, personas y Teams se agregan como conocimiento y requieren licencia."),
      ("Agent Builder · crear documentos", "Create documents, charts, and code", "Verificado (Code interpreter)."),
      ("Copilot Studio · agregar herramienta", "Tools > Add a tool", "Nombre del botón no verificado; confirmar en la nueva experiencia."),
      ("Copilot Studio · confirmación", "Ask the end user before running", "Verificado (por defecto «No»). es-ES: «Pregunte al usuario final antes de ejecutar»."),
      ("Copilot Studio · publicar", "Teams and Microsoft 365 Copilot > Make agent available in Microsoft Copilot", "La etiqueta vigente dice «Microsoft Copilot» (no «Microsoft 365 Copilot»). El nombre del canal: confirmar."),
      ("Copilot Studio · catálogo", "Availability options > Submit to org catalog", "Aprobación en el Centro de administración de Teams (Manage apps).")]
DRY = [("Prueba 1 · POE nuevo (Copilot Chat con instrucciones + SKILL.md pegados) · prueba aproximada", "Conservó los 13 valores; marcó código, supervisión y aprobación, EPP, frecuencia, acción correctiva para ATP y control de cambios; no inventó EPP, frecuencia ni acciones. Leyenda y cierre correctos."),
       ("Prueba 2 · Reordenar escalamiento · prueba aproximada", "Conservó los 12 elementos (10.8 a 11.2 °Bx, 2 y 3 lecturas, 15 y 30 minutos, «Retenido-Calidad», ESC-BRX-01, canal y llamada). Marcó código, suplentes, aviso a distribución, disposición del producto y control de cambios. «Quién reinicia la línea» lo cubrió parcialmente (preguntó quién la detiene). No agregó niveles ni tiempos."),
       ("Prueba 3 · Evaluación de vacíos en Word · prueba aproximada", "Generó un documento de Word (Evaluacion_de_vacios_POE-ALM-007.docx). Marcó límite de humedad, responsables del muestreo, qué hacer si no cumple, la ambigüedad de los 90 min y control de cambios. No inventó límite de humedad ni el contenido de F-ALM-07B. No mencionó la revisión de limpieza del camión."),
       ("Agent Builder real (crear con prompt, skills automáticas, conocimiento)", "Sin probar: no se crean agentes en ningún tenant (instrucción del cliente)."),
       ("Copilot Studio (herramientas, correos, publicación)", "Sin probar: preparar en el tenant de demo.")]


def guide():
    body = f"""<div class="card"><h2>Resumen</h2><p>Sesión de agentes, martes 10 de noviembre de 2026, TDx Bepensa. 60 minutos, demo en vivo. Público general con RH; puede que no hayan ido a otras sesiones. Hora de la sesión por confirmar.</p>
<p><b>Propuesta de roles:</b> {ER} conduce la escalera, Agent Builder (crear, skills y pruebas 1–2), gobierno y el caso Andi. {HU} conduce conocimiento, la prueba 3, la tabla de decisión y todo Copilot Studio. Quien no conduce maneja la segunda pantalla con los planes B listos.</p>
<div class="callout imp">No crear agentes, listas ni conexiones en ningún tenant hasta que se defina el tenant de demo. Todo lo que dice «antes de la sesión» se prepara ahí, no en el tenant de Bepensa.</div></div>
<div class="card"><h2>Minuto a minuto</h2>{tbl(["Minuto", "Bloque", "Conduce", "Qué se hace", "Plan B"], MINUTE)}<p>Total: {sum(b - a for a, b, *_ in AGENDA)} minutos.</p></div>
<div class="card"><h2>Preparación antes de la sesión (tenant de demo)</h2><ul class="cb">
<li>Agente 1 creado como respaldo (con instrucciones, 2 skills y la carpeta de conocimiento) por si la creación en vivo tarda.</li>
<li>Carpeta de SharePoint «Procedimientos vigentes» con los 5 documentos de 3_Conocimiento_SharePoint.</li>
<li>Agente 2 construido en Copilot Studio (nueva experiencia): Get emails (V3), Reply to email (V3), Create item, Search for users (V2); sin Send an email. Create a chat se agrega en vivo.</li>
<li>Lista «{LISTA}» con el esquema del CSV; usuarios de demo para Search for users.</li>
<li><b>Buzón de prueba y fechas de los correos:</b> el <b>Correo 2 (urgente) debe llegar el lunes 9 de noviembre</b>: dice «desde mañana», inicia el 10 y la regla de urgencia es inicio a menos de 72 horas de la fecha del correo. Si se envía otro día, ajustar las fechas del correo (inicio al día siguiente del envío). El <b>Correo 1 y el Correo 3 pueden enviarse antes</b>.</li>
<li><b>Copilot Credits:</b> construir, probar y evaluar el agente consume Copilot Credits. Conviene construirlo una sola vez y probarlo lo justo (una corrida por correo en el ensayo).</li>
<li>Capturas de pantalla de cada paso como último recurso.</li></ul></div>
<div class="card"><h2>Por qué quitamos «Send an email»</h2><p>{E(SEND_EMAIL_DECISION)}</p></div>
<div class="card"><h2>Nombres de la interfaz</h2>{tbl(["Dónde", "En la guía", "Estado"], UI)}</div>
<div class="card"><h2>Pruebas</h2>{tbl(["Prueba", "Resultado"], DRY)}</div>
<div class="card"><h2>Mensajes que hay que cuidar</h2><ul><li>Andi: usar las cifras del caso de estudio de Microsoft Learn (8 de septiembre de 2026): 1,200 de aproximadamente 3,600 empleados activos en Argentina lo usan cada mes; casi 5,000 conversaciones con duración promedio de 6 min 33 s; CSAT de 4.1 de 5 con 976 encuestas; una parte importante de las preguntas llega fuera del horario de RH. Contexto: La empresa opera en Argentina, Brasil, Chile y Paraguay, con miles de empleados en oficinas y plantas embotelladoras (caso de estudio de Microsoft Learn).</li>
<li>Licencias del harness: «consume Copilot Credits»; la documentación dice que la licencia de Microsoft 365 Copilot permite crear agentes del harness, pero también que se cobran créditos desde que se empieza a crear. No prometer que está «incluido».</li>
<li>«Usar solo las fuentes especificadas»: prioriza, no bloquea.</li><li>El GitHub Copilot harness no es el servicio GitHub Copilot.</li></ul></div>"""
    open(os.path.join(INT, "Guia_Presentador_INTERNAL.html"), "w", encoding="utf-8").write(page("Guía del presentador · Sesión de agentes", "TDx Bepensa · martes 10 de noviembre de 2026 · 60 minutos", body))


def tenant():
    items = [("Agent Builder", ["Con una cuenta con licencia: ¿aparece Agentes > Nuevo agente? ¿Con qué nombres en español (Agentes & Aptitudes, Describir, Configurar, Pruébelo)?",
                                "Pegar el prompt en español: ¿crea las 2 skills solo? ¿Las instrucciones quedan en español?", "Subir los 2 .zip de skills (plan B). ¿Hay barreras de información que impidan agregar skills?",
                                "Agregar la carpeta de SharePoint de conocimiento. ¿Cómo se llama hoy «Uploaded files» / «Attachments»?", "Correr las Pruebas 1, 2 y 3 y compararlas con el libro de respuestas.", "¿La prueba 3 crea el archivo de Word?"]),
             ("Copilot Studio", ["¿La nueva experiencia (GitHub Copilot harness) está disponible en el ambiente? ¿Hay Copilot Credits asignados?", "Crear las conexiones de Outlook, SharePoint, Office 365 Users y Teams con la cuenta de demo.",
                                 "Agregar Create a chat en vivo y activar «Ask the end user before running».", "Probar los 3 correos y comparar con los resultados esperados.", "Publicar en Teams and Microsoft 365 Copilot; revisar la etiqueta «Make agent available in Microsoft Copilot».",
                                 "Abrir Availability options y llegar a Submit to org catalog sin enviarlo."]),
             ("Gobierno", ["¿Quién puede crear y compartir agentes en el tenant de Bepensa?", "¿Hay pago por uso configurado para usuarios sin licencia?", "¿Quién aprueba el catálogo de la organización?"]),
             ("Salón", ["Proyector con dos pantallas; navegador con sesión iniciada en el tenant de demo; capturas de respaldo."])]
    body = '<div class="callout imp">Probar en el tenant de demo antes del martes. No crear nada en el tenant de Bepensa sin autorización de TDx.</div>' + "".join(
        f"<div class='card'><h2>{t}</h2><ul class='cb'>" + "".join(f"<li>{E(x)}</li>" for x in xs) + "</ul></div>" for t, xs in items)
    open(os.path.join(INT, "Pruebas_Tenant_INTERNAL.html"), "w", encoding="utf-8").write(page("Lista de pruebas en el tenant", "Sesión de agentes", body))


def answer_book():
    wb = Workbook(); H = Font(bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor="1E1B4B"); W = Alignment(wrap_text=True, vertical="top")
    ws = wb.active; ws.title = "Leeme"; ws["A1"] = "Libro de respuestas · INTERNO"; ws["A1"].font = Font(bold=True, size=14, color="B42318")
    ws["A3"] = "Cada prueba: qué debe conservar el agente sin cambios, qué debe marcar como faltante y qué indicaría que inventó algo."
    for i, p in enumerate(PRUEBAS, 1):
        s = wb.create_sheet(f"Prueba_{i}")
        for j, h in enumerate(["Debe conservar sin cambios", "Debe marcar como faltante", "Señal de que inventó algo"], 1): c = s.cell(1, j, h); c.font = H; c.fill = HF
        n = max(len(p["conservar"]), len(p["faltantes"]), len(p["invento"]))
        for r in range(n):
            for j, k in enumerate(["conservar", "faltantes", "invento"], 1):
                if r < len(p[k]): s.cell(r + 2, j, p[k][r]).alignment = W
        for c_ in "ABC": s.column_dimensions[c_].width = 55
    s = wb.create_sheet("Agente2_Correos")
    keys = list(CORREOS[0]["esperado"].keys())
    for j, h in enumerate(["Campo"] + [c["tipo"] for c in CORREOS], 1): c = s.cell(1, j, h); c.font = H; c.fill = HF
    for r, k in enumerate(keys + ["Acciones"], 2):
        s.cell(r, 1, k)
        for j, c in enumerate(CORREOS, 2): s.cell(r, j, str(c["esperado"].get(k, c["acciones"]) if k != "Acciones" else c["acciones"])).alignment = W
    for c_, w in zip("ABCD", (20, 40, 40, 40)): s.column_dimensions[c_].width = w
    s = wb.create_sheet("Limites_verificados")
    for j, h in enumerate(["Dato", "Valor", "Fuente"], 1): c = s.cell(1, j, h); c.font = H; c.fill = HF
    for r, row in enumerate(LIMITES, 2):
        for j, v in enumerate(row, 1): s.cell(r, j, v)
    for c_, w in zip("ABC", (50, 20, 90)): s.column_dimensions[c_].width = w
    wb.save(os.path.join(INT, "Libro_Respuestas_INTERNAL.xlsx"))


L5 = "https://learn.microsoft.com/es-es/power-platform/guidance/case-studies/coca-cola-andina-hr-support"
L1, L2, L3, L4 = ("https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills", "https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge",
                  "https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview", "https://www.microsoft.com/en/customers/story/26256-coca-cola-andina-microsoft-copilot-studio")
LIMITES = [("Skills por agente", "8", L1), ("Tamaño máximo del .zip de una skill", "50 MB", L1), ("Tamaño máximo por archivo dentro del .zip", "25 MB", L1), ("Instrucciones de una skill", "menos de 20,000 caracteres", L1),
           ("Instrucciones del agente", "8,000 caracteres", L1), ("Archivos de SharePoint", "100", L2), ("Listas de SharePoint", "1", L2), ("Archivos de OneDrive", "50", L2), ("Archivos subidos", "20", L2),
           ("Sitios web", "4", L2), ("Chats de Teams", "5", L2), ("Reuniones de Teams", "5", L2), ("Andi: usuarios al mes", "1,200 de ~3,600 empleados activos en Argentina", L5), ("Andi: conversaciones", "casi 5,000; duración promedio 6 min 33 s", L5), ("Andi: CSAT", "4.1 de 5 (976 encuestas)", L5)]


def handout():
    d = Document(); st = d.styles["Normal"]; st.font.name = "Segoe UI"; st.font.size = Pt(9.5)
    for s in d.sections: s.left_margin = s.right_margin = Cm(1.6); s.top_margin = s.bottom_margin = Cm(1.3)
    h = d.add_heading("Agentes en Microsoft 365: de la skill al agente que actúa", 0)
    for r in h.runs: r.font.color.rgb = RGBColor(0x1E, 0x1B, 0x4B); r.font.size = Pt(20)
    d.add_paragraph("Una skill es un buen prompt escrito una vez. La escalera: prompt → prompt guardado → skill → agente → agente que actúa.")
    t = d.add_table(rows=1, cols=3); t.style = "Light Grid Accent 1"
    for c, x in zip(t.rows[0].cells, ["Escalón", "Qué es", "Ejemplo"]): c.text = x
    for n, de, ex in LADDER:
        r = t.add_row().cells; r[0].text, r[1].text, r[2].text = n, de, ex
    d.add_heading("¿Agent Builder o Copilot Studio?", 2)
    for x in ["Agent Builder: instrucciones, skills y documentos de Microsoft 365; crea documentos y gráficos. Empieza aquí.", "Copilot Studio: cuando el agente debe actuar en otros sistemas (correo, listas, Teams), con flujos o canales externos. Consume Copilot Credits.",
              "Elige por lo que el agente hace, no por cuántas personas lo usan."]: d.add_paragraph(x, style="List Bullet")
    d.add_heading("Datos clave (Microsoft Learn, noviembre de 2026)", 2)
    for x in ["Skills: hasta 8 por agente, .zip de hasta 50 MB con SKILL.md en la raíz; requieren licencia de Microsoft 365 Copilot o pago por uso; recién disponibles; puede que todavía no aparezcan en tu organización.",
              "Instrucciones del agente: hasta 8,000 caracteres.", "Conocimiento: 100 archivos de SharePoint, 1 lista, 50 de OneDrive, 20 subidos, 4 sitios web, 5 chats y 5 reuniones.",
              "«Usar solo las fuentes especificadas» da prioridad a tus fuentes; no bloquea el conocimiento general.", "Copilot Studio: activa «Ask the end user before running» en las herramientas que llegan a otras personas."]:
        d.add_paragraph(x, style="List Bullet")
    d.add_heading("Plantilla para crear tu agente", 2)
    p = d.add_paragraph(PLANTILLA); p.runs[0].font.size = Pt(9)
    d.add_heading("Ideas por área", 2)
    t = d.add_table(rows=1, cols=3); t.style = "Light Grid Accent 1"
    for c, x in zip(t.rows[0].cells, ["Área", "Agente que responde", "Agente que actúa"]): c.text = x
    for a, b, c in IDEAS:
        r = t.add_row().cells; r[0].text, r[1].text, r[2].text = a, b, c
    d.add_heading("Para Recursos Humanos", 2)
    for x in ["Preguntas frecuentes de políticas con las políticas como conocimiento.", "Registro de solicitudes de personal con confirmación humana antes de responder o abrir chats.",
              "Un agente no decide sobre personas (contratar, evaluar, sancionar) y no usa datos personales sensibles.", "Caso real: «Andi», agente de RH de Coca-Cola Andina en Copilot Studio, por WhatsApp: 1,200 de ~3,600 empleados activos en Argentina lo usan cada mes; CSAT de 4.1 de 5 (caso de estudio de Microsoft Learn, septiembre de 2026)."]:
        d.add_paragraph(x, style="List Bullet")
    d.add_heading("Uso responsable", 2)
    d.add_paragraph("Dueño claro para cada agente, fuentes revisadas, borradores marcados como «BORRADOR - NO CONTROLADO», confirmación humana en las acciones y nada de datos sensibles. Los nombres de los botones pueden variar según la versión y el idioma.")
    cp = d.core_properties; cp.author = "Zava Bebidas (ficticio)"; cp.last_modified_by = "Zava Bebidas (ficticio)"; cp.title = "Agentes en Microsoft 365"; cp.comments = ""
    path = os.path.join(CF, "Agentes_Hoja_para_llevar.docx"); d.save(path); return path


if __name__ == "__main__":
    guide(); tenant(); answer_book(); print(handout())
