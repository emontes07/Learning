# -*- coding: utf-8 -*-
"""Contenido de la guía del asistente (index.html). Todas las cifras vienen de answers.compute()."""
import html
import zava_data as Z, answers as A
from answers import mdp, pesos, num, pct, pts
from gen_docs import T, CLAIMS, briefing_lines

K = A.compute()
E = html.escape
FB = "files/1_Archivos_de_practica/"
FC = "files/2_Checkpoints/"
ZIP = "files/Zava_Bebidas_Finanzas_Archivos.zip"

TARJETA = """REGLAS ZAVA (pégalas antes de tu primera pregunta en cada archivo)
1. Zava Bebidas es una empresa ficticia. Importes en pesos mexicanos (MXN); volumen en cajas unidad (CU).
2. CEDIS: Norte, Centro, Golfo y Península. Canales: Tradicional, Moderno y Consumo en sitio.
3. Precio por CU = Ventas netas / Volumen. Calcúlalo sobre totales; nunca promedies precios.
4. Margen bruto = Utilidad bruta / Ventas netas. EBITDA = Utilidad bruta − Gastos de distribución − Gastos corporativos.
5. Variación = Real − Comparativo; variación % = Real / Comparativo − 1.
6. Usa fórmulas que hagan referencia a las hojas, no valores pegados, y no modifiques las hojas originales.
7. Cada cifra que me des debe decir de qué hoja y columna sale. Si un dato no está en el archivo, di "no está en los datos"; no lo estimes.
8. Etiqueta como Observado lo que sale de los datos y como Estimación lo que pronostiques o supongas.
9. Formato de México: punto decimal y coma de miles; importes grandes en millones con un decimal; porcentajes con un decimal."""

