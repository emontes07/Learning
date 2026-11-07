# -*- coding: utf-8 -*-
"""INTERNAL: guía del presentador, libro de respuestas, lista de pruebas en tenant. CUSTOMER_FACING: hoja para llevar."""
import os, json, html, datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from docx import Document
from docx.shared import Pt, RGBColor, Cm
import zava_data as Z, answers as A
from answers import mdp, pesos, num, pct, pts
from gen_docs import T, CLAIMS, briefing_lines
from content import P, CASOS, TARJETA

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_Finanzas_Lab_v1"
INT = os.path.join(ROOT, "INTERNAL"); CF = os.path.join(ROOT, "CUSTOMER_FACING")
os.makedirs(INT, exist_ok=True); os.makedirs(CF, exist_ok=True)
K = A.compute(); E = html.escape

CSS = """:root{--p:#1E1B4B;--s:#4338CA;--a:#F97316;--bg:#f5f5fb;--t:#172033;--m:#5d6b82;--b:#d8dee9}
*{box-sizing:border-box}body{margin:0;font-family:"Segoe UI",system-ui,Arial,sans-serif;color:var(--t);background:var(--bg);line-height:1.5}
.banner{background:#b42318;color:#fff;font-weight:700;text-align:center;padding:6px;letter-spacing:.08em}
.hero{background:linear-gradient(120deg,var(--p),var(--s) 60%,var(--a) 140%);color:#fff;padding:26px 32px}.hero h1{margin:.2em 0;font-size:1.8rem}
.hero .eyebrow{text-transform:uppercase;letter-spacing:.12em;font-size:.78rem;font-weight:700;opacity:.9}
main{max-width:1250px;margin:0 auto;padding:20px}.card{background:#fff;border:1px solid var(--b);border-radius:14px;padding:18px 24px;margin-bottom:18px}
h2{color:var(--p);margin:.1em 0 .5em}h3{color:var(--s)}table{border-collapse:collapse;width:100%;font-size:.88rem;margin:8px 0}
th,td{border-bottom:1px solid var(--b);padding:6px 8px;text-align:left;vertical-align:top}th{background:#eef0fb;color:var(--p)}
.callout{border-left:5px solid var(--a);background:#fff4ec;padding:10px 14px;border-radius:0 10px 10px 0;margin:10px 0}.warn{border-left-color:#d97706;background:#fff4df}.imp{border-left-color:#b42318;background:#ffe9e7}.ok{border-left-color:#2f7d1f;background:#eaf8ef}
.pill{display:inline-block;border-radius:99px;padding:1px 9px;font-size:.78rem;font-weight:600;background:#e0e7ff;color:#3730a3}.e{background:#fde7d4;color:#9a3412}.h{background:#dcfce7;color:#166534}
code,pre{background:#eef2f7;border-radius:6px}pre{padding:10px;white-space:pre-wrap;font-size:.85rem}ul.cb{list-style:none;padding-left:4px}ul.cb li:before{content:"\\2610  ";color:var(--s)}
small,.m{color:var(--m)}"""


def page(title, sub, body, eyebrow="Interno · Microsoft · No compartir ni publicar"):
    return f"""<!DOCTYPE html><html lang="es-MX"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)}</title><style>{CSS}</style></head>
<body><div class="banner">INTERNO · SOLO PRESENTADORES DE MICROSOFT · NO COMPARTIR NI PUBLICAR</div><header class="hero"><div class="eyebrow">{E(eyebrow)}</div><h1>{E(title)}</h1><div>{sub}</div></header><main>{body}</main></body></html>"""


def tbl(head, rows):
    return "<table><thead><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>"


