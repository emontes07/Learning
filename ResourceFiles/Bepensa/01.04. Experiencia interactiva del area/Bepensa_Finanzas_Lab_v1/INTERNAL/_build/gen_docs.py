"""Word y PowerPoint: correos y minuta, plantilla del Consejo y checkpoints de los ejercicios 1 y 5."""
import os, re, copy
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from pptx import Presentation
from pptx.util import Inches, Pt as PPt
from pptx.dml.color import RGBColor as PRGB
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from lxml import etree
import zava_data as Z, answers as A
from answers import mdp, pesos, num, pct, pts

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_Finanzas_Lab_v1"
F1 = os.path.join(ROOT, "files", "1_Archivos_de_practica")
F2 = os.path.join(ROOT, "files", "2_Checkpoints")
K = A.compute()
GREEN = RGBColor(0x0F, 0x5F, 0x4A)


def F():
    """Textos de cifras usados en documentos, guía y verificación."""
    return dict(
        ventas_r=mdp(K["ventas_r"]), ventas_var_p=mdp(K["ventas_var_p"], sign=True), ventas_varpct_p=pct(K["ventas_varpct_p"]),
        ventas_varpct_a=pct(K["ventas_varpct_a"]), vol_r=num(K["vol_r"]), vol_varpct_p=pct(K["vol_varpct_p"]), vol_varpct_a=pct(K["vol_varpct_a"]),
        ef_vol=mdp(K["ef_volumen"], sign=True), ef_mez=mdp(K["ef_mezcla"], sign=True), ef_pre=mdp(K["ef_precio"], sign=True),
        az_cu=pct(K["azucar_cu_varpct_p"]), az_tar=mdp(K["cost_tarifa_azucar"], sign=True),
        mb_r=pct(K["mb_r"], sign=False), mb_p=pct(K["mb_p"], sign=False), mb_pts=pts(K["mb_var_p_pts"]),
        golfo_vol=pct(K["vol_varpct_p_Golfo"]), golfo_dist=mdp(K["dist_var_p_Golfo"], sign=True), norte_vol=pct(K["vol_varpct_p_Norte"]),
        pen_vol_a=pct(K["vol_varpct_a_Península"]), pen_vol_p=pct(K["vol_varpct_p_Península"]),
        ebitda_pre=mdp(K["ebitda_r"]), ebitda_aj=mdp(K["ebitda_r_aj"]), ebitda_p=mdp(K["ebitda_p"]), ebitda_var=mdp(K["ebitda_var_p"], sign=True),
        ebitda_pct=pct(K["ebitda_varpct_p"]), ajuste=pesos(K["ebitda_ajuste"], sign=True),
        caja=mdp(K["caja_total"]), caja_exacta=pesos(K["caja_total"]), coral12=mdp(K["coral_12nov"]), coral13=mdp(K["coral_13nov"]),
        traspaso=mdp(K["coral_traspaso_necesario"]), dup=pesos(K["duplicado"]), dif=pesos(K["conc_diferencia_inicial"]),
        cobr=pct(K["cobranza_oct_cumpl"], sign=False), dso=num(K["dso_moderno_oct"], 1), dso_jul=num(K["dso_moderno_jul"], 1),
        atip=num(K["atipico_vol"]), atip_exc=num(K["atipico_exceso"]), g_adj=pct(K["fc_g_total_adj"]), g_raw=pct(K["fc_g_total_raw"]),
        q4_vol=num(K["fc_q4_vol"]), q4_ventas=mdp(K["fc_q4_ventas"]), q4_vs=pct(K["fc_q4_ventas_vs_pp"]),
        esc_az=mdp(K["esc_azucar"], sign=True), esc_tc=mdp(K["esc_tc"], sign=True), esc_comb=mdp(K["esc_comb"], sign=True), esc_pct=pct(K["esc_comb_pct_ub"]),
    )


T = F()

