# -*- coding: utf-8 -*-
"""Genera los archivos de práctica, skills, conocimiento y archivos de Copilot Studio."""
import os, csv, zipfile, io
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from zcontent import *

ROOT = r"C:\Users\erikmontes\ZavaBuild\Bepensa_Agentes_Lab_v1"
F = lambda *p: os.path.join(ROOT, "files", *p)
GREEN = RGBColor(0x0F, 0x5F, 0x4A)


def doc(title, lines, path, note="Documento de práctica. Empresa, procedimientos y cifras son ficticios."):
    d = Document(); st = d.styles["Normal"]; st.font.name = "Segoe UI"; st.font.size = Pt(11)
    for s in ("Heading 1", "Title"): d.styles[s].font.name = "Segoe UI"; d.styles[s].font.color.rgb = GREEN
    for sec in d.sections: sec.left_margin = sec.right_margin = Cm(2.2)
    d.add_heading(f"Zava Bebidas · {title}", 1)
    p = d.add_paragraph(note); p.runs[0].italic = True
    for l in lines: d.add_paragraph(l)
    d.core_properties.author = "Zava Bebidas (ficticio)"; d.core_properties.last_modified_by = "Zava Bebidas (ficticio)"; d.core_properties.title = title
    d.save(path)


def skill_zip(name, text):
    path = F("2_Skills", f"{name}.zip")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("SKILL.md", text.encode("utf-8"))
    io.open(F("2_Skills", f"{name}_SKILL.md"), "w", encoding="utf-8", newline="\n").write(text)
    return path


def main():
    for p in PRUEBAS: doc(p["titulo"], p["texto"], F("1_Textos_de_practica", p["archivo"]))
    for fn, t, lines in CONOCIMIENTO: doc(t, lines, F("3_Conocimiento_SharePoint", fn), "Procedimiento ficticio para la carpeta de conocimiento de SharePoint del agente.")
    skill_zip("formato-estandar-poe", SKILL_POE); skill_zip("formato-estandar-escalamiento", SKILL_ESC)
    io.open(F("2_Skills", "Instrucciones_Asistente_Estandares.txt"), "w", encoding="utf-8").write(INSTRUCCIONES_A1)
    with open(F("4_Copilot_Studio", "Lista_Solicitudes_de_Personal_esquema.csv"), "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f); w.writerow(["Columna", "Tipo", "Obligatoria", "Valores o nota"]); w.writerows(ESQUEMA)
    for c in CORREOS:
        txt = f"De: {c['rol']} <{c['de']}>\nPara: Solicitudes de personal <solicitudes.personal@zavabebidas.example>\nFecha: {c['fecha']}\nAsunto: {c['asunto']}\n\n" + "\n".join(c["cuerpo"]) + "\n\n(Correo ficticio de práctica.)\n"
        io.open(F("4_Copilot_Studio", c["archivo"]), "w", encoding="utf-8").write(txt)
    io.open(F("4_Copilot_Studio", "Instrucciones_Agente_Solicitudes_de_Personal.txt"), "w", encoding="utf-8").write(INSTRUCCIONES_A2)
    zp = F("Zava_Agentes_Archivos.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for sub in ("1_Textos_de_practica", "2_Skills", "3_Conocimiento_SharePoint", "4_Copilot_Studio"):
            for n in sorted(os.listdir(F(sub))): z.write(F(sub, n), f"Zava_Agentes/{sub}/{n}")
    print("ok", len(SKILL_POE), len(SKILL_ESC), len(INSTRUCCIONES_A1), len(INSTRUCCIONES_A2), len(PROMPT_ES))


if __name__ == "__main__":
    main()
