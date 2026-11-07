# -*- coding: utf-8 -*-
"""Archivos de práctica y checkpoints (sesión general)."""
import os, re, copy, json
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, Reference
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from pptx import Presentation
from pptx.util import Inches, Pt as PPt
from pptx.dml.color import RGBColor as PRGB
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from lxml import etree
import zdata as Z
from zdata import num, pct, pesos, hrs

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_General_Lab_v1"
F1 = os.path.join(ROOT, "files", "1_Archivos_de_practica"); F2 = os.path.join(ROOT, "files", "2_Checkpoints")
K, RAW, CLEAN, COM = Z.compute()
GREEN = "0F5F4A"
HF = Font(bold=True, color="FFFFFF"); HFILL = PatternFill("solid", fgColor=GREEN)
TT = Font(bold=True, size=13, color=GREEN); B = Font(bold=True); NOTE = Font(italic=True, color="555555")
N0 = '#,##0'; N1 = '0.0'; N2 = '0.00'; PCT = '0.0%'
COLS = ["Mes", "Region", "Solicitudes_recibidas", "Solicitudes_atendidas", "Tiempo_respuesta_horas", "Satisfaccion_1a5", "Encuestas_respondidas", "Presupuesto_asignado", "Presupuesto_ejercido"]
FMT = [None, None, N0, N0, N1, N2, N0, N0, N0]

T = dict(rec=num(K["rec_3T"]), ate=num(K["ate_3T"]), pct_ate=pct(K["pct_ate_3T"]), tiempo=hrs(K["tiempo_3T"]), tiempo2=hrs(K["tiempo_2T"]),
         tdelta=hrs(K["tiempo_delta"], True), sat=num(K["sat_3T"], 2), sat2=num(K["sat_2T"], 2), sdelta=num(K["sat_delta"], 2, True),
         golfo_t=hrs(K["tiempo_3T_Golfo"]), golfo_s=num(K["sat_3T_Golfo"], 2), pres=pct(K["pres_pct_3T"]), pres_ej=pesos(K["pres_ej_3T"]),
         pres_as=pesos(K["pres_asig_3T"]), sucio_t=hrs(K["tiempo_3T_sucio"]), sucio_a=num(K["ate_3T_sucio"]), dup=num(K["dup_atendidas"]),
         atip=hrs(K["atipico"]), com=num(K["com_total"]), t1=num(K["tema_n_Tiempo de respuesta"]), t1p=pct(K["tema_pct_tiempo"], 0),
         t1c=num(K["tema_cal_Tiempo de respuesta"], 1), meta_t=hrs(Z.META_TIEMPO), meta_s=num(Z.META_SAT, 2), pen_med=hrs(K["atipico_mediana_region"]))

CLAIMS = [
    (f"En el tercer trimestre atendimos {T['ate']} solicitudes.", "Verificado", f"Hoja Hechos: {T['ate']} solicitudes atendidas (datos limpios; falta Centro agosto)."),
    (f"El tiempo de respuesta promedio del trimestre fue de {T['sucio_t']}.", "Incorrecto", f"Esa cifra incluye el duplicado y el valor atípico. Con datos limpios es {T['tiempo']}."),
    (f"Todas las regiones superaron la meta de satisfacción de {T['meta_s']}.", "Incorrecto", f"Golfo quedó en {T['golfo_s']}; el promedio general fue {T['sat']}."),
    (f"Atendimos el {T['pct_ate']} de las solicitudes que recibimos.", "Verificado", f"Hoja Hechos: {T['pct_ate']}."),
    ("El nuevo portal redujo los tiempos de respuesta en Norte.", "No verificable", "Los tiempos de Norte bajaron, pero los datos no permiten atribuirlo al portal (no hay grupo de comparación ni datos del portal)."),
    ("El tiempo de respuesta se disparó contra el segundo trimestre.", "Exagerado", f"Subió {T['tdelta']} ({T['tiempo2']} a {T['tiempo']}); no es un salto grande y sigue dentro de la meta de {T['meta_t']}."),
]


def table(ws, name, headers, rows, fmts, start=1, widths=None):
    for j, h in enumerate(headers, 1):
        c = ws.cell(start, j, h); c.font = HF; c.fill = HFILL; c.alignment = Alignment(wrap_text=True, vertical="center")
    for i, r in enumerate(rows, start + 1):
        for j, v in enumerate(r, 1):
            c = ws.cell(i, j, v)
            if fmts[j - 1]: c.number_format = fmts[j - 1]
    t = Table(displayName=name, ref=f"A{start}:{get_column_letter(len(headers))}{start + len(rows)}")
    t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium7", showRowStripes=True); ws.add_table(t)
    for j in range(1, len(headers) + 1): ws.column_dimensions[get_column_letter(j)].width = (widths[j - 1] if widths else 16)
    ws.freeze_panes = ws.cell(start + 1, 1)


