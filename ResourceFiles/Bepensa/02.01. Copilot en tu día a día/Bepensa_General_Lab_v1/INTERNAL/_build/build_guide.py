# -*- coding: utf-8 -*-
import os
from content import *

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_General_Lab_v1"
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, "collab_style.css"), encoding="utf-8").read()
JS = open(os.path.join(HERE, "collab_script.js"), encoding="utf-8").read()
JS = JS.replace("bepensa-colaboracion-v1", "zava-general-lab-v1").replace("' of '+boxes.length+' casillas completadas'", "' de '+boxes.length+' casillas completadas'")
JS = JS.split("document.querySelectorAll('.fac')")[0]
CSS += """
.lvl{display:inline-block;font-size:.74rem;font-weight:700;border-radius:99px;padding:2px 10px;letter-spacing:.02em}
.lvl-req{background:#4338CA;color:#fff}.lvl-ver{background:#e0e7ff;color:#3730a3}.lvl-demo{background:#fde7d4;color:#9a3412}.lvl-opt{background:#eef2f7;color:#334155}.lvl-reto{background:#1E1B4B;color:#fdba74}
.lvl-sum{margin-left:6px}
.legend{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0}.legend div{flex:1 1 200px;background:#f7f9fc;border:1px solid var(--border);border-radius:10px;padding:8px 12px;font-size:.92rem}
.rule{background:linear-gradient(120deg,#1E1B4B,#4338CA);color:#fff;border-radius:14px;padding:14px 20px;margin:12px 0;font-size:1.05rem}.rule b{color:#fdba74}
.nolic{background:#eef2f7;border-color:#64748b}
.variant{border:1px dashed #F97316;background:#fffaf5;border-radius:12px;padding:10px 14px;margin:12px 0}.variant .prompt{margin:8px 0}
"""

STORY = ("Eres líder del Centro de Servicio Interno de Zava Bebidas, una empresa ficticia. Tu área atiende las solicitudes de los colaboradores en 4 regiones. "
         "El jueves 19 de noviembre presentas la revisión del tercer trimestre a la dirección y tienes lo de siempre: un Excel con indicadores, un Excel con comentarios de una encuesta, "
         "un Word con notas y el procedimiento, y una plantilla de PowerPoint. Hoy vas de los datos a la presentación, y a los correos que siguen, con Copilot en cada paso.")
AGENDA = [("12:00–12:05", "#ch0", "0. Arranque", "Archivos y reglas listos"), ("12:05–12:12", "#chD", "La demo completa", "Ver el recorrido de punta a punta"),
          ("12:12–12:20", "#ch1", "1. Ponte al día", "Tus pendientes (opcional, con tus datos)"), ("12:20–12:45", "#ch2", "2. Excel: revisa, analiza y documenta", "Hoja Hechos y temas de la encuesta"),
          ("12:45–13:03", "#ch3", "3. Word: el reporte", "Reporte de una página y preguntas frecuentes"), ("13:03–13:25", "#ch4", "4. PowerPoint: la presentación", "Presentación con gráfica y notas"),
          ("13:25–13:38", "#ch5", "5. Outlook y Teams", "Correo, agenda y mensaje revisados"), ("13:38–13:45", "#ch6", "6. Lleva tus prompts", "Tus prompts guardados"),
          ("13:45–14:00", "#ch7", "7. Preguntas y trae tu caso", "Tu caso encaminado")]
FILES = [("Zava_Indicadores_Servicio_2026.xlsx", "Ejercicio 2: indicadores por mes y región (sin revisar)", "xl"),
         ("Zava_Encuesta_Servicio_3T2026.xlsx", "Ejercicio 2.4: comentarios anónimos de la encuesta", "xl"),
         ("Zava_Notas_y_Politicas_Servicio.docx", "Ejercicios 3 y 5: notas de reuniones, procedimiento, política de trabajo híbrido y el borrador de un colega", "wd"),
         ("Zava_Plantilla_Revision.pptx", "Ejercicio 4: plantilla de la presentación", "pp")]
CKS = [("CHECKPOINT_Ej2_Resultado_Excel.xlsx", "Resultado del ejercicio 2: Datos_limpios, Resumen_3T, Hechos y temas de la encuesta"),
       ("CHECKPOINT_Ej3_Resultado_Reporte.docx", "Resultado del ejercicio 3: reporte y preguntas frecuentes"),
       ("CHECKPOINT_Ej4_Resultado_Presentacion.pptx", "Resultado del ejercicio 4: presentación con gráfica y notas"),
       ("CHECKPOINT_Ej5_Resultado_Correos.docx", "Resultado del ejercicio 5: correo, agenda, mensaje y revisión")]
ICON = {"xl": ("X", "#1d6f42"), "wd": ("W", "#185abd"), "pp": ("P", "#c43e1c")}
NOLIC_FILE = "Sube el archivo a Copilot Chat (en la aplicación Microsoft Copilot, <b>+</b> y la opción para cargar archivos) y usa el mismo prompt. Copia el resultado y pégalo en tu archivo."


