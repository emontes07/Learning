# -*- coding: utf-8 -*-
"""Contenido de la guía general (index.html)."""
import html
import zdata as Z
from zdata import num, pct, pesos, hrs
from gen_files import T, CLAIMS, reporte_lines, faq

K, RAW, CLEAN, COM = Z.compute()
E = html.escape
FB, FC, ZIP = "files/1_Archivos_de_practica/", "files/2_Checkpoints/", "files/Zava_Bebidas_Archivos_Practica.zip"

TARJETA = """REGLAS (pégalas antes de tu primera pregunta en cada archivo)
1. Zava Bebidas es una empresa ficticia. Datos del Centro de Servicio Interno, enero a septiembre de 2026, regiones Norte, Centro, Golfo y Península.
2. Tercer trimestre (3T) = julio a septiembre; segundo trimestre (2T) = abril a junio.
3. Tiempo de respuesta: promedio ponderado por Solicitudes_atendidas. Satisfacción: promedio ponderado por Encuestas_respondidas. Nunca promedies promedios.
4. Antes de calcular, revisa duplicados, valores atípicos y meses faltantes. Dime qué encontraste y no corrijas nada sin decírmelo.
5. Usa fórmulas, no valores pegados, y no modifiques la hoja original.
6. Cada cifra que me des debe decir de qué hoja y columna sale. Si un dato no está en el archivo, di "no está en los datos".
7. Formato de México: punto decimal y coma de miles; porcentajes y horas con un decimal; satisfacción con dos decimales.
8. Los comentarios de encuestas son anónimos: no intentes identificar a nadie y quita los nombres de personas."""

