# -*- coding: utf-8 -*-
import os, html
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
from docx import Document
from docx.shared import Pt, RGBColor, Cm
import zdata as Z
from zdata import num, pct, hrs, pesos
from gen_files import T, CLAIMS
from content import P, CASOS, FAQ, TARJETA, VAR

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_General_Lab_v1"
INT, CF = os.path.join(ROOT, "INTERNAL"), os.path.join(ROOT, "CUSTOMER_FACING")
K, RAW, CLEAN, COM = Z.compute(); E = html.escape
CSS = """:root{--p:#1E1B4B;--s:#4338CA;--a:#F97316;--b:#d8dee9}body{margin:0;font-family:"Segoe UI",Arial;color:#172033;background:#f5f5fb;line-height:1.5}
.banner{background:#b42318;color:#fff;font-weight:700;text-align:center;padding:6px}.hero{background:linear-gradient(120deg,var(--p),var(--s) 60%,var(--a) 140%);color:#fff;padding:24px 32px}
main{max-width:1250px;margin:auto;padding:20px}.card{background:#fff;border:1px solid var(--b);border-radius:14px;padding:16px 24px;margin-bottom:16px}h2{color:var(--p)}h3{color:var(--s)}
table{border-collapse:collapse;width:100%;font-size:.88rem}th,td{border-bottom:1px solid var(--b);padding:6px 8px;text-align:left;vertical-align:top}th{background:#eef0fb}
.callout{border-left:5px solid var(--a);background:#fff4ec;padding:10px 14px;border-radius:0 10px 10px 0;margin:10px 0}.warn{border-left-color:#d97706;background:#fff4df}.imp{border-left-color:#b42318;background:#ffe9e7}
.pill{border-radius:99px;padding:1px 9px;font-size:.78rem;font-weight:600}.e{background:#fde7d4;color:#9a3412}.h{background:#dcfce7;color:#166534}ul.cb{list-style:none;padding-left:4px}ul.cb li:before{content:"\\2610  ";color:var(--s)}.m{color:#5d6b82}"""


def page(title, sub, body):
    return f"""<!DOCTYPE html><html lang="es-MX"><head><meta charset="utf-8"><title>{E(title)}</title><style>{CSS}</style></head><body><div class="banner">INTERNO · SOLO PRESENTADORES DE MICROSOFT · NO COMPARTIR NI PUBLICAR</div>
<header class="hero"><div>Interno · Microsoft</div><h1>{E(title)}</h1><div>{sub}</div></header><main>{body}</main></body></html>"""


def tbl(h, rows): return "<table><tr>" + "".join(f"<th>{x}</th>" for x in h) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table>"