def welcome():
    sm = "".join(f'<a class="sm-step" href="#ch{i}"><b>{i}</b><span>{t}</span></a>' for i, t in enumerate(["Ponte al día", "Excel", "Word", "PowerPoint", "Outlook y Teams", "Tus prompts"], 1))
    ag = table(["Hora (Mérida)", "Bloque", "Te llevas"], [[h, f'<a href="{a}">{t}</a>', y] for h, a, t, y in AGENDA])
    legend = ('<div class="legend"><div><span class="lvl lvl-req">Requerido</span> Lo haces en la sesión.</div><div><span class="lvl lvl-ver">Ver y comparar</span> Lo vemos en pantalla y comparas con el checkpoint.</div>'
              '<div><span class="lvl lvl-demo">Demo</span> Solo observar.</div><div><span class="lvl lvl-opt">Opcional</span> Si te sobra tiempo o después.</div><div><span class="lvl lvl-reto">Reto</span> Para quien va adelante.</div></div>')
    lic = (f'<div class="legend"><div>{LIC} Usa funciones de la licencia (tus correos, chats, reuniones y archivos, o funciones avanzadas dentro de la app). Si no te aparece algo, usa la ruta con Copilot Chat.</div>'
           f'<div>{CHAT} Lo puedes hacer subiendo el archivo a Copilot Chat, aunque no tengas licencia.</div></div>')
    return f"""<section class="card" id="bienvenida"><h2>Bienvenida</h2><p class="lead">{STORY}</p><div class="storymap">{sm}</div>
<h3>Agenda (12:00 a 14:00, hora de Mérida)</h3>{ag}<h3>Cómo leer cada ejercicio</h3>{legend}
<p>Cada ejercicio dice qué archivos usas, qué produce para el siguiente paso, los prompts con botón <b>Copiar</b>, <b>Lo que verás</b> y <b>Si no te sale</b>, con un checkpoint para alcanzar al grupo. Los ejercicios 2 a 5 traen una <b>variante por área</b> (Recursos Humanos, Comercial y Operaciones).</p>
<h3>¿Tienes licencia?</h3>{lic}<p><b>¿Cómo sé cuál tengo?</b> Abre Copilot en Excel y busca la etiqueta en el panel de Copilot: <b>M365 Copilot (Premium)</b> significa que tienes licencia de Microsoft 365 Copilot; <b>M365 Copilot (Basic)</b> significa que tienes Copilot Chat, con acceso estándar a Copilot en Excel. Con Basic intenta los ejercicios dentro de Excel, Word y PowerPoint; si una función no te aparece, usa la ruta con Copilot Chat que trae cada ejercicio. Lo que sí requiere licencia: responder con tus datos de trabajo (correos, chats, reuniones y archivos, ejercicios 1.1 y 1.2), programar indicaciones y los agentes Analista e Investigador.</p>
<div class="rule"><b>Copilot propone, tú verificas.</b> Copilot te lleva rápido a un buen borrador; tú respondes por lo que envías. Por eso revisamos los datos al inicio y el mensaje al final.</div>
<div class="callout important" id="responsable"><div class="callout-title">Uso responsable</div><div><ul><li>No subas datos personales sensibles (salud, salario de una persona, datos de contacto personales, evaluaciones individuales) a menos que la política de tu área lo permita y sea necesario.</li><li>Trabaja con datos anónimos o agregados; quita nombres antes de compartir resultados.</li><li>No uses Copilot para tomar decisiones sobre personas (contratar, evaluar, promover o sancionar). Puede ayudarte a redactar y ordenar información; la decisión y la responsabilidad son tuyas.</li><li>Revisa cada cifra y cada afirmación antes de enviar.</li></ul></div></div>
<div class="callout note"><div class="callout-title">Datos ficticios</div><div>Zava Bebidas, sus regiones, comentarios y cifras son ficticios. Los mismos prompts funcionan con tus archivos reales guardados en el OneDrive o SharePoint de la empresa.</div></div></section>"""


def file_card(name, desc, kind):
    t, c = ICON[kind]
    return f'<a class="file" href="{FB}{name}" download><span class="xl" style="background:{c}">{t}</span><span><b>{name}</b><br><small>{desc}</small></span></a>'