CLAIMS = [  # borrador comercial para el Consejo: (afirmación, veredicto esperado, por qué)
    (f"Las ventas netas de octubre superaron el presupuesto en {pct(K['ventas_varpct_p'], sign=False)} ({mdp(K['ventas_var_p'])}).", "Verificado",
     f"Hoja Variaciones, fila Total: {T['ventas_varpct_p']} y {T['ventas_var_p']}."),
    ("El volumen creció 9.9 % contra octubre del año pasado.", "Incorrecto",
     f"El volumen creció {T['vol_varpct_a']}; el {T['ventas_varpct_a']} es el crecimiento de las ventas, no del volumen."),
    ("Golfo fue el único CEDIS por debajo del presupuesto en volumen.", "Incorrecto",
     f"Norte también quedó abajo ({T['norte_vol']}); Golfo quedó en {T['golfo_vol']}."),
    (f"El costo de azúcar por caja subió {pct(K['azucar_cu_varpct_p'], sign=False)} contra presupuesto.", "Verificado", f"Hoja Puente_Ppto, renglón Azúcar (costo por CU): {T['az_cu']}."),
    ("Banco Ceiba ya confirmó que esta semana reembolsará el cargo duplicado.", "No verificable",
     "Los archivos solo muestran que la reclamación se envió el 3 de noviembre y que el banco responde en 5 días hábiles; no hay evidencia de una confirmación."),
    ("Península tuvo un crecimiento extraordinario en volumen, muy por encima del resto de los CEDIS.", "Exagerado",
     f"Península fue el CEDIS que más creció, pero {T['pen_vol_a']} contra el año anterior ({T['vol_varpct_a']} la compañía y {pct(K['vol_varpct_a_Centro'])} Centro): bueno, no extraordinario."),
    ("Según nuestro pronóstico (estimación), las ventas del cuarto trimestre quedarían ligeramente arriba del presupuesto.", "Verificado",
     f"Pronóstico 4T vs presupuesto: {T['q4_vs']}; está etiquetado como estimación."),
    ("Los consumidores prefieren cada vez más las presentaciones retornables.", "No verificable",
     "Los archivos no tienen datos por presentación ni de preferencia del consumidor."),
]


# ---------------------------------------------------------------- Word helpers
def new_doc():
    d = Document()
    st = d.styles["Normal"]; st.font.name = "Segoe UI"; st.font.size = Pt(10.5)
    for s in ("Heading 1", "Heading 2", "Heading 3"):
        d.styles[s].font.name = "Segoe UI"; d.styles[s].font.color.rgb = GREEN
    for sec in d.sections: sec.left_margin = sec.right_margin = Cm(2.2)
    return d


def mail(d, de, para, fecha, asunto, body):
    p = d.add_paragraph(); p.paragraph_format.space_before = Pt(10)
    for lbl, val in (("De: ", de), ("Para: ", para), ("Fecha: ", fecha), ("Asunto: ", asunto)):
        r = p.add_run(lbl); r.bold = True; p.add_run(val + "\n")
    for para_ in body: d.add_paragraph(para_)
    d.add_paragraph("—" * 30)


