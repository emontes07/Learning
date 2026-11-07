# -*- coding: utf-8 -*-
"""Ediciones puntuales (5 nov, ajustes de licencias y 4.2/4.3)."""
import io

def rep(path, pairs):
    s = io.open(path, encoding="utf-8").read()
    for a, b in pairs:
        if a not in s: raise SystemExit(f"NO ENCONTRADO en {path}: {a[:70]}")
        s = s.replace(a, b)
    io.open(path, "w", encoding="utf-8").write(s)

rep("content.py", [
    ('"4.3b": """Actualiza',
     '"4.3plan": """En la diapositiva de las tres acciones, agrega la cuarta acción que aparece en /Zava_Reporte_3T (sección «Acciones para el 4T»). Usa el mismo formato que las otras viñetas y no cambies nada más.""",\n"4.3b": """Actualiza'),
    ("f\"El tiempo promedio del 3T sube a {T['sucio_t']}\"]",
     "f\"Con solo este problema, el tiempo promedio del 3T sube a {hrs(K['tiempo_3T_solo_atipico'])}\"]"),
    ('"Copilot Chat responde con información de la web y con los archivos que subes o abres. Con licencia de Microsoft 365 Copilot, además usa tus datos de trabajo (correos, chats, reuniones y archivos) y trabaja dentro de Excel, Word, PowerPoint, Outlook y Teams para crear y editar."',
     '"Con Copilot Chat (en el panel de Copilot aparece «M365 Copilot (Basic)») respondes con la web y con los archivos que abres o subes, y tienes acceso estándar a Copilot en apps como Excel. La licencia de Microsoft 365 Copilot («M365 Copilot (Premium)») agrega, entre otras cosas, respuestas con tus datos de trabajo (correos, chats, reuniones y archivos), programar indicaciones y los agentes Analista e Investigador. Lo que puedes hacer dentro de Excel, Word y PowerPoint con cada una también depende de la configuración de tu empresa."'),
])

rep("build_guide.py", [
    ('<p>Si no tienes licencia de Microsoft 365 Copilot, cada ejercicio trae una ruta con Copilot Chat. Si no sabes cuál tienes: abre Excel y busca el icono de Copilot; si te deja crear hojas o editar, tienes licencia.</p>',
     '<p><b>¿Cómo sé cuál tengo?</b> Abre Copilot en Excel y busca la etiqueta en el panel de Copilot: <b>M365 Copilot (Premium)</b> significa que tienes licencia de Microsoft 365 Copilot; <b>M365 Copilot (Basic)</b> significa que tienes Copilot Chat, con acceso estándar a Copilot en Excel. Con Basic intenta los ejercicios dentro de Excel, Word y PowerPoint; si una función no te aparece, usa la ruta con Copilot Chat que trae cada ejercicio. Lo que sí requiere licencia: responder con tus datos de trabajo (correos, chats, reuniones y archivos, ejercicios 1.1 y 1.2), programar indicaciones y los agentes Analista e Investigador.</p>'),
    ('<div>{LIC} Copilot dentro de Excel, Word, PowerPoint, Outlook y Teams para crear y editar, y respuestas con tus correos, chats, reuniones y archivos.</div>',
     '<div>{LIC} Usa funciones de la licencia (tus correos, chats, reuniones y archivos, o funciones avanzadas dentro de la app). Si no te aparece algo, usa la ruta con Copilot Chat.</div>'),
    ('intro="Dos caminos: (a) pídelo a Copilot en PowerPoint con <b>/</b> al Excel, o (b) copia la gráfica de la hoja Resumen_3T y pégala en la diapositiva 3.",\n                prompts=[("Gráfica desde el Excel", "PowerPoint", "4.2")],',
     'intro="<b>Camino principal:</b> en Excel selecciona la gráfica de la hoja Resumen_3T, cópiala (<b>Ctrl + C</b>) y pégala en la diapositiva 3 (<b>Ctrl + V</b>). Revisa que las cifras coincidan con la tabla de abajo.</p><p><b>Pruébalo (no está documentado):</b> pídele a Copilot en PowerPoint la gráfica escribiendo <b>/</b> para elegir el Excel. Si no funciona, quédate con el camino principal.",\n                prompts=[("Pruébalo: gráfica con / al Excel", "PowerPoint", "4.2")],'),
    ('nolic="Usa el camino (b): copia la gráfica desde Excel.",', 'nolic="El camino principal (copiar y pegar la gráfica) funciona igual sin licencia.",'),
    ('                fail=ck("CHECKPOINT_Ej4_Resultado_Presentacion.pptx", "el ejercicio 5") + " Tiene notas del orador.",',
     '                fail=("<b>Si «Actualiza desde el Word» no cambia nada</b>, pide el cambio directo en la diapositiva de acciones:"\n'
     '                      f\'<div class="prompt"><div class="prompt-head"><span class="prompt-label">Plan B: agrega la cuarta acción</span><span class="mode mode-ppt">PowerPoint</span><button class="copy" type="button" aria-label="Copiar: Plan B, agrega la cuarta acción">Copiar</button></div><pre id="p-lab-4-3-planb">{E(P["4.3plan"])}</pre></div>\'\n'
     '                      + ck("CHECKPOINT_Ej4_Resultado_Presentacion.pptx", "el ejercicio 5") + " Tiene notas del orador."),'),
    ('"Tus mejores prompts de hoy", "Prompts guardados y compartidos",', '"Tus mejores prompts de hoy", "Prompts guardados y compartidos", lic=CHAT,'),
    ('desde donde lo puedes compartir con tu equipo. Si se repite cada semana, también puedes usar <b>Programar esta indicación</b>.",',
     'desde donde lo puedes compartir con tu equipo. Guardar funciona con Copilot Chat. Programarlo requiere licencia de Microsoft 365 Copilot: si el prompt se repite cada semana, usa <b>Programar esta indicación</b> (pestaña Work IQ).",'),
])