P = {
"D": """Demo de punta a punta (el presentador lo hace en pantalla):
1. Excel: «Revisa la hoja Indicadores, dime qué problemas de datos hay y crea un resumen del 3T por región con una gráfica.»
2. Word: «Escribe un reporte de una página del 3T con base en /Zava_Notas_y_Politicas_Servicio y estas cifras: [pega la hoja Hechos].»
3. PowerPoint: «Crea una presentación de 5 diapositivas a partir de /Zava_Reporte_3T con esta plantilla.»
4. Ajuste: «Haz la diapositiva 2 más corta, agrega la gráfica de tiempo por región y escribe las notas del orador.»""",
"1.1a": """Resume mis correos de las últimas 24 horas que me piden algo. Para cada uno: quién lo pide (puesto o equipo), qué necesita y para cuándo. Ordena por urgencia y no incluyas boletines ni notificaciones automáticas.""",
"1.1b": """¿Qué acuerdos y pendientes salieron de mi última reunión sobre [tema]? Dime quién quedó responsable de cada uno y qué me toca a mí.""",
"1.1c": """Resume lo que pasó en mis chats de Teams desde ayer: decisiones, preguntas que me hicieron y que no he contestado, y archivos que me compartieron.""",
"1.2": """Busca el archivo más reciente que me compartieron sobre [tema]. Dime quién lo compartió, cuándo, y resúmelo en 3 viñetas.""",
"2.1": """Revisa la hoja Indicadores antes de analizarla. Busca: (1) renglones duplicados, (2) valores atípicos en cualquier columna (compáralos con los otros meses de la misma región) y (3) combinaciones de mes y región que falten entre enero y septiembre de 2026.
Para cada problema dime la región, el mes, la columna y el valor, y qué efecto tendría en el análisis si no lo corrijo. No cambies nada todavía.""",
"2.2a": """Crea una hoja Datos_limpios con la misma tabla que Indicadores, pero:
- sin el renglón duplicado,
- con una columna Excluir_del_tiempo que diga "Sí" en el renglón con el tiempo de respuesta atípico y "No" en los demás (no borres el valor),
- con una columna Trimestre (1T, 2T o 3T).
No modifiques la hoja Indicadores.""",
"2.2b": """Con Datos_limpios crea una hoja Resumen_3T con fórmulas: una fila por región y una fila Total, solo del 3T. Columnas: solicitudes recibidas, solicitudes atendidas, % atendidas, tiempo de respuesta ponderado por atendidas (sin los renglones con Excluir_del_tiempo = "Sí"), satisfacción ponderada por encuestas, presupuesto asignado, ejercido y % ejercido. Debajo calcula el tiempo y la satisfacción del 2T para comparar.
Después inserta una gráfica de columnas del tiempo de respuesta por región.""",
"2.2c": """Inserta una tabla dinámica con Datos_limpios: regiones en filas, meses del 3T en columnas y la suma de Solicitudes_atendidas como valores.""",
"2.3": """Crea una hoja Hechos con columnas: #, Hecho, Cifra, Unidad, Fuente (hoja y fila) y Revisado por (vacía).
Incluye, con fórmulas que apunten a Resumen_3T: solicitudes recibidas y atendidas del 3T, % atendidas, tiempo de respuesta del 3T y del 2T, tiempo de Golfo, satisfacción del 3T, del 2T y de Golfo, presupuesto asignado, ejercido y % ejercido.
Agrega un renglón que diga qué datos faltan (mes y región) para que nadie lo olvide.
Regla: nada entra al reporte ni a la presentación si no está en esta hoja.""",
"2.4": """Agrega a la hoja Comentarios una columna Tema y clasifica cada comentario en uno de estos temas: Tiempo de respuesta, Seguimiento y comunicación, Trato del personal, Portal de solicitudes u Otros.
Agrega otra columna Menciona_a_una_persona (Sí o No).
Después crea una tabla con fórmulas: número de comentarios por tema, % del total y calificación promedio.
Dime en 3 viñetas qué dicen los usuarios, sin citar comentarios que mencionen a una persona.""",
"3.1": """Escribe un reporte de una página del tercer trimestre del Centro de Servicio Interno para la dirección.
Usa solo estas cifras de la hoja Hechos: [pega aquí la hoja Hechos, columnas Hecho y Cifra]
y las notas de reuniones de /Zava_Notas_y_Politicas_Servicio.
Secciones: Resultados; Lo que explica los resultados; Calidad de los datos; Acciones para el 4T.
Máximo 4 viñetas por sección. Cada cifra igual que en Hechos; si algo no está, no lo inventes.""",
"3.2a": """Reescribe este reporte en un tono más ejecutivo y directo, sin cambiar ninguna cifra. Que quepa en media página.""",
"3.2b": """Resume el reporte en 3 líneas para un correo a la dirección.""",
"3.3": """Con la sección «Procedimiento de atención de solicitudes internas» de /Zava_Notas_y_Politicas_Servicio, escribe 5 preguntas frecuentes que haría un colaborador, con respuestas de máximo 2 líneas. Usa solo lo que dice el procedimiento; si algo no está, escribe «El procedimiento no lo indica».""",
"4.1": """Crea una presentación de 5 diapositivas a partir de /Zava_Reporte_3T con el diseño de esta plantilla: una portada, un resumen con las cifras clave, una diapositiva para la gráfica de tiempo por región, una con lo que dicen los usuarios y una con las tres acciones.
Conserva las cifras exactamente como están en el documento.""",
"4.2": """En la diapositiva 3 agrega una gráfica de columnas con el tiempo de respuesta del 3T por región: Norte, Centro, Golfo y Península. Usa las cifras de la hoja Resumen_3T de /Zava_Indicadores_Servicio_2026 y agrega una línea de texto con la meta de 24 horas.""",
"4.3a": """Haz la diapositiva 2 más corta: máximo 4 viñetas de una línea, con la cifra al inicio de cada viñeta.""",
"4.3plan": """En la diapositiva de las tres acciones, agrega la cuarta acción que aparece en /Zava_Reporte_3T (sección «Acciones para el 4T»). Usa el mismo formato que las otras viñetas y no cambies nada más.""",
"4.3b": """Actualiza la presentación con la versión nueva de /Zava_Reporte_3T: cambia solo las diapositivas donde haya diferencias y dime qué cambiaste.""",
"4.3c": """Escribe las notas del orador de cada diapositiva: 3 líneas con lo que debo decir y una posible pregunta de la dirección con su respuesta.""",
"5.1": """Escribe un correo para la dirección con el reporte y la presentación del 3T. Tono profesional y breve (máximo 120 palabras): 3 cifras clave, el problema principal (Golfo) y una petición concreta. Termina con una pregunta para confirmar en la revisión del 19 de noviembre.""",
"5.2a": """Crea la agenda de una reunión de 30 minutos para la revisión trimestral: resultados (10 min), Golfo: causas y plan (10 min), acciones y decisiones (10 min). Agrega en una línea el objetivo de la reunión.""",
"5.2b": """Escribe un mensaje corto para el canal de Teams de mi equipo con los resultados del 3T: tono cercano, 3 cifras, un reconocimiento al equipo y el reto principal. Máximo 70 palabras, sin datos de personas.""",
"5.3": """Eres un revisor independiente: no participaste en el análisis.
Revisa las 6 afirmaciones del «Borrador del mensaje al equipo (versión de un colega)» de /Zava_Notas_y_Politicas_Servicio contra la hoja Hechos de mi Excel: [pega aquí la hoja Hechos].
Para cada afirmación da un veredicto:
- Verificado: los datos confirman la cifra y la afirmación.
- Incorrecto: una cifra de los datos la contradice directamente.
- No verificable: los datos no tienen evidencia para confirmarla ni para descartarla.
- Exagerado: tiene base en los datos, pero la sobredimensiona.
Tabla: #, afirmación, veredicto, cifra correcta y fuente.""",
"6.1": """Lee mi archivo /[tu archivo de indicadores] y escribe el resumen del mes para mi jefe en 5 viñetas: volumen, tiempo de respuesta contra meta, satisfacción, la región o el tema que más preocupa y una acción. Antes, dime si hay duplicados, atípicos o meses faltantes. Cita la hoja de cada cifra.""",
"6.2a": """Analista: con el archivo adjunto Zava_Indicadores_Servicio_2026.xlsx, revisa la calidad de los datos y muéstrame la tendencia mensual del tiempo de respuesta por región con una gráfica. ¿Qué región empeoró más en el 3T y desde qué mes?""",
"6.2b": """Investigador: ¿qué prácticas recomiendan las fuentes públicas para reducir el tiempo de respuesta de una mesa de servicio interna sin aumentar el presupuesto? Dame 5 prácticas con su fuente.""",
"7.2": """Objetivo: [qué quieres obtener y para quién].
Contexto: [área, periodo y por qué lo necesitas].
Fuentes: [escribe / y elige el archivo, correo o reunión; di qué hojas o secciones usar].
Expectativas: [formato (tabla, 5 viñetas, correo), extensión, cifras con su fuente, "no está en los datos" si falta algo].
Antes de responder, hazme hasta 3 preguntas si algo no está claro.""",
}