P = {}
P["1.1a"] = """Usa la hoja Movimientos. Dame la posición de caja al 30 de octubre de 2026: el saldo final de cada banco y el total, y compáralos contra el saldo mínimo de la hoja Parametros.
Después revisa la hoja Proyeccion_Nov y dime qué banco queda por debajo de su saldo mínimo, en qué fecha y por cuánto, y qué traspaso adicional se necesitaría para que no baje del mínimo en todo el periodo.
Por último, busca en Movimientos un pago que se salga del patrón de su banco (por ejemplo, el doble de lo habitual) y que no se explique por un pago periódico como la quincena de azúcar, la nómina o los impuestos. Dime banco, fecha, columna e importe.
Muestra cada cifra con la hoja de donde sale."""
P["1.1b"] = """Con la hoja KPIs, dime cómo va la cobranza de octubre contra la meta (en %) y qué indicador empeoró más de julio a octubre. Da una explicación de una línea y aclara qué no se puede saber con estos datos."""
P["1.2"] = """Eres analista de Tesorería de Zava Bebidas. Usa el documento /Zava_Correos_y_Minuta_Oct2026 y estas cifras de caja:
[pega aquí la respuesta del ejercicio 1.1]

1. Escribe un briefing de caja para el CFO en exactamente 5 líneas: (1) posición de caja; (2) y (3) las dos alertas principales, con fecha e importe; (4) un KPI de cobranza; (5) las decisiones que el CFO debe tomar.
2. Después redacta un correo al CFO de máximo 120 palabras, con asunto, que termine con una pregunta concreta.
Importes grandes en millones de pesos con un decimal. No inventes cifras: usa solo las que te di o las del documento. Si el documento explica una alerta, dilo."""
P["1.3"] = """Resume este hilo en 3 viñetas: qué se decidió, qué está pendiente y quién debe hacer qué (por puesto). Después propón una respuesta breve."""
P["2.1a"] = """Concilia la cuenta de Banco Ceiba de octubre.
1. Crea una hoja Cruce_Banco con un renglón por cada movimiento de Estado_Cuenta y columnas con fórmulas (no valores pegados) que cuenten: cuántas veces aparece su Referencia en Estado_Cuenta, cuántas en Auxiliar_Bancos, y cuántas en Auxiliar_Bancos con el mismo Cargo y Abono.
2. Agrega una columna Estatus con fórmula que diga "Sin contrapartida", "Importe distinto", "Repetido" o "Conciliado".
3. Haz lo mismo en una hoja Cruce_Libros para Auxiliar_Bancos contra Estado_Cuenta.
No modifiques las hojas originales. Al terminar, dime cuántos renglones no están conciliados en cada hoja."""
P["2.1b"] = """Con Cruce_Banco y Cruce_Libros, crea la hoja Partidas con un renglón por partida sin conciliar: tipo (depósito en tránsito, comisión no registrada, cargo duplicado o error de captura), referencia, fecha, importe en banco, importe en libros y diferencia, todo con fórmulas SUMIFS sobre Estado_Cuenta y Auxiliar_Bancos. Indica qué lado se ajusta (banco o libros) y la acción.
Abajo suma las diferencias y compárala, con fórmula, contra la diferencia entre el saldo final de Estado_Cuenta y el de Auxiliar_Bancos."""
P["2.2"] = """Actúa como revisor independiente: no uses las hojas Cruce_Banco, Cruce_Libros ni Partidas.
Usando solo Estado_Cuenta y Auxiliar_Bancos, completa la hoja Conciliacion con fórmulas:
saldo según banco + depósitos en tránsito + cargos del banco por aclarar = saldo ajustado según banco;
saldo según libros + correcciones − cargos del banco no registrados = saldo ajustado según libros;
y una celda Diferencia que debe dar 0.00. Si no da 0.00, dime qué falta y no la fuerces."""
P["2.3"] = """Escribe un reporte de conciliación de Banco Ceiba para Contraloría en 6 líneas: saldos según banco y libros, cada partida con su importe y acción, el saldo ajustado y quién debe hacer qué. Usa solo la hoja Conciliacion y la hoja Partidas."""
P["3.1"] = """Crea una hoja Variaciones con una fila por CEDIS y una fila Total.
Columnas: volumen real, presupuesto y año anterior; ventas netas real, presupuesto y año anterior; variación en pesos y en % contra presupuesto y contra año anterior; utilidad bruta real y presupuesto; margen bruto real y presupuesto; gastos de distribución real y presupuesto y su variación.
Usa fórmulas SUMIFS sobre Datos_ER y Gastos_Distribucion, no valores pegados.
Después dime en 3 viñetas qué CEDIS explica la mayor parte de la variación contra presupuesto y por qué."""
P["3.2"] = """Crea una hoja Puente_Ppto con fórmulas que expliquen la diferencia entre presupuesto y real.
1. Ventas netas: arma una tabla por CEDIS y canal con volumen y ventas real y presupuesto, y calcula tres efectos:
   volumen = (volumen real total − volumen presupuesto total) × precio promedio presupuesto;
   mezcla = suma de (volumen real × precio presupuesto de cada CEDIS y canal) − volumen real total × precio promedio presupuesto;
   precio = ventas reales − suma de (volumen real × precio presupuesto de cada CEDIS y canal).
   Comprueba con fórmula que volumen + mezcla + precio = ventas reales − ventas presupuesto.
2. Costo de ventas por insumo (azúcar, PET, concentrado y otros): efecto volumen, efecto costo unitario y variación % del costo por CU.
3. EBITDA de presupuesto a real preliminar con Gastos_Distribucion y Gastos_Corporativos."""
P["3.3"] = """Crea la hoja Hechos_del_cierre con columnas: #, Hecho, Cifra, Unidad, Fuente (hoja y celda o cálculo), Tipo (Observado o Estimación) y Revisado por (vacía).
Incluye, con fórmulas que apunten a Variaciones y Puente_Ppto: ventas netas reales y su variación en $ y % contra presupuesto y en % contra año anterior; volumen real y su variación %; los efectos volumen, mezcla y precio; la variación % del costo de azúcar por CU; margen bruto real y presupuesto; variación de volumen y de distribución de Golfo; EBITDA real preliminar y presupuesto.
Agrega los ajustes de la conciliación del ejercicio 2: comisión bancaria no registrada de 16,000.00 (resta al EBITDA; el IVA de 2,560.00 es acreditable y no afecta resultados), cargo duplicado por reclamar de 2,436,900.00 (cuenta por cobrar al banco, no afecta resultados) y el EBITDA real ajustado con su variación % contra presupuesto.
Regla: nada entra a la presentación del Consejo si no está en esta hoja."""
P["4.1a"] = """Revisa Historico_Volumen. ¿Hay algún mes atípico en algún CEDIS? Compáralo contra el mismo mes del año anterior y contra los meses vecinos, y dime CEDIS, mes, volumen y por qué lo consideras atípico. No lo corrijas todavía."""
P["4.1b"] = """Crea una hoja Pronostico con fórmulas:
1. Reemplaza el mes atípico por el promedio redondeado de los meses anterior y posterior del mismo CEDIS (sin cambiar Historico_Volumen).
2. Calcula por CEDIS el crecimiento enero–octubre 2026 contra enero–octubre 2025 con la serie ajustada, y también el total sin ajustar para comparar.
3. Pronostica noviembre y diciembre 2026 como el mismo mes de 2025 × (1 + crecimiento), redondeado a cajas enteras.
4. Volumen del 4T = octubre 2026 real + noviembre + diciembre.
5. Ventas de noviembre y diciembre = volumen pronosticado × precio promedio real de octubre del CEDIS (Supuestos_Forecast). Ventas del 4T = octubre real + noviembre + diciembre.
6. Compara el 4T contra presupuesto (octubre de Datos_ER + Presupuesto_NovDic).
7. Utilidad bruta de noviembre y diciembre con el costo por CU real de octubre de Supuestos_Forecast (azúcar + PET + concentrado × tipo de cambio + otros).
Marca cada columna como Observado o Estimación."""
P["4.2"] = """Crea una hoja Escenarios sobre la utilidad bruta de noviembre y diciembre 2026, con referencias a celdas de Supuestos_Forecast y al volumen de noviembre y diciembre de la hoja Pronostico:
- Base.
- Azúcar +10 %: el costo de azúcar por CU sube 10 %.
- Tipo de cambio +1.00 MXN por USD: el concentrado está 100 % en dólares; el PET, 50 % (costo PET por CU × proporción en dólares × aumento del tipo de cambio / tipo de cambio actual).
- Combinado.
Para cada escenario muestra el cambio de costo por CU, el impacto en pesos y el impacto % sobre la utilidad bruta base. Etiqueta todo como Estimación.
Después agrega al final de Hechos_del_cierre: el volumen atípico excluido, el crecimiento ajustado, el pronóstico de volumen y ventas del 4T y su variación contra presupuesto, y el impacto de cada escenario, con su fuente y Tipo = Estimación."""
P["4.3"] = """Con el archivo adjunto Zava_Cierre_Oct2026.xlsx (hoja Historico_Volumen), pronostica el volumen de noviembre y diciembre 2026 por CEDIS con un método que considere estacionalidad. Antes, detecta y explica cualquier dato atípico y no lo uses para la tendencia. Muestra el método, el código que usaste y una gráfica real vs pronóstico. Compara tu resultado con este pronóstico: [pega el total de noviembre y diciembre de tu hoja Pronostico]."""
P["5.1"] = """Usa solo la hoja Hechos_del_cierre de /Zava_Cierre_Oct2026 y la minuta de /Zava_Correos_y_Minuta_Oct2026.
Escribe el resumen para la sesión de Consejo del jueves 26 de noviembre con estas 6 secciones: Mensajes clave; Octubre contra presupuesto y año anterior; Puente de ventas y costos; Caja y conciliación; Pronóstico del 4T y escenarios; Riesgos y decisiones que solicitamos.
Máximo 4 viñetas por sección. Cada viñeta lleva su cifra y, entre paréntesis, el número de hecho de donde sale. Marca como (Estimación) todo lo que sea pronóstico o escenario.
Escribe los importes en millones de pesos con un decimal y los porcentajes con un decimal.
Al final de cada sección agrega "Nota para el orador:" con 2 líneas. No agregues cifras que no estén en la hoja."""
P["5.2"] = """Crea una presentación de 7 diapositivas a partir de /Zava_Resumen_Consejo con el diseño de esta plantilla: una portada y una diapositiva por sección.
Conserva las cifras exactamente como están en el documento y la etiqueta (Estimación) donde aparezca.
Pon el texto de cada "Nota para el orador" en las notas del orador de su diapositiva."""
P["5.3"] = """Actúa primero como un consejero independiente y después como el auditor externo.
Con la presentación /Zava_Consejo_Oct2026 y la solicitud del auditor en /Zava_Correos_y_Minuta_Oct2026, dame una tabla con 8 preguntas probables del Consejo y 6 del auditor. Para cada una: respuesta corta basada en los datos, soporte que tendríamos que llevar (archivo, hoja o documento) y responsable por puesto.
Marca las preguntas que hoy NO podemos responder con estos archivos y qué nos falta."""
P["5.4"] = """Eres un revisor independiente: no participaste en el análisis.
Revisa las 8 afirmaciones del correo "Borrador de mensaje para el Consejo (versión comercial)" de /Zava_Correos_y_Minuta_Oct2026 contra /Zava_Cierre_Oct2026 (hojas Hechos_del_cierre, Variaciones y Datos_ER).
Para cada afirmación da un veredicto:
- Verificado: los datos confirman la cifra y la afirmación.
- Incorrecto: los datos la contradicen.
- No verificable: los archivos no tienen evidencia para confirmarla ni para descartarla (por ejemplo, algo que pudo pasar después del cierre o un dato que no existe en los archivos).
- Exagerado: tiene base en los datos, pero la sobredimensiona.
Tabla: #, afirmación, veredicto, cifra correcta y fuente. No supongas nada que no esté en los archivos."""
P["6.1"] = """Lee /Zava_Flujo_Caja_Diario_Oct2026 (hojas Movimientos, Proyeccion_Nov, Parametros y KPIs) y escribe el briefing de caja de esta semana en 5 líneas: posición por banco contra su mínimo, bancos que caerán bajo su mínimo en los próximos 10 días hábiles con fecha e importe, movimientos atípicos, cobranza contra meta y decisiones que necesito tomar. Cita la hoja de cada cifra y di "no está en los datos" si algo falta."""
P["6.2"] = """---
name: conciliacion-bancaria
description: Concilia un estado de cuenta contra el auxiliar de bancos por referencia e importe, lista las partidas y comprueba que la diferencia quede en 0.00.
---
## Entradas
- Una hoja con el estado de cuenta del banco y otra con el auxiliar de bancos. Ambas con Fecha, Referencia, Concepto, Cargo, Abono y Saldo.

## Pasos
1. Crea Cruce_Banco y Cruce_Libros con fórmulas COUNTIF/COUNTIFS por Referencia y por Referencia + importe.
2. Estatus por renglón: Sin contrapartida, Importe distinto, Repetido o Conciliado.
3. Crea Partidas con SUMIFS: tipo, referencia, importe en banco, importe en libros, diferencia y lado que se ajusta.
4. Comprueba con fórmula que la suma de diferencias = saldo final banco − saldo final libros.
5. Llena la conciliación y deja una celda Diferencia que debe dar 0.00.

## Nunca
- Pegar valores en lugar de fórmulas, modificar las hojas originales o forzar la diferencia a cero."""
P["6.3"] = """Objetivo: [qué quieres obtener y para quién, por ejemplo: "un análisis de variaciones de gastos para mi director"].
Contexto: [área, periodo y por qué lo necesitas].
Fuentes: [escribe / y elige el archivo, correo o reunión; di qué hojas o columnas usar].
Expectativas: [formato (tabla, 5 viñetas, correo), extensión, cifras con su fuente, "no está en los datos" si falta algo].
Antes de responder, hazme hasta 3 preguntas si algo no está claro."""

