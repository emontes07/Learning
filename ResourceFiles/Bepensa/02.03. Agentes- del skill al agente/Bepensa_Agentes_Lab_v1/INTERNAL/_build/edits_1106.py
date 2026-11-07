# -*- coding: utf-8 -*-
"""Ajustes del 6 de noviembre: caso Andi (Learn), skills recién disponibles y preparación del Agente 2."""
import io

LEARN = "https://learn.microsoft.com/es-es/power-platform/guidance/case-studies/coca-cola-andina-hr-support"
NUEVO = "recién disponibles; puede que todavía no aparezcan en tu organización"


def rep(path, pairs):
    s = io.open(path, encoding="utf-8").read()
    for a, b in pairs:
        if a not in s: raise SystemExit(f"NO ENCONTRADO en {path}: {a[:80]}")
        s = s.replace(a, b)
    io.open(path, "w", encoding="utf-8").write(s)


rep("build_guide.py", [
    ("En Agent Builder un agente puede tener hasta 8 skills; las skills personalizadas están en versión preliminar.",
     f"En Agent Builder un agente puede tener hasta 8 skills; las skills están {NUEVO}."),
    ("Requiere licencia de Microsoft 365 Copilot o pago por uso. Las skills personalizadas están en versión preliminar.",
     f"Requiere licencia de Microsoft 365 Copilot o pago por uso. Las skills están {NUEVO}."),
    ("Licencia de Microsoft 365 Copilot o pago por uso; hasta 8 por agente; en versión preliminar. Si la organización usa barreras de información",
     f"Licencia de Microsoft 365 Copilot o pago por uso; hasta 8 por agente; {NUEVO}. Si la organización usa barreras de información"),
    ('            "<li><b>Cómo funciona:</b> personaliza la respuesta con Microsoft Entra ID, busca la respuesta en un repositorio de conocimiento en SharePoint y, si el colaborador necesita hablar con RH, escala con un flujo de Power Automate a un CRM en Power Apps. Se publicó en WhatsApp.</li>"\n'
     '            "<li><b>Resultados que reporta la historia:</b> se probó en cuatro regiones de Argentina y hoy lo usan de forma activa más de 300 colaboradores; el equipo de RH dedica mucho menos tiempo a responder preguntas básicas y repetitivas.</li>"',
     '            "<li><b>Cómo funciona:</b> los colaboradores le escriben por WhatsApp; Microsoft Entra ID autentica y aporta los datos del perfil; el contenido de RH vive en SharePoint; y si Andi no puede resolver, crea un ticket a RH con Power Automate, que RH atiende en Power Apps.</li>"\n'
     '            "<li><b>Resultados:</b> 1,200 de aproximadamente 3,600 empleados activos en Argentina lo usan cada mes; casi 5,000 conversaciones, con una duración promedio de 6 min 33 s; satisfacción (CSAT) de 4.1 de 5, con 976 encuestas. Una parte importante de las preguntas llega fuera del horario de RH, cuando antes había que esperar al día siguiente.</li>"'),
    ("<p class=\"small muted\">Fuentes: historia de cliente de Microsoft «Coca-Cola Andina» (microsoft.com/customers) y Microsoft News Center Latinoamérica. La historia no publica porcentajes de resolución ni tiempo ahorrado.</p>",
     "<p class=\"small muted\">Fuentes: caso de estudio de Microsoft Learn «Coca-Cola Andina mejora el soporte de RR. HH. para el personal de primera línea con Copilot Studio» (8 de septiembre de 2026), historia de cliente de Microsoft y Microsoft News Center Latinoamérica.</p>"),
    ('        ("Historia de cliente: Coca-Cola Andina", "https://www.microsoft.com/en/customers/story/26256-coca-cola-andina-microsoft-copilot-studio")]',
     f'        ("Caso de estudio en Microsoft Learn: Coca-Cola Andina", "{LEARN}"),\n        ("Historia de cliente: Coca-Cola Andina", "https://www.microsoft.com/en/customers/story/26256-coca-cola-andina-microsoft-copilot-studio")]'),
])

