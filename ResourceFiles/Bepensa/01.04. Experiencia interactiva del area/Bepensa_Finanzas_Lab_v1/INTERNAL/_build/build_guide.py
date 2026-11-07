# -*- coding: utf-8 -*-
"""Arma index.html (guía del asistente)."""
import os
from content import *
from content import P

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_Finanzas_Lab_v1"
SES = r"C:\Users\erikmontes\.scout\copilot\session-state\ded84ae8-8a58-4dac-89d7-7ac881332856\files"
CSS = open(os.path.join(SES, "collab_style.css"), encoding="utf-8").read()
JS = open(os.path.join(SES, "collab_script.js"), encoding="utf-8").read()
JS = JS.replace("bepensa-colaboracion-v1", "zava-finanzas-lab-v1").replace("' of '+boxes.length+' casillas completadas'", "' de '+boxes.length+' casillas completadas'")
JS = JS.split("document.querySelectorAll('.fac')")[0]
CSS += """
.lvl{display:inline-block;font-size:.74rem;font-weight:700;border-radius:99px;padding:2px 10px;letter-spacing:.02em}
.lvl-req{background:#4338CA;color:#fff}.lvl-ver{background:#e0e7ff;color:#3730a3}.lvl-demo{background:#fde7d4;color:#9a3412}.lvl-opt{background:#eef2f7;color:#334155}.lvl-reto{background:#1E1B4B;color:#fdba74}
.lvl-sum{margin-left:6px}
.legend{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0}.legend div{flex:1 1 200px;background:#f7f9fc;border:1px solid var(--border);border-radius:10px;padding:8px 12px;font-size:.92rem}
.anat{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.anat div{background:#f0f4f9;border-radius:12px;padding:10px 12px;border-top:4px solid var(--brand-secondary)}.anat div:last-child{border-top-color:var(--brand-accent)}.anat b{display:block;color:var(--brand-primary)}.anat span{font-size:.88rem;color:var(--text-muted)}
@media (max-width:960px){.anat{grid-template-columns:1fr 1fr}}
.rule{background:linear-gradient(120deg,#1E1B4B,#4338CA);color:#fff;border-radius:14px;padding:14px 20px;margin:12px 0;font-size:1.05rem}.rule b{color:#fdba74}
"""

STORY = ("Es martes 3 de noviembre de 2026 en Zava Bebidas, una embotelladora regional ficticia con 4 CEDIS y 3 canales. Octubre está cerrando, el presupuesto 2027 está en curso "
         "y el Consejo sesiona el jueves 26 de noviembre. Hoy harás, en dos horas, lo que el equipo de Finanzas hace en dos semanas: del briefing de caja a la presentación del Consejo. "
         "Lo que encuentres en cada ejercicio alimenta al siguiente.")

AGENDA = [("12:00–12:05", "#ch0", "0. Arranque: archivos, Copilot en Excel y reglas", "Archivos abiertos"),
          ("12:05–12:20", "#ch1", "1. Briefing de caja y KPIs", "Briefing de 5 líneas y correo al CFO"),
          ("12:20–12:40", "#ch2", "2. Conciliaciones y reportes", "Partidas sin conciliar con fórmulas"),
          ("12:40–13:05", "#ch3", "3. Cierre y presupuesto", "Hoja Hechos del cierre"),
          ("13:05–13:25", "#ch4", "4. Análisis y forecasting", "Pronóstico del 4T y escenarios"),
          ("13:25–13:50", "#ch5", "5. Preparación de Consejo y auditoría", "Presentación, preguntas y revisión"),
          ("13:50–14:00", "#ch6", "6. Automatiza y trae tu caso", "Tu prompt guardado y tu caso")]

FILES = [
    ("1_Archivos_de_practica", "Zava_Flujo_Caja_Diario_Oct2026.xlsx", "Ejercicio 1: saldos diarios por banco, proyección al 13 de noviembre, mínimos y KPIs", "xl"),
    ("1_Archivos_de_practica", "Zava_Correos_y_Minuta_Oct2026.docx", "Ejercicios 1 y 5: hilo de correos, borrador comercial para el Consejo y minuta del comité", "wd"),
    ("1_Archivos_de_practica", "Zava_Conciliacion_Banco_Ceiba_Oct2026.xlsx", "Ejercicio 2: estado de cuenta, auxiliar de bancos y formato de conciliación", "xl"),
    ("1_Archivos_de_practica", "Zava_Estado_Cuenta_Banco_Ceiba_Oct2026.csv", "Ejercicio 2 (opcional): el estado de cuenta tal como lo descarga el banco", "csv"),
    ("1_Archivos_de_practica", "Zava_Cierre_Oct2026.xlsx", "Ejercicios 3 y 4: estado de resultados, gastos, histórico de volumen y supuestos del forecast", "xl"),
    ("1_Archivos_de_practica", "Zava_Plantilla_Consejo.pptx", "Ejercicio 5: plantilla de la presentación del Consejo", "pp"),
]
CKS = [("CHECKPOINT_Ej1_Resultado_Briefing.docx", "Resultado del ejercicio 1"), ("CHECKPOINT_Ej2_Resultado_Conciliacion.xlsx", "Resultado del ejercicio 2"),
       ("CHECKPOINT_Ej3_Resultado_Cierre.xlsx", "Resultado del ejercicio 3: empieza aquí el 4"), ("CHECKPOINT_Ej4_Resultado_Forecast.xlsx", "Resultado del ejercicio 4: empieza aquí el 5"),
       ("CHECKPOINT_Ej5_Resultado_Resumen_Consejo.docx", "Resumen para el Consejo (ejercicio 5.1)"), ("CHECKPOINT_Ej5_Resultado_Consejo.pptx", "Presentación del Consejo (ejercicio 5.2)")]
ICON = {"xl": ("X", "#1d6f42"), "wd": ("W", "#185abd"), "pp": ("P", "#c43e1c"), "csv": ("CSV", "#4b5563")}


def file_card(folder, name, desc, kind):
    t, c = ICON[kind]
    return f'<a class="file" href="files/{folder}/{name}" download><span class="xl" style="background:{c}">{t}</span><span><b>{name}</b><br><small>{desc}</small></span></a>'