ER, HU = '<span class="pill e">Erik</span>', '<span class="pill h">Humberto</span>'
PACE = [("11:30", "12:00", "Receso", "Ambos", "Pedir que descarguen el .zip y lo suban a OneDrive", "Enlace en el chat de la reunión", "—"),
        ("12:00", "12:05", "0. Arranque", ER, "Archivos en OneDrive, Copilot abierto, tarjeta de reglas", "Mano arriba quien no tenga licencia → ruta Copilot Chat", "Saltar la explicación de trabajo vs web"),
        ("12:05", "12:12", "Demo completa", ER, "Observan el recorrido Excel → Word → PowerPoint → ajuste", "—", "Demo de 4 min con los checkpoints ya abiertos"),
        ("12:12", "12:20", "1. Ponte al día (opcional)", HU, "Prompts con sus propios datos", "Solo quien quiera", "Saltarlo; dejarlo de tarea"),
        ("12:20", "12:26", "2.1 Revisa los datos", HU, "Solo chat", "Duplicado, atípico y mes faltante", "—"),
        ("12:26", "12:34", "2.2 Resumen y gráfica", HU, "Modo de edición, 3 prompts", f"Tiempo total {T['tiempo']}; Golfo {T['golfo_t']}", "Solo 2.2b; tabla dinámica como demo"),
        ("12:34", "12:39", "2.3 Hechos", HU, "Modo de edición", "12:38: quien no tenga Hechos abre CHECKPOINT_Ej2", "Abrir directo el checkpoint"),
        ("12:39", "12:45", "2.4 Encuesta", HU, "Temas y nombres", f"{T['t1']} comentarios de tiempo de respuesta", "Demo"),
        ("12:45", "12:53", "3.1 Reporte", ER, "Word con / y Hechos pegada", "Cifras iguales a Hechos", "—"),
        ("12:53", "12:57", "3.2 Tono y resumen", ER, "Reescritura", "Ninguna cifra cambia", "Saltar"),
        ("12:57", "13:03", "3.3 Preguntas frecuentes", ER, "Con el procedimiento; variante RH con la política híbrida", "13:02: CHECKPOINT_Ej3", "Demo"),
        ("13:03", "13:11", "4.1 Presentación", ER, "PowerPoint con la plantilla y / al reporte", "5 diapositivas", "—"),
        ("13:11", "13:17", "4.2 Gráfica", ER, "Copilot o copiar y pegar", "Golfo sobresale", "Copiar y pegar"),
        ("13:17", "13:25", "4.3 Ajustes y notas", ER, "El momento «me ajusta la presentación»", "13:24: CHECKPOINT_Ej4", "Solo 4.3a y 4.3c"),
        ("13:25", "13:29", "5.1 Correo", HU, "Borrador con Copilot, sin enviar", "—", "Demo"),
        ("13:29", "13:33", "5.2 Agenda y mensaje", HU, "Sin enviar", "—", "Saltar"),
        ("13:33", "13:38", "5.3 Veredictos", HU, "Chat nuevo", "2/2/1/1", "No recortar"),
        ("13:38", "13:45", "6. Tus prompts", HU, "Guardar mensaje; demo Analista e Investigador", "—", "Solo guardar"),
        ("13:45", "14:00", "7. Preguntas y trae tu caso", "Ambos", "Preguntas frecuentes preparadas; casos de la sala", "Recoger 3 casos (al menos uno de RH)", "—")]
CUT90 = [("0. Arranque", "4", "Sin trabajo vs web"), ("Demo completa", "5", "Con checkpoints abiertos"), ("1. Ponte al día", "0", "Tarea"),
         ("2.1 Revisa los datos", "6", "Igual"), ("2.2 Resumen", "6", "Solo 2.2b; tabla dinámica en demo"), ("2.3 Hechos", "4", "Igual"), ("2.4 Encuesta", "3", "Demo con el checkpoint"),
         ("3.1 Reporte", "7", "Igual"), ("3.2 y 3.3", "3", "Demo de preguntas frecuentes (variante RH)"), ("4.1 Presentación", "7", "Igual"), ("4.2 Gráfica", "4", "Copiar y pegar"),
         ("4.3 Ajustes y notas", "6", "4.3a y 4.3c"), ("5.1 y 5.2", "3", "Demo"), ("5.3 Veredictos", "6", "En sala"), ("6. Tus prompts", "3", "Solo guardar"),
         ("7. Preguntas y tu caso", "10", "Preguntas frecuentes primero"), ("Colchón", "3", "Rezagados"), ("Colchón para preguntas", "10", "Preguntas de la sala durante o al final")]
UI = [("Aplicación Microsoft Copilot · pestaña Work IQ", "Nombre de la pestaña de datos de trabajo y del modo web", "Usado según tu indicación; confirmar el texto en la interfaz en español."),
      ("Copilot Chat · cargar archivos", "«+» y la opción para cargar archivos", "En inglés: «Upload images and files»; la doc es-ES dice «Adjuntar contenido» / «Cargar»."),
      ("Excel · modos", "Modo de solo chat, modo Plan, modo de edición; Ctrl + Mayús + M", "En inglés (5 nov): Chat only, Plan, Allow editing; Ctrl+Shift+M. Confirmar en español."),
      ("Excel · abrir Copilot", "Icono en la esquina inferior derecha, Alt + C", "Doc es-ES; confirmar en las laptops."),
      ("Word · / a un Excel", "La guía pide pegar la hoja Hechos en el prompt", "No está documentado que Word referencie .xlsx; por eso se pega."),
      ("PowerPoint · / a un Word y a un Excel", "Crear desde el reporte; gráfica desde el Excel", "Referenciar archivos está documentado en «Editar con Copilot»; la gráfica desde Excel no: hay plan B (copiar y pegar)."),
      ("PowerPoint · notas del orador", "Copilot escribe notas", "No documentado; plan B en la guía."),
      ("Outlook", "«Borrador con Copilot», «Resumen por Copilot»", "Doc es-ES."),
      ("Guardar prompts", "«Guardar mensaje», «Sus mensajes», galería de Copilot", "Doc es-ES mezcla «Galería de consultas» e «indicaciones». La guía dice que guardar funciona con Copilot Chat y programar requiere licencia."),
      ("Etiquetas de licencia", "«M365 Copilot (Basic)» / «M365 Copilot (Premium)» en el panel de Copilot", "Según la FAQ de Copilot en Excel; confirmar dónde aparece en Excel, Word y PowerPoint en español."),
      ("Funciones dentro de las apps con Basic", "La guía invita a intentarlo y da ruta con Copilot Chat", "Por confirmar en el tenant: modos de edición, crear hojas, Word y PowerPoint con cuentas Basic."),
      ("Agentes", "«Agentes» > «Analista» / «Investigador»", "Doc es-ES.")]