# --------------------------------------------------------------- helpers HTML
LVL = {"Requerido": "lvl-req", "Ver y comparar": "lvl-ver", "Demo": "lvl-demo", "Opcional": "lvl-opt", "Reto": "lvl-reto"}
MODE = {"Solo chat": "mode-chat", "Plan": "mode-plan", "Edición": "mode-edit", "Copilot Chat": "mode-teams", "Outlook": "mode-outlook",
        "PowerPoint": "mode-ppt", "Word": "mode-outlook", "Analista": "mode-agent", "Aptitud": "mode-agent", "Reglas": "mode-plan"}
LIC = '<span class="req req-lic">Licencia Microsoft 365 Copilot</span>'


def table(head, rows, cls=""):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def dl(path, label=None):
    name = path.split("/")[-1]
    return f'<a href="{E(path)}" download>{E(label or name)}</a>'


def lab(id, n, title, level, time, goal, app, inputs, produces, intro="", prompts=(), expect="", fail="", checks=(), callouts=(), lic=LIC):
    meta = (f'<div class="meta"><span><b>Tiempo</b> {time}</span><span><b>Objetivo</b> {goal}</span>'
            f'<span><b>App</b> {app}</span><span><b>Requiere</b> {lic}</span></div>'
            f'<div class="chain"><div><span class="chain-k">Usas</span>{inputs}</div><div><span class="chain-k add">Produce para el siguiente paso</span>{produces}</div></div>')
    pr = ""
    for k, (label, mode, key) in enumerate(prompts):
        pid = f"p-{id}-{k}"
        pr += (f'<div class="prompt"><div class="prompt-head"><span class="prompt-label">{E(label)}</span><span class="mode {MODE[mode]}">{mode}</span>'
               f'<button class="copy" type="button" aria-label="Copiar: {E(label)}">Copiar</button></div><pre id="{pid}">{E(P[key] if key in P else key)}</pre></div>')
    co = "".join(f'<div class="callout {c}"><div class="callout-title">{t}</div><div>{b}</div></div>' for c, t, b in callouts)
    ex = f'<div class="callout expect"><div class="callout-title">Lo que verás</div><div>{expect}</div></div>' if expect else ""
    fl = f'<div class="callout catchup"><div class="callout-title">Si no te sale</div><div>{fail}</div></div>' if fail else ""
    ck = ""
    if checks:
        ck = '<div class="selfcheck"><div class="callout-title">Para practicar después</div><ul>' + "".join(
            f'<li><label><input type="checkbox" data-key="{id}-{i}"> {c}</label></li>' for i, c in enumerate(checks)) + "</ul></div>"
    intro_html = f"<p>{intro}</p>" if intro else ""
    return (f'<details class="lab" id="{id}"><summary><span class="lab-num">{n}</span><span class="lab-title">{title}</span>'
            f'<span class="lvl {LVL[level]} lvl-sum">{level}</span></summary><div class="lab-body">{meta}{intro_html}{pr}{ex}{co}{fl}{ck}</div></details>')