def leeme(ws, title, lines):
    ws["A1"] = title; ws["A1"].font = Font(bold=True, size=14, color=GREEN)
    for i, l in enumerate(lines, 3): ws.cell(i, 1, l).alignment = Alignment(wrap_text=True)
    ws.column_dimensions["A"].width = 120


def indicadores(path):
    wb = Workbook(); ws = wb.active; ws.title = "Leeme"
    leeme(ws, "Zava Bebidas · Centro de Servicio Interno · indicadores 2026 (datos ficticios)", [
        "El Centro de Servicio Interno atiende solicitudes de los colaboradores (equipos, accesos, trámites y servicios generales) en 4 regiones: Norte, Centro, Golfo y Península.",
        "Indicadores: un renglón por mes (enero a septiembre de 2026) y región, tal como sale del sistema de solicitudes. No se ha revisado: puede tener errores.",
        "Tiempo_respuesta_horas: promedio del mes en horas hábiles. Satisfaccion_1a5: promedio de la encuesta de cierre (1 a 5). Presupuesto en pesos (MXN).",
        "Para promedios de varios meses o regiones: pondera el tiempo por Solicitudes_atendidas y la satisfacción por Encuestas_respondidas.",
        "Metas: hoja Metas. Tercer trimestre (3T) = julio a septiembre; segundo trimestre (2T) = abril a junio.",
        "Empresa, regiones y cifras son ficticias.",
    ])
    ws = wb.create_sheet("Indicadores")
    table(ws, "tblIndicadores", COLS, [[r[c] for c in COLS] for r in RAW], FMT, widths=[10, 12, 14, 14, 14, 14, 14, 16, 16])
    ws = wb.create_sheet("Metas")
    table(ws, "tblMetas", ["Indicador", "Meta", "Nota"], [["Tiempo de respuesta (horas hábiles)", Z.META_TIEMPO, "Máximo, promedio ponderado del trimestre"],
          ["Satisfacción (1 a 5)", Z.META_SAT, "Mínimo, promedio ponderado del trimestre"], ["Presupuesto ejercido", 1.0, "No rebasar el asignado"]], [None, N2, None], widths=[36, 10, 46])
    wb.save(path)


def encuesta(path):
    wb = Workbook(); ws = wb.active; ws.title = "Leeme"
    leeme(ws, "Zava Bebidas · Encuesta de servicio interno · 3T 2026 (comentarios anónimos, ficticios)", [
        "Comentarios abiertos de la encuesta de cierre de solicitudes, julio a septiembre de 2026. Son anónimos: no hay nombre ni número de empleado de quien responde.",
        "Algunos comentarios pueden mencionar a alguien del equipo por su nombre. Antes de compartir resultados, quita esos nombres.",
        "Empresa, comentarios y cifras son ficticios."])
    ws = wb.create_sheet("Comentarios")
    table(ws, "tblComentarios", ["ID", "Region", "Mes", "Calificacion_1a5", "Comentario"], [[c["ID"], c["Region"], c["Mes"], c["Calificacion_1a5"], c["Comentario"]] for c in COM],
          [None, None, None, N0, None], widths=[8, 12, 10, 14, 80])
    wb.save(path)


# ------------------------------------------------------------------ Word
def new_doc():
    d = Document(); st = d.styles["Normal"]; st.font.name = "Segoe UI"; st.font.size = Pt(10.5)
    for s in ("Heading 1", "Heading 2", "Heading 3", "Title"):
        d.styles[s].font.name = "Segoe UI"; d.styles[s].font.color.rgb = RGBColor(0x0F, 0x5F, 0x4A)
    for sec in d.sections: sec.left_margin = sec.right_margin = Cm(2.2)
    return d