NOLIC = """<ul><li>Al inicio pedir que abran Copilot en Excel y digan qué etiqueta ven en el panel: <b>M365 Copilot (Premium)</b> = con licencia; <b>M365 Copilot (Basic)</b> = Copilot Chat, con acceso estándar a Copilot en Excel (página de Microsoft «Frequently asked questions about Copilot in Excel»).</li>
<li>Requiere licencia con seguridad: datos de trabajo (1.1 y 1.2), programar indicaciones (6.1), Analista e Investigador (6.2).</li>
<li><b>Por confirmar en el tenant:</b> qué pueden hacer las cuentas Basic dentro de Excel, Word y PowerPoint (2.2, 2.3, 2.4, 3.x, 4.x). Mientras tanto, la guía mantiene la ruta con Copilot Chat como respaldo.</li>
<li>Ruta sin licencia (está en cada ejercicio): subir el archivo a Copilot Chat en la aplicación Microsoft Copilot, usar el mismo prompt y pegar el resultado en Excel, Word o PowerPoint.</li>
<li>Funcionan igual con Copilot Chat: 2.1, 2.4, 3.3, 5.1, 5.2, 5.3 y 7.1 (etiqueta verde).</li>
<li>Si una cuenta Basic no puede hacer algo dentro de la app: ruta con Copilot Chat o checkpoint. Sentar en pareja a quien no pueda avanzar con alguien con Premium.</li>
<li>Si más de la mitad no tiene licencia: hacer los ejercicios de Excel y PowerPoint como «Ver y comparar» y dejar los de Copilot Chat como práctica.</li></ul>"""