def welcome():
    sm = "".join(f'<a class="sm-step" href="#ch{i}"><b>{i}</b><span>{t}</span></a>' for i, t in enumerate(
        ["Briefing de caja", "Conciliaciones", "Cierre y presupuesto", "Forecasting", "Consejo y auditoría", "Automatiza"], 1))
    ag = table(["Hora (Mérida)", "Ejercicio", "Te llevas"], [[h, f'<a href="{a}">{t}</a>', y] for h, a, t, y in AGENDA])
    legend = ('<div class="legend"><div><span class="lvl lvl-req">Requerido</span> Lo haces en la sesión.</div>'
              '<div><span class="lvl lvl-ver">Ver y comparar</span> Lo vemos en pantalla y comparas con el checkpoint (o lo haces si vas adelante).</div>'
              '<div><span class="lvl lvl-demo">Demo</span> Solo observar.</div><div><span class="lvl lvl-opt">Opcional</span> Si te sobra tiempo o después.</div>'
              '<div><span class="lvl lvl-reto">Reto</span> Para quien va adelante.</div></div>')
    return f"""<section class="card" id="bienvenida"><h2>Bienvenida</h2>
<p class="lead">{STORY}</p>
<div class="storymap">{sm}</div>
<h3>Agenda (12:00 a 14:00, hora de Mérida)</h3>{ag}
<h3>Cómo leer cada ejercicio</h3>{legend}
<p>Cada ejercicio dice qué archivos usas, qué produce para el siguiente paso, los prompts con botón <b>Copiar</b>, <b>Lo que verás</b> (las cifras que debes obtener) y <b>Si no te sale</b>, con un checkpoint para alcanzar al grupo. Ritmo: lo vemos, lo haces, comparas con tu vecino.</p>
<div class="rule"><b>Copilot propone, tú verificas.</b> Copilot te lleva rápido a un buen borrador; tú respondes por cada cifra que sale de tu escritorio. Por eso cada ejercicio trae una comprobación y el último revisa todo.</div>
<div class="callout note"><div class="callout-title">Datos ficticios</div><div>Zava Bebidas, sus CEDIS, bancos, proveedores y cifras son ficticios. Los mismos prompts funcionan con tus archivos reales: guárdalos en el OneDrive o SharePoint de la empresa y sigue las políticas de datos de tu área.</div></div>
<div class="callout tip"><div class="callout-title">Licencias y funciones</div><div>Todos los ejercicios usan tu licencia de Microsoft 365 Copilot. Algunas funciones llegan por etapas: si no ves un botón, no es un error tuyo; usa el checkpoint y sigue.</div></div>
</section>"""


def ch0():
    files = "".join(file_card(*f) for f in FILES)
    cks = table(["Archivo", "Para qué"], [[dl(FC + f), d] for f, d in CKS])
    anat = ('<div class="anat"><div><b>Objetivo</b><span>Qué quieres y para quién.</span></div><div><b>Contexto</b><span>Periodo, área, por qué.</span></div>'
            '<div><b>Fuentes</b><span>Qué hoja, archivo o correo usar.</span></div><div><b>Expectativas</b><span>Formato, extensión, cifras con fuente.</span></div></div>')
    modes = ('<div class="modes"><div class="mode-card"><div class="mode-name">Modo de solo chat</div><p>Analiza y responde. No cambia el libro. Úsalo para preguntar.</p></div>'
             '<div class="mode-card"><div class="mode-name">Modo Plan</div><p>Copilot te muestra los pasos antes de hacerlos y tú confirmas. Úsalo para construir varias hojas.</p></div>'
             '<div class="mode-card"><div class="mode-name">Modo de edición (Permitir edición)</div><p>Es el modo predeterminado. Copilot cambia el libro: crea hojas y fórmulas. <b>Ctrl + Z</b> deshace y el <b>Historial de versiones</b> de OneDrive guarda lo anterior.</p></div></div>')
    know = table(["Archivo y hoja", "Qué tiene"], [
        ["Flujo de caja · Movimientos", f"Un renglón por banco y día hábil (1 al 30 de octubre): saldo inicial, entradas, salidas y saldo final. Banco Ceiba concentra la cobranza; Coral paga proveedores; Jade, nómina e impuestos."],
        ["Flujo de caja · Proyeccion_Nov", "Del 2 al 13 de noviembre: cobranza esperada, traspasos (positivo entra, negativo sale), pagos programados y nómina."],
        ["Conciliación · Estado_Cuenta / Auxiliar_Bancos", f"Movimientos de octubre de Banco Ceiba según el banco ({K['conc_mov_banco']} renglones) y según contabilidad ({K['conc_mov_libros']}). La Referencia es la llave."],
        ["Cierre · Datos_ER", "Escenario (Real, Presupuesto, Año anterior) × CEDIS × Canal: volumen, ventas, costos por insumo y utilidad bruta."],
        ["Cierre · Gastos_Distribucion / Gastos_Corporativos", "Por CEDIS y por concepto. Las cifras reales son preliminares: les faltan los ajustes de la conciliación."],
        ["Cierre · Historico_Volumen / Supuestos_Forecast / Presupuesto_NovDic", "Volumen mensual por CEDIS desde enero 2025, costos y tipo de cambio de octubre, parámetros de escenarios y presupuesto de noviembre y diciembre."],
    ])
    labs = lab("lab-0-1", "0.1", "Descarga los archivos y abre Copilot en Excel", "Requerido", "3 min", "Todo listo para trabajar", "OneDrive · Excel",
               "El paquete de archivos", "Tus archivos en OneDrive, abiertos en Excel",
               intro=f'<a class="btn-dl" href="{ZIP}" download>Descargar todos los archivos (.zip)</a> o descárgalos uno por uno:</p><div class="files">{files}</div><p>',
               expect=("<ol><li>Descomprime el .zip y sube la carpeta a tu <b>OneDrive</b> (por ejemplo, <i>Copilot Finanzas</i>).</li>"
                       "<li>Abre <b>Zava_Flujo_Caja_Diario_Oct2026.xlsx</b> desde OneDrive en Excel para la web o en Excel de escritorio; verifica que <b>Autoguardado</b> esté activo.</li>"
                       "<li>Abre Copilot con el <b>icono de Copilot</b> en la esquina inferior derecha de Excel (o <b>Alt + C</b>). El panel de Copilot se abre a la derecha.</li></ol>"),
               callouts=[("tip", "¿Por qué en OneDrive?", "Copilot trabaja mejor con archivos guardados en la nube: puedes referenciarlos con <b>/</b> desde Copilot Chat, Word y PowerPoint, y el historial de versiones te protege.")],
               fail="Si no puedes subir a OneDrive, trabaja el archivo local en Excel de escritorio. Para los ejercicios 5.1 y 5.2 adjunta los archivos con <b>+</b> y la opción para cargar archivos.",
               checks=["Subí la carpeta a OneDrive y abrí Copilot en Excel."])
    labs += lab("lab-0-2", "0.2", "Tres modos, cuatro partes del prompt y las reglas Zava", "Requerido", "2 min", "Pedir bien desde el primer prompt", "Excel",
                "Lo que viste en Arte del prompting", "La tarjeta de reglas pegada en tu chat",
                intro=f"Repaso de 30 segundos de la sesión de las 11:00, aplicado a Finanzas:</p>{anat}<h3>Los modos de Copilot en Excel</h3>{modes}<p>Cambia de modo con el botón que está junto al cuadro de chat (o <b>Ctrl + Mayús + M</b>). Copilot en Excel trabaja sobre el libro abierto. Pega esta tarjeta al empezar cada chat para que todas las respuestas usen las mismas definiciones:",
                prompts=[("Tarjeta de reglas Zava", "Reglas", TARJETA)],
                callouts=[("note", "Conoce tus archivos", know)],
                checks=["Pegué la tarjeta de reglas al inicio del chat."])
    return chapter("ch0", "Arranque", "0. Arranque", ["5 minutos", "Excel", "Copilot propone, tú verificas"],
                   "Antes del primer número: los archivos en OneDrive, Copilot abierto y unas reglas que hacen que cada respuesta use las mismas definiciones de la empresa.",
                   labs, f'<div class="chapter-inner"><h3>Checkpoints para alcanzar al grupo</h3>{cks}</div>')