def chapter(id, num_, title, tags, story, labs_html, extra=""):
    t = "".join(f"<span>{x}</span>" for x in tags)
    return (f'<section class="module" id="{id}"><div class="module-head"><div class="module-num">{num_}</div><h2>{title}</h2>'
            f'<div class="module-tags">{t}</div></div><div class="story"><div class="story-label">La historia</div><p>{story}</p></div>{extra}{labs_html}</section>')


def ck(file, ej):
    return f'Abre {dl(FC + file)} (carpeta 2_Checkpoints): tiene el resultado de este ejercicio. Compáralo con lo tuyo y continúa el ejercicio {ej} con ese archivo.'


# --------------------------------------------------------------- tablas de cifras
def t_caja():
    rows = [[b, pesos(K[k]), pesos(Z.MINIMO[b]), "Arriba"] for b, k in (("Banco Ceiba", "caja_ceiba"), ("Banco Coral", "caja_coral"), ("Banco Jade", "caja_jade"))]
    rows.append(["<b>Total</b>", f"<b>{pesos(K['caja_total'])}</b>", pesos(K["caja_minimos_total"]), ""])
    return table(["Banco", "Saldo al 30/10", "Saldo mínimo", "Contra mínimo"], rows)


def t_var():
    rows = []
    for c in Z.CEDIS:
        rows.append([c, pct(K[f"vol_varpct_p_{c}"]), pct(K[f"vol_varpct_a_{c}"]), mdp(K[f"ventas_var_p_{c}"], sign=True), pct(K[f"ventas_varpct_p_{c}"]),
                     pct(K[f"ub_r_{c}"] / K[f"ventas_r_{c}"], sign=False), mdp(K[f"dist_var_p_{c}"], sign=True)])
    rows.append(["<b>Total</b>", pct(K["vol_varpct_p"]), pct(K["vol_varpct_a"]), mdp(K["ventas_var_p"], sign=True), pct(K["ventas_varpct_p"]),
                 pct(K["mb_r"], sign=False), mdp(K["dist_var_p"], sign=True)])
    return table(["CEDIS", "Vol. vs ppto", "Vol. vs AA", "Ventas vs ppto", "Ventas % vs ppto", "Margen bruto real", "Distribución vs ppto"], rows)