ER, HU = '<span class="pill e">Erik</span>', '<span class="pill h">Humberto</span>'
PACE = [  # inicio, fin, bloque, conduce, sala, señal / checkpoint, si vas tarde
    ("11:30", "12:00", "Receso (antes de empezar)", "Ambos", "Pedir en el receso que descarguen el .zip y lo suban a OneDrive (diapositiva o mensaje en el chat de la reunión)", "Confirmar en el salón que el enlace de descarga funciona", "—"),
    ("12:00", "12:05", "0. Arranque", ER, "Abren el flujo de caja en OneDrive, Copilot abierto, pegan la tarjeta", "12:05: manos arriba quien no ve Copilot → trabajar en pareja", "Saltar el repaso del prompt (ya se vio a las 11:00)"),
    ("12:05", "12:13", "1.1 Caja y alertas", ER, "Prompt 1.1a y 1.1b en modo de solo chat; comprueban una cifra", "Coral el 12/11 debe salir por debajo del mínimo", "Hacer solo 1.1a"),
    ("12:13", "12:20", "1.2 Briefing y correo al CFO", ER, "Copilot Chat con / al documento; Borrador con Copilot sin enviar", "12:18: quien no tenga briefing abre CHECKPOINT_Ej1", "1.2 como demo"),
    ("12:20", "12:30", "2.1 Partidas con fórmulas", HU, "Modo Plan; Cruce_Banco, Cruce_Libros, Partidas", "12:28: menos de la mitad con Partidas → abrir CHECKPOINT_Ej2", "Solo 2.1a + ver Partidas en el checkpoint"),
    ("12:30", "12:36", "2.2 Comprobación independiente", HU, "Chat nuevo; Conciliacion debe dar 0.00", "Diferencia 0.00", "2.2 como demo (2 min)"),
    ("12:36", "12:40", "Debrief conciliación", HU, "¿Quién encontró las 4? Truco del 9", "Conectar el duplicado con la alerta del 1.1", "Recortar a 1 min"),
    ("12:40", "12:48", "3.1 Variaciones", ER, "Modo de edición; hoja Variaciones", f"Golfo {T['golfo_vol']} en volumen", "—"),
    ("12:48", "12:56", "3.2 Puente (ver y comparar)", ER, "Miran la pantalla; comparan con la tabla; los rápidos lo hacen", f"Precio {T['ef_pre']}, volumen {T['ef_vol']}, mezcla {T['ef_mez']}", "Mostrar solo el resultado del checkpoint"),
    ("12:56", "13:05", "3.3 Hechos del cierre", ER, "Modo de edición; agregan ajustes de la conciliación", "13:03: abrir CHECKPOINT_Ej3 quien no termine", "Abrir directo el checkpoint del 3"),
    ("13:05", "13:15", "4.1 Atípico y pronóstico", HU, "Solo chat para el atípico, Plan para el pronóstico", f"Golfo julio 2026; 4T {T['q4_vs']} vs ppto", "4.1a en sala + 4.1b como demo"),
    ("13:15", "13:22", "4.2 Escenarios", HU, "Modo de edición; Escenarios y renglones Estimación", f"Combinado {T['esc_comb']}", "Ver en checkpoint"),
    ("13:22", "13:25", "Debrief forecast", HU, "Observado vs Estimación", "13:25: todos abren CHECKPOINT_Ej4 si no terminaron", "—"),
    ("13:25", "13:31", "5.1 Resumen para el Consejo", ER, "Copilot Chat con / al libro y al documento", "Cada viñeta con número de hecho", "Usar el resumen del checkpoint"),
    ("13:31", "13:38", "5.2 Presentación", ER, "PowerPoint con la plantilla; notas del orador", "Tres cifras revisadas", "Demo con el checkpoint"),
    ("13:38", "13:44", "5.3 Preguntas y soporte", HU, "Copilot Chat o Prepararse para preguntas", "Lista de soporte para el auditor", "Demo de 2 min"),
    ("13:44", "13:50", "5.4 Revisión con veredictos", ER, "Chat nuevo; 8 afirmaciones", "3/2/2/1 (la 5 puede variar)", "No recortar: es el cierre de la historia"),
    ("13:50", "13:53", "6.1 Guardar y programar (demo)", HU, "Ven la demo; guardan su prompt", "—", "Mencionar y pasar a 6.3"),
    ("13:53", "14:00", "6.3 Trae tu caso + cierre", "Ambos", "Prueban la plantilla con un caso real; tabla de 10 casos", "Recoger 3 casos en voz alta", "—"),
]
CUT90 = [("0. Arranque", "3", "Archivos descargados en el receso; sin repaso del prompt"), ("1.1 Caja y alertas", "8", "Solo 1.1a"), ("1.2 Briefing", "4", "Demo; el correo queda como tarea"),
         ("2.1 Partidas", "12", "2.1a + 2.1b"), ("2.2 Comprobación", "3", "Demo"), ("3.1 Variaciones", "8", "Igual"), ("3.2 Puente", "2", "Solo mostrar el checkpoint"),
         ("3.3 Hechos del cierre", "8", "Igual"), ("4.1 Pronóstico", "8", "4.1a en sala, 4.1b demo; todos abren CHECKPOINT_Ej4"), ("4.2 Escenarios", "4", "Demo con la tabla"),
         ("5.1 + 5.2", "6", "Demo continua con los checkpoints del 5"), ("5.3 Preguntas", "2", "Demo"), ("5.4 Veredictos", "8", "En sala, completo"),
         ("6. Trae tu caso + cierre", "8", "Sin 6.1; plantilla 6.3 y tabla de casos"), ("Colchón", "6", "Preguntas, rezagados")]