def ch1():
    b = "".join(f"<li>{E(l)}</li>" for l in briefing_lines())
    labs = lab("lab-1-1", "1.1", "Posición de caja, alertas y KPIs", "Requerido", "8 min", "Saber dónde está el dinero y qué se viene", "Excel",
               "Zava_Flujo_Caja_Diario_Oct2026.xlsx", "Cifras de caja y alertas para el briefing",
               intro="Abre el flujo de caja, pega la tarjeta de reglas y usa el <b>modo de solo chat</b>.",
               prompts=[("Posición de caja y alertas", "Solo chat", "1.1a"), ("KPIs de cobranza", "Solo chat", "1.1b")],
               expect=(t_caja() + f"<ul><li><b>Alerta de liquidez:</b> Banco Coral baja a {pesos(K['coral_12nov'])} el 12 de noviembre (mínimo {pesos(Z.MINIMO['Banco Coral'])}) por el pago de azúcar de {pesos(K['pago_azucar_12nov'])}, y a {pesos(K['coral_13nov'])} el 13. Traspaso adicional necesario: al menos {pesos(K['coral_traspaso_necesario'])}.</li>"
                       f"<li><b>Movimiento atípico:</b> Banco Ceiba, 22 de octubre, Pagos_proveedores {pesos(K['atipico_22oct_pagos'])}: exactamente el doble del pago de PET de {pesos(K['duplicado'])}, que aparece cargado dos veces (y aproximadamente el doble del pago de PET del 8 de octubre, {pesos(K['pago_pet_08oct'])}).</li>"
                       f"<li><b>KPIs:</b> cobranza de octubre al {T['cobr']} de la meta; el DSO del canal Moderno pasó de {T['dso_jul']} a {T['dso']} días.</li></ul>"),
               callouts=[("warning", "Verifica una cifra", "Filtra Movimientos por Banco Coral y 30/10: el Saldo_final debe coincidir con lo que dijo Copilot. Una verificación de 20 segundos te evita un error frente al CFO.")],
               fail="Si Copilot no encuentra la alerta, pregúntale directo: «¿Qué saldo final tiene Banco Coral el 12 y el 13 de noviembre en Proyeccion_Nov?». Si sigue sin salir, usa las cifras de esta tabla para el 1.2.",
               checks=["Pedí la posición de caja y comprobé una cifra a mano.", "Le pedí a Copilot que buscara movimientos atípicos."])
    labs += lab("lab-1-2", "1.2", "Del Excel y los correos a un briefing de 5 líneas y el correo al CFO", "Requerido", "7 min", "Un briefing que el CFO lee en 30 segundos",
                "Copilot Chat (aplicación Microsoft Copilot) · Outlook", "Las cifras del 1.1 y Zava_Correos_y_Minuta_Oct2026.docx", "El briefing y el borrador del correo (no se envía)",
                intro="En la aplicación Microsoft Copilot, escribe <b>/</b> y elige el documento de correos (o adjúntalo con <b>+</b> y la opción para cargar o adjuntar archivos). Pega en el prompt la respuesta del 1.1. Si Copilot muestra el correo con un botón para enviarlo, <b>no lo envíes</b>.",
                prompts=[("Briefing y correo al CFO", "Copilot Chat", "1.2")],
                expect=f"<ol>{b}</ol><p>El correo menciona las dos alertas y termina con una pregunta, por ejemplo: «¿Autorizas el traspaso a Coral para el miércoles 11 de noviembre?». Copilot debería relacionar el cargo atípico del 22 de octubre con el correo de Tesorería sobre el pago de PET.</p>",
                callouts=[("tip", "Llévalo a Outlook (sin enviar)", "En Outlook, crea un correo nuevo y usa <b>Borrador con Copilot</b>: pega el briefing y pide «Conviértelo en un correo para el CFO, tono neutral, corto». Revisa y <b>no lo envíes</b>: hoy es práctica.")],
                fail=ck("CHECKPOINT_Ej1_Resultado_Briefing.docx", 2),
                checks=["Generé el briefing en 5 líneas con cifras que comprobé.", "Redacté el correo al CFO con Borrador con Copilot."])
    labs += lab("lab-1-3", "1.3", "En tu bandeja real: resumir un hilo largo", "Opcional", "después", "Ponerte al día con un hilo de cierre", "Outlook",
                "Un hilo real de tu bandeja", "Un resumen con pendientes y responsables",
                intro="Abre un hilo largo y usa <b>Resumen por Copilot</b> en la parte superior del correo. Después pide más detalle:",
                prompts=[("Resumen con pendientes", "Outlook", "1.3")],
                checks=["Resumí un hilo real y saqué los pendientes."])
    return chapter("ch1", "Escenario 1", "1. Briefing de caja y KPIs", ["15 minutos", "Excel", "Copilot Chat", "Outlook"],
                   "El CFO pidió para el martes un briefing corto: posición de caja por banco, alertas de las próximas dos semanas y qué decisiones debe tomar. Tienes el flujo de caja diario y un hilo de correos.", labs)