def guide():
    script = "".join(f"<h3>{t}</h3><p>{s}</p>" for t, s in [
        ("Arranque (12:00)", "«En la mañana vieron el marco, la colaboración y cómo pedir. Ahora lo usamos en un día normal: un Excel, un reporte, una presentación y los correos.» Explicar las dos etiquetas de licencia y la tarjeta de reglas."),
        ("Demo completa (12:05)", "Es lo que pidió el cliente. En 7 minutos: Excel (revisar y resumir) → Word (reporte con / a las notas) → PowerPoint (presentación con la plantilla) → un prompt que ajusta la presentación. Tener los checkpoints abiertos por si algo tarda. Cerrar: «ahora lo hacen ustedes, paso a paso»."),
        ("Excel (12:20)", "El mensaje: revisar antes de analizar. Mostrar el efecto: sin limpiar (duplicado y atípico juntos), el tiempo sale en " + T["sucio_t"] + " en lugar de " + T["tiempo"] + ". La hoja Hechos es la regla de oro. En 2.4, insistir en anonimato y en no citar comentarios con nombres."),
        ("Word (12:45)", "Pegar Hechos en el prompt y usar / para las notas. En 3.3, mostrar la variante RH con la política de trabajo híbrido."),
        ("PowerPoint (13:03)", "El momento «me ajusta la presentación» está en 4.3b: cambiar el Word y pedir a PowerPoint que actualice solo lo que cambió."),
        ("Outlook y Teams (13:25)", "Nada se envía. 5.3 es el cierre de la historia: el borrador del colega tiene una cifra sin limpiar y una afirmación causal sin evidencia."),
        ("Preguntas y caso (13:45)", "Empezar con las preguntas frecuentes de la guía; luego 2 o 3 casos de la sala, al menos uno de RH si hay asistentes de RH. Agentes: solo si preguntan.")])
    key = tbl(["Ejercicio", "Lo que debe salir"], [
        ["2.1", f"Duplicado Golfo 2026-09 ({T['dup']} atendidas); atípico Península 2026-07 ({T['atip']}); falta Centro 2026-08."],
        ["2.2 / 2.3", f"Recibidas {T['rec']}; atendidas {T['ate']} ({T['pct_ate']}); tiempo {T['tiempo']} (2T {T['tiempo2']}); Golfo {T['golfo_t']}; satisfacción {T['sat']} (2T {T['sat2']}); Golfo {T['golfo_s']}; presupuesto {T['pres_ej']} de {T['pres_as']} ({T['pres']}). Sin limpiar: {T['sucio_a']} atendidas y {T['sucio_t']}."],
        ["2.4", "; ".join(f"{t} {num(K[f'tema_n_{t}'])}" for t, *_ in Z.THEMES) + f"; {num(K['com_con_nombre'])} comentarios con nombre."],
        ["5.3", "; ".join(f"{i}. {c[1]}" for i, c in enumerate(CLAIMS, 1))]])
    dry = tbl(["Prueba", "Resultado"], DRY)
    body = f"""<div class="card"><h2>Resumen</h2><p>Sesión general, martes 10 de noviembre de 2026, BImpulsa. <b>Supuesto:</b> bloque práctico de 12:00 a 14:00 (Mérida, UTC−6), igual que el lunes; por confirmar. Público de varias áreas, con un grupo pequeño de RH. Licencias por confirmar. Asistentes distintos a los del lunes: la guía no menciona nada del lunes.</p>
<p>Pidió el cliente: una demo completa para un usuario normal (Excel → PowerPoint → Word → prompt que ajusta la presentación), preguntas y respuestas, y ejemplos de RH.</p>
<p><b>Propuesta de roles (confirmar):</b> {ER} conduce el arranque, la demo, Word y PowerPoint; {HU} conduce Ponte al día, Excel, Outlook/Teams y los prompts. Ambos en preguntas.</p></div>
<div class="card"><h2>Tabla de ritmo (hora de Mérida)</h2>{tbl(["Inicio", "Fin", "Bloque", "Conduce", "Sala", "Señal o checkpoint", "Si vas tarde"], PACE)}</div>
<div class="card"><h2>Ruta recortada a 90 minutos</h2>{tbl(["Bloque", "Min", "Cómo"], CUT90)}<p class="m">Total: {sum(int(c[1]) for c in CUT90)} minutos.</p></div>
<div class="card"><h2>Si alguien no tiene licencia</h2>{NOLIC}</div>
<div class="card"><h2>Guion</h2>{script}</div>
<div class="card"><h2>Cifras clave</h2>{key}</div>
<div class="card"><h2>Preguntas frecuentes preparadas</h2>{tbl(["Pregunta", "Respuesta"], [[E(q), E(a)] for q, a in FAQ])}<div class="callout warn">La respuesta sobre entrenamiento de modelos y datos sigue la documentación pública de Microsoft para cuentas de trabajo; si preguntan detalles (retención, ubicación de datos), remitir a TI y a la documentación oficial.</div></div>
<div class="card"><h2>Nombres de la interfaz por confirmar</h2>{tbl(["Dónde", "Texto en la guía", "Estado"], UI)}</div>
<div class="card"><h2>Pruebas en vivo</h2>{dry}</div>
<div class="card"><h2>Riesgos</h2><ul><li>Muchos sin licencia: ver la sección anterior.</li><li>Descarga lenta: .zip por el chat de la reunión o memoria USB.</li><li>Copilot lento con muchas personas: el presentador corre el prompt y la sala compara con el checkpoint.</li>
<li>Preguntas de RH sobre datos de personas: responder con el recuadro de uso responsable y canalizar a TI y a la política de la empresa.</li></ul></div>"""
    open(os.path.join(INT, "Guia_Presentador_INTERNAL.html"), "w", encoding="utf-8").write(page("Guía del presentador · Copilot en tu día a día", "Bootcamp TDx Bepensa · martes 10 de noviembre de 2026 · 12:00–14:00 (Mérida, por confirmar)", body))