def notas(path):
    d = new_doc()
    d.add_heading("Zava Bebidas · Centro de Servicio Interno · notas y políticas", 0)
    d.add_paragraph("Documento de práctica. Empresa, personas y cifras son ficticias; las personas se identifican solo por su puesto.").italic = True
    d.add_heading("1. Notas de reuniones del equipo", 1)
    for t, items in [("Reunión semanal · jueves 8 de octubre de 2026", ["Golfo tiene dos vacantes en la mesa de servicio desde julio; el equipo está saturado y los tiempos subieron.",
                       "El portal de solicitudes nuevo está en piloto en Norte desde agosto.", "Recordatorio: la meta de tiempo de respuesta es de 24 horas hábiles y la de satisfacción, 4.20."]),
                     ("Reunión con la dirección · jueves 22 de octubre de 2026", ["La dirección pide la revisión trimestral para el jueves 19 de noviembre de 2026.",
                       "Quiere ver: volumen atendido, tiempo de respuesta, satisfacción, presupuesto y tres acciones para el siguiente trimestre.",
                       "Pide un reporte de una página y una presentación corta (máximo 6 diapositivas)."]),
                     ("Reunión semanal · jueves 29 de octubre de 2026", ["Acuerdo: cubrir las dos vacantes de Golfo en noviembre.", "Acuerdo: extender el portal a Centro en enero de 2027.",
                       "Acuerdo: enviar al equipo un mensaje con los resultados del trimestre después de la revisión.", "Pendiente: el sistema no exportó los datos de Centro de agosto; Sistemas lo está revisando."])]:
        d.add_heading(t, 2)
        for i in items: d.add_paragraph(i, style="List Bullet")
    d.add_heading("2. Procedimiento de atención de solicitudes internas", 1)
    for h, ps in [("Objetivo", ["Dar a los colaboradores una atención rápida y trazable a sus solicitudes de equipos, accesos, trámites y servicios generales."]),
                  ("Prioridades y tiempos objetivo", ["Urgente (la operación se detiene): primera respuesta en 4 horas hábiles.", "Alta (afecta a varias personas): solución en 24 horas hábiles.",
                                                     "Normal: solución en 48 horas hábiles."]),
                  ("Cómo se registra", ["Toda solicitud se registra en el portal o en la mesa de servicio; no se atienden solicitudes por chat personal.", "Cada solicitud recibe un folio y un responsable."]),
                  ("Escalamiento", ["Si una solicitud supera su tiempo objetivo, se escala al líder de la región; si supera el doble, al líder del Centro de Servicio Interno."]),
                  ("Encuesta de cierre", ["Al cerrar cada solicitud se envía una encuesta anónima de 1 a 5 con un comentario opcional."]),
                  ("Excepciones", ["Cierres de mes y periodos vacacionales pueden ampliar los tiempos objetivo; se avisa con una semana de anticipación."])]:
        d.add_heading(h, 3)
        for p in ps: d.add_paragraph(p)
    d.add_heading("3. Política de trabajo híbrido (ejemplo para Recursos Humanos)", 1)
    for p in ["Aplica a puestos administrativos cuya función lo permita, con acuerdo del líder.", "Se trabajan 3 días presenciales a la semana; el equipo acuerda cuáles.",
              "La solicitud se hace en el portal de Recursos Humanos y la aprueba el líder en un máximo de 5 días hábiles.", "La empresa proporciona laptop y apoyo de conectividad; el mobiliario de casa corre por cuenta del colaborador.",
              "Puestos de operación, planta y atención en sitio no aplican.", "La política se revisa cada año."]:
        d.add_paragraph(p, style="List Bullet")
    d.add_heading("4. Borrador del mensaje al equipo (versión de un colega)", 1)
    d.add_paragraph("Un colega preparó este borrador para enviar al equipo después de la revisión. Revísalo antes de usarlo:")
    for i, c in enumerate(CLAIMS, 1): d.add_paragraph(f"{i}. {c[0]}")
    d.save(path)


# ------------------------------------------------------------------ PowerPoint
C = dict(green="0F5F4A", lime="8CC63F", ink="1F2A2E", light="EEF6EA", grey="5E6B66")
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main", "p": "http://schemas.openxmlformats.org/presentationml/2006/main"}


def base():
    prs = Presentation(); old = prs.slide_width
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5); f = prs.slide_width / old
    master = prs.slide_master; theme = master.part.part_related_by(RT.THEME); xml = theme.blob.decode("utf-8")
    clr = f'<a:clrScheme name="Zava Bebidas"><a:dk1><a:srgbClr val="{C["ink"]}"/></a:dk1><a:lt1><a:srgbClr val="FFFFFF"/></a:lt1><a:dk2><a:srgbClr val="{C["green"]}"/></a:dk2><a:lt2><a:srgbClr val="{C["light"]}"/></a:lt2><a:accent1><a:srgbClr val="{C["green"]}"/></a:accent1><a:accent2><a:srgbClr val="{C["lime"]}"/></a:accent2><a:accent3><a:srgbClr val="2E8B6E"/></a:accent3><a:accent4><a:srgbClr val="F2A900"/></a:accent4><a:accent5><a:srgbClr val="4F7C8A"/></a:accent5><a:accent6><a:srgbClr val="A3B1AB"/></a:accent6><a:hlink><a:srgbClr val="{C["green"]}"/></a:hlink><a:folHlink><a:srgbClr val="4F7C8A"/></a:folHlink></a:clrScheme>'
    fnt = '<a:fontScheme name="Zava Bebidas"><a:majorFont><a:latin typeface="Segoe UI Semibold"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont><a:minorFont><a:latin typeface="Segoe UI"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont></a:fontScheme>'
    xml = re.sub(r"<a:clrScheme.*?</a:clrScheme>", clr, xml, flags=re.S); xml = re.sub(r"<a:fontScheme.*?</a:fontScheme>", fnt, xml, flags=re.S); theme._blob = xml.encode("utf-8")
    for shp in list(master.shapes) + [s for l in master.slide_layouts for s in l.shapes]:
        try:
            if shp.left is not None: shp.left = int(shp.left * f); shp.width = int(shp.width * f)
        except Exception: pass
    tmp = prs.slides.add_slide(prs.slide_layouts[6])
    band = tmp.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, prs.slide_height - Inches(0.14), prs.slide_width, Inches(0.14))
    band.fill.solid(); band.fill.fore_color.rgb = PRGB.from_string(C["lime"]); band.line.fill.background()
    tb = tmp.shapes.add_textbox(Inches(0.5), prs.slide_height - Inches(0.55), Inches(8), Inches(0.3))
    r = tb.text_frame.paragraphs[0].add_run(); r.text = "Zava Bebidas  |  Centro de Servicio Interno  |  Uso interno (ficticio)"; r.font.size = PPt(10); r.font.color.rgb = PRGB.from_string(C["grey"])
    for el in (band._element, tb._element): master.shapes._spTree.append(copy.deepcopy(el))
    rid = prs.slides._sldIdLst[-1].rId; prs.part.drop_rel(rid); prs.slides._sldIdLst.remove(prs.slides._sldIdLst[-1])
    return prs