def ch2():
    labs = lab("lab-2-1", "2.1", "Banco contra auxiliar: partidas sin conciliar con fórmulas", "Requerido", "10 min", "Encontrar las partidas con fórmulas que se pueden auditar",
               "Excel", "Zava_Conciliacion_Banco_Ceiba_Oct2026.xlsx", "Hojas Cruce_Banco, Cruce_Libros y Partidas",
               intro="Abre la conciliación, pega la tarjeta de reglas y cambia a <b>modo Plan</b>: revisa los pasos que propone Copilot antes de confirmar.",
               prompts=[("Cruce con fórmulas", "Plan", "2.1a"), ("Partidas sin conciliar", "Edición", "2.1b")],
               expect=(f"<p>Diferencia de saldos al 31 de octubre: banco {pesos(K['conc_saldo_banco'])}, libros {pesos(K['conc_saldo_libros'])}; diferencia {pesos(K['conc_diferencia_inicial'])}. Cuatro partidas la explican (5 renglones si Copilot separa el IVA de la comisión):</p>" + t_partidas() +
                       f"<p>En Cruce_Banco quedan 5 renglones sin conciliar (comisión, IVA, los dos cargos repetidos y el importe distinto). En Cruce_Libros, 2 o 3: el depósito en tránsito, el importe distinto y, según cómo arme Copilot la fórmula, el pago de PET que en el banco aparece dos veces. La suma de diferencias de Partidas es igual a la diferencia de saldos.</p>"),
               callouts=[("tip", "Truco de contador", f"Una diferencia divisible entre 9 suele ser una transposición: {pesos(K['error_dif'])} / 9 = {pesos(K['error_dif'] / 9)}. Es el {pesos(K['error_banco'])} capturado como {pesos(K['error_libros'])}."),
                         ("note", "Conexión con el ejercicio 1", "El cargo duplicado es el movimiento atípico del 22 de octubre que encontraste en el flujo de caja.")],
               fail=ck("CHECKPOINT_Ej2_Resultado_Conciliacion.xlsx", "2.2") + " Si Copilot pegó valores en lugar de fórmulas, pídele: «Reemplaza los valores por fórmulas que hagan referencia a Estado_Cuenta y Auxiliar_Bancos».",
               checks=["Crucé banco contra libros con fórmulas, no con texto.", "Encontré las 4 partidas y la suma cuadró con la diferencia de saldos."])
    labs += lab("lab-2-2", "2.2", "Comprobación independiente: la conciliación debe dar 0.00", "Requerido", "6 min", "Que otra ruta llegue al mismo resultado",
                "Excel (chat nuevo)", "Estado_Cuenta, Auxiliar_Bancos y la hoja Conciliacion", "La conciliación terminada",
                intro="Inicia un <b>chat nuevo</b> en el panel de Copilot para que no arrastre lo anterior, y usa el <b>modo de edición</b>.",
                prompts=[("Revisor independiente", "Edición", "2.2")],
                expect=table(["Concepto", "Importe"], [["Saldo según estado de cuenta", pesos(K["conc_saldo_banco"])], ["(+) Depósito en tránsito", pesos(K["dep_transito"])],
                             ["(+) Cargo duplicado por aclarar", pesos(K["duplicado"])], ["<b>Saldo ajustado según banco</b>", f"<b>{pesos(K['conc_ajustado_banco'])}</b>"],
                             ["Saldo según libros", pesos(K["conc_saldo_libros"])], ["(+) Corrección del error de captura", pesos(K["error_dif"])],
                             ["(−) Comisión e IVA no registrados", pesos(-K["comision_total"])], ["<b>Saldo ajustado según libros</b>", f"<b>{pesos(K['conc_ajustado_libros'])}</b>"],
                             ["<b>Diferencia</b>", "<b>0.00</b>"]]),
                callouts=[("important", "Por qué una segunda ruta", "Si le pides al mismo chat que revise su propio trabajo, tiende a confirmarlo. Una ruta distinta (otras hojas, otro chat) que llega a 0.00 es una prueba real.")],
                fail=ck("CHECKPOINT_Ej2_Resultado_Conciliacion.xlsx", 3),
                checks=["Hice la comprobación en un chat nuevo y me dio 0.00."])
    labs += lab("lab-2-3", "2.3", "Reporte de conciliación para Contraloría", "Opcional", "3 min", "El reporte que acompaña la conciliación", "Excel",
                "Hojas Conciliacion y Partidas", "Un reporte de 6 líneas", prompts=[("Reporte de conciliación", "Solo chat", "2.3")],
                callouts=[("tip", "Con el CSV del banco", "¿Tu banco te da un CSV? Abre <b>Zava_Estado_Cuenta_Banco_Ceiba_Oct2026.csv</b> en Excel, conviértelo en tabla (<b>Inicio</b> &gt; <b>Dar formato como tabla</b>) y repite el 2.1 contra tu auxiliar.")],
                checks=["Generé el reporte de conciliación."])
    return chapter("ch2", "Escenario 2", "2. Conciliaciones y reportes", ["20 minutos", "Excel", "Modo Plan y modo de edición"],
                   f"Contraloría reporta una diferencia de {pesos(K['conc_diferencia_inicial'])} entre el estado de cuenta de Banco Ceiba y el auxiliar. Antes de cerrar hay que explicarla con fórmulas que el auditor pueda seguir, y comprobarla por una segunda ruta.", labs)