def correos():
    d = new_doc()
    d.add_heading("Zava Bebidas · Correos y minuta · cierre de octubre 2026", 0)
    d.add_paragraph("Documento de práctica. Empresa, personas, bancos, proveedores y cifras son ficticios. Los remitentes se identifican solo por su puesto.").italic = True
    d.add_heading("1. Hilo de correos", 1)
    mail(d, "Dirección de Finanzas (CFO)", "Tesorería; Contraloría; Planeación Financiera", "lunes 2 de noviembre de 2026, 8:05",
         "Cierre de octubre y Consejo del 26 de noviembre",
         ["Equipo:", "Para el martes necesito un briefing corto de caja: posición al cierre de octubre por banco, alertas de las próximas dos semanas y qué decisiones tengo que tomar.",
          "Para el Consejo del jueves 26 de noviembre quiero: resultados de octubre contra presupuesto y año anterior, explicación de la variación (volumen, precio, mezcla y costos), el pronóstico del cuarto trimestre y la sensibilidad a azúcar y tipo de cambio.",
          "Cada cifra que presentemos debe tener su fuente. No quiero sorpresas con la auditoría.", "Gracias."])
    mail(d, "Gerencia de Tesorería", "Dirección de Finanzas (CFO)", "lunes 2 de noviembre de 2026, 10:40", "RE: Cierre de octubre y Consejo del 26 de noviembre",
         ["Dos puntos para el briefing:",
          "1) El 12 de noviembre Banco Coral paga la quincena de azúcar, ya con el precio nuevo: 41.2 millones. Estoy revisando si los traspasos programados alcanzan.",
          "2) En Banco Ceiba vemos el pago a Envases del Sureste Ficticio (preformas PET) del 22 de octubre dos veces en banca electrónica. Lo estamos revisando con Contraloría."])
    mail(d, "Compras (insumos)", "Dirección de Finanzas (CFO); Planeación Financiera", "viernes 30 de octubre de 2026, 17:20", "Aviso del ingenio: posible ajuste al precio del azúcar",
         ["El Ingenio del Golfo (proveedor ficticio) nos avisó de un posible ajuste de hasta 10 % en el precio del azúcar para noviembre y diciembre por la zafra corta.",
          "Todavía no está confirmado. Sugiero incluirlo como escenario en el pronóstico."])
    mail(d, "Contraloría", "Dirección de Finanzas (CFO); Gerencia de Tesorería", "martes 3 de noviembre de 2026, 9:15", "Conciliación Banco Ceiba octubre",
         ["La conciliación de Banco Ceiba de octubre tiene una diferencia de 3,722,060.00 entre banco y libros. Hoy la terminamos.",
          "Ya enviamos al banco la reclamación del cargo duplicado; el banco responde en 5 días hábiles.",
          "Recordatorio: los ajustes de la conciliación entran al cierre antes de mandar cifras al Consejo."])
    mail(d, "Despacho de auditoría externa (ficticio)", "Contraloría", "martes 3 de noviembre de 2026, 12:30", "Revisión interina: solicitud preliminar",
         ["Para la revisión interina les pediremos: conciliaciones bancarias de octubre con su soporte, el análisis de variaciones mayores a 5 % contra presupuesto, el soporte de los supuestos del pronóstico y los contratos o avisos de precio de los insumos principales.",
          "Les confirmamos fechas la próxima semana."])
    mail(d, "Dirección Comercial", "Dirección de Finanzas (CFO)", "miércoles 4 de noviembre de 2026, 18:02", "Borrador de mensaje para el Consejo (versión comercial)",
         ["Te comparto mi propuesta de mensajes para el Consejo. Revísalos, por favor:"] + [f"{i}. {c[0]}" for i, c in enumerate(CLAIMS, 1)])
    d.add_heading("2. Minuta del Comité de Finanzas", 1)
    d.add_paragraph("Miércoles 28 de octubre de 2026 · Asistentes: Dirección de Finanzas, Tesorería, Contraloría, Planeación Financiera y Dirección Comercial (por puesto).")
    d.add_heading("Temas", 2)
    for t in ["Golfo: la tormenta tropical de la semana del 12 al 16 de octubre cerró rutas varios días; hubo que rerutear la distribución con unidades rentadas.",
              "Golfo, julio 2026: la venta extraordinaria a un evento regional fue única y no se repetirá. No debe usarse para tendencias ni pronósticos.",
              "Canal Moderno: dos cadenas de autoservicio ampliaron sus plazos de pago; el DSO del canal sigue subiendo.",
              "Presupuesto 2027: Planeación Financiera entrega los supuestos preliminares el 20 de noviembre.",
              "Consejo: sesión el jueves 26 de noviembre de 2026. El paquete se envía a los consejeros el 23 de noviembre."]:
        d.add_paragraph(t, style="List Bullet")
    d.add_heading("Acuerdos", 2)
    for t in ["Tesorería envía el briefing de caja al CFO los martes.",
              "Contraloría cierra la conciliación de Banco Ceiba y reclama al banco cualquier cargo no reconocido.",
              "Planeación Financiera prepara el pronóstico del 4T con escenarios de azúcar y tipo de cambio.",
              "Toda cifra para el Consejo se documenta en una hoja de hechos con su fuente."]:
        d.add_paragraph(t, style="List Number")
    path = os.path.join(F1, "Zava_Correos_y_Minuta_Oct2026.docx"); d.save(path); return path


def briefing_lines():
    return [
        f"Posición de caja al 30 de octubre: {T['caja']} en tres bancos (Ceiba {mdp(K['caja_ceiba'])}, Coral {mdp(K['caja_coral'])}, Jade {mdp(K['caja_jade'])}); los tres arriba de su saldo mínimo.",
        f"Alerta 1: Banco Coral cae a {T['coral12']} el 12 de noviembre (mínimo {mdp(Z.MINIMO['Banco Coral'])}) por el pago de azúcar y queda en {T['coral13']} el 13; se requiere un traspaso adicional de al menos {T['traspaso']} desde Ceiba.",
        f"Alerta 2: el 22 de octubre Banco Ceiba registra pagos a proveedores por {mdp(K['atipico_22oct_pagos'])}, el doble del pago normal de PET; posible cargo duplicado de {T['dup']} (en revisión con Contraloría).",
        f"KPI: cobranza de octubre al {T['cobr']} de la meta; el DSO del canal Moderno subió de {T['dso_jul']} a {T['dso']} días desde julio.",
        "Decisiones: autorizar el traspaso a Coral antes del 12 de noviembre y dar seguimiento a la reclamación del cargo duplicado.",
    ]