def slide(prs, title, bullets, notes, first=False):
    s = prs.slides.add_slide(prs.slide_layouts[0 if first else 1]); s.shapes.title.text = title
    t, body = s.shapes.title, s.placeholders[1]
    if first:
        bg = s.background.fill; bg.solid(); bg.fore_color.rgb = PRGB.from_string(C["light"])
        t.left, t.top, t.width, t.height = Inches(0.8), Inches(2.3), Inches(11.7), Inches(1.4)
        body.left, body.top, body.width, body.height = Inches(0.8), Inches(3.9), Inches(11.7), Inches(1.4)
        body.text = "\n".join(bullets)
        for p in body.text_frame.paragraphs:
            for r in p.runs: r.font.size = PPt(20); r.font.color.rgb = PRGB.from_string(C["grey"])
    else:
        t.left, t.top, t.width, t.height = Inches(0.6), Inches(0.35), Inches(12.1), Inches(1.0)
        body.left, body.top, body.width, body.height = Inches(0.6), Inches(1.6), Inches(12.1 if bullets is not None else 5.6), Inches(5.0)
        t.text_frame.paragraphs[0].alignment = PP_ALIGN.LEFT
        tf = body.text_frame; tf.clear()
        for i, b in enumerate(bullets or []):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.text = b
            for r in p.runs: r.font.size = PPt(20)
    for r in t.text_frame.paragraphs[0].runs: r.font.color.rgb = PRGB.from_string(C["green"]); r.font.size = PPt(30 if not first else 36)
    if notes: s.notes_slide.notes_text_frame.text = notes
    return s


def plantilla(path):
    prs = base()
    slide(prs, "Título de la presentación", ["Fecha · Área"], "", True)
    slide(prs, "Título de la diapositiva", ["Mensaje principal en una línea", "Dato que lo respalda (con fuente en la hoja Hechos)", "Qué decidimos o qué sigue"], "Las notas del orador van aquí.")
    prs.save(path)


def deck_slides():
    return [
        ("Revisión trimestral · 3T 2026", ["Centro de Servicio Interno · jueves 19 de noviembre de 2026", "Zava Bebidas (ficticia)"], "Presentar el objetivo: resultados del trimestre y tres acciones."),
        ("Resumen del trimestre", [f"Atendimos {T['ate']} solicitudes: el {T['pct_ate']} de las recibidas", f"Tiempo de respuesta {T['tiempo']}: dentro de la meta de {T['meta_t']}",
                                   f"Satisfacción {T['sat']}: abajo de la meta de {T['meta_s']}", f"Presupuesto ejercido: {T['pres']} del asignado"],
         "Datos limpios: sin el renglón duplicado de Golfo y sin el valor atípico de Península. Falta Centro de agosto (Sistemas lo revisa)."),
        ("Tiempo de respuesta por región", None, f"Golfo ({T['golfo_t']}) es la única región arriba de la meta, por las dos vacantes desde julio."),
        ("Lo que dicen los usuarios", [f"{T['com']} comentarios en la encuesta del trimestre", f"Tema principal: tiempo de respuesta ({T['t1']} comentarios, {T['t1p']}), calificación promedio {T['t1c']}",
                                       "Lo mejor valorado: el trato del personal", "Pedido recurrente: saber en qué estatus está la solicitud"],
         "Los comentarios son anónimos y se quitaron los nombres del equipo que aparecían en dos de ellos."),
        ("Tres acciones para el 4T", ["Cubrir las dos vacantes de Golfo en noviembre", "Avisos automáticos de estatus en el portal", "Extender el portal a Centro en enero de 2027"],
         "Pedir a la dirección apoyo para acelerar las contrataciones de Golfo."),
    ]