UI_UNVERIFIED = [
    ("Excel · modos", "«modo de edición», «modo Plan», «modo de solo chat»", "Vistos en la página es-ES (traducción automática); confirmar el texto exacto en la interfaz es-MX."),
    ("Excel · abrir Copilot", "«icono de Copilot en la esquina inferior derecha», Alt + C", "Página es-ES del botón de acción dinámica; confirmar en las laptops de Bepensa (canal de actualización)."),
    ("Excel · chat nuevo", "«chat nuevo» en el panel de Copilot", "En la interfaz en inglés (5 nov) el botón se llama «New chat» y está arriba del panel. Verificar el texto en español."),
    ("Excel · selector de modo", "Botón junto al cuadro de chat, Ctrl + Mayús + M", "En inglés: «Allow editing» (predeterminado), «Plan», «Chat only»; atajo Ctrl+Shift+M. Confirmar los textos en español (la doc es-ES dice «Permitir el modo de edición»)."),
    ("Copilot Chat · adjuntar", "«+» y la opción de cargar archivos", "La doc es-ES dice «Adjuntar contenido» / «Cargar»; la interfaz en inglés de hoy dice «Upload images and files» y «Attach cloud files». La guía usa una descripción genérica."),
    ("PowerPoint · crear desde archivo", "Referenciar el documento con / en el panel de Copilot", "La página dedicada «desde un archivo» ya no existe; está documentado referenciar archivos en el prompt. Probar con la plantilla."),
    ("PowerPoint · notas del orador", "Copilot escribe notas del orador", "No documentado. La guía trae plan B (pegarlas en el panel de Notas)."),
    ("PowerPoint · Habilidades", "«Habilidades» > «Prepararse para preguntas»", "Visto en es-ES; confirmar disponibilidad en el tenant."),
    ("Excel · aptitudes", "«Administrar complementos & aptitudes» > «Crear carpeta de OneDrive» > «Abrir carpeta de habilidades»; «Agregar» > «Elegir complementos y aptitudes»", "Vistos en es-ES; la página mezcla «aptitudes» y «habilidades». Función en despliegue."),
    ("Copilot Chat · guardar", "«Guardar mensaje», «Sus mensajes», «Galería de consultas de Copilot»", "Vistos en es-ES; la misma página también dice «indicaciones» y «avisos»."),
    ("Copilot Chat · programar", "«Programar esta indicación», «Configuración y más» > «Indicaciones programadas»", "Vistos en es-ES. Las etiquetas de frecuencia no están documentadas."),
    ("Analista", "«Agentes» > «Analista»", "Visto en es-ES. Si ejecuta Python y los límites de archivo no están documentados en es-ES."),
    ("Word · referenciar Excel", "/ a un .xlsx desde Word", "No documentado; por eso el 5.1 se hace en Copilot Chat."),
]