def ckpt_ej1():
    d = new_doc()
    d.add_heading("CHECKPOINT · Resultado del Ejercicio 1: briefing de caja y correo al CFO", 0)
    d.add_paragraph("Úsalo si no terminaste el Ejercicio 1. Tu versión puede variar en redacción; las cifras deben coincidir.").italic = True
    d.add_heading("Briefing de caja (5 líneas)", 1)
    for l in briefing_lines(): d.add_paragraph(l, style="List Number")
    d.add_heading("Borrador de correo al CFO (no se envía en el laboratorio)", 1)
    d.add_paragraph("Asunto: Briefing de caja · cierre de octubre y alertas al 13 de noviembre")
    d.add_paragraph("Hola:")
    d.add_paragraph(f"Cerramos octubre con {T['caja']} en bancos, arriba de los mínimos. Hay dos alertas: Banco Coral queda bajo su mínimo el 12 de noviembre por el pago de azúcar (necesitamos traspasar al menos {T['traspaso']} desde Ceiba) y un posible cargo duplicado de {T['dup']} en Ceiba que Contraloría ya reclamó al banco.")
    d.add_paragraph(f"La cobranza de octubre quedó al {T['cobr']} de la meta y el DSO de Moderno sigue subiendo ({T['dso']} días).")
    d.add_paragraph("¿Autorizas el traspaso a Coral para el miércoles 11 de noviembre?")
    d.add_paragraph("Saludos,\nTesorería")
    path = os.path.join(F2, "CHECKPOINT_Ej1_Resultado_Briefing.docx"); d.save(path); return path


def board_slides():
    """Contenido de la presentación del Consejo (título, viñetas, notas)."""
    return [
        ("Resultados de octubre y pronóstico del 4T 2026", ["Sesión de Consejo · jueves 26 de noviembre de 2026", "Dirección de Finanzas · Zava Bebidas (ficticia)"],
         "Agradecer y anunciar los tres mensajes: crecimos contra el año anterior, el azúcar presionó el margen y el 4T depende de dos riesgos de costo."),
        ("Mensajes clave", [f"Ventas netas {T['ventas_r']}: {T['ventas_varpct_p']} vs presupuesto y {T['ventas_varpct_a']} vs año anterior",
                            f"Margen bruto {T['mb_r']} ({T['mb_pts']} vs presupuesto) por el azúcar ({T['az_cu']} por caja)",
                            f"EBITDA ajustado {T['ebitda_aj']}, {T['ebitda_pct']} vs presupuesto",
                            f"Pronóstico 4T (estimación): ventas {T['q4_ventas']}, {T['q4_vs']} vs presupuesto"],
         "Cada cifra viene de la hoja Hechos del cierre. El EBITDA ya incluye el ajuste de la conciliación bancaria."),
        ("Octubre: real contra presupuesto y año anterior", [f"Volumen {T['vol_r']} CU: {T['vol_varpct_p']} vs presupuesto, {T['vol_varpct_a']} vs año anterior",
                            f"Golfo {T['golfo_vol']} en volumen por la tormenta tropical; distribución {T['golfo_dist']} vs presupuesto",
                            f"Península y Centro compensaron el volumen; Norte quedó en {T['norte_vol']}"],
         "Si preguntan por Golfo: la tormenta cerró rutas del 12 al 16 de octubre; el rerruteo explica el gasto de distribución adicional."),
        ("Puente de ventas y de costos contra presupuesto", [f"Precio {T['ef_pre']}; volumen {T['ef_vol']}; mezcla {T['ef_mez']}",
                            f"Azúcar: efecto costo unitario {T['az_tar']}",
                            f"Margen bruto {T['mb_r']} vs {T['mb_p']} presupuestado"],
         "El precio explicó el crecimiento de ventas; la mezcla restó porque creció Moderno, el canal de menor precio, y bajó Consumo en sitio, el de mayor precio."),
        ("Caja y conciliación bancaria", [f"Posición de caja al 30 de octubre: {T['caja']}",
                            f"Conciliación de Banco Ceiba explicada: {T['dif']} en 4 partidas",
                            f"Cargo duplicado por {T['dup']} reclamado al banco",
                            f"Comisión no registrada: ajuste de {T['ajuste']} al EBITDA"],
         "El cargo duplicado no afecta resultados; es una cuenta por cobrar al banco mientras responde."),
        ("Pronóstico del 4T y escenarios (estimación)", [f"Volumen 4T {T['q4_vol']} CU; ventas {T['q4_ventas']} ({T['q4_vs']} vs presupuesto)",
                            f"Tendencia sin el dato atípico de julio en Golfo: {T['g_adj']} (con el atípico: {T['g_raw']})",
                            f"Azúcar +10 %: {T['esc_az']}; tipo de cambio +1.00: {T['esc_tc']}",
                            f"Combinado: {T['esc_comb']} de utilidad bruta nov–dic ({T['esc_pct']})"],
         "Todo en esta lámina es estimación. Octubre es real; noviembre y diciembre se pronostican con la tendencia sin el atípico."),
        ("Riesgos y decisiones que solicitamos", ["Autorizar coberturas o negociación de azúcar para diciembre",
                            "Dar seguimiento al DSO del canal Moderno con las cadenas",
                            "Confirmar la recuperación del cargo duplicado antes del cierre de noviembre"],
         "Cerrar pidiendo las decisiones. Preguntas probables: precio del azúcar 2027, tipo de cambio y plazos de cadenas."),
    ]