DRY = [["Pendiente", "Se llena con las pruebas en vivo."]]


def tenant():
    items = [("Primero: plan B del 4.3", ["Correr 4.3b (actualizar la presentación desde el Word). Si no cambia nada, correr el plan B: agregar la cuarta acción en la diapositiva de acciones tomándola de /Zava_Reporte_3T. Anotar cuál funciona y ajustar el guion de la demo."]),
             ("Acceso y licencias", ["Confirmar qué asistentes tienen licencia de Microsoft 365 Copilot y quiénes solo Copilot Chat.", "Con una cuenta con licencia y otra sin licencia: anotar qué etiqueta ve cada una en el panel de Copilot («M365 Copilot (Premium)» o «M365 Copilot (Basic)») y qué puede hacer en Excel (modos, crear hojas y fórmulas), Word (redactar, reescribir, /) y PowerPoint (crear desde un archivo, editar diapositivas).",
                                     "¿Aparece la pestaña Work IQ en la aplicación Microsoft Copilot? ¿Cómo se llama el modo web en español?", "Descargar el .zip desde la ubicación de TDx y subirlo a OneDrive."]),
             ("Excel", ["Correr 2.1 en modo de solo chat: ¿encuentra el duplicado, el atípico y el mes faltante?", "Correr 2.2a, 2.2b y 2.2c: ¿crea Datos_limpios, Resumen_3T con fórmulas ponderadas, la gráfica y la tabla dinámica?",
                        "Correr 2.3 y comparar Hechos con CHECKPOINT_Ej2.", "Correr 2.4: ¿clasifica en los 5 temas y marca los 2 comentarios con nombre?", "Confirmar Ctrl + Mayús + M y los nombres de los modos en español.", "Medir tiempos de respuesta."]),
             ("Word", ["Correr 3.1 con / a las notas y Hechos pegada: ¿respeta las cifras?", "¿Permite / a un archivo de Excel? Si sí, simplificar el 3.1.", "Correr 3.2 y 3.3 (y la variante RH)."]),
             ("PowerPoint", ["Correr 4.1 con la plantilla y / al reporte.", "Correr 4.2 por el camino principal (copiar y pegar la gráfica). Probar también el «Pruébalo» con / al Excel.",
                             "Correr 4.3b: cambiar el Word y pedir la actualización. ¿Cambia solo lo necesario?", "Correr 4.3c: ¿escribe notas del orador?", "¿Hay kit de marca publicado?"]),
             ("Outlook, Teams y Copilot Chat", ["«Borrador con Copilot» en Outlook nuevo y clásico.", "Correr 5.3 en chat nuevo y anotar los 6 veredictos.",
                                                "Sin licencia: subir archivos a Copilot Chat y correr 2.1, 2.4, 3.3 y 5.3.", "«Guardar mensaje» y «Sus mensajes»: ¿texto exacto en español? ¿Disponible sin licencia?",
                                                "«Programar esta indicación» en la pestaña Work IQ (requiere licencia y experiencias conectadas)."]),
             ("Agentes", ["Agentes > Analista e Investigador: ¿disponibles? Correr 6.2a y 6.2b."]),
             ("Salón", ["Wi-Fi para todos al mismo tiempo; proyector; enlace de la guía en el chat de la reunión."])]
    body = "<div class='callout imp'>Hacer antes del martes con cuentas del tenant de Bepensa (una con licencia y una sin licencia).</div>" + "".join(
        f"<div class='card'><h2>{t}</h2><ul class='cb'>" + "".join(f"<li>{E(x)}</li>" for x in xs) + "</ul></div>" for t, xs in items)
    open(os.path.join(INT, "Pruebas_Tenant_Bepensa_INTERNAL.html"), "w", encoding="utf-8").write(page("Lista de pruebas en el tenant de Bepensa", "Copilot en tu día a día", body))