VAR = {  # variantes por área
"2": [("Recursos Humanos", "Con la hoja de resultados de la encuesta de clima laboral (anónima), agrupa los comentarios por tema, calcula el % de cada tema y la calificación promedio por área. No muestres grupos de menos de 5 respuestas y no intentes identificar a nadie."),
      ("Comercial", "Con el reporte de visitas del mes, dime qué clientes no se visitaron en 30 días, la efectividad de las promociones por región y una gráfica de visitas por vendedor (sin calificar a las personas)."),
      ("Operaciones", "Con el registro de entregas, revisa duplicados y fechas faltantes, y crea un resumen de entregas a tiempo por CEDIS y semana con una gráfica.")],
"3": [("Recursos Humanos", "Con /[política] escribe 8 preguntas frecuentes para los colaboradores. Otra: «Redacta una descripción de puesto de Analista de Servicio Interno: objetivo, 6 responsabilidades, requisitos y competencias, con lenguaje incluyente.»"),
      ("Comercial", "Con /[reporte de visitas] escribe un resumen de una página para el gerente regional: logros, clientes en riesgo y siguientes pasos."),
      ("Operaciones", "Con /[bitácora de incidencias] escribe el procedimiento paso a paso para atender una entrega rechazada, con responsables y tiempos.")],
"4": [("Recursos Humanos", "Crea una presentación de bienvenida para nuevos ingresos a partir de /[plan de inducción]: agenda de la primera semana, a quién acudir y políticas clave."),
      ("Comercial", "Crea una presentación de resultados de la promoción del mes a partir de /[reporte], con una gráfica por región."),
      ("Operaciones", "Crea una presentación de indicadores de servicio de la semana a partir de /[reporte], con las 3 incidencias principales.")],
"5": [("Recursos Humanos", "Redacta el correo de bienvenida para un nuevo ingreso con su plan de la primera semana. Otra: «Escribe un comunicado sobre la política de trabajo híbrido en tono cercano, con las 3 reglas clave.»"),
      ("Comercial", "Redacta el correo de seguimiento a un cliente después de la visita, con los acuerdos y la fecha de la próxima visita."),
      ("Operaciones", "Redacta el aviso al equipo sobre el cambio de horario de entregas, con lo que cambia, desde cuándo y a quién preguntar.")],
}