def resumen_ej5():
    d = new_doc()
    d.add_heading("CHECKPOINT · Resumen para el Consejo · octubre 2026", 0)
    d.add_paragraph("Resultado del Ejercicio 5.1. Fuente única: hoja Hechos_del_cierre (CHECKPOINT_Ej4_Resultado_Forecast.xlsx). Úsalo como archivo de origen para la presentación.").italic = True
    for t, bullets, notes in board_slides()[1:]:
        d.add_heading(t, 1)
        for b in bullets: d.add_paragraph(b, style="List Bullet")
        p = d.add_paragraph(); r = p.add_run("Nota para el orador: " + notes); r.italic = True
    path = os.path.join(F2, "CHECKPOINT_Ej5_Resultado_Resumen_Consejo.docx"); d.save(path); return path


# ---------------------------------------------------------------- PowerPoint
C = dict(green="0F5F4A", lime="8CC63F", ink="1F2A2E", light="EEF6EA", grey="5E6B66", white="FFFFFF")
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main", "p": "http://schemas.openxmlformats.org/presentationml/2006/main"}


def base():
    prs = Presentation(); old = prs.slide_width
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5); f = prs.slide_width / old
    master = prs.slide_master; theme = master.part.part_related_by(RT.THEME)
    xml = theme.blob.decode("utf-8")
    clr = f"""<a:clrScheme name="Zava Bebidas"><a:dk1><a:srgbClr val="{C['ink']}"/></a:dk1><a:lt1><a:srgbClr val="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="{C['green']}"/></a:dk2><a:lt2><a:srgbClr val="{C['light']}"/></a:lt2><a:accent1><a:srgbClr val="{C['green']}"/></a:accent1><a:accent2><a:srgbClr val="{C['lime']}"/></a:accent2><a:accent3><a:srgbClr val="2E8B6E"/></a:accent3><a:accent4><a:srgbClr val="F2A900"/></a:accent4><a:accent5><a:srgbClr val="4F7C8A"/></a:accent5><a:accent6><a:srgbClr val="A3B1AB"/></a:accent6><a:hlink><a:srgbClr val="{C['green']}"/></a:hlink><a:folHlink><a:srgbClr val="4F7C8A"/></a:folHlink></a:clrScheme>"""
    fnt = """<a:fontScheme name="Zava Bebidas"><a:majorFont><a:latin typeface="Segoe UI Semibold"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont><a:minorFont><a:latin typeface="Segoe UI"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont></a:fontScheme>"""
    xml = re.sub(r"<a:clrScheme.*?</a:clrScheme>", clr, xml, flags=re.S)
    xml = re.sub(r"<a:fontScheme.*?</a:fontScheme>", fnt, xml, flags=re.S)
    theme._blob = xml.encode("utf-8")
    for shp in list(master.shapes) + [s for l in master.slide_layouts for s in l.shapes]:
        try:
            if shp.left is not None: shp.left = int(shp.left * f); shp.width = int(shp.width * f)
        except Exception: pass
    ts = master._element.find(".//p:txStyles/p:titleStyle/a:lvl1pPr/a:defRPr", NS)
    if ts is not None:
        for ch in list(ts):
            if ch.tag.endswith("solidFill"): ts.remove(ch)
        sf = etree.Element(f"{{{NS['a']}}}solidFill"); etree.SubElement(sf, f"{{{NS['a']}}}schemeClr", val="tx2"); ts.insert(0, sf); ts.set("sz", "3000")
    tmp = prs.slides.add_slide(prs.slide_layouts[6])
    band = tmp.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, prs.slide_height - Inches(0.14), prs.slide_width, Inches(0.14))
    band.fill.solid(); band.fill.fore_color.rgb = PRGB.from_string(C["lime"]); band.line.fill.background()
    tb = tmp.shapes.add_textbox(Inches(0.5), prs.slide_height - Inches(0.55), Inches(8), Inches(0.3))
    r = tb.text_frame.paragraphs[0].add_run(); r.text = "Zava Bebidas  |  Dirección de Finanzas  |  Confidencial (ficticio)"
    r.font.size = PPt(10); r.font.color.rgb = PRGB.from_string(C["grey"])
    for el in (band._element, tb._element): master.shapes._spTree.append(copy.deepcopy(el))
    rid = prs.slides._sldIdLst[-1].rId; prs.part.drop_rel(rid); prs.slides._sldIdLst.remove(prs.slides._sldIdLst[-1])
    return prs