def deck_ckpt(path):
    prs = base(); sl = deck_slides()
    for i, (t, b, n) in enumerate(sl):
        s = slide(prs, t, b, n, first=(i == 0))
        if b is None:
            cd = CategoryChartData(); cd.categories = Z.REG
            cd.add_series("Tiempo de respuesta 3T (h)", [round(K[f"tiempo_3T_{g}"], 1) for g in Z.REG])
            gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.8), Inches(1.6), Inches(8), Inches(5), cd); ch = gf.chart
            ch.has_legend = False; ch.plots[0].has_data_labels = True; ch.plots[0].data_labels.number_format = '0.0'; ch.plots[0].data_labels.number_format_is_linked = False
            ch.series[0].format.fill.solid(); ch.series[0].format.fill.fore_color.rgb = PRGB.from_string(C["green"])
            tb = s.shapes.add_textbox(Inches(9.1), Inches(2.2), Inches(3.8), Inches(3)); tf = tb.text_frame; tf.word_wrap = True
            for k, txt in enumerate([f"Meta: {T['meta_t']}", f"Total: {T['tiempo']}", f"Golfo: {T['golfo_t']}"]):
                p = tf.paragraphs[0] if k == 0 else tf.add_paragraph(); p.text = txt
                for r in p.runs: r.font.size = PPt(22); r.font.bold = (k == 2)
            for ph in list(s.placeholders):
                if ph.placeholder_format.idx == 1: ph._element.getparent().remove(ph._element)
    prs.save(path)


# ------------------------------------------------------------------ checkpoints Word
def reporte_lines():
    return [
        ("Resultados", [f"Atendimos {T['ate']} de {T['rec']} solicitudes recibidas ({T['pct_ate']}).", f"El tiempo de respuesta promedio fue de {T['tiempo']} (meta: {T['meta_t']}); en el 2T fue de {T['tiempo2']}.",
                        f"La satisfacción fue de {T['sat']} (meta: {T['meta_s']}); en el 2T, {T['sat2']}.", f"Ejercimos {T['pres_ej']} de {T['pres_as']} asignados ({T['pres']})."]),
        ("Lo que explica los resultados", [f"Golfo tuvo un tiempo de {T['golfo_t']} y satisfacción de {T['golfo_s']} por dos vacantes en la mesa de servicio desde julio.",
                                           f"En la encuesta, {T['t1']} de {T['com']} comentarios ({T['t1p']}) hablan del tiempo de respuesta; el trato del personal es lo mejor valorado."]),
        ("Calidad de los datos", [f"Se quitó un renglón duplicado (Golfo, septiembre) y se excluyó un tiempo atípico de {T['atip']} (Península, julio) que se debe confirmar.",
                                  "Faltan los datos de Centro de agosto; Sistemas lo revisa. Las cifras de volumen y presupuesto no incluyen ese mes."]),
        ("Acciones para el 4T", ["Cubrir las dos vacantes de Golfo en noviembre.", "Activar avisos de estatus en el portal.", "Extender el portal a Centro en enero de 2027."]),
    ]


def faq():
    return [("¿Cuánto tarda en resolverse mi solicitud?", "Depende de la prioridad: urgente, primera respuesta en 4 horas hábiles; alta, solución en 24; normal, en 48."),
            ("¿Puedo pedir apoyo por chat a alguien del equipo?", "No. Toda solicitud se registra en el portal o en la mesa de servicio para tener folio y responsable."),
            ("¿Qué pasa si mi solicitud se retrasa?", "Se escala al líder de la región; si supera el doble del tiempo objetivo, al líder del Centro de Servicio Interno."),
            ("¿Mi respuesta en la encuesta es anónima?", "Sí. La encuesta de cierre es anónima."),
            ("¿Hay excepciones a los tiempos?", "Sí: en cierres de mes y periodos vacacionales, con aviso de una semana de anticipación.")]


def reporte_ckpt(path):
    d = new_doc(); d.add_heading("CHECKPOINT · Reporte del 3T 2026 · Centro de Servicio Interno", 0)
    d.add_paragraph("Resultado del ejercicio 3. Fuente: hoja Hechos (CHECKPOINT_Ej2_Resultado_Excel.xlsx) y notas de reuniones.").italic = True
    for h, items in reporte_lines():
        d.add_heading(h, 2)
        for i in items: d.add_paragraph(i, style="List Bullet")
    d.add_page_break(); d.add_heading("Preguntas frecuentes del procedimiento de atención de solicitudes", 1)
    for q, a in faq():
        p = d.add_paragraph(); p.add_run(q).bold = True; d.add_paragraph(a)
    d.save(path)