LVL = {"Requerido": "lvl-req", "Ver y comparar": "lvl-ver", "Demo": "lvl-demo", "Opcional": "lvl-opt", "Reto": "lvl-reto"}
MODE = {"Solo chat": "mode-chat", "Plan": "mode-plan", "Edición": "mode-edit", "Copilot Chat": "mode-teams", "Outlook": "mode-outlook", "Teams": "mode-teams",
        "PowerPoint": "mode-ppt", "Word": "mode-outlook", "Analista": "mode-agent", "Investigador": "mode-agent", "Reglas": "mode-plan", "Demo": "mode-ppt"}
LIC = '<span class="req req-lic">Requiere licencia de Microsoft 365 Copilot</span>'
CHAT = '<span class="req req-m365">Funciona con Copilot Chat</span>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def dl(path, label=None): return f'<a href="{E(path)}" download>{E(label or path.split("/")[-1])}</a>'


def lab(id, n, title, level, time, goal, app, inputs, produces, lic=LIC, intro="", prompts=(), expect="", fail="", checks=(), callouts=(), nolic="", variant=None):
    meta = (f'<div class="meta"><span><b>Tiempo</b> {time}</span><span><b>Objetivo</b> {goal}</span><span><b>App</b> {app}</span><span><b>Requiere</b> {lic}</span></div>'
            f'<div class="chain"><div><span class="chain-k">Usas</span>{inputs}</div><div><span class="chain-k add">Produce para el siguiente paso</span>{produces}</div></div>')
    pr = ""
    for k, (label, mode, key) in enumerate(prompts):
        pr += (f'<div class="prompt"><div class="prompt-head"><span class="prompt-label">{E(label)}</span><span class="mode {MODE[mode]}">{mode}</span>'
               f'<button class="copy" type="button" aria-label="Copiar: {E(label)}">Copiar</button></div><pre id="p-{id}-{k}">{E(P.get(key, key))}</pre></div>')
    ex = f'<div class="callout expect"><div class="callout-title">Lo que verás</div><div>{expect}</div></div>' if expect else ""
    co = "".join(f'<div class="callout {c}"><div class="callout-title">{t}</div><div>{b}</div></div>' for c, t, b in callouts)
    nl = f'<div class="callout nolic"><div class="callout-title">Sin licencia de Microsoft 365 Copilot</div><div>{nolic}</div></div>' if nolic else ""
    va = ""
    if variant:
        va = '<div class="variant"><div class="callout-title">Variante por área</div>' + "".join(
            f'<div class="prompt"><div class="prompt-head"><span class="prompt-label">{E(a)}</span><button class="copy" type="button" aria-label="Copiar: variante {E(a)}">Copiar</button></div><pre id="p-{id}-v{i}">{E(t)}</pre></div>'
            for i, (a, t) in enumerate(VAR[variant])) + "</div>"
    fl = f'<div class="callout catchup"><div class="callout-title">Si no te sale</div><div>{fail}</div></div>' if fail else ""
    ck = ('<div class="selfcheck"><div class="callout-title">Para practicar después</div><ul>' + "".join(
        f'<li><label><input type="checkbox" data-key="{id}-{i}"> {c}</label></li>' for i, c in enumerate(checks)) + "</ul></div>") if checks else ""
    return (f'<details class="lab" id="{id}"><summary><span class="lab-num">{n}</span><span class="lab-title">{title}</span><span class="lvl {LVL[level]} lvl-sum">{level}</span></summary>'
            f'<div class="lab-body">{meta}{"<p>" + intro + "</p>" if intro else ""}{pr}{ex}{co}{nl}{va}{fl}{ck}</div></details>')