def ch0():
    files = "".join(file_card(*f) for f in FILES)
    cks = table(["Archivo", "Para qué"], [[dl(FC + f), d] for f, d in CKS])
    labs = lab("lab-0-1", "0.1", "Descarga los archivos y ábrelos desde OneDrive", "Requerido", "3 min", "Todo listo para trabajar", "OneDrive · Excel", "El paquete de archivos", "Tus archivos en OneDrive", lic=CHAT,
               intro=f'<a class="btn-dl" href="{ZIP}" download>Descargar todos los archivos (.zip)</a> o uno por uno:</p><div class="files">{files}</div><p>',
               expect="<ol><li>Descomprime el .zip y sube la carpeta a tu <b>OneDrive</b> (por ejemplo, <i>Copilot Practica</i>).</li><li>Abre <b>Zava_Indicadores_Servicio_2026.xlsx</b> desde OneDrive y verifica que <b>Autoguardado</b> esté activo.</li><li>Abre Copilot con el <b>icono de Copilot</b> en la esquina inferior derecha de Excel (o <b>Alt + C</b>).</li></ol>",
               nolic="Abre la aplicación Microsoft Copilot en el navegador. En cada ejercicio vas a subir el archivo con <b>+</b> y la opción para cargar archivos.",
               fail="Si no puedes subir a OneDrive, trabaja los archivos en tu equipo y súbelos a Copilot Chat cuando el ejercicio lo pida.",
               checks=["Subí la carpeta a OneDrive y abrí Copilot."])
    labs += lab("lab-0-2", "0.2", "Datos de trabajo o web, y la tarjeta de reglas", "Requerido", "2 min", "Saber con qué información responde Copilot", "Aplicación Microsoft Copilot · Excel",
                "Lo que viste en Arte del prompting", "La tarjeta de reglas pegada en tu chat", lic=CHAT,
                intro="En la aplicación Microsoft Copilot hay dos formas de responder: con tus <b>datos de trabajo</b> (pestaña <b>Work IQ</b>: correos, chats, reuniones y archivos; requiere licencia de Microsoft 365 Copilot) o con la <b>web</b> (información pública). Elige según tu pregunta: «¿qué me pidió mi jefe?» es de trabajo; «¿qué es un indicador de nivel de servicio?» es de web. Dentro de Excel, Word y PowerPoint, Copilot trabaja con el archivo abierto: pega esta tarjeta al inicio de cada chat.",
                prompts=[("Tarjeta de reglas", "Reglas", TARJETA)],
                callouts=[("tip", "Los tres modos de Copilot en Excel", "<b>Modo de solo chat</b>: responde sin cambiar el libro. <b>Modo Plan</b>: te muestra los pasos antes de hacerlos. <b>Modo de edición</b> (predeterminado): crea hojas y fórmulas; <b>Ctrl + Z</b> deshace. Cambia de modo con el botón junto al cuadro de chat o <b>Ctrl + Mayús + M</b>.")],
                checks=["Pegué la tarjeta de reglas al inicio del chat."])
    return chapter("ch0", "Arranque", "0. Arranque", ["5 minutos", "OneDrive", "Copilot"], "Antes del primer número: los archivos en la nube, Copilot abierto y unas reglas para que cada respuesta use las mismas definiciones.", labs,
                   f'<div class="chapter-inner"><h3>Checkpoints para alcanzar al grupo</h3>{cks}</div>')


def chD():
    labs = lab("lab-d", "Demo", "De un Excel a una presentación ajustada con un prompt", "Demo", "7 min", "Ver el recorrido completo antes de hacerlo", "Excel · Word · PowerPoint",
               "Los 4 archivos de práctica", "La idea de todo lo que vas a hacer hoy",
               intro="El presentador hace el recorrido completo en pantalla. Tú solo observa: después lo haces paso a paso en los ejercicios 2 a 4.",
               prompts=[("Los 4 prompts de la demo", "Demo", "D")],
               expect="Un Excel revisado con su resumen y gráfica, un reporte de una página en Word y una presentación de 5 diapositivas con la plantilla, que se ajusta con un prompt.")
    return chapter("chD", "Demo", "La demo completa", ["7 minutos", "Excel → Word → PowerPoint"], "«Tengo un Excel, lo combino con un PowerPoint, voy a Word, hago un prompt y me ajusta la presentación.» Así se ve el recorrido de punta a punta.", labs)


def ch1():
    labs = lab("lab-1-1", "1.1", "Resume tus correos, chats y reuniones", "Opcional", "5 min", "Saber qué te toca hoy en un minuto", "Aplicación Microsoft Copilot (Work IQ) · Outlook · Teams",
               "Tus propios correos, chats y reuniones", "Tu lista de pendientes",
               intro="Este ejercicio usa <b>tus datos reales</b>. Hazlo solo si te sientes cómodo; nadie ve tu pantalla. Cambia lo que está entre [corchetes].",
               prompts=[("Correos que me piden algo", "Copilot Chat", "1.1a"), ("Acuerdos de una reunión", "Copilot Chat", "1.1b"), ("Mis chats desde ayer", "Copilot Chat", "1.1c")],
               expect="Respuestas con tus propios correos, reuniones y chats. Copilot solo ve lo que tú ya puedes ver.",
               callouts=[("tip", "Prompts seguros", "Pide resúmenes de lo tuyo y evita pedir información de otras personas. Si una respuesta incluye algo sensible, no la compartas.")],
               nolic="Copilot Chat sin licencia no lee tus correos ni tus chats. Usa el resumen dentro de Outlook (<b>Resumen por Copilot</b>, si está disponible) o pasa al ejercicio 2.",
               checks=["Resumí mis pendientes con un prompt."])
    labs += lab("lab-1-2", "1.2", "Encuentra un archivo y resúmelo", "Opcional", "3 min", "Dejar de buscar archivos a mano", "Aplicación Microsoft Copilot (Work IQ)", "Tus archivos de OneDrive y SharePoint", "El archivo y su resumen",
                prompts=[("Buscar y resumir", "Copilot Chat", "1.2")], nolic="Abre el archivo y súbelo a Copilot Chat para resumirlo.",
                checks=["Encontré un archivo con Copilot."])
    return chapter("ch1", "Paso 1", "1. Ponte al día", ["8 minutos", "Opcional", "Tus datos"], "Antes de preparar la revisión, te pones al día con lo que llegó desde ayer.", labs)