rep("gen_internal.py", [
    ('("7. Preguntas y tu caso", "10", "Preguntas frecuentes primero"), ("Colchón", "3", "Rezagados")]',
     '("7. Preguntas y tu caso", "10", "Preguntas frecuentes primero"), ("Colchón", "3", "Rezagados"), ("Colchón para preguntas", "10", "Preguntas de la sala durante o al final")]'),
    ('NOLIC = """<ul><li>Al inicio pedir manos arriba: ¿quién no ve Copilot dentro de Excel o no puede editar? Sentarlos juntos o en pareja con alguien con licencia.</li>',
     'NOLIC = """<ul><li>Al inicio pedir que abran Copilot en Excel y digan qué etiqueta ven en el panel: <b>M365 Copilot (Premium)</b> = con licencia; <b>M365 Copilot (Basic)</b> = Copilot Chat, con acceso estándar a Copilot en Excel (página de Microsoft «Frequently asked questions about Copilot in Excel»).</li>\n<li>Requiere licencia con seguridad: datos de trabajo (1.1 y 1.2), programar indicaciones (6.1), Analista e Investigador (6.2).</li>\n<li><b>Por confirmar en el tenant:</b> qué pueden hacer las cuentas Basic dentro de Excel, Word y PowerPoint (2.2, 2.3, 2.4, 3.x, 4.x). Mientras tanto, la guía mantiene la ruta con Copilot Chat como respaldo.</li>'),
    ('<li>No funcionan sin licencia: 1.1 y 1.2 (datos de trabajo), las ediciones dentro de las apps (2.2, 2.3, 3.1, 4.x) y Analista e Investigador. Para esos, usar los checkpoints y la ruta alterna.</li>',
     '<li>Si una cuenta Basic no puede hacer algo dentro de la app: ruta con Copilot Chat o checkpoint. Sentar en pareja a quien no pueda avanzar con alguien con Premium.</li>'),
    ('("Guardar prompts", "«Guardar mensaje», «Sus mensajes», galería de Copilot", "Doc es-ES mezcla «Galería de consultas» e «indicaciones». La guía dice «galería de Copilot». ¿Disponible sin licencia?"),',
     '("Guardar prompts", "«Guardar mensaje», «Sus mensajes», galería de Copilot", "Doc es-ES mezcla «Galería de consultas» e «indicaciones». La guía dice que guardar funciona con Copilot Chat y programar requiere licencia."),\n      ("Etiquetas de licencia", "«M365 Copilot (Basic)» / «M365 Copilot (Premium)» en el panel de Copilot", "Según la FAQ de Copilot en Excel; confirmar dónde aparece en Excel, Word y PowerPoint en español."),\n      ("Funciones dentro de las apps con Basic", "La guía invita a intentarlo y da ruta con Copilot Chat", "Por confirmar en el tenant: modos de edición, crear hojas, Word y PowerPoint con cuentas Basic."),'),
    ('"Confirmar qué asistentes tienen licencia de Microsoft 365 Copilot y quiénes solo Copilot Chat.", "Con una cuenta de cada tipo, abrir Excel, Word y PowerPoint: ¿qué ve cada una?",',
     '"Confirmar qué asistentes tienen licencia de Microsoft 365 Copilot y quiénes solo Copilot Chat.", "Con una cuenta con licencia y otra sin licencia: anotar qué etiqueta ve cada una en el panel de Copilot («M365 Copilot (Premium)» o «M365 Copilot (Basic)») y qué puede hacer en Excel (modos, crear hojas y fórmulas), Word (redactar, reescribir, /) y PowerPoint (crear desde un archivo, editar diapositivas).",'),
    ('    items = [("Acceso y licencias", [',
     '    items = [("Primero: plan B del 4.3", ["Correr 4.3b (actualizar la presentación desde el Word). Si no cambia nada, correr el plan B: agregar la cuarta acción en la diapositiva de acciones tomándola de /Zava_Reporte_3T. Anotar cuál funciona y ajustar el guion de la demo."]),\n             ("Acceso y licencias", ['),
    ('"Correr 4.2: ¿puede crear la gráfica con / al Excel? Si no, quedarse con copiar y pegar."',
     '"Correr 4.2 por el camino principal (copiar y pegar la gráfica). Probar también el «Pruébalo» con / al Excel."'),
    ('d.add_paragraph("Licencia: Ponte al día, Encontrar un archivo y las ediciones dentro de Excel, Word y PowerPoint requieren licencia de Microsoft 365 Copilot. Sin licencia, sube el archivo a Copilot Chat y pega el resultado.").italic = True',
     'd.add_paragraph("Licencia: en el panel de Copilot, «M365 Copilot (Premium)» = con licencia; «M365 Copilot (Basic)» = Copilot Chat. Requieren licencia: Ponte al día y Encontrar un archivo (datos de trabajo), programar indicaciones, Analista e Investigador. Si algo no te aparece en Excel, Word o PowerPoint, sube el archivo a Copilot Chat y pega el resultado.").italic = True'),
])