def guide():
    pace = tbl(["Inicio", "Fin", "Bloque", "Conduce", "Qué hace la sala", "Señal o checkpoint", "Si vas tarde"], PACE)
    cut = tbl(["Bloque", "Min", "Cómo"], CUT90) + f"<p class='m'>Total: {sum(int(c[1]) for c in CUT90)} minutos.</p>"
    ui = tbl(["Dónde", "Texto usado en la guía", "Estado"], UI_UNVERIFIED)
    key = tbl(["Ejercicio", "Cifras que deben salir"], [
        ["1.1", f"Caja {T['caja_exacta']} (Ceiba {pesos(K['caja_ceiba'])}, Coral {pesos(K['caja_coral'])}, Jade {pesos(K['caja_jade'])}). Coral {pesos(K['coral_12nov'])} el 12/11 y {pesos(K['coral_13nov'])} el 13/11; traspaso ≥ {pesos(K['coral_traspaso_necesario'])}. Atípico 22/10 Ceiba {pesos(K['atipico_22oct_pagos'])}. Cobranza {T['cobr']}; DSO Moderno {T['dso_jul']} → {T['dso']}."],
        ["2", f"Banco {pesos(K['conc_saldo_banco'])}; libros {pesos(K['conc_saldo_libros'])}; diferencia {T['dif']}. Tránsito {pesos(K['dep_transito'])}; comisión {pesos(K['comision'])} + IVA {pesos(K['comision_iva'])}; duplicado {T['dup']}; error {pesos(K['error_dif'])}. Ajustado {pesos(K['conc_ajustado_banco'])}."],
        ["3", f"Ventas {T['ventas_r']} ({T['ventas_varpct_p']} ppto; {T['ventas_varpct_a']} AA). Volumen {T['vol_r']} CU ({T['vol_varpct_p']}; {T['vol_varpct_a']}). Efectos: volumen {T['ef_vol']}, mezcla {T['ef_mez']}, precio {T['ef_pre']}. Azúcar {T['az_cu']}/CU ({T['az_tar']}). MB {T['mb_r']} vs {T['mb_p']}. EBITDA {pesos(K['ebitda_r'])} → ajustado {pesos(K['ebitda_r_aj'])} vs {pesos(K['ebitda_p'])} ({T['ebitda_pct']})."],
        ["4", f"Atípico Golfo jul-2026 {T['atip']} CU → {num(K['atipico_reemplazo'])}. Crecimiento {T['g_adj']} (sin ajustar {T['g_raw']}). 4T {T['q4_vol']} CU; {T['q4_ventas']} ({T['q4_vs']}). Escenarios: azúcar {T['esc_az']}, TC {T['esc_tc']}, combinado {T['esc_comb']} ({T['esc_pct']})."],
        ["5.4", "; ".join(f"{i}. {c[1]}" for i, c in enumerate(CLAIMS, 1))],
    ])
    script = ""
    S = [
        ("0. Arranque (12:00)", "«Ya vieron el marco, la colaboración y el arte del prompt. Ahora lo aplicamos a su trabajo: dos horas, un cierre completo, de la caja al Consejo, con una empresa ficticia que se parece mucho a la suya.» Mostrar la regla «Copilot propone, tú verificas». Pedir que peguen la tarjeta de reglas.",
         "Si alguien no ve Copilot en Excel: abrir el archivo desde OneDrive en Excel para la web. Si sigue sin verlo, trabajar en pareja."),
        ("1. Briefing de caja (12:05)", "«El CFO quiere saber dónde está el dinero y qué viene.» Correr 1.1a en pantalla. Preguntar: ¿quién vio la alerta de Coral? ¿Quién vio algo raro el 22 de octubre? (sembrar el duplicado). En 1.2, mostrar cómo / trae el documento y cómo Copilot une Excel y correos.",
         "Hacer una verificación en voz alta: filtrar Coral 30/10."),
        ("2. Conciliaciones (12:20)", "«Esto es lo que más tiempo les come cada mes.» Insistir: fórmulas, no texto. Modo Plan para ver los pasos. En 2.2: chat nuevo = revisor independiente. Truco del 9 para el error de captura.",
         "Si Copilot pega valores, mostrar el prompt de rescate de la guía."),
        ("3. Cierre y presupuesto (12:40)", "«Vendimos más que el presupuesto pero ganamos menos: ¿por qué?» 3.1 en sala; 3.2 lo construye el presentador (es el más pesado) y la sala compara. 3.3: «nada entra al Consejo si no está en Hechos del cierre».",
         "Si preguntan por la fórmula de mezcla: es el estándar precio-volumen-mezcla; el checkpoint la tiene en Puente_Ppto."),
        ("4. Forecasting (13:05)", "«Un mes raro puede arruinar un pronóstico.» Pedir que pregunten antes de construir (4.1a). Conectar con la minuta. Observado vs Estimación. Escenarios con referencias a celdas para poder moverlos en vivo.",
         "Si alguien pregunta por métodos más avanzados: Analista (4.3) o Python en Excel; no entrar a detalle."),
        ("5. Consejo y auditoría (13:25)", "«Del Excel al Consejo sin copiar y pegar cifras.» 5.1 en Copilot Chat; 5.2 en PowerPoint con la plantilla; 5.3 preguntas incómodas; 5.4 es el clímax: el borrador comercial tiene errores y Copilot, como revisor, los encuentra.",
         "Si 5.2 falla en el tenant, usar el checkpoint y enseñar el panel de Notas."),
        ("6. Automatiza y trae tu caso (13:50)", "Demo rápida de Programar esta indicación con el prompt 6.1 (ya lo vieron a las 10:00; aquí es aplicado). Luego 6.3: «¿quién trae un caso?». Recoger 3 casos y resolver uno en pantalla.",
         "Agentes: solo si preguntan. Demo sugerida: agente de conciliaciones con la receta del 6.2 como instrucciones."),
    ]
    for t, s, n in S:
        script += f"<h3>{t}</h3><p>{s}</p><div class='callout'><b>Nota:</b> {n}</div>"
    pre = """<h3>Antes del lunes</h3><ul class="cb">
<li>Correr los ejercicios 1 a 5 en el tenant de Bepensa con una cuenta de prueba en español (ver Pruebas_Tenant_Bepensa_INTERNAL.html).</li>
<li>Acordar con TDx dónde se alojan index.html, la carpeta files/ y el .zip (ubicación aprobada por Bepensa; el chat de la reunión de Teams como respaldo). No publicar en GitHub Pages sin aprobación.</li>
<li>Pedir a TDx que envíe el enlace antes del receso de las 11:30.</li>
<li>Confirmar con Humberto la división de bloques y quién recorre la sala.</li>
<li>Tener abiertos en la laptop del presentador: los 5 archivos, los checkpoints y la guía en la sección 0.</li></ul>
<h3>Lunes, antes de las 12:00</h3><ul class="cb"><li>Probar el enlace de descarga desde una laptop de Bepensa.</li><li>Iniciar sesión en Copilot y abrir Excel con el flujo de caja.</li><li>Pegar la tarjeta de reglas en un chat de prueba.</li></ul>"""
    demos = tbl(["Demo", "Cuándo", "Cómo"], [
        ["3.2 Puente", "12:48", "Modo Plan con el prompt 3.2 sobre tu propio libro; comparar con CHECKPOINT_Ej3."],
        ["4.3 Analista (si sobra tiempo)", "13:22", "Agentes > Analista, adjuntar Zava_Cierre_Oct2026.xlsx, prompt 4.3."],
        ["5.2 PowerPoint", "13:31", "Plantilla + / Zava_Resumen_Consejo; si falla, CHECKPOINT_Ej5_Resultado_Consejo.pptx."],
        ["6.1 Programar indicación", "13:50", "Pasar el cursor sobre el prompt 6.1 > Programar esta indicación > semanal, martes 8:00."],
        ["Agente (solo si preguntan)", "13:53", "Agente de conciliaciones: instrucciones = receta 6.2; conocimiento = carpeta de conciliaciones. Mostrar 2 minutos; no es parte del laboratorio."],
    ])
    dry = tbl(["Prueba", "Resultado", "Ajuste"], [
        ["5.4 veredictos · 6 corridas en Copilot Chat (tenant Microsoft, contenido pegado)", "Afirmaciones 1–4, 6–8 estables tras el ajuste. La 5 alterna entre No verificable e Incorrecto.", "Se reescribieron las afirmaciones 5 y 6, se agregó una regla de decisión al prompt y una nota en la guía para discutir la 5."],
        ["1.2 briefing y correo · 1 corrida", "Cifras exactas, dos alertas, KPI, decisiones; correo con pregunta final. Copilot ofrece un botón para enviar el correo.", "Se agregó a la guía «no lo envíes» y la regla de millones con un decimal."],
        ["5.1 resumen para el Consejo · 1 corrida", "Todas las cifras coinciden con Hechos del cierre y cita cada hecho; usó pesos exactos en lugar de millones.", "Se agregó la regla de formato al prompt."],
        ["Excel para la web 1.1a (modo Chat only) · 1 corrida", "Todas las cifras correctas (caja, Coral 12 y 13/11, traspaso, atípico 22/10), pero también listó las quincenas de azúcar, nómina e impuestos como atípicas. Tardó ~1.5 min.", "Se afinó el prompt para excluir pagos periódicos."],
        ["Excel para la web 2.1a (Allow editing) · 1 corrida", "Creó Cruce_Banco y Cruce_Libros con fórmulas vivas. Cruce_Banco: 5 no conciliados (esperado). Cruce_Libros: 3 (contó también el PET repetido). ~2 min.", "La guía acepta 2 o 3 en Cruce_Libros."],
        ["Excel para la web 2.1b · 1 corrida", "Partidas con SUMIFS; 5 renglones (separó el IVA); suma = diferencia de saldos; control 0.00. ~3.5 min.", "La guía acepta 4 partidas o 5 renglones. Ritmo: 2.1 puede pasar de 10 min; tener listo el checkpoint."],
        ["Excel para la web 3.1 (Allow editing) · 1 corrida", "Creó Variaciones con SUMIFS; cifras correctas (Golfo −$7.1 millones, −5.4 %; total +$4.3 millones, +0.6 %). Usó formato de España (coma decimal). ~2.5 min.", "Se agregó «formato de México» a la tarjeta de reglas."],
        ["Excel 2.2, 3.2, 3.3, 4.x y PowerPoint 5.2", "No probados en la app por tiempo.", "Probarlos en el tenant de Bepensa (lista de pruebas)."],
    ])
    body = f"""<div class="card"><h2>Resumen</h2><p>Bloque «Experiencia interactiva del área», lunes 9 de noviembre de 2026, 12:00–14:00 (hora de Mérida, UTC−6), presencial en BImpulsa. 64 invitados de Finanzas con licencia de Microsoft 365 Copilot. Antes: AI Framework (9:00), Collaboration Framework (10:00: Loop, Facilitator, Workspaces, agentes, Brand kits) y Arte del prompting (11:00–11:30), receso 11:30–12:00.</p>
<p>Historia: Zava Bebidas (ficticia), cierre de octubre 2026 → Consejo del 26 de noviembre. Cada ejercicio alimenta al siguiente. Agentes solo si preguntan.</p>
<p><b>Propuesta de roles (confirmar con Humberto):</b> {ER} conduce 0, 1, 3 y 5; {HU} conduce 2, 4 y 6. Quien no conduce recorre la sala y avisa cuándo abrir checkpoints.</p></div>
<div class="card"><h2>Tabla de ritmo (hora de Mérida)</h2>{pace}</div>
<div class="card"><h2>Ruta recortada a 90 minutos</h2>{cut}</div>
<div class="card"><h2>Guion por escenario</h2>{script}</div>
<div class="card"><h2>Cifras clave para la sala</h2>{key}<p class="m">Detalle completo en Libro_Respuestas_INTERNAL.xlsx.</p></div>
<div class="card"><h2>Demos</h2>{demos}</div>
<div class="card"><h2>Nombres de la interfaz por confirmar</h2><div class="callout warn">Verificados contra support.microsoft.com/es-es (las páginas es-MX redirigen a es-ES y son traducción automática). Lo siguiente no se pudo verificar o puede variar: confírmalo en el tenant antes del lunes.</div>{ui}</div>
<div class="card"><h2>Preparación</h2>{pre}</div>
<div class="card"><h2>Pruebas en vivo con Copilot (5 de noviembre)</h2>{dry}</div>
<div class="card"><h2>Riesgos y plan B</h2><ul>
<li><b>Descarga lenta o bloqueada:</b> enviar el .zip por el chat de la reunión de Teams; tener una memoria USB con la carpeta.</li>
<li><b>Copilot en Excel no aparece en algunas laptops:</b> Excel para la web desde OneDrive; si no, trabajar en pareja.</li>
<li><b>Copilot tarda con 64 personas a la vez:</b> el presentador corre el prompt en pantalla y la sala compara con el checkpoint.</li>
<li><b>Etiquetas de confidencialidad:</b> si la política aplica etiquetas por defecto, los archivos de práctica podrían quedar etiquetados; no afecta a Copilot salvo cifrado. Probarlo.</li>
<li><b>Preguntas sobre datos reales de Bepensa:</b> responder con el principio (Copilot solo ve lo que el usuario ya puede ver) y canalizar a TI.</li></ul></div>"""
    open(os.path.join(INT, "Guia_Presentador_INTERNAL.html"), "w", encoding="utf-8").write(
        page("Guía del presentador · Copilot para Finanzas: del cierre al Consejo", "Bootcamp de Finanzas · TDx Bepensa · lunes 9 de noviembre de 2026 · 12:00–14:00 (Mérida)", body))