def answer_book():
    wb = Workbook(); ws = wb.active; ws.title = "Leeme"; ws["A1"] = "Libro de respuestas · INTERNO"; ws["A1"].font = Font(bold=True, size=14, color="B42318")
    H = Font(bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor="1E1B4B")
    def sh(name, head, rows, w):
        s = wb.create_sheet(name)
        for j, h in enumerate(head, 1): c = s.cell(1, j, h); c.font = H; c.fill = HF
        for i, r in enumerate(rows, 2):
            for j, v in enumerate(r, 1): s.cell(i, j, v)
        for j, x in enumerate(w, 1): s.column_dimensions[chr(64 + j)].width = x
    sh("Ej2_Problemas", ["Problema", "Región", "Mes", "Valor"], [["Duplicado", Z.DUP[0], Z.DUP[1], K["dup_atendidas"]], ["Atípico (tiempo)", Z.OUT[0], Z.OUT[1], Z.OUT[2]], ["Mes faltante", Z.MISS[0], Z.MISS[1], None]], [20, 14, 10, 12])
    sh("Ej2_Resumen_3T", ["Región", "Atendidas", "Tiempo", "Satisfacción", "% ejercido"], [[g, K[f"ate_3T_{g}"], K[f"tiempo_3T_{g}"], K[f"sat_3T_{g}"], K[f"pres_pct_3T_{g}"]] for g in Z.REG] +
       [["Total", K["ate_3T"], K["tiempo_3T"], K["sat_3T"], K["pres_pct_3T"]]], [12, 12, 12, 12, 12])
    sh("Ej2_Temas", ["Tema", "Comentarios", "Calificación"], [[t, K[f"tema_n_{t}"], K[f"tema_cal_{t}"]] for t, *_ in Z.THEMES], [30, 12, 12])
    sh("Ej5_Veredictos", ["#", "Afirmación", "Veredicto", "Por qué"], [[i, *c] for i, c in enumerate(CLAIMS, 1)], [4, 70, 16, 80])
    sh("Cifras_clave", ["Clave", "Valor"], [[k, v] for k, v in K.items() if isinstance(v, (int, float))], [34, 20])
    wb.save(os.path.join(INT, "Libro_Respuestas_INTERNAL.xlsx"))


GEN = [("Ponerte al día", "Copilot Chat (Work IQ)", P["1.1a"]), ("Encontrar y resumir un archivo", "Copilot Chat (Work IQ)", P["1.2"]),
       ("Revisar datos antes de analizar", "Excel · Copilot Chat", "Revisa la hoja [nombre] antes de analizarla: duplicados, valores atípicos y meses o registros faltantes. Para cada problema dime dónde está y qué efecto tendría. No cambies nada."),
       ("Resumen con gráfica", "Excel", "Crea una hoja Resumen con fórmulas por [región/área] y [periodo]: [indicadores]. Pondera los promedios por [volumen]. Inserta una gráfica de columnas de [indicador]."),
       ("Hoja Hechos", "Excel", "Crea una hoja Hechos: #, hecho, cifra (fórmula a la hoja de origen), unidad, fuente y revisado por. Nada entra al reporte si no está aquí."),
       ("Comentarios por tema", "Excel · Copilot Chat", "Clasifica los comentarios de la columna [columna] en estos temas: [temas]. Cuenta cuántos hay por tema, el % y la calificación promedio. No cites comentarios que mencionen a una persona."),
       ("Reporte de una página", "Word", "Escribe un reporte de una página para [público] con estas cifras: [pega Hechos] y /[notas]. Secciones: resultados, causas, calidad de los datos y acciones. No inventes cifras."),
       ("Preguntas frecuentes", "Word · Copilot Chat", "Con /[política o procedimiento], escribe [n] preguntas frecuentes con respuestas de máximo 2 líneas. Si algo no está, escribe «El documento no lo indica»."),
       ("Presentación desde un Word y ajustes", "PowerPoint", "Crea una presentación de [n] diapositivas a partir de /[documento] con esta plantilla. Después: «Actualiza la presentación con la versión nueva de /[documento] y dime qué cambiaste» y «Escribe las notas del orador»."),
       ("Revisión antes de enviar", "Copilot Chat (chat nuevo)", "Eres un revisor independiente. Revisa cada afirmación de [borrador] contra [datos] con los veredictos Verificado, Incorrecto, No verificable o Exagerado, con la cifra correcta y la fuente.")]