def ch2():
    labs = lab("lab-2-1", "2.1", "Revisa los datos antes de analizarlos", "Requerido", "6 min", "Encontrar los errores antes de que lleguen a la dirección", "Excel",
               "Zava_Indicadores_Servicio_2026.xlsx", "La lista de problemas de datos", lic=CHAT,
               intro="Abre el Excel, pega la tarjeta de reglas y usa el <b>modo de solo chat</b>.",
               prompts=[("Revisa los datos", "Solo chat", "2.1")],
               expect=t_problemas() + f"<p>Con los dos problemas juntos (duplicado y atípico), el tiempo promedio del 3T saldría en {T['sucio_t']}; con solo el atípico, en {hrs(K['tiempo_3T_solo_atipico'])}. Con datos limpios es {T['tiempo']}. Copilot puede mencionar otras variaciones normales; lo importante es que encuentre estos tres.</p>",
               nolic=NOLIC_FILE, checks=["Encontré el duplicado, el atípico y el mes faltante."])
    labs += lab("lab-2-2", "2.2", "Limpia, resume y grafica", "Requerido", "8 min", "Un resumen del trimestre por región con gráfica", "Excel",
                "La hoja Indicadores y los problemas del 2.1", "Hojas Datos_limpios y Resumen_3T, gráfica y tabla dinámica",
                intro="Cambia al <b>modo de edición</b>. Corre los prompts en orden.",
                prompts=[("Datos limpios", "Edición", "2.2a"), ("Resumen y gráfica", "Edición", "2.2b"), ("Tabla dinámica", "Edición", "2.2c")],
                expect=t_resumen() + f"<p>Tiempo de respuesta del 2T: {T['tiempo2']}; satisfacción del 2T: {T['sat2']}. Golfo es la única región arriba de la meta de tiempo y abajo de la meta de satisfacción. Sin limpiar (con el duplicado y el atípico juntos), el tiempo del 3T saldría en {T['sucio_t']}.</p>",
                callouts=[("tip", "Revisa una cifra", "Haz clic en la celda del tiempo total y pide: «Explícame esta fórmula». Debe ponderar por solicitudes atendidas y excluir el renglón marcado.")],
                nolic="Sube el Excel a Copilot Chat y pide el mismo resumen como tabla; crea la tabla dinámica tú mismo (<b>Insertar</b> &gt; <b>Tabla dinámica</b>) y la gráfica desde ella.",
                fail=ck("CHECKPOINT_Ej2_Resultado_Excel.xlsx", "el 2.3"), checks=["Creé el resumen con fórmulas y una gráfica.", "Revisé una fórmula con Copilot."])
    labs += lab("lab-2-3", "2.3", "La hoja Hechos: cada cifra con su fuente", "Requerido", "5 min", "Una sola fuente para el reporte y la presentación", "Excel",
                "La hoja Resumen_3T", "Hoja Hechos (la usas en los ejercicios 3, 4 y 5)",
                prompts=[("Hoja Hechos", "Edición", "2.3")],
                expect=table(["Hecho", "Cifra"], [["Solicitudes recibidas 3T", T["rec"]], ["Solicitudes atendidas 3T", T["ate"]], ["% atendidas", T["pct_ate"]], ["Tiempo de respuesta 3T / 2T", f"{T['tiempo']} / {T['tiempo2']}"],
                             ["Tiempo Golfo 3T", T["golfo_t"]], ["Satisfacción 3T / 2T", f"{T['sat']} / {T['sat2']}"], ["Satisfacción Golfo 3T", T["golfo_s"]],
                             ["Presupuesto ejercido / asignado", f"{T['pres_ej']} / {T['pres_as']} ({T['pres']})"], ["Datos faltantes", "Centro, agosto 2026"]]),
                callouts=[("note", "La regla de oro", "Si una cifra no está en Hechos, no entra al reporte ni a la presentación. Así cualquiera puede rastrear cada número.")],
                nolic="Copia la tabla de «Lo que verás» en una hoja nueva llamada Hechos y agrega la fuente de cada cifra.",
                fail=ck("CHECKPOINT_Ej2_Resultado_Excel.xlsx", "el ejercicio 3"), checks=["Mi hoja Hechos tiene la fuente de cada cifra."])
    labs += lab("lab-2-4", "2.4", "Agrupa los comentarios de la encuesta por tema", "Requerido", "6 min", "Saber qué dicen los usuarios sin leer 60 comentarios", "Excel",
                "Zava_Encuesta_Servicio_3T2026.xlsx", "Temas y conteos para el reporte", lic=CHAT,
                intro="Abre la encuesta y usa el <b>modo de edición</b>.",
                prompts=[("Temas de la encuesta", "Edición", "2.4")],
                expect=t_temas() + f"<p>El tema principal (tiempo de respuesta) y el total deben coincidir; entre temas parecidos, como Seguimiento y Portal, Copilot puede mover unos cuantos comentarios. Lo importante es la historia, no el conteo exacto. Debe marcar {num(K['com_con_nombre'])} comentarios que mencionan a alguien del equipo por su nombre: quítalos antes de compartir.</p>",
                callouts=[("important", "Comentarios anónimos", "No intentes identificar a quien escribió un comentario y no compartas comentarios con nombres de personas. Si un grupo tiene muy pocas respuestas, no lo reportes por separado.")],
                nolic=NOLIC_FILE, variant="2", fail=ck("CHECKPOINT_Ej2_Resultado_Excel.xlsx", "el ejercicio 3") + " La hoja Comentarios_temas tiene la clasificación.",
                checks=["Agrupé los comentarios por tema.", "Identifiqué y quité los comentarios con nombres."])
    return chapter("ch2", "Paso 2", "2. Excel: revisa, analiza y documenta", ["25 minutos", "Excel", "Solo chat y modo de edición"],
                   "El Excel salió directo del sistema y nadie lo ha revisado. Antes de calcular nada, revisas; después resumes, grafica y dejas cada cifra con su fuente.", labs)