def chapter(id, num_, title, tags, story, labs, extra=""):
    t = "".join(f"<span>{x}</span>" for x in tags)
    return (f'<section class="module" id="{id}"><div class="module-head"><div class="module-num">{num_}</div><h2>{title}</h2><div class="module-tags">{t}</div></div>'
            f'<div class="story"><div class="story-label">La historia</div><p>{story}</p></div>{extra}{labs}</section>')


def ck(file, nxt): return f'Abre {dl(FC + file)} (carpeta 2_Checkpoints): tiene el resultado de este ejercicio. Compáralo con lo tuyo y continúa {nxt} con ese archivo.'


def t_problemas():
    return table(["Problema", "Dónde", "Valor", "Qué pasa si no lo corriges"], [
        ["Renglón duplicado", "Golfo · septiembre 2026", f"{T['dup']} solicitudes atendidas, dos veces", f"Las solicitudes atendidas del 3T suben a {T['sucio_a']}"],
        ["Valor atípico", "Península · julio 2026 · Tiempo_respuesta_horas", f"{T['atip']} (los otros meses rondan {T['pen_med']})", f"Con solo este problema, el tiempo promedio del 3T sube a {hrs(K['tiempo_3T_solo_atipico'])}"],
        ["Mes faltante", "Centro · agosto 2026", "No hay renglón", "El volumen y el presupuesto del 3T quedan incompletos; hay que avisarlo"]])


def t_resumen():
    rows = [[g, num(K[f"ate_3T_{g}"]), hrs(K[f"tiempo_3T_{g}"]), num(K[f"sat_3T_{g}"], 2), pct(K[f"pres_pct_3T_{g}"])] for g in Z.REG]
    rows.append(["<b>Total</b>", f"<b>{T['ate']}</b>", f"<b>{T['tiempo']}</b>", f"<b>{T['sat']}</b>", f"<b>{T['pres']}</b>"])
    return table(["Región", "Atendidas 3T", "Tiempo de respuesta", "Satisfacción", "% presupuesto ejercido"], rows)


def t_temas():
    rows = [[t, num(K[f"tema_n_{t}"]), pct(K[f"tema_n_{t}"] / K["com_total"], 0), num(K[f"tema_cal_{t}"], 1)] for t, *_ in Z.THEMES]
    return table(["Tema", "Comentarios", "% del total", "Calificación promedio"], rows)


def t_claims():
    return table(["#", "Afirmación", "Veredicto esperado", "Por qué"], [[i, E(c[0]), f"<b>{c[1]}</b>", E(c[2])] for i, c in enumerate(CLAIMS, 1)])