RH = [("Descripción de puesto", "Redacta una descripción de puesto de [puesto]: objetivo, 6 responsabilidades, requisitos, competencias y condiciones, con lenguaje incluyente y sin requisitos que discriminen (edad, género, estado civil)."),
      ("Plan de inducción", "Crea un plan de inducción de 2 semanas para [puesto] en [área]: actividades por día, responsables (por puesto), documentos a revisar y un punto de control al final de cada semana."),
      ("Clima laboral (anónimo)", "Con los resultados anónimos de la encuesta de clima, agrupa los comentarios por tema y calcula el % por tema. No muestres grupos de menos de 5 respuestas ni intentes identificar a nadie."),
      ("Preguntas frecuentes de una política", "Con /[política], escribe 8 preguntas frecuentes para los colaboradores, con respuestas cortas. Si algo no está en la política, dilo."),
      ("Comunicado interno", "Escribe un comunicado sobre [cambio o política] en tono cercano: qué cambia, desde cuándo, a quién aplica y a quién preguntar. Máximo 150 palabras.")]


def handout():
    d = Document(); st = d.styles["Normal"]; st.font.name = "Segoe UI"; st.font.size = Pt(9.5)
    for s in d.sections: s.left_margin = s.right_margin = Cm(1.6); s.top_margin = s.bottom_margin = Cm(1.4)
    h = d.add_heading("Copilot en tu día a día: 10 casos para llevar", 0)
    for r in h.runs: r.font.color.rgb = RGBColor(0x1E, 0x1B, 0x4B)
    d.add_paragraph("Bootcamp · martes 10 de noviembre de 2026. Cambia lo que está entre [corchetes]. Escribe / para elegir tus archivos guardados en OneDrive o SharePoint.")
    p = d.add_paragraph(); p.add_run("Copilot propone, tú verificas. ").bold = True; p.add_run("Pide la fuente de cada cifra, revisa los datos antes de analizarlos y revisa el mensaje antes de enviarlo.")
    t = d.add_table(rows=1, cols=4); t.style = "Light Grid Accent 1"
    for c, x in zip(t.rows[0].cells, ["#", "Caso", "App", "Prompt"]): c.text = x
    for i, (c, a, pr) in enumerate(GEN, 1):
        r = t.add_row().cells; r[0].text, r[1].text, r[2].text, r[3].text = str(i), c, a, pr
    for row in t.rows:
        for j, w in enumerate((Cm(0.8), Cm(3.4), Cm(2.9), Cm(10.9))): row.cells[j].width = w
    d.add_paragraph("Licencia: en el panel de Copilot, «M365 Copilot (Premium)» = con licencia; «M365 Copilot (Basic)» = Copilot Chat. Requieren licencia: Ponte al día y Encontrar un archivo (datos de trabajo), programar indicaciones, Analista e Investigador. Si algo no te aparece en Excel, Word o PowerPoint, sube el archivo a Copilot Chat y pega el resultado.").italic = True
    d.add_heading("Para Recursos Humanos", 1)
    t = d.add_table(rows=1, cols=2); t.style = "Light Grid Accent 1"
    for c, x in zip(t.rows[0].cells, ["Caso", "Prompt"]): c.text = x
    for c, pr in RH:
        r = t.add_row().cells; r[0].text, r[1].text = c, pr
    for row in t.rows:
        for j, w in enumerate((Cm(4), Cm(14))): row.cells[j].width = w
    d.add_heading("Uso responsable", 2)
    for x in ["No subas datos personales sensibles (salud, salario de una persona, datos de contacto personales, evaluaciones individuales) si no es necesario y permitido.", "Trabaja con datos anónimos o agregados y quita nombres antes de compartir.",
              "No uses Copilot para decidir sobre personas (contratar, evaluar, promover o sancionar): la decisión es tuya.", "Revisa cifras y afirmaciones antes de enviar."]:
        d.add_paragraph(x, style="List Bullet")
    path = os.path.join(CF, "Copilot_Dia_a_Dia_10_Casos_Hoja_para_llevar.docx"); d.save(path); return path


if __name__ == "__main__":
    import json
    dp = os.path.join(ROOT, "_build", "dry_run.json")
    if os.path.exists(dp): DRY[:] = json.load(open(dp, encoding="utf-8"))
    guide(); tenant(); answer_book(); print(handout())