def ch3():
    rep = "".join(f"<b>{h}</b><ul>" + "".join(f"<li>{E(i)}</li>" for i in items) + "</ul>" for h, items in reporte_lines())
    labs = lab("lab-3-1", "3.1", "Reporte de una página a partir de Hechos y las notas", "Requerido", "8 min", "El reporte para la dirección en minutos", "Word",
               "Hoja Hechos y Zava_Notas_y_Politicas_Servicio.docx", "Zava_Reporte_3T.docx (lo usas en el ejercicio 4)",
               intro="Crea un documento de Word en blanco en tu OneDrive y guárdalo como <b>Zava_Reporte_3T</b>. Abre Copilot en Word, escribe <b>/</b> para elegir el documento de notas y pega la hoja Hechos (selecciona las columnas Hecho y Cifra en Excel y cópialas).",
               prompts=[("Reporte de una página", "Word", "3.1")], expect=rep,
               nolic="Sube el documento de notas a Copilot Chat, pega la hoja Hechos en el prompt y copia la respuesta en Word.",
               fail=ck("CHECKPOINT_Ej3_Resultado_Reporte.docx", "el 3.2"), checks=["Generé el reporte con cifras iguales a Hechos."])
    labs += lab("lab-3-2", "3.2", "Cambia el tono y resume", "Requerido", "4 min", "El mismo contenido para dos públicos", "Word", "Tu reporte", "Una versión ejecutiva y un resumen de 3 líneas",
                intro="Selecciona el texto del reporte y usa Copilot sobre la selección (o en el panel).",
                prompts=[("Tono ejecutivo", "Word", "3.2a"), ("Resumen para correo", "Word", "3.2b")],
                expect="La misma información, más corta, con las mismas cifras. Revisa que no haya cambiado ningún número.",
                nolic="Pega el texto en Copilot Chat con el mismo prompt.", checks=["Cambié el tono sin cambiar las cifras."])
    labs += lab("lab-3-3", "3.3", "Preguntas frecuentes de un procedimiento", "Requerido", "5 min", "Que la gente encuentre la respuesta sin preguntarte", "Word",
                "Zava_Notas_y_Politicas_Servicio.docx", "Preguntas frecuentes listas para publicar", lic=CHAT,
                prompts=[("Preguntas frecuentes", "Word", "3.3")],
                expect="<ol>" + "".join(f"<li><b>{E(q)}</b> {E(a)}</li>" for q, a in faq()) + "</ol>",
                nolic=NOLIC_FILE, variant="3", fail=ck("CHECKPOINT_Ej3_Resultado_Reporte.docx", "el ejercicio 4"),
                checks=["Generé preguntas frecuentes de un procedimiento."])
    return chapter("ch3", "Paso 3", "3. Word: el reporte", ["18 minutos", "Word"], "La dirección pidió un reporte de una página. Con la hoja Hechos y las notas de tus reuniones, Word lo escribe; tú lo revisas.", labs)