def tenant_tests():
    items = [
        ("Acceso", ["Iniciar sesión con una cuenta de prueba de Finanzas con licencia de Microsoft 365 Copilot e interfaz en español.",
                    "Descargar el .zip desde la ubicación que defina TDx y subir la carpeta a OneDrive.",
                    "Confirmar si la política aplica etiquetas de confidencialidad por defecto a archivos nuevos y si eso bloquea a Copilot."]),
        ("Excel", ["Abrir Zava_Flujo_Caja_Diario_Oct2026.xlsx en Excel para la web y en Excel de escritorio: ¿aparece el icono de Copilot? ¿Funciona Alt + C?",
                   "Anotar los nombres exactos de los modos (edición, Plan, solo chat) y del botón para iniciar un chat nuevo.",
                   "Confirmar que Ctrl + Mayús + M cambia de modo en el panel de Copilot (en Excel para la web y de escritorio).",
                   "Anotar el nombre exacto en español de «Manage plugins & skills» (la doc es-ES dice «Administrar complementos & aptitudes»; ¿aparece «Administrar complementos y aptitudes»?) y dónde está en el panel.",
                   "Correr 1.1a y 1.1b: ¿sale la alerta de Coral del 12/11 y el atípico del 22/10?",
                   "Correr 2.1a y 2.1b en modo Plan: ¿crea hojas con fórmulas (no valores)? ¿Partidas suma la diferencia?",
                   "Correr 2.2 en chat nuevo: ¿la conciliación da 0.00?",
                   "Correr 3.1, 3.2 y 3.3: comparar con CHECKPOINT_Ej3 (ventas, efectos, EBITDA ajustado).",
                   "Correr 4.1a, 4.1b y 4.2: ¿detecta Golfo julio 2026? ¿4T y escenarios coinciden con CHECKPOINT_Ej4?",
                   "Medir el tiempo de respuesta de cada prompt (meta: menos de 90 segundos)."]),
        ("Copilot Chat", ["Probar / para referenciar Zava_Correos_y_Minuta_Oct2026 y Zava_Cierre_Oct2026 desde OneDrive.",
                          "Anotar los nombres del menú + (cargar o adjuntar archivos).",
                          "Correr 1.2, 5.1, 5.3 y 5.4 (chat nuevo). Para 5.4 anotar los 8 veredictos.",
                          "Guardar un mensaje y programar una indicación (Programar esta indicación); confirmar que la opción existe en el tenant.",
                          "Confirmar que «Programar esta indicación» aparece en la pestaña Work IQ de Microsoft Copilot, y que requiere licencia de Microsoft 365 Copilot y las experiencias conectadas activadas (si TI las tiene desactivadas, la opción no aparece).",
                          "Anotar el texto exacto en español de: la opción para guardar (¿«Guardar mensaje»?), el nombre de la galería (¿«Galería de indicaciones» o «Galería de consultas»?) y la pestaña de prompts guardados (¿«Sus mensajes»?). Corregir la guía si difieren."]),
        ("PowerPoint y Outlook", ["Abrir Zava_Plantilla_Consejo.pptx, guardarla como Zava_Consejo_Oct2026 y correr 5.2 con / al resumen.",
                                  "¿Escribe notas del orador? Si no, confirmar el plan B (panel de Notas).",
                                  "¿Está la habilidad «Prepararse para preguntas»?",
                                  "Outlook: ¿aparece «Borrador con Copilot» y «Resumen por Copilot»? (nuevo Outlook y clásico)."]),
        ("Agentes y otros", ["Agentes > Analista: ¿disponible? Correr 4.3 con el archivo adjunto.",
                             "Excel: ¿están las aptitudes personalizadas (Administrar complementos & aptitudes)?",
                             "Investigador: ¿disponible? (solo se menciona).",
                             "Si preguntan por agentes: ¿está habilitado crear agentes para usuarios de Finanzas?"]),
        ("Salón", ["Wi-Fi para 64 laptops con OneDrive y Copilot al mismo tiempo.", "Proyector y audio; segunda pantalla para la guía.",
                   "Enlace de la guía y de los archivos visible en el chat de la reunión de Teams."]),
    ]
    body = ""
    for t, xs in items:
        body += f"<div class='card'><h2>{t}</h2><ul class='cb'>" + "".join(f"<li>{E(x)}</li>" for x in xs) + "</ul></div>"
    body = "<div class='callout imp'>Hacer antes del lunes 9 de noviembre con una cuenta del tenant de Bepensa. Lo que falle se cambia a «Demo» o «Ver y comparar» en la guía del presentador.</div>" + body
    open(os.path.join(INT, "Pruebas_Tenant_Bepensa_INTERNAL.html"), "w", encoding="utf-8").write(page("Lista de pruebas en el tenant de Bepensa", "Copilot para Finanzas: del cierre al Consejo", body))