CASOS = [
    ("Ponerte al día con correos, chats y reuniones", "1.1", "Copilot Chat (Work IQ) · Outlook · Teams", LIC),
    ("Encontrar un archivo y resumirlo", "1.2", "Copilot Chat (Work IQ)", LIC),
    ("Revisar datos antes de analizarlos: duplicados, atípicos y faltantes", "2.1", "Excel · Copilot Chat", CHAT),
    ("Resumen con tabla dinámica y gráfica", "2.2", "Excel", LIC),
    ("Hoja Hechos: cada cifra con su fuente", "2.3", "Excel", LIC),
    ("Agrupar comentarios de una encuesta por tema", "2.4", "Excel · Copilot Chat", CHAT),
    ("Reporte de una página y cambio de tono", "3.1 · 3.2", "Word", LIC),
    ("Preguntas frecuentes de una política o procedimiento", "3.3", "Word · Copilot Chat", CHAT),
    ("Presentación desde un Word, con gráfica, ajustes y notas del orador", "4.1 · 4.2 · 4.3", "PowerPoint", LIC),
    ("Correo, agenda y mensaje al equipo, revisados antes de enviar", "5.1 · 5.2 · 5.3", "Outlook · Teams · Copilot Chat", CHAT),
]
FAQ = [
    ("¿Copilot usa mis datos para entrenar el modelo?", "Con tu cuenta de trabajo, Microsoft indica que tus indicaciones, las respuestas y los datos de tu organización no se usan para entrenar los modelos base. Aplican las políticas de seguridad y privacidad de tu empresa."),
    ("¿Qué información puede ver Copilot?", "Solo lo que tú ya tienes permiso de ver: tus correos, chats, reuniones y archivos, o los archivos que tú subes. No ve lo de otras personas si tú no tienes acceso."),
    ("¿Qué diferencia hay entre Copilot Chat y la licencia de Microsoft 365 Copilot?", "Con Copilot Chat (en el panel de Copilot aparece «M365 Copilot (Basic)») respondes con la web y con los archivos que abres o subes, y tienes acceso estándar a Copilot en apps como Excel. La licencia de Microsoft 365 Copilot («M365 Copilot (Premium)») agrega, entre otras cosas, respuestas con tus datos de trabajo (correos, chats, reuniones y archivos), programar indicaciones y los agentes Analista e Investigador. Lo que puedes hacer dentro de Excel, Word y PowerPoint con cada una también depende de la configuración de tu empresa."),
    ("¿Por qué me da una respuesta distinta a la de mi compañero?", "Copilot genera cada respuesta; el mismo prompt puede variar en redacción. Por eso pedimos cifras con fuente y revisamos antes de enviar."),
    ("¿Puedo confiar en las cifras?", "Copilot propone, tú verificas. Pide la hoja y la columna de cada cifra, revisa una a mano y guarda las cifras en una hoja Hechos."),
    ("¿Puedo usarlo con información de personas?", "Con cuidado: usa datos anónimos o agregados, solo lo necesario, y respeta las políticas de la empresa. No lo uses para decidir sobre personas (contrataciones, evaluaciones, sanciones)."),
    ("¿Funciona en español?", "Sí. Puedes escribir en español y pedirle formato de México (punto decimal y coma de miles)."),
    ("¿Tengo que guardar mis archivos en OneDrive?", "Es lo recomendable: así puedes referenciarlos con / desde Word, PowerPoint y Copilot Chat, y el historial de versiones te protege."),
    ("No veo un botón que sale en la guía, ¿qué hago?", "Las funciones llegan por etapas y TI decide qué se activa. Usa el checkpoint, sigue con el ejercicio y anótalo para preguntarlo."),
    ("¿Puedo hacer mi propio agente?", "Lo viste en la sesión de las 10:00. Primero guarda y comparte tus prompts; si lo que respondes se repite cada semana con los mismos documentos, pregunta a TI por los agentes."),
]