def ch3():
    labs = lab("lab-3-1", "3.1", "Variaciones real contra presupuesto y año anterior", "Requerido", "8 min", "Saber qué CEDIS movió el resultado", "Excel",
               "Zava_Cierre_Oct2026.xlsx", "Hoja Variaciones",
               intro="Abre el cierre, pega la tarjeta de reglas y usa el <b>modo de edición</b>.",
               prompts=[("Variaciones por CEDIS", "Edición", "3.1")],
               expect=t_var() + f"<p>Golfo explica la caída de volumen (tormenta tropical, según la minuta) y además gastó {T['golfo_dist']} más en distribución. Ventas totales {T['ventas_r']}, {T['ventas_varpct_p']} contra presupuesto.</p>",
               fail=f"Si una cifra no coincide, pide: «Muéstrame la fórmula de la celda» y revisa el rango. " + ck("CHECKPOINT_Ej3_Resultado_Cierre.xlsx", "3.3"),
               checks=["Construí la hoja Variaciones con SUMIFS y revisé una fórmula."])
    labs += lab("lab-3-2", "3.2", "Puente precio–volumen–mezcla y costos", "Ver y comparar", "8 min", "Explicar la variación, no solo reportarla", "Excel",
                "Hoja Variaciones y Datos_ER", "Hoja Puente_Ppto",
                intro="Lo construimos en pantalla en <b>modo Plan</b>. Compara con la tabla y con el checkpoint del ejercicio 3. Si vas adelante, hazlo tú.",
                prompts=[("Puente de ventas, costos y EBITDA", "Plan", "3.2")],
                expect=t_puente() + t_costos() + f"<p>El precio sumó; el volumen y la mezcla restaron (creció Moderno, el canal de menor precio, y bajó Consumo en sitio, el de mayor precio). El azúcar subió {T['az_cu']} por caja y explica casi todo el aumento del costo. Margen bruto {T['mb_r']} contra {T['mb_p']} presupuestado ({T['mb_pts']}). EBITDA preliminar {T['ebitda_pre']} contra {T['ebitda_p']}.</p>",
                fail=ck("CHECKPOINT_Ej3_Resultado_Cierre.xlsx", "3.3"),
                checks=["Entendí el puente volumen–mezcla–precio y comprobé que suma la variación total."])
    labs += lab("lab-3-3", "3.3", "Hechos del cierre: cada cifra con su fuente", "Requerido", "9 min", "Una sola fuente de verdad para el Consejo", "Excel",
                "Variaciones, Puente_Ppto y las partidas del ejercicio 2", "Hoja Hechos_del_cierre (alimenta los ejercicios 4 y 5)",
                prompts=[("Hechos del cierre", "Edición", "3.3")],
                expect=table(["Hecho", "Cifra"], [["Ventas netas reales", pesos(K["ventas_r"])], ["Variación contra presupuesto", f"{pesos(K['ventas_var_p'], sign=True)} ({T['ventas_varpct_p']})"],
                             ["Variación contra año anterior", T["ventas_varpct_a"]], ["Volumen real", f"{T['vol_r']} CU ({T['vol_varpct_p']} vs ppto; {T['vol_varpct_a']} vs AA)"],
                             ["EBITDA real preliminar", pesos(K["ebitda_r"])], ["Ajuste por comisión bancaria", T["ajuste"]], ["EBITDA real ajustado", pesos(K["ebitda_r_aj"])],
                             ["EBITDA presupuesto", pesos(K["ebitda_p"])], ["Variación % EBITDA ajustado", T["ebitda_pct"]]]),
                callouts=[("note", "La regla de oro", "Si una cifra no está en Hechos del cierre, no entra a la presentación. Así el auditor y el Consejo pueden rastrear cada número hasta su hoja.")],
                fail=ck("CHECKPOINT_Ej3_Resultado_Cierre.xlsx", 4),
                checks=["Mi hoja Hechos del cierre tiene fuente y tipo en cada renglón.", "Incluí los ajustes de la conciliación."])
    labs += lab("lab-3-4", "Reto", "Supuestos del presupuesto 2027", "Reto", "después", "Arrancar el presupuesto con los aprendizajes del cierre", "Excel · Copilot Chat",
                "Hechos del cierre", "Una lista de supuestos 2027 para discutir",
                prompts=[("Supuestos 2027", "Copilot Chat", "Con /Zava_Cierre_Oct2026 (hojas Hechos_del_cierre e Historico_Volumen) y la minuta de /Zava_Correos_y_Minuta_Oct2026, propón una lista de supuestos para el presupuesto 2027: volumen por CEDIS, precio, azúcar, tipo de cambio y distribución. Para cada uno: valor propuesto, de dónde sale, qué riesgo tiene y qué dato nos falta. Marca todo como Estimación.")],
                checks=["Propuse supuestos 2027 con su fuente y su riesgo."])
    return chapter("ch3", "Escenario 3", "3. Cierre y presupuesto", ["25 minutos", "Excel", "Variaciones, puente y hechos"],
                   "Con la conciliación cuadrada, toca explicar octubre: ¿por qué las ventas superaron el presupuesto pero el EBITDA no? Y dejar cada cifra con su fuente, porque el auditor y el Consejo la van a pedir.", labs)


def ch4():
    labs = lab("lab-4-1", "4.1", "El dato atípico y el pronóstico del trimestre", "Requerido", "10 min", "Un pronóstico que no se deja engañar por un mes raro", "Excel",
               "Tu Zava_Cierre_Oct2026.xlsx con Hechos del cierre (o el checkpoint del ejercicio 3)", "Hoja Pronostico",
               intro="Primero pregunta en <b>modo de solo chat</b>; después construye en <b>modo Plan</b>.",
               prompts=[("Busca el dato atípico", "Solo chat", "4.1a"), ("Pronóstico del 4T", "Plan", "4.1b")],
               expect=(f"<p><b>Atípico:</b> Golfo, julio 2026, {T['atip']} CU, muy por arriba de julio 2025 ({num(Z.build_all()['hist'][('Golfo', '2025-07')])}) y de junio y agosto 2026. La minuta lo confirma: venta extraordinaria a un evento, no recurrente. Se reemplaza por {num(K['atipico_reemplazo'])} CU.</p>"
                       + t_pron() + f"<p>Crecimiento total sin el atípico {T['g_adj']} (con el atípico sería {T['g_raw']}: inflaría el pronóstico). <b>4T (Estimación):</b> volumen {T['q4_vol']} CU; ventas {T['q4_ventas']}, {T['q4_vs']} contra presupuesto.</p>"),
               callouts=[("important", "Observado o Estimación", "Octubre es Observado. Noviembre, diciembre y el total del 4T son Estimación. Esa etiqueta viaja contigo hasta la presentación del Consejo.")],
               fail=ck("CHECKPOINT_Ej4_Resultado_Forecast.xlsx", "4.2") + " (también tiene la hoja Pronostico).",
               checks=["Encontré el dato atípico y lo expliqué con la minuta.", "Construí el pronóstico con fórmulas y etiquetas Observado/Estimación."])
    labs += lab("lab-4-2", "4.2", "Escenarios: azúcar +10 % y tipo de cambio", "Requerido", "7 min", "Cuantificar los dos riesgos que preocupan al CFO", "Excel",
                "Hojas Pronostico y Supuestos_Forecast", "Hoja Escenarios y renglones Estimación en Hechos del cierre",
                prompts=[("Escenarios", "Edición", "4.2")],
                expect=t_esc() + f"<p>Utilidad bruta base de noviembre y diciembre (Estimación): {mdp(K['fc_nd_ub'])}. El aviso del ingenio (correo de Compras) justifica el escenario de azúcar.</p>",
                fail=ck("CHECKPOINT_Ej4_Resultado_Forecast.xlsx", 5),
                checks=["Calculé los escenarios con referencias a celdas.", "Agregué las estimaciones a Hechos del cierre."])
    labs += lab("lab-4-3", "4.3", "Otra ruta: pronóstico con Analista", "Opcional", "después", "Comparar tu método contra uno con estacionalidad",
                "Agente Analista", "Zava_Cierre_Oct2026.xlsx adjunto", "Un segundo pronóstico para comparar",
                intro="En la aplicación Microsoft Copilot, en <b>Agentes</b>, selecciona <b>Analista</b> y adjunta el archivo con <b>+</b>.",
                prompts=[("Pronóstico con Analista", "Analista", "4.3")],
                expect="Las cifras serán distintas a las tuyas porque el método es otro. Lo valioso es la comparación: si ambos métodos cuentan la misma historia, tienes más confianza; si no, ya sabes qué discutir.",
                checks=["Comparé mi pronóstico con el de Analista."])
    return chapter("ch4", "Escenario 4", "4. Análisis y forecasting", ["20 minutos", "Excel", "Analista (opcional)"],
                   "El CFO quiere el pronóstico del cuarto trimestre y la sensibilidad a dos riesgos: el posible aumento del azúcar y el tipo de cambio. En la serie hay un mes que no se parece a los demás.", labs)