def ch4():
    labs = lab("lab-4-1", "4.1", "La presentación a partir del Word", "Requerido", "8 min", "Del reporte a 5 diapositivas con la plantilla", "PowerPoint",
               "Zava_Plantilla_Revision.pptx y Zava_Reporte_3T.docx", "Zava_Revision_3T.pptx",
               intro="Abre <b>Zava_Plantilla_Revision.pptx</b> desde OneDrive, guárdala como <b>Zava_Revision_3T</b>, abre Copilot y escribe <b>/</b> para elegir tu reporte.",
               prompts=[("Presentación desde el reporte", "PowerPoint", "4.1")],
               expect=f"Cinco diapositivas con la plantilla verde de Zava. Revisa tres cifras contra Hechos: atendidas {T['ate']}, tiempo {T['tiempo']} y satisfacción {T['sat']}.",
               nolic="Sube el reporte a Copilot Chat y pide el texto de cada diapositiva; pégalo en la plantilla.",
               fail=ck("CHECKPOINT_Ej4_Resultado_Presentacion.pptx", "el 4.2"), checks=["Creé la presentación desde mi reporte."])
    labs += lab("lab-4-2", "4.2", "Una diapositiva con datos del Excel", "Requerido", "6 min", "Que la gráfica salga de los datos revisados", "PowerPoint · Excel",
                "Hoja Resumen_3T", "La diapositiva de tiempo por región",
                intro="<b>Camino principal:</b> en Excel selecciona la gráfica de la hoja Resumen_3T, cópiala (<b>Ctrl + C</b>) y pégala en la diapositiva 3 (<b>Ctrl + V</b>). Revisa que las cifras coincidan con la tabla de abajo.</p><p><b>Pruébalo (no está documentado):</b> pídele a Copilot en PowerPoint la gráfica escribiendo <b>/</b> para elegir el Excel. Si no funciona, quédate con el camino principal.",
                prompts=[("Pruébalo: gráfica con / al Excel", "PowerPoint", "4.2")],
                expect=table(["Región", "Tiempo 3T"], [[g, hrs(K[f"tiempo_3T_{g}"])] for g in Z.REG]) + f"<p>Meta: {T['meta_t']}. Golfo es la barra que sobresale.</p>",
                nolic="El camino principal (copiar y pegar la gráfica) funciona igual sin licencia.", fail=ck("CHECKPOINT_Ej4_Resultado_Presentacion.pptx", "el 4.3"),
                checks=["Agregué una gráfica que coincide con Resumen_3T."])
    labs += lab("lab-4-3", "4.3", "Ajusta con prompts y agrega notas del orador", "Requerido", "6 min", "«Hago un prompt y me ajusta la presentación»", "PowerPoint · Word",
                "Tu presentación y tu reporte", "Presentación lista con notas",
                intro="Primero acorta una diapositiva. Después cambia algo en tu reporte de Word (por ejemplo, agrega una cuarta acción), guarda y pide a PowerPoint que actualice la presentación. Por último, las notas del orador.",
                prompts=[("Acorta la diapositiva 2", "PowerPoint", "4.3a"), ("Actualiza desde el Word", "PowerPoint", "4.3b"), ("Notas del orador", "PowerPoint", "4.3c")],
                expect="La diapositiva 2 con 4 viñetas cortas; solo cambian las diapositivas afectadas por tu cambio en Word; notas en el panel <b>Notas</b> de cada diapositiva.",
                callouts=[("tip", "Si no aparecen las notas", "Abre el panel de <b>Notas</b> (barra inferior) y pega el texto que te dé Copilot, diapositiva por diapositiva."),
                          ("note", "¿Brand kit?", "Si tu empresa publicó un kit de marca (lo viste a las 10:00), elígelo al crear la presentación en lugar de la plantilla.")],
                nolic="Pide en Copilot Chat el texto corregido y las notas; pégalos en PowerPoint.", variant="4",
                fail=("<b>Si «Actualiza desde el Word» no cambia nada</b>, pide el cambio directo en la diapositiva de acciones:"
                      f'<div class="prompt"><div class="prompt-head"><span class="prompt-label">Plan B: agrega la cuarta acción</span><span class="mode mode-ppt">PowerPoint</span><button class="copy" type="button" aria-label="Copiar: Plan B, agrega la cuarta acción">Copiar</button></div><pre id="p-lab-4-3-planb">{E(P["4.3plan"])}</pre></div>'
                      + ck("CHECKPOINT_Ej4_Resultado_Presentacion.pptx", "el ejercicio 5") + " Tiene notas del orador."),
                checks=["Ajusté la presentación con un prompt.", "Agregué notas del orador."])
    return chapter("ch4", "Paso 4", "4. PowerPoint: la presentación", ["22 minutos", "PowerPoint", "Word", "Excel"],
                   "La dirección quiere máximo 6 diapositivas. Las armas desde tu reporte, con una gráfica que sale del Excel revisado, y la ajustas con prompts.", labs)


def ch5():
    labs = lab("lab-5-1", "5.1", "Correo de seguimiento a la dirección", "Requerido", "4 min", "Enviar el material con un mensaje claro", "Outlook",
               "Tu reporte y tu presentación", "Un borrador de correo (no se envía)", lic=CHAT,
               intro="En Outlook crea un correo nuevo y usa <b>Borrador con Copilot</b>. <b>No lo envíes</b>: hoy es práctica.",
               prompts=[("Correo a la dirección", "Outlook", "5.1")],
               expect="Un correo de menos de 120 palabras con 3 cifras de Hechos, Golfo como problema principal y una pregunta al final.",
               nolic="Pide el correo en Copilot Chat y pégalo en Outlook.", checks=["Redacté el correo con Borrador con Copilot sin enviarlo."])
    labs += lab("lab-5-2", "5.2", "Agenda de la reunión y mensaje al equipo", "Requerido", "4 min", "La reunión y el equipo, listos", "Outlook · Teams",
                "Tu reporte", "La agenda y el mensaje (no se envían)", lic=CHAT,
                intro="La agenda en una invitación nueva de Outlook con Copilot (lo viste a las 10:00). El mensaje de Teams escríbelo con Copilot y pégalo en el cuadro de mensaje del canal <b>sin enviarlo</b>.",
                prompts=[("Agenda de 30 minutos", "Outlook", "5.2a"), ("Mensaje al equipo", "Teams", "5.2b")],
                expect="Una agenda con tres temas y tiempos, y un mensaje cercano de menos de 70 palabras, sin datos de personas.",
                nolic="Pide ambos textos en Copilot Chat.", variant="5", checks=["Preparé la agenda y el mensaje al equipo."])
    labs += lab("lab-5-3", "5.3", "Antes de enviar: revisión con veredictos", "Requerido", "5 min", "Que nada incorrecto salga de tu área", "Aplicación Microsoft Copilot (chat nuevo)",
                "El borrador de un colega (sección 4 del documento de notas) y tu hoja Hechos", "La lista de correcciones", lic=CHAT,
                intro="Abre un <b>chat nuevo</b>: el revisor no debe haber participado en el análisis. Escribe <b>/</b> para elegir el documento de notas (o súbelo) y pega la hoja Hechos.",
                prompts=[("Revisor independiente", "Copilot Chat", "5.3")],
                expect=t_claims() + "<p>Resultado esperado: 2 Verificado, 2 Incorrecto, 1 No verificable y 1 Exagerado. Si Copilot duda entre dos veredictos, discútelo con tu vecino: lo importante es no enviar lo Incorrecto ni lo Exagerado.</p>",
                callouts=[("important", "Los cuatro veredictos", "<b>Verificado</b>: los datos lo confirman. <b>Incorrecto</b>: los datos lo contradicen. <b>No verificable</b>: no hay evidencia para confirmarlo ni para descartarlo. <b>Exagerado</b>: tiene base, pero lo sobredimensiona.")],
                fail=ck("CHECKPOINT_Ej5_Resultado_Correos.docx", "el ejercicio 6"), checks=["Revisé el borrador con los cuatro veredictos.", "Corregí lo Incorrecto y lo Exagerado."])
    return chapter("ch5", "Paso 5", "5. Outlook y Teams", ["13 minutos", "Outlook", "Teams", "Copilot Chat"],
                   "Con el reporte y la presentación listos, toca avisar: un correo a la dirección, la agenda de la revisión y un mensaje al equipo. Un colega ya escribió un borrador; antes de enviarlo, lo revisas contra los datos.", labs)