def answer_book():
    wb = Workbook(); ws = wb.active; ws.title = "Leeme"
    ws["A1"] = "Libro de respuestas · INTERNO · No compartir"; ws["A1"].font = Font(bold=True, size=14, color="B42318")
    ws["A3"] = "Todas las cifras salen de _build/answers.py (la misma base que genera los archivos). Reporte de verificación: Reporte_Verificacion_Cifras_INTERNAL.html."
    H = Font(bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor="1E1B4B")
    def sheet(name, head, rows, w=None):
        s = wb.create_sheet(name)
        for j, h in enumerate(head, 1): c = s.cell(1, j, h); c.font = H; c.fill = HF
        for i, r in enumerate(rows, 2):
            for j, v in enumerate(r, 1): s.cell(i, j, v)
        for j, ww in enumerate(w or [30] * len(head), 1): s.column_dimensions[chr(64 + j)].width = ww
        return s
    sheet("Ej1_Caja", ["Concepto", "Valor", "Texto"], [
        ["Saldo Banco Ceiba 30/10", K["caja_ceiba"], pesos(K["caja_ceiba"])], ["Saldo Banco Coral 30/10", K["caja_coral"], pesos(K["caja_coral"])],
        ["Saldo Banco Jade 30/10", K["caja_jade"], pesos(K["caja_jade"])], ["Posición total", K["caja_total"], pesos(K["caja_total"])],
        ["Coral 12/11 (proyección)", K["coral_12nov"], pesos(K["coral_12nov"])], ["Coral 13/11 (proyección)", K["coral_13nov"], pesos(K["coral_13nov"])],
        ["Traspaso adicional mínimo", K["coral_traspaso_necesario"], pesos(K["coral_traspaso_necesario"])],
        ["Atípico Ceiba 22/10 pagos a proveedores", K["atipico_22oct_pagos"], pesos(K["atipico_22oct_pagos"])], ["Pago PET 08/10", K["pago_pet_08oct"], pesos(K["pago_pet_08oct"])],
        ["Cobranza oct / meta", K["cobranza_oct_cumpl"], T["cobr"]], ["DSO Moderno jul → oct", K["dso_moderno_delta"], f"{T['dso_jul']} → {T['dso']}"]] +
        [[f"Briefing línea {i}", None, l] for i, l in enumerate(briefing_lines(), 1)], [42, 18, 110])
    sheet("Ej2_Conciliacion", ["Concepto", "Valor", "Texto"], [[k, K[k], pesos(K[k])] for k in (
        "conc_saldo_banco", "conc_saldo_libros", "conc_diferencia_inicial", "dep_transito", "comision", "comision_iva", "duplicado", "error_banco", "error_libros", "error_dif",
        "conc_ajustado_banco", "conc_ajustado_libros")], [30, 18, 22])
    rows = []
    for c in Z.CEDIS + ["Total"]:
        sfx = "" if c == "Total" else f"_{c}"
        rows.append([c, K[f"vol_r{sfx}"], K[f"vol_p{sfx}"], K[f"vol_varpct_p{sfx}"], K[f"vol_varpct_a{sfx}"], K[f"ventas_r{sfx}"], K[f"ventas_p{sfx}"],
                     K[f"ventas_var_p{sfx}"], K[f"ventas_varpct_p{sfx}"], K[f"ventas_varpct_a{sfx}"], K[f"ub_r{sfx}"] / K[f"ventas_r{sfx}"]])
    sheet("Ej3_Variaciones", ["CEDIS", "Vol real", "Vol ppto", "Vol % ppto", "Vol % AA", "Ventas real", "Ventas ppto", "Var $ ppto", "Var % ppto", "Var % AA", "MB real"], rows, [12] + [15] * 10)
    sheet("Ej3_Puente", ["Concepto", "Valor", "Texto"], [[k, K[k], mdp(K[k], sign=True) if "pct" not in k else pct(K[k])] for k in (
        "ef_volumen", "ef_mezcla", "ef_precio", "ventas_var_p", "cost_vol_azucar", "cost_tarifa_azucar", "azucar_cu_varpct_p", "cost_tarifa_pet", "cost_tarifa_conc", "cost_tarifa_otros",
        "cost_vol_total", "cost_tarifa_total", "ebitda_p", "ebitda_r", "ebitda_ajuste", "ebitda_r_aj", "ebitda_varpct_p")], [30, 18, 22])
    rows = [[c, K[f"fc_g_{c}"], K[f"fc_vol_{c}_11"], K[f"fc_vol_{c}_12"], K[f"precio_oct_{c}"]] for c in Z.CEDIS]
    s = sheet("Ej4_Pronostico", ["CEDIS", "Crecimiento ajustado", "Nov 2026", "Dic 2026", "Precio oct"], rows, [14, 20, 14, 14, 14])
    for i, (k, v) in enumerate([("Atípico Golfo jul-2026", K["atipico_vol"]), ("Reemplazo", K["atipico_reemplazo"]), ("Crecimiento total ajustado", K["fc_g_total_adj"]),
                                ("Crecimiento total sin ajustar", K["fc_g_total_raw"]), ("4T volumen", K["fc_q4_vol"]), ("4T ventas", K["fc_q4_ventas"]), ("4T ventas ppto", K["pp_q4_ventas"]),
                                ("4T ventas vs ppto", K["fc_q4_ventas_vs_pp"]), ("UB nov–dic base", K["fc_nd_ub"]), ("Escenario azúcar", K["esc_azucar"]), ("Escenario TC", K["esc_tc"]),
                                ("Combinado", K["esc_comb"]), ("Combinado % UB", K["esc_comb_pct_ub"])], 8):
        s.cell(i, 1, k); s.cell(i, 2, v)
    sheet("Ej5_Veredictos", ["#", "Afirmación", "Veredicto", "Por qué"], [[i, c[0], c[1], c[2]] for i, c in enumerate(CLAIMS, 1)], [4, 70, 16, 80])
    sheet("Cifras_clave", ["Clave", "Valor"], [[k, v] for k, v in K.items() if isinstance(v, (int, float))], [34, 22])
    wb.save(os.path.join(INT, "Libro_Respuestas_INTERNAL.xlsx"))