def ch5():
    labs = lab("lab-5-1", "5.1", "Del Excel al resumen para el Consejo", "Requerido", "6 min", "Un texto donde cada cifra se puede rastrear",
               "Copilot Chat · Word", "Hechos del cierre y la minuta", "Zava_Resumen_Consejo.docx (fuente de la presentación)",
               intro="En la aplicación Microsoft Copilot, escribe <b>/</b> y elige tu libro de cierre y el documento de correos. Si tu libro no está en OneDrive, usa el checkpoint del ejercicio 4.",
               prompts=[("Resumen para el Consejo", "Copilot Chat", "5.1")],
               expect=f"<p>Seis secciones con viñetas como: «Ventas netas {T['ventas_r']}, {T['ventas_varpct_p']} contra presupuesto (hecho 1, 3)» y «Escenario combinado {T['esc_comb']} (Estimación)». Copia el resultado en un documento de Word nuevo y guárdalo en OneDrive como <b>Zava_Resumen_Consejo</b>.</p>",
               fail=f"Usa {dl(FC + 'CHECKPOINT_Ej5_Resultado_Resumen_Consejo.docx')} como fuente para el 5.2.",
               checks=["Generé el resumen y cada viñeta cita su hecho."])
    labs += lab("lab-5-2", "5.2", "La presentación del Consejo con la plantilla y notas del orador", "Requerido", "7 min", "Del documento a 7 diapositivas con la imagen de la empresa",
                "PowerPoint", "Zava_Plantilla_Consejo.pptx y Zava_Resumen_Consejo.docx", "Zava_Consejo_Oct2026.pptx",
                intro="Abre <b>Zava_Plantilla_Consejo.pptx</b> desde OneDrive, guárdala como <b>Zava_Consejo_Oct2026</b>, abre Copilot y referencia el documento con <b>/</b>.",
                prompts=[("Presentación desde el resumen", "PowerPoint", "5.2")],
                expect=f"<p>Siete diapositivas con la plantilla verde de Zava. Revisa tres cifras contra Hechos del cierre: ventas {T['ventas_r']}, EBITDA ajustado {T['ebitda_aj']} ({T['ebitda_pct']}) y escenario combinado {T['esc_comb']}. La lámina del pronóstico debe decir Estimación.</p>",
                callouts=[("tip", "Si no aparecen las notas", "Abre el panel de <b>Notas</b> (barra inferior) y pega cada «Nota para el orador» del resumen. O pide a Copilot, diapositiva por diapositiva: «Escribe las notas del orador de esta diapositiva con base en /Zava_Resumen_Consejo»."),
                          ("note", "¿Brand kit?", "Si tu empresa publica un kit de marca (lo viste a las 10:00), puedes elegirlo en lugar de la plantilla.")],
                fail=f"Abre {dl(FC + 'CHECKPOINT_Ej5_Resultado_Consejo.pptx')} y continúa con el 5.3.",
                checks=["Creé la presentación con la plantilla y revisé tres cifras."])
    labs += lab("lab-5-3", "5.3", "Preguntas probables del Consejo y del auditor, y la lista de soporte", "Requerido", "6 min", "Llegar preparado a la sesión y a la auditoría",
                "Copilot Chat · PowerPoint", "Tu presentación y la solicitud del auditor", "Tabla de preguntas, respuestas y soporte",
                prompts=[("Preguntas y soporte", "Copilot Chat", "5.3")],
                expect=("<ul><li><b>Consejo:</b> ¿por qué cayó Golfo y cuándo se recupera?; ¿qué haremos con el azúcar en diciembre y 2027?; ¿por qué sube el DSO de Moderno?; ¿qué tan confiable es el pronóstico?</li>"
                        "<li><b>Auditor:</b> conciliación de Banco Ceiba con sus partidas; soporte de la reclamación del cargo duplicado; análisis de variaciones mayores a 5 % (Golfo en volumen y distribución); soporte de los supuestos del pronóstico y del aviso de precio del azúcar.</li>"
                        "<li><b>Lo que no podemos responder hoy:</b> si el banco ya reembolsó el cargo duplicado, y el efecto de la tormenta por canal.</li></ul>"),
                callouts=[("tip", "Desde PowerPoint", "En el panel de Copilot de PowerPoint, en <b>Habilidades</b>, prueba <b>Prepararse para preguntas</b> sobre tu presentación.")],
                checks=["Preparé las preguntas probables y la lista de soporte."])
    labs += lab("lab-5-4", "5.4", "Revisión final con veredictos", "Requerido", "6 min", "Que nada falso llegue al Consejo", "Copilot Chat (chat nuevo)",
                "El borrador comercial (en el documento de correos) y tu libro de cierre", "La lista de correcciones antes de enviar",
                intro="Abre un <b>chat nuevo</b>: el revisor no debe haber participado en el análisis.",
                prompts=[("Revisor independiente", "Copilot Chat", "5.4")],
                expect=t_claims() + "<p>Resultado esperado: 3 Verificado, 2 Incorrecto, 2 No verificable y 1 Exagerado. La afirmación 5 a veces sale como Incorrecto: discútelo con tu vecino. Los archivos no la contradicen (la reclamación sigue abierta), simplemente no hay evidencia; por eso es No verificable. Si Copilot marca «Verificado» algo que no lo está, pídele la celda exacta de donde sale.</p>",
                callouts=[("important", "Los cuatro veredictos", "<b>Verificado</b>: la cifra y la afirmación coinciden con los datos. <b>Incorrecto</b>: la cifra o el hecho no coinciden. <b>No verificable</b>: los archivos no permiten comprobarlo. <b>Exagerado</b>: tiene base, pero lo sobredimensiona.")],
                checks=["Revisé el borrador con los cuatro veredictos.", "Corregí lo Incorrecto y lo Exagerado antes de enviarlo."])
    return chapter("ch5", "Escenario 5", "5. Preparación de Consejo y auditoría", ["25 minutos", "Copilot Chat", "Word", "PowerPoint"],
                   "Con los hechos del cierre y el pronóstico listos, se arma el paquete para el Consejo del 26 de noviembre. La Dirección Comercial mandó su propio borrador de mensajes: antes de enviar nada, todo se revisa contra los datos.", labs)