def ch6():
    labs = lab("lab-6-1", "6.1", "Guarda y comparte tus prompts", "Requerido", "4 min", "No volver a escribir el mismo prompt", "Aplicación Microsoft Copilot",
               "Tus mejores prompts de hoy", "Prompts guardados y compartidos", lic=CHAT,
               intro="Lo viste a las 10:00; aquí lo aplicas a lo de hoy. En Copilot Chat pasa el cursor sobre tu prompt y selecciona <b>Guardar mensaje</b>; queda en <b>Sus mensajes</b> de la galería de Copilot, desde donde lo puedes compartir con tu equipo. Guardar funciona con Copilot Chat. Programarlo requiere licencia de Microsoft 365 Copilot: si el prompt se repite cada semana, usa <b>Programar esta indicación</b> (pestaña Work IQ).",
               prompts=[("Resumen del mes (para guardar)", "Copilot Chat", "6.1")],
               expect="Tu prompt guardado y listo para usar con tus propios archivos.", checks=["Guardé un prompt.", "Compartí un prompt con mi equipo."])
    labs += lab("lab-6-2", "6.2", "Analista e Investigador", "Demo", "3 min", "Saber cuándo usar un agente para análisis o investigación", "Aplicación Microsoft Copilot (Agentes)",
                "El Excel de indicadores (Analista) y la web (Investigador)", "Ideas para tu trabajo",
                intro="El presentador lo muestra. En la aplicación Microsoft Copilot, en <b>Agentes</b>, selecciona <b>Analista</b> para analizar datos a fondo o <b>Investigador</b> para investigar un tema con fuentes.",
                prompts=[("Analista", "Analista", "6.2a"), ("Investigador", "Investigador", "6.2b")],
                expect="Analista revisa la calidad de los datos, grafica la tendencia y muestra los pasos que siguió. Investigador entrega un informe con fuentes citadas; revisa las fuentes antes de usarlas.")
    return chapter("ch6", "Paso 6", "6. Lleva tus prompts", ["7 minutos", "Copilot Chat", "Agentes"], "Hiciste el recorrido una vez. La próxima, empiezas con tus prompts guardados.", labs)


def ch7():
    casos = table(["#", "Caso", "Ejercicio", "App", "Requiere"], [[i, c, " · ".join(f'<a href="#lab-{x.strip().replace(".", "-")}">{x.strip()}</a>' for x in e.split("·")), a, l] for i, (c, e, a, l) in enumerate(CASOS, 1)])
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    labs = lab("lab-7-1", "7.1", "Trae tu caso", "Reto", "10 min", "Salir con un caso real encaminado", "La app que uses en tu caso", "Un archivo, correo o reporte tuyo", "Tu primer resultado y el siguiente paso", lic=CHAT,
               intro="Elige un caso de la tabla o uno propio y usa esta plantilla con tus archivos de la empresa:", prompts=[("Plantilla para tu caso", "Copilot Chat", "7.2")],
               callouts=[("important", "Antes de usar tus datos", 'Repasa el recuadro de <a href="#responsable">uso responsable</a>.')], checks=["Probé la plantilla con un caso real.", "Elegí un caso para esta semana."])
    extra = f'<div class="chapter-inner" id="casos"><h3>10 casos para cualquier área</h3>{casos}<h3 id="faq">Preguntas frecuentes</h3><div class="faq">{faqs}</div></div>'
    return chapter("ch7", "Cierre", "7. Preguntas y trae tu caso", ["15 minutos", "Tus archivos"], "Lo que más sirve es probarlo con algo tuyo. Trae tu caso y tus preguntas.", labs, extra)