GENERIC = [  # caso, app, prompt genérico (sin cifras de Zava)
    ("Briefing de caja", "Excel", "Con la hoja [Movimientos], dame la posición de caja al [fecha] por banco contra su saldo mínimo, los bancos que caerán bajo su mínimo en los próximos 10 días hábiles (fecha e importe) y cualquier movimiento atípico. Cita la hoja de cada cifra."),
    ("Correos a briefing y correo al CFO", "Copilot Chat · Outlook", "Con /[documento o hilo] y estas cifras: [pega], escribe un briefing de 5 líneas (posición, 2 alertas con fecha e importe, un KPI, decisiones) y un correo de máximo 120 palabras que termine con una pregunta concreta. No inventes cifras."),
    ("Conciliación bancaria", "Excel", "Crea hojas de cruce con fórmulas COUNTIFS entre [estado de cuenta] y [auxiliar] por Referencia e importe, con Estatus por renglón, y una hoja Partidas con SUMIFS que explique la diferencia de saldos. No modifiques las hojas originales."),
    ("Variaciones", "Excel", "Crea una hoja Variaciones por [región/CEDIS] con real, presupuesto y año anterior, variaciones en $ y %, margen y gastos, con fórmulas SUMIFS sobre [hoja de datos]. Luego explica en 3 viñetas qué explica la variación."),
    ("Puente precio–volumen–mezcla", "Excel", "Crea una hoja Puente con fórmulas para los efectos volumen, mezcla y precio por [región y canal], y comprueba que sumen la variación total. Agrega el puente de costos por insumo."),
    ("Hechos del cierre", "Excel", "Crea la hoja Hechos_del_cierre: #, hecho, cifra (fórmula a la hoja de origen), unidad, fuente, tipo (Observado/Estimación) y revisado por. Nada entra a la presentación si no está aquí."),
    ("Pronóstico y escenarios", "Excel · Analista", "Revisa [histórico] y dime si hay meses atípicos y por qué. Luego pronostica [periodo] sin el atípico, con fórmulas, y crea escenarios de [insumo] +10 % y tipo de cambio +1.00 con referencias a celdas. Etiqueta Observado y Estimación."),
    ("Presentación para el Consejo", "Copilot Chat · PowerPoint", "Usa solo /[hoja de hechos] para escribir el resumen del Consejo en [n] secciones, cada viñeta con su cifra y número de hecho. Después, en PowerPoint con tu plantilla: «Crea una presentación a partir de /[resumen] con notas del orador»."),
    ("Preguntas del Consejo y del auditor", "Copilot Chat", "Actúa como consejero independiente y como auditor externo. Con /[presentación] dame las preguntas probables, la respuesta corta, el soporte que hay que llevar y lo que hoy no podemos responder."),
    ("Revisión final con veredictos", "Copilot Chat (chat nuevo)", "Eres revisor independiente. Revisa cada afirmación de /[borrador] contra /[archivo de datos] con los veredictos Verificado, Incorrecto, No verificable o Exagerado, con la cifra correcta y la fuente."),
]