def fill_slide(prs, title, bullets, notes, first=False):
    if first:
        s = prs.slides.add_slide(prs.slide_layouts[0]); s.shapes.title.text = title
        s.placeholders[1].text = "\n".join(bullets)
        bg = s.background.fill; bg.solid(); bg.fore_color.rgb = PRGB.from_string(C["light"])
    else:
        s = prs.slides.add_slide(prs.slide_layouts[1]); s.shapes.title.text = title
        tf = s.placeholders[1].text_frame; tf.clear()
        for i, b in enumerate(bullets):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.text = b
            for r in p.runs: r.font.size = PPt(20)
    t = s.shapes.title; body = s.placeholders[1]
    if first:
        t.left, t.top, t.width, t.height = Inches(0.8), Inches(2.3), Inches(11.7), Inches(1.4)
        body.left, body.top, body.width, body.height = Inches(0.8), Inches(3.9), Inches(11.7), Inches(1.4)
        for p in body.text_frame.paragraphs:
            for r in p.runs: r.font.size = PPt(20); r.font.color.rgb = PRGB.from_string(C["grey"])
    else:
        t.left, t.top, t.width, t.height = Inches(0.6), Inches(0.35), Inches(12.1), Inches(1.0)
        body.left, body.top, body.width, body.height = Inches(0.6), Inches(1.6), Inches(12.1), Inches(5.0)
        t.text_frame.paragraphs[0].alignment = PP_ALIGN.LEFT
        for r in t.text_frame.paragraphs[0].runs: r.font.size = PPt(30)
    for r in s.shapes.title.text_frame.paragraphs[0].runs: r.font.color.rgb = PRGB.from_string(C["green"])
    if notes: s.notes_slide.notes_text_frame.text = notes
    return s


def plantilla():
    prs = base()
    fill_slide(prs, "Título de la sesión de Consejo", ["Fecha · Área"], "", first=True)
    fill_slide(prs, "Título de la lámina", ["Mensaje principal en una línea", "Dato que lo respalda (con fuente en Hechos del cierre)", "Implicación o decisión"],
               "Las notas del orador van aquí.")
    path = os.path.join(F1, "Zava_Plantilla_Consejo.pptx"); prs.save(path); return path


def deck_ej5():
    prs = base()
    for i, (t, b, n) in enumerate(board_slides()):
        fill_slide(prs, t, b, n, first=(i == 0))
    path = os.path.join(F2, "CHECKPOINT_Ej5_Resultado_Consejo.pptx"); prs.save(path); return path


if __name__ == "__main__":
    for fn in (correos, ckpt_ej1, resumen_ej5, plantilla, deck_ej5): print(fn())