def ch6():
    labs = lab("lab-6-1", "6.1", "Guarda y programa el prompt del briefing", "Demo", "3 min", "Que el briefing de cada martes empiece solo", "Copilot Chat",
               "El prompt del briefing", "Una indicación guardada y programada",
               intro="Lo viste a las 10:00; aquí lo aplicamos al briefing. En Copilot Chat, pasa el cursor sobre tu prompt y selecciona <b>Guardar mensaje</b> (queda en <b>Sus mensajes</b> de la Galería de consultas de Copilot). Para programarlo: pasa el cursor sobre el prompt &gt; <b>Programar esta indicación</b> &gt; elige cuándo y cuántas veces &gt; <b>Guardar</b>.",
               prompts=[("Briefing semanal para programar", "Copilot Chat", "6.1")],
               expect="El resultado aparece en <b>Chats</b> cada vez que se ejecuta. Puedes tener hasta 10 indicaciones programadas y administrarlas en <b>Configuración y más</b> (…) &gt; <b>Indicaciones programadas</b> (Ejecutar ahora, Editar programación, Desactivar o Eliminar). Lee el archivo en su ubicación: guarda cada semana la versión nueva con el mismo nombre en la misma carpeta y revisa el resultado antes de reenviarlo.",
               checks=["Guardé mi prompt del briefing.", "Programé una indicación semanal."])
    labs += lab("lab-6-2", "6.2", "Una aptitud de Excel para conciliar cada mes", "Opcional", "después", "Convertir el ejercicio 2 en una receta reutilizable", "Excel",
                "El texto de abajo", "La aptitud conciliacion-bancaria",
                intro="Si tu Excel ya tiene aptitudes personalizadas: en el panel de Copilot, <b>Administrar complementos &amp; aptitudes</b> &gt; <b>Crear carpeta de OneDrive</b> &gt; <b>Abrir carpeta de habilidades</b>. Crea una carpeta <i>conciliacion-bancaria</i> con un archivo <i>SKILL.md</i> que contenga este texto. Úsala desde <b>Agregar</b> &gt; <b>Elegir complementos y aptitudes</b>.",
                prompts=[("SKILL.md · conciliacion-bancaria", "Aptitud", "6.2")],
                callouts=[("tip", "Si aún no tienes aptitudes", "Guarda el texto en un documento y pégalo al inicio del chat cada mes. Funciona igual.")],
                checks=["Guardé la receta de conciliación (aptitud o documento)."])
    labs += lab("lab-6-3", "6.3", "Trae tu caso", "Reto", "5 min", "Salir con un caso real resuelto o encaminado", "La app que uses en tu caso",
                "Un archivo, correo o reporte tuyo", "Tu primer resultado y el siguiente paso",
                intro="Elige un caso de la tabla de abajo o uno propio. Usa esta plantilla con tus datos (en el OneDrive de la empresa):",
                prompts=[("Plantilla para tu caso", "Copilot Chat", "6.3")],
                callouts=[("note", "¿Análisis más profundo?", "Para datos grandes o análisis que requieren código, prueba <b>Analista</b> (en <b>Agentes</b>). Para investigar un tema con fuentes (por ejemplo, perspectivas del precio del azúcar), <b>Investigador</b>."),
                          ("note", "¿Y los agentes?", "Si quieres ver cómo se vería un agente de conciliaciones para tu equipo, pregúntanos al final: lo mostramos en vivo.")],
                checks=["Probé la plantilla con un caso real.", "Elegí un caso para la próxima semana."])
    casos = table(["#", "Caso de Finanzas", "Ejercicio", "App"], [[i, c, " · ".join(f'<a href="#lab-{x.strip().replace(".", "-")}">{x.strip()}</a>' for x in e.split("·")), a] for i, (c, e, a) in enumerate(CASOS, 1)])
    plan = ('<div class="cwr"><div class="cwr-step crawl"><div class="cwr-name">Esta semana</div><p>Usa la tarjeta de reglas y el briefing con tus archivos reales. Comprueba una cifra en cada respuesta.</p></div>'
            '<div class="cwr-step walk"><div class="cwr-name">Este mes</div><p>Cierre con conciliación por fórmulas, Hechos del cierre y revisión con veredictos antes de cada envío.</p></div>'
            '<div class="cwr-step run"><div class="cwr-name">Este trimestre</div><p>Prompts programados, aptitudes de Excel y, si el equipo lo pide, un agente de Finanzas.</p></div></div>')
    return chapter("ch6", "Cierre", "6. Automatiza y trae tu caso", ["10 minutos", "Copilot Chat", "Excel", "Tus archivos"],
                   "Hiciste el ciclo completo una vez. El siguiente martes no deberías empezar de cero: guarda lo que funcionó y pruébalo con un caso tuyo.", labs,
                   f'<div class="chapter-inner" id="casos"><h3>Los 10 casos de Finanzas de hoy</h3>{casos}<h3>Tu plan</h3>{plan}</div>')