rep("gen_internal.py", [
    ("Si no hay opción de skills: pegar el SKILL.md en las instrucciones y explicar que es preliminar.",
     "Si no hay opción de skills: pegar el SKILL.md en las instrucciones y explicar que las skills están recién disponibles y puede que todavía no aparezcan en la organización."),
    ('"Contar la historia con las cifras verificadas: más de 300 usuarios activos, 4 regiones de Argentina, WhatsApp.", "No mencionar porcentajes: la historia no los publica."',
     '"Contar el caso con las cifras de Microsoft Learn: 1,200 de ~3,600 empleados activos en Argentina al mes, casi 5,000 conversaciones (6 min 33 s en promedio), CSAT 4.1 de 5 con 976 encuestas, muchas preguntas fuera del horario de RH. WhatsApp, Entra ID, SharePoint y ticket a RH.", "Fuente: caso de estudio de Microsoft Learn del 8 de septiembre de 2026."'),
    ("<li>Andi: solo cifras de la historia (más de 300 usuarios activos, 4 regiones de Argentina, WhatsApp) y de la nota de Microsoft Latinoamérica (más de 16,000 colaboradores). No hay porcentajes publicados.</li>",
     f"<li>Andi: usar las cifras del caso de estudio de Microsoft Learn (8 de septiembre de 2026): 1,200 de aproximadamente 3,600 empleados activos en Argentina lo usan cada mes; casi 5,000 conversaciones con duración promedio de 6 min 33 s; CSAT de 4.1 de 5 con 976 encuestas; una parte importante de las preguntas llega fuera del horario de RH. Contexto: más de 16,000 colaboradores (nota de Microsoft Latinoamérica).</li>"),
    ('("Andi: usuarios activos", "más de 300", L4), ("Andi: regiones de prueba en Argentina", "4", L4)]',
     '("Andi: usuarios al mes", "1,200 de ~3,600 empleados activos en Argentina", L5), ("Andi: conversaciones", "casi 5,000; duración promedio 6 min 33 s", L5), ("Andi: CSAT", "4.1 de 5 (976 encuestas)", L5)]'),
    ('L1, L2, L3, L4 = (', f'L5 = "{LEARN}"\nL1, L2, L3, L4 = ('),
    ("requieren licencia de Microsoft 365 Copilot o pago por uso; en versión preliminar.",
     f"requieren licencia de Microsoft 365 Copilot o pago por uso; {NUEVO}."),
    ('"Caso real: «Andi», agente de RH de Coca-Cola Andina en Copilot Studio; lo usan de forma activa más de 300 colaboradores (historia de cliente de Microsoft)."',
     '"Caso real: «Andi», agente de RH de Coca-Cola Andina en Copilot Studio, por WhatsApp: 1,200 de ~3,600 empleados activos en Argentina lo usan cada mes; CSAT de 4.1 de 5 (caso de estudio de Microsoft Learn, septiembre de 2026)."'),
    ("<li>Lista «{LISTA}» con el esquema del CSV; buzón de prueba con los 3 correos; usuarios de demo para Search for users.</li>",
     "<li>Lista «{LISTA}» con el esquema del CSV; usuarios de demo para Search for users.</li>\n"
     "<li><b>Buzón de prueba y fechas de los correos:</b> el <b>Correo 2 (urgente) debe llegar el lunes 9 de noviembre</b>: dice «desde mañana», inicia el 10 y la regla de urgencia es inicio a menos de 72 horas de la fecha del correo. Si se envía otro día, ajustar las fechas del correo (inicio al día siguiente del envío). El <b>Correo 1 y el Correo 3 pueden enviarse antes</b>.</li>\n"
     "<li><b>Copilot Credits:</b> construir, probar y evaluar el agente consume Copilot Credits. Conviene construirlo una sola vez y probarlo lo justo (una corrida por correo en el ensayo).</li>"),
])

rep("verify.py", [
    ("('Coca-Cola Andina: % de resolución o tiempo ahorrado', 'No publicado en la historia: no se usa', 'https://www.microsoft.com/en/customers/story/26256-coca-cola-andina-microsoft-copilot-studio')]",
     f"('Skills en Agent Builder: estado', 'Sin marca de versión preliminar ni Frontier (página actualizada el 6 de noviembre de 2026); se conserva la nota de barreras de información', 'https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills')]"),
    ('"Duarte", "Rocio", "Rocío",', '"Duarte", "Rocio", "Rocío", "Ricardo", "Colla", "Valderrama",'),
])
print("ok")