def correos_ckpt(path):
    d = new_doc(); d.add_heading("CHECKPOINT · Resultado del ejercicio 5: correo, agenda, mensaje y revisión", 0)
    d.add_paragraph("Borradores de ejemplo: no se envían durante la práctica.").italic = True
    d.add_heading("Correo de seguimiento a la dirección", 2)
    d.add_paragraph("Asunto: Revisión trimestral del 3T · reporte y presentación")
    d.add_paragraph(f"Les comparto el reporte y la presentación del 3T. En resumen: atendimos {T['ate']} solicitudes ({T['pct_ate']}), con un tiempo de respuesta de {T['tiempo']}, dentro de la meta. La satisfacción quedó en {T['sat']}, abajo de la meta, por Golfo. Proponemos tres acciones para el 4T y les pedimos apoyo para acelerar las contrataciones de Golfo. ¿Podemos confirmarlo en la revisión del 19 de noviembre?")
    d.add_heading("Agenda de la revisión (30 minutos)", 2)
    for a in ["Resultados del trimestre (10 min)", "Golfo: causas y plan (10 min)", "Acciones para el 4T y decisiones (10 min)"]: d.add_paragraph(a, style="List Number")
    d.add_heading("Mensaje al equipo en Teams", 2)
    d.add_paragraph(f"¡Equipo! Cerramos el 3T con {T['ate']} solicitudes atendidas y un tiempo de respuesta de {T['tiempo']}, dentro de la meta. Lo más valorado por los usuarios es su trato. Nuestro reto: Golfo y avisar el estatus de cada solicitud. ¡Gracias por el esfuerzo!")
    d.add_heading("Revisión del borrador del colega", 2)
    t = d.add_table(rows=1, cols=3); t.style = "Light Grid Accent 1"
    for c, x in zip(t.rows[0].cells, ["Afirmación", "Veredicto", "Por qué"]): c.text = x
    for c in CLAIMS:
        r = t.add_row().cells; r[0].text, r[1].text, r[2].text = c
    d.save(path)