def t_puente():
    rows = [["Ventas presupuesto", mdp(K["ventas_p"])], ["Efecto volumen", mdp(K["ef_volumen"], sign=True)], ["Efecto mezcla", mdp(K["ef_mezcla"], sign=True)],
            ["Efecto precio", mdp(K["ef_precio"], sign=True)], ["<b>Ventas real</b>", f"<b>{mdp(K['ventas_r'])}</b>"]]
    return table(["Puente de ventas", "Importe"], rows)


def t_costos():
    rows = []
    for m, n in (("azucar", "Azúcar"), ("pet", "PET"), ("conc", "Concentrado"), ("otros", "Otros costos de producción")):
        rows.append([n, mdp(K[f"cost_vol_{m}"], sign=True), mdp(K[f"cost_tarifa_{m}"], sign=True), pct(K[f"{m}_cu_varpct_p"])])
    rows.append(["<b>Total</b>", mdp(K["cost_vol_total"], sign=True), mdp(K["cost_tarifa_total"], sign=True), ""])
    return table(["Insumo", "Efecto volumen", "Efecto costo unitario", "Costo por CU vs ppto"], rows)


def t_partidas():
    rows = [["Depósito en tránsito", Z.DEP_TRANSITO["ref"], "—", pesos(K["dep_transito"]), "Banco"],
            ["Comisión bancaria no registrada (más IVA)", Z.COMISION["ref"], f"{pesos(K['comision'])} + {pesos(K['comision_iva'])}", "—", "Libros"],
            ["Cargo duplicado", Z.DUPLICADO["ref"], f"{pesos(K['duplicado'])} (segundo cargo)", "—", "Banco"],
            ["Error de captura", Z.ERROR_CAPTURA["ref"], pesos(K["error_banco"]), pesos(K["error_libros"]), "Libros"]]
    return table(["Partida", "Referencia", "En banco", "En libros", "Se ajusta en"], rows)