def handout():
    d = Document()
    st = d.styles["Normal"]; st.font.name = "Segoe UI"; st.font.size = Pt(9.5)
    for s in d.sections: s.left_margin = s.right_margin = Cm(1.6); s.top_margin = s.bottom_margin = Cm(1.4)
    h = d.add_heading("Copilot para Finanzas: 10 casos para llevar", 0)
    for r in h.runs: r.font.color.rgb = RGBColor(0x1E, 0x1B, 0x4B)
    d.add_paragraph("Bootcamp de Finanzas · lunes 9 de noviembre de 2026. Cambia lo que está entre [corchetes] por tus archivos. Usa archivos del OneDrive o SharePoint de la empresa y revisa cada cifra antes de enviarla.")
    p = d.add_paragraph(); r = p.add_run("Regla: Copilot propone, tú verificas. "); r.bold = True
    p.add_run("Antes de tu primera pregunta en un archivo, pega tus reglas (definiciones, fórmulas, formato y «di no está en los datos si falta algo»).")
    t = d.add_table(rows=1, cols=4); t.style = "Light Grid Accent 1"
    for c, txt in zip(t.rows[0].cells, ["#", "Caso", "App", "Prompt"]): c.text = txt
    for i, (c, a, pr) in enumerate(GENERIC, 1):
        row = t.add_row().cells; row[0].text = str(i); row[1].text = c; row[2].text = a; row[3].text = pr
    for row in t.rows:
        for j, w in enumerate((Cm(0.8), Cm(3.4), Cm(2.8), Cm(11))): row.cells[j].width = w
    d.add_heading("Anatomía del prompt", 2)
    d.add_paragraph("Objetivo (qué y para quién) · Contexto (periodo, área) · Fuentes (escribe / y elige el archivo) · Expectativas (formato, extensión, cifras con fuente).")
    d.add_heading("Para que se vuelva hábito", 2)
    for x in ["Guarda el prompt que te funcionó y prográmalo si se repite cada semana.", "Pide fórmulas, no valores pegados, y revisa una celda.",
              "Haz la revisión final en un chat nuevo, como revisor independiente.", "Etiqueta Observado y Estimación en todo lo que llegue al Consejo."]:
        d.add_paragraph(x, style="List Bullet")
    path = os.path.join(CF, "Copilot_Finanzas_10_Casos_Hoja_para_llevar.docx"); d.save(path); return path


if __name__ == "__main__":
    guide(); tenant_tests(); answer_book(); print(handout())