# ------------------------------------------------------------------ checkpoint Excel
def excel_ckpt(path):
    wb = load_workbook(os.path.join(F1, "Zava_Indicadores_Servicio_2026.xlsx"))
    ws = wb.create_sheet("Revision"); ws["A1"] = "Revisión de datos antes de analizar"; ws["A1"].font = TT
    hdr = ["Problema", "Dónde", "Qué se hizo", "Comprobación (fórmula)"]
    for j, h in enumerate(hdr, 1): c = ws.cell(3, j, h); c.font = HF; c.fill = HFILL
    n = len(RAW) + 1
    rows = [["Renglón duplicado", "Golfo · 2026-09", "Se quitó uno de los dos renglones en Datos_limpios", f'=SUMPRODUCT((Indicadores!$A$2:$A${n}="2026-09")*(Indicadores!$B$2:$B${n}="Golfo"))'],
            ["Valor atípico de tiempo de respuesta", f"Península · 2026-07 ({Z.OUT[2]} h)", "Se conserva y se excluye del promedio de tiempo; confirmar con el dueño del dato",
             f'=_xlfn.MAXIFS(Indicadores!$E$2:$E${n},Indicadores!$B$2:$B${n},"Península")'],
            ["Mes faltante", "Centro · 2026-08", "Se reporta sin ese mes y se avisa en el reporte", f'=SUMPRODUCT((Indicadores!$A$2:$A${n}="2026-08")*(Indicadores!$B$2:$B${n}="Centro"))']]
    for i, r in enumerate(rows, 4):
        for j, v in enumerate(r, 1): ws.cell(i, j, v)
    for j, w in enumerate([36, 30, 60, 22], 1): ws.column_dimensions[get_column_letter(j)].width = w
    ws = wb.create_sheet("Datos_limpios")
    cols = COLS + ["Excluir_del_tiempo", "Trimestre"]
    data = [[r[c] for c in COLS] + ["Sí" if (r["Region"], r["Mes"]) == Z.OUT[:2] else "No", "3T" if r["Mes"] in Z.T3 else ("2T" if r["Mes"] in Z.T2 else "1T")] for r in CLEAN]
    for r in data:
        if r[1] == Z.OUT[0] and r[0] == Z.OUT[1]: r[4] = Z.OUT[2]
    table(ws, "tblLimpios", cols, data, FMT + [None, None], widths=[10, 12, 14, 14, 14, 14, 14, 16, 16, 12, 10])
    m = len(data) + 1
    D = lambda col: f"Datos_limpios!${col}$2:${col}${m}"
    ws = wb.create_sheet("Resumen_3T"); ws["A1"] = "Resumen del 3T 2026 por región (datos limpios, fórmulas)"; ws["A1"].font = TT
    h = ["Región", "Recibidas", "Atendidas", "% atendidas", "Tiempo de respuesta (h, ponderado)", "Satisfacción (ponderada)", "Presupuesto asignado", "Presupuesto ejercido", "% ejercido"]
    for j, x in enumerate(h, 1): c = ws.cell(3, j, x); c.font = HF; c.fill = HFILL; c.alignment = Alignment(wrap_text=True)
    T3 = f'{D("K")},"3T"'
    for i, g in enumerate(Z.REG + ["Total"], 4):
        ws.cell(i, 1, g)
        crit = T3 + (f',{D("B")},$A{i}' if g != "Total" else "")
        ws.cell(i, 2, f"=SUMIFS({D('C')},{crit})"); ws.cell(i, 3, f"=SUMIFS({D('D')},{crit})"); ws.cell(i, 4, f"=C{i}/B{i}")
        ws.cell(i, 5, f'=SUMPRODUCT(({D("K")}="3T")*({D("J")}="No")' + (f'*({D("B")}=$A{i})' if g != "Total" else "") + f'*{D("E")}*{D("D")})/SUMIFS({D("D")},{crit},{D("J")},"No")')
        ws.cell(i, 6, f'=SUMPRODUCT(({D("K")}="3T")' + (f'*({D("B")}=$A{i})' if g != "Total" else "") + f'*{D("F")}*{D("G")})/SUMIFS({D("G")},{crit})')
        ws.cell(i, 7, f"=SUMIFS({D('H')},{crit})"); ws.cell(i, 8, f"=SUMIFS({D('I')},{crit})"); ws.cell(i, 9, f"=H{i}/G{i}")
        for j, f in ((2, N0), (3, N0), (4, PCT), (5, N1), (6, N2), (7, N0), (8, N0), (9, PCT)): ws.cell(i, j).number_format = f
    for j in range(1, 10): ws.cell(8, j).font = B
    for j, w in enumerate([12, 12, 12, 12, 18, 16, 16, 16, 12], 1): ws.column_dimensions[get_column_letter(j)].width = w
    ws.cell(10, 1, "2T (abril a junio), para comparar").font = B
    T2 = f'{D("K")},"2T"'
    ws.cell(11, 1, "Tiempo 2T"); ws.cell(11, 5, f'=SUMPRODUCT(({D("K")}="2T")*{D("E")}*{D("D")})/SUMIFS({D("D")},{T2})').number_format = N1
    ws.cell(12, 1, "Satisfacción 2T"); ws.cell(12, 6, f'=SUMPRODUCT(({D("K")}="2T")*{D("F")}*{D("G")})/SUMIFS({D("G")},{T2})').number_format = N2
    ws.cell(13, 1, "Sin limpiar (Indicadores, 3T)").font = B
    n_ = len(RAW) + 1; I = lambda col: f"Indicadores!${col}$2:${col}${n_}"
    ws.cell(14, 1, "Atendidas sin limpiar"); ws.cell(14, 3, f'=SUMPRODUCT(ISNUMBER(MATCH({I("A")},{{"2026-07","2026-08","2026-09"}},0))*{I("D")})').number_format = N0
    ws.cell(15, 1, "Tiempo sin limpiar"); ws.cell(15, 5, f'=SUMPRODUCT(ISNUMBER(MATCH({I("A")},{{"2026-07","2026-08","2026-09"}},0))*{I("E")}*{I("D")})/C14').number_format = N1
    ch = BarChart(); ch.type = "col"; ch.title = "Tiempo de respuesta 3T por región (h)"; ch.y_axis.title = "Horas"
    ch.add_data(Reference(ws, min_col=5, min_row=3, max_row=7), titles_from_data=True); ch.set_categories(Reference(ws, min_col=1, min_row=4, max_row=7))
    ch.height, ch.width = 8, 16; ws.add_chart(ch, "K3")
    # comentarios con tema
    ws = wb.create_sheet("Comentarios_temas")
    table(ws, "tblTemas", ["ID", "Region", "Mes", "Calificacion_1a5", "Comentario", "Tema", "Menciona_a_una_persona"],
          [[c["ID"], c["Region"], c["Mes"], c["Calificacion_1a5"], c["Comentario"], c["_tema"], "Sí" if c["_nombre"] else "No"] for c in COM],
          [None, None, None, N0, None, None, None], widths=[8, 12, 10, 12, 70, 26, 14])
    q = len(COM) + 1
    ws.cell(1, 9, "Tema").font = B; ws.cell(1, 10, "Comentarios").font = B; ws.cell(1, 11, "% del total").font = B; ws.cell(1, 12, "Calificación promedio").font = B
    for i, (tema, *_ ) in enumerate(Z.THEMES, 2):
        ws.cell(i, 9, tema); ws.cell(i, 10, f'=COUNTIF($F$2:$F${q},I{i})'); ws.cell(i, 11, f"=J{i}/COUNTA($A$2:$A${q})").number_format = PCT
        ws.cell(i, 12, f'=AVERAGEIF($F$2:$F${q},I{i},$D$2:$D${q})').number_format = N1
    ws.cell(8, 9, "Comentarios que mencionan a una persona"); ws.cell(8, 10, f'=COUNTIF($G$2:$G${q},"Sí")')
    for c_, w in (("I", 34), ("J", 12), ("K", 12), ("L", 18)): ws.column_dimensions[c_].width = w
    # Hechos
    ws = wb.create_sheet("Hechos"); ws["A1"] = "Hechos del 3T 2026 · cada cifra con su fuente"; ws["A1"].font = TT
    ws["A2"] = "Regla: nada entra al reporte ni a la presentación si no está en esta hoja."
    for j, x in enumerate(["#", "Hecho", "Cifra", "Unidad", "Fuente", "Revisado por"], 1): c = ws.cell(4, j, x); c.font = HF; c.fill = HFILL
    H = [("Solicitudes recibidas 3T (sin Centro agosto)", "=Resumen_3T!B8", "solicitudes", "Resumen_3T, fila Total", N0),
         ("Solicitudes atendidas 3T", "=Resumen_3T!C8", "solicitudes", "Resumen_3T, fila Total", N0),
         ("% de solicitudes atendidas", "=Resumen_3T!D8", "%", "Resumen_3T, fila Total", PCT),
         ("Tiempo de respuesta promedio 3T (ponderado, sin atípico)", "=Resumen_3T!E8", "horas", "Resumen_3T, fila Total", N1),
         ("Tiempo de respuesta promedio 2T", "=Resumen_3T!E11", "horas", "Resumen_3T, Tiempo 2T", N1),
         ("Tiempo de respuesta Golfo 3T", "=Resumen_3T!E6", "horas", "Resumen_3T, fila Golfo", N1),
         ("Satisfacción promedio 3T (ponderada)", "=Resumen_3T!F8", "1 a 5", "Resumen_3T, fila Total", N2),
         ("Satisfacción promedio 2T", "=Resumen_3T!F12", "1 a 5", "Resumen_3T, Satisfacción 2T", N2),
         ("Satisfacción Golfo 3T", "=Resumen_3T!F6", "1 a 5", "Resumen_3T, fila Golfo", N2),
         ("Presupuesto ejercido 3T", "=Resumen_3T!H8", "MXN", "Resumen_3T, fila Total", N0),
         ("Presupuesto asignado 3T", "=Resumen_3T!G8", "MXN", "Resumen_3T, fila Total", N0),
         ("% del presupuesto ejercido", "=Resumen_3T!I8", "%", "Resumen_3T, fila Total", PCT),
         ("Comentarios de la encuesta", f"=COUNTA(Comentarios_temas!A2:A{q})", "comentarios", "Comentarios_temas", N0),
         ("Comentarios sobre tiempo de respuesta", "=Comentarios_temas!J2", "comentarios", "Comentarios_temas, tabla de temas", N0),
         ("Tiempo sin limpiar (con duplicado y atípico)", "=Resumen_3T!E15", "horas", "Resumen_3T, Sin limpiar · solo para mostrar el efecto", N1)]
    for i, (h, f, u, s, nf) in enumerate(H, 5):
        ws.cell(i, 1, i - 4); ws.cell(i, 2, h); c = ws.cell(i, 3, f); c.number_format = nf; ws.cell(i, 4, u); ws.cell(i, 5, s)
    for j, w in enumerate([4, 56, 16, 12, 48, 14], 1): ws.column_dimensions[get_column_letter(j)].width = w
    wb.save(path)


if __name__ == "__main__":
    indicadores(os.path.join(F1, "Zava_Indicadores_Servicio_2026.xlsx"))
    encuesta(os.path.join(F1, "Zava_Encuesta_Servicio_3T2026.xlsx"))
    notas(os.path.join(F1, "Zava_Notas_y_Politicas_Servicio.docx"))
    plantilla(os.path.join(F1, "Zava_Plantilla_Revision.pptx"))
    excel_ckpt(os.path.join(F2, "CHECKPOINT_Ej2_Resultado_Excel.xlsx"))
    reporte_ckpt(os.path.join(F2, "CHECKPOINT_Ej3_Resultado_Reporte.docx"))
    deck_ckpt(os.path.join(F2, "CHECKPOINT_Ej4_Resultado_Presentacion.pptx"))
    correos_ckpt(os.path.join(F2, "CHECKPOINT_Ej5_Resultado_Correos.docx"))
    json.dump({k: v for k, v in K.items() if isinstance(v, (int, float))}, open(os.path.join(ROOT, "_build", "answer_key.json"), "w"), indent=1)
    print("ok")