def t_pron():
    rows = [[c, pct(K[f"fc_g_{c}"]), num(K[f"fc_vol_{c}_11"]), num(K[f"fc_vol_{c}_12"])] for c in Z.CEDIS]
    rows.append(["<b>Total</b>", pct(K["fc_g_total_adj"]), num(sum(K[f"fc_vol_{c}_11"] for c in Z.CEDIS)), num(sum(K[f"fc_vol_{c}_12"] for c in Z.CEDIS))])
    return table(["CEDIS", "Crecimiento ajustado", "Nov 2026 (Est.)", "Dic 2026 (Est.)"], rows)


def t_esc():
    rows = [["Azúcar +10 %", num(K["esc_azucar_cu"], 2), mdp(K["esc_azucar"], sign=True), pct(K["esc_azucar"] / K["fc_nd_ub"])],
            ["Tipo de cambio +1.00", num(K["esc_tc_conc_cu"] + K["esc_tc_pet_cu"], 2), mdp(K["esc_tc"], sign=True), pct(K["esc_tc"] / K["fc_nd_ub"])],
            ["<b>Combinado</b>", num(K["esc_azucar_cu"] + K["esc_tc_conc_cu"] + K["esc_tc_pet_cu"], 2), f"<b>{mdp(K['esc_comb'], sign=True)}</b>", pct(K["esc_comb_pct_ub"])]]
    return table(["Escenario (Estimación)", "Más costo por CU (MXN)", "Impacto utilidad bruta nov–dic", "Impacto %"], rows)


def t_claims():
    return table(["#", "Afirmación", "Veredicto esperado", "Por qué"], [[i, E(c[0]), f"<b>{c[1]}</b>", E(c[2])] for i, c in enumerate(CLAIMS, 1)])


CASOS = [  # caso, ejercicio, apps
    ("Briefing de caja: posición por banco, alertas y movimientos atípicos", "1.1", "Excel"),
    ("Analizar correos y la minuta para escribir el briefing y el correo al CFO", "1.2 · 1.3", "Copilot Chat · Word · Outlook"),
    ("Conciliación bancaria con fórmulas y comprobación independiente", "2.1 · 2.2 · 2.3", "Excel"),
    ("Variaciones real contra presupuesto y año anterior por CEDIS", "3.1", "Excel"),
    ("Puente precio–volumen–mezcla y costos por insumo", "3.2", "Excel"),
    ("Hechos del cierre: cada cifra con su fuente", "3.3", "Excel"),
    ("Pronóstico del trimestre con dato atípico y escenarios de azúcar y tipo de cambio", "4.1 · 4.2 · 4.3", "Excel · Analista"),
    ("Presentación para el Consejo con notas del orador, desde un Excel", "5.1 · 5.2", "Copilot Chat · Word · PowerPoint"),
    ("Preguntas probables del Consejo y del auditor, con su lista de soporte", "5.3", "Copilot Chat · PowerPoint (Investigador opcional)"),
    ("Revisión final con veredictos y prompts que se repiten cada semana", "5.4 · 6.1", "Copilot Chat · Teams · Outlook"),
]