def reference():
    faq = [("Copilot pegó valores en lugar de fórmulas", "Pide: «Reemplaza los valores por fórmulas que hagan referencia a las hojas de origen». Revisa una celda con F2."),
           ("Copilot dice que no encuentra una hoja o columna", "Escribe el nombre exacto de la hoja y la columna, como aparecen en el archivo. Revisa que el archivo esté guardado en OneDrive."),
           ("La cifra de Copilot no coincide con «Lo que verás»", "Pide la fórmula o la celda de donde sale. Casi siempre es un filtro (Escenario o CEDIS) o un subtotal sumado dos veces."),
           ("No veo el botón o la opción", "Las funciones llegan por etapas y la configuración de TI puede variar. Usa el checkpoint y sigue; anótalo para preguntarlo al final."),
           ("Copilot se tarda o se detiene", "Usa <b>Detener</b>, divide el prompt en dos y vuelve a intentar. En el modo Plan, confirma paso por paso."),
           ("¿Puedo usar esto con datos reales?", "Sí, en archivos del OneDrive o SharePoint de la empresa y respetando las etiquetas de confidencialidad. Copilot solo ve lo que tú ya puedes ver.")]
    f = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    gl = [("CU", "Caja unidad, la unidad de volumen."), ("CEDIS", "Centro de distribución."), ("Efecto mezcla", "Cambio en ventas por vender más de canales con distinto precio."),
          ("Depósito en tránsito", "Registrado en libros, aún no abonado por el banco."), ("Observado", "Cifra que sale de los datos."), ("Estimación", "Pronóstico o escenario.")]
    g = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in gl)
    refs = [("Introducción a Copilot en Excel", "https://support.microsoft.com/es-es/excel/copilot/get-started-with-copilot-in-excel"),
            ("Aptitudes de Copilot en Excel", "https://support.microsoft.com/es-es/excel/copilot/copilot-in-excel-skills"),
            ("Editar con Copilot en PowerPoint", "https://support.microsoft.com/es-es/powerpoint/edit-with-copilot-in-powerpoint"),
            ("Borrador de un correo con Copilot en Outlook", "https://support.microsoft.com/es-es/outlook/copilot-pages/draft-an-email-message-with-copilot-in-outlook"),
            ("Guardar sus indicaciones favoritas", "https://support.microsoft.com/es-es/microsoft-365-copilot/save-your-favorite-prompts-to-use-again"),
            ("Programar sus indicaciones más usadas", "https://support.microsoft.com/es-es/microsoft-365-copilot/schedule-your-most-used-copilot-prompts"),
            ("Introducción a Analista", "https://support.microsoft.com/es-es/microsoft-365-copilot/get-started-with-analyst-in-microsoft-365-copilot")]
    r = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in refs)
    return f"""<section class="card" id="ayuda"><h2>Si algo falla</h2><div class="faq">{f}</div></section>
<section class="card" id="glosario"><h2>Glosario</h2><div class="glossary">{g}</div></section>
<section class="card" id="refs"><h2>Referencias</h2><ul>{r}</ul><p class="small muted">Los nombres de botones y menús pueden variar según la versión y el idioma de tu Microsoft 365.</p></section>"""


def nav():
    groups = [("#bienvenida", "Bienvenida", [])]
    for id_, t, labs_ in [("ch0", "0. Arranque", [("lab-0-1", "0.1 Archivos y Copilot"), ("lab-0-2", "0.2 Modos y reglas")]),
                          ("ch1", "1. Briefing de caja", [("lab-1-1", "1.1 Caja y alertas"), ("lab-1-2", "1.2 Briefing y correo"), ("lab-1-3", "1.3 Tu bandeja")]),
                          ("ch2", "2. Conciliaciones", [("lab-2-1", "2.1 Partidas con fórmulas"), ("lab-2-2", "2.2 Comprobación"), ("lab-2-3", "2.3 Reporte")]),
                          ("ch3", "3. Cierre y presupuesto", [("lab-3-1", "3.1 Variaciones"), ("lab-3-2", "3.2 Puente"), ("lab-3-3", "3.3 Hechos del cierre"), ("lab-3-4", "Reto: supuestos 2027")]),
                          ("ch4", "4. Forecasting", [("lab-4-1", "4.1 Atípico y pronóstico"), ("lab-4-2", "4.2 Escenarios"), ("lab-4-3", "4.3 Analista")]),
                          ("ch5", "5. Consejo y auditoría", [("lab-5-1", "5.1 Resumen"), ("lab-5-2", "5.2 Presentación"), ("lab-5-3", "5.3 Preguntas"), ("lab-5-4", "5.4 Veredictos")]),
                          ("ch6", "6. Automatiza", [("lab-6-1", "6.1 Guardar y programar"), ("lab-6-2", "6.2 Aptitud de Excel"), ("lab-6-3", "6.3 Trae tu caso"), ("casos", "Los 10 casos")])]:
        groups.append((f"#{id_}", t, labs_))
    out = ""
    for href, t, labs_ in groups:
        if not labs_:
            out += f'<a class="nav-top" href="{href}">{t}</a>'; continue
        out += f'<div class="nav-group"><a class="nav-mod" href="{href}">{t}</a>' + "".join(f'<a class="nav-lab" href="#{a}">{b}</a>' for a, b in labs_) + "</div>"
    out += '<div class="nav-group"><a class="nav-mod" href="#ayuda">Si algo falla</a><a class="nav-mod" href="#glosario">Glosario</a><a class="nav-mod" href="#refs">Referencias</a></div>'
    return out


def build():
    body = welcome() + ch0() + ch1() + ch2() + ch3() + ch4() + ch5() + ch6() + reference()
    page = f"""<!DOCTYPE html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>Copilot para Finanzas: del cierre al Consejo</title>
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#bienvenida">Ir al contenido</a>
<header class="hero">
<div class="eyebrow">Bootcamp de Finanzas &middot; TDx Bepensa &middot; Lunes 9 de noviembre de 2026</div>
<h1>Copilot para Finanzas: del cierre al Consejo</h1>
<p>Experiencia interactiva del área: cinco escenarios de Finanzas en una sola historia, del briefing de caja a la presentación del Consejo, con archivos de práctica, prompts listos para copiar y checkpoints para no quedarte atrás.</p>
<div class="tags"><span>120 minutos</span><span>Práctica guiada en tu laptop</span><span>Excel &middot; Copilot Chat &middot; Word &middot; PowerPoint &middot; Outlook</span><span>Datos ficticios</span><span>10 casos de Finanzas</span></div>
</header>
<div class="shell">
<div>
<button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="sideNav">Menú: ejercicios</button>
<nav class="side" id="sideNav" aria-label="Navegación">
<div class="nav-title">Tu avance</div>
<div class="progress"><div class="bar"><i id="progBar"></i></div><small id="progTxt"></small></div>
<div class="controls"><button type="button" id="expandAll">Abrir todo</button><button type="button" id="collapseAll">Cerrar todo</button></div>
{nav()}
<div class="controls" style="margin-top:12px"><button type="button" id="resetProg">Reiniciar casillas</button></div>
</nav>
</div>
<main id="main">
{body}
<footer>Copilot para Finanzas: del cierre al Consejo &middot; v1 &middot; Empresa y datos ficticios con fines de capacitación.</footer>
</main>
</div>
<script>{JS}</script>
</body>
</html>"""
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f: f.write(page)
    return page


if __name__ == "__main__":
    print(len(build()))