def refs():
    rs = [("Introducción a Copilot en Excel", "https://support.microsoft.com/es-es/excel/copilot/get-started-with-copilot-in-excel"),
          ("Editar con Copilot en PowerPoint", "https://support.microsoft.com/es-es/powerpoint/edit-with-copilot-in-powerpoint"),
          ("Copilot en Word", "https://support.microsoft.com/es-es/word/welcome-to-copilot-in-word"),
          ("Borrador de un correo con Copilot en Outlook", "https://support.microsoft.com/es-es/outlook/copilot-pages/draft-an-email-message-with-copilot-in-outlook"),
          ("Guardar sus indicaciones favoritas", "https://support.microsoft.com/es-es/microsoft-365-copilot/save-your-favorite-prompts-to-use-again"),
          ("Copilot Chat con y sin licencia de Microsoft 365 Copilot", "https://support.microsoft.com/es-es/microsoft-365-copilot/how-copilot-chat-works-with-and-without-a-microsoft-365-copilot-license")]
    r = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in rs)
    return f'<section class="card" id="refs"><h2>Referencias</h2><ul>{r}</ul><p class="small muted">Los nombres de botones y menús pueden variar según la versión y el idioma de tu Microsoft 365.</p></section>'


def nav():
    g = [("ch0", "0. Arranque", [("lab-0-1", "0.1 Archivos"), ("lab-0-2", "0.2 Trabajo o web")]), ("chD", "La demo completa", []),
         ("ch1", "1. Ponte al día", [("lab-1-1", "1.1 Tus pendientes"), ("lab-1-2", "1.2 Un archivo")]),
         ("ch2", "2. Excel", [("lab-2-1", "2.1 Revisa los datos"), ("lab-2-2", "2.2 Resumen y gráfica"), ("lab-2-3", "2.3 Hechos"), ("lab-2-4", "2.4 Encuesta")]),
         ("ch3", "3. Word", [("lab-3-1", "3.1 Reporte"), ("lab-3-2", "3.2 Tono y resumen"), ("lab-3-3", "3.3 Preguntas frecuentes")]),
         ("ch4", "4. PowerPoint", [("lab-4-1", "4.1 Desde el Word"), ("lab-4-2", "4.2 Gráfica"), ("lab-4-3", "4.3 Ajustes y notas")]),
         ("ch5", "5. Outlook y Teams", [("lab-5-1", "5.1 Correo"), ("lab-5-2", "5.2 Agenda y mensaje"), ("lab-5-3", "5.3 Veredictos")]),
         ("ch6", "6. Tus prompts", [("lab-6-1", "6.1 Guardar y compartir"), ("lab-6-2", "6.2 Analista e Investigador")]),
         ("ch7", "7. Preguntas y tu caso", [("lab-7-1", "7.1 Trae tu caso"), ("casos", "10 casos"), ("faq", "Preguntas frecuentes")])]
    out = '<a class="nav-top" href="#bienvenida">Bienvenida</a>'
    for i, t, ls in g:
        out += f'<div class="nav-group"><a class="nav-mod" href="#{i}">{t}</a>' + "".join(f'<a class="nav-lab" href="#{a}">{b}</a>' for a, b in ls) + "</div>"
    return out + '<div class="nav-group"><a class="nav-mod" href="#responsable">Uso responsable</a><a class="nav-mod" href="#refs">Referencias</a></div>'


def build():
    body = welcome() + ch0() + chD() + ch1() + ch2() + ch3() + ch4() + ch5() + ch6() + ch7() + refs()
    page = f"""<!DOCTYPE html>
<html lang="es-MX"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light">
<title>Copilot en tu día a día: de los datos a la presentación</title><style>{CSS}</style></head>
<body><a class="skip" href="#bienvenida">Ir al contenido</a>
<header class="hero"><div class="eyebrow">Bootcamp &middot; TDx Bepensa &middot; Martes 10 de noviembre de 2026</div>
<h1>Copilot en tu día a día: de los datos a la presentación</h1>
<p>Un recorrido práctico para cualquier área: revisas un Excel, escribes el reporte en Word, armas la presentación en PowerPoint y la ajustas con un prompt, y preparas los correos que siguen, con archivos de práctica, prompts listos para copiar y checkpoints para no quedarte atrás.</p>
<div class="tags"><span>120 minutos</span><span>Práctica guiada en tu laptop</span><span>Excel &middot; Word &middot; PowerPoint &middot; Outlook &middot; Teams</span><span>Con y sin licencia</span><span>Variantes para RH, Comercial y Operaciones</span><span>Datos ficticios</span></div></header>
<div class="shell"><div><button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="sideNav">Menú: ejercicios</button>
<nav class="side" id="sideNav" aria-label="Navegación"><div class="nav-title">Tu avance</div><div class="progress"><div class="bar"><i id="progBar"></i></div><small id="progTxt"></small></div>
<div class="controls"><button type="button" id="expandAll">Abrir todo</button><button type="button" id="collapseAll">Cerrar todo</button></div>{nav()}
<div class="controls" style="margin-top:12px"><button type="button" id="resetProg">Reiniciar casillas</button></div></nav></div>
<main id="main">{body}<footer>Copilot en tu día a día: de los datos a la presentación &middot; v1 &middot; Empresa y datos ficticios con fines de capacitación.</footer></main></div>
<script>{JS}</script></body></html>"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page)
    return len(page)


if __name__ == "__main__":
    print(build())