rep("verify.py", [
    ('R["tiempo_3T_sucio"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in r3) / R["ate_3T_sucio"]',
     'R["tiempo_3T_sucio"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in r3) / R["ate_3T_sucio"]\nco = [r for r in clean if r["Mes"] in Q["3T"]]\nR["tiempo_3T_solo_atipico"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in co) / sum(r["Solicitudes_atendidas"] for r in co)'),
])
print("ok")
rep("build_guide.py", [
    ('expect=t_problemas() + "<p>Copilot puede mencionar otras variaciones normales; lo importante es que encuentre estos tres.</p>",',
     'expect=t_problemas() + f"<p>Con los dos problemas juntos (duplicado y atípico), el tiempo promedio del 3T saldría en {T[\'sucio_t\']}; con solo el atípico, en {hrs(K[\'tiempo_3T_solo_atipico\'])}. Con datos limpios es {T[\'tiempo\']}. Copilot puede mencionar otras variaciones normales; lo importante es que encuentre estos tres.</p>",'),
    ("Sin limpiar, el tiempo del 3T saldría en {T['sucio_t']}.</p>\",",
     "Sin limpiar (con el duplicado y el atípico juntos), el tiempo del 3T saldría en {T['sucio_t']}.</p>\","),
])
print("ok2")
