# -*- coding: utf-8 -*-
"""Zava Bebidas · Centro de Servicio Interno. Base única de datos ficticios y libro de respuestas maestro."""
import random, math

REG = ["Norte", "Centro", "Golfo", "Península"]
MESES = [f"2026-{m:02d}" for m in range(1, 10)]
T2, T3 = ["2026-04", "2026-05", "2026-06"], ["2026-07", "2026-08", "2026-09"]
META_TIEMPO, META_SAT = 24.0, 4.20
DUP = ("Golfo", "2026-09")
OUT = ("Península", "2026-07", 412.0)
MISS = ("Centro", "2026-08")
BASE = {"Norte": 410, "Centro": 620, "Golfo": 350, "Península": 380}
TIEMPO = {"Norte": 21.0, "Centro": 22.5, "Golfo": 29.0, "Península": 19.5}
SAT = {"Norte": 4.30, "Centro": 4.25, "Golfo": 3.95, "Península": 4.35}
PRES = {"Norte": 380_000, "Centro": 520_000, "Golfo": 310_000, "Península": 340_000}
SEAS = [0.92, 0.95, 1.00, 1.02, 1.04, 1.03, 1.06, 1.08, 1.05]


def xround(x, d=0):
    f = 10 ** d
    return math.floor(x * f + 0.5) / f


def build_rows():
    rr = random.Random(1110)
    rows = []
    for i, m in enumerate(MESES):
        for r in REG:
            rec = int(xround(BASE[r] * SEAS[i] * (1 + 0.01 * i) * (1 + rr.uniform(-0.03, 0.03))))
            rate = rr.uniform(0.93, 0.975)
            ate = int(xround(rec * rate))
            t = TIEMPO[r] * (1 + rr.uniform(-0.06, 0.06))
            if r == "Golfo" and m in T3: t += 4.5          # Golfo empeora en 3T (vacantes)
            if r == "Norte" and m >= "2026-08": t -= 3.0     # Norte mejora desde agosto (piloto del portal)
            s = SAT[r] + rr.uniform(-0.06, 0.06)
            if r == "Golfo" and m in T3: s -= 0.12
            enc = int(xround(ate * rr.uniform(0.22, 0.28)))
            ej = int(xround(PRES[r] * rr.uniform(0.91, 1.01), -2))
            rows.append(dict(Mes=m, Region=r, Solicitudes_recibidas=rec, Solicitudes_atendidas=ate, Tiempo_respuesta_horas=xround(t, 1),
                             Satisfaccion_1a5=xround(s, 2), Encuestas_respondidas=enc, Presupuesto_asignado=PRES[r], Presupuesto_ejercido=ej))
    clean = [r for r in rows if (r["Region"], r["Mes"]) != MISS]
    raw = []
    for r in clean:
        rr_ = dict(r)
        if (r["Region"], r["Mes"]) == OUT[:2]: rr_["Tiempo_respuesta_horas"] = OUT[2]
        raw.append(rr_)
        if (r["Region"], r["Mes"]) == DUP: raw.append(dict(rr_))
    true_out = next(r["Tiempo_respuesta_horas"] for r in clean if (r["Region"], r["Mes"]) == OUT[:2])
    return raw, clean, true_out


THEMES = [  # tema, n, calificación base, comentarios (únicos)
    ("Tiempo de respuesta", 18, 2.4, ["Mi solicitud tardó más de una semana en resolverse.", "Tuve que esperar varios días para que alguien la revisara.", "Las solicitudes urgentes no se atienden como urgentes.",
     "El tiempo de respuesta es muy largo para trámites sencillos.", "Esperé tres días solo para que asignaran mi solicitud.", "En cierre de mes todo se retrasa muchísimo.",
     "Me resolvieron, pero mucho después de lo que necesitaba.", "Tardan demasiado en contestar en la región.", "La respuesta llegó cuando ya no la necesitaba.",
     "Un cambio de acceso no debería tomar cuatro días.", "Pedí un equipo nuevo y tardó casi dos semanas.", "Muy lento para algo que se resuelve en minutos.",
     "Desde julio los tiempos de atención empeoraron.", "Nos dijeron 24 horas y fueron 72.", "La atención es buena, pero la espera es demasiado larga.",
     "Para algo urgente tuve que esperar al día siguiente.", "Tardaron cinco días en reemplazar un mouse.", "Ojalá resolvieran más rápido las solicitudes sencillas."]),
    ("Seguimiento y comunicación", 14, 3.0, ["No sé en qué estatus está mi solicitud.", "Nadie me avisó que ya estaba resuelta.", "Me gustaría recibir actualizaciones del avance por correo.",
     "Tuve que llamar dos veces para saber qué pasaba.", "Cerraron mi solicitud sin explicarme qué hicieron.", "Falta comunicación cuando hay retrasos.",
     "No queda claro a quién escribir si algo se atora.", "Me avisaron del retraso hasta que pregunté.", "Nunca supe quién tenía mi solicitud.",
     "Me gustaría que me confirmaran cuando la reciben.", "Me pidieron la misma información dos veces y nadie explicó por qué.", "Cuando la escalaron no me dijeron a quién.",
     "No recibí respuesta a mi correo de seguimiento.", "Sería bueno un aviso cuando cambie de estatus."]),
    ("Trato del personal", 12, 4.6, ["El equipo siempre es amable y paciente.", "Me explicaron todo con mucha claridad.", "Excelente actitud de la mesa de servicio.",
     "Se nota que les interesa resolver.", "Muy buena disposición aunque estaban saturados.", "Me atendieron con respeto en la llamada.",
     "La persona que me ayudó fue muy profesional.", "Siempre contestan con cortesía.", "Me trataron muy bien aunque mi caso era complicado.", "Gracias por la paciencia para explicarme el proceso."]),
    ("Portal de solicitudes", 10, 3.4, ["El portal nuevo es más fácil de usar.", "No encuentro la categoría correcta en el portal.", "El formulario del portal pide demasiados datos.",
     "Desde el portal puedo ver el estatus, eso ayuda.", "El portal se cae a veces en la tarde.", "En el portal no puedo adjuntar archivos grandes.",
     "Me gusta poder levantar la solicitud desde el celular en el portal.", "El buscador del portal no encuentra nada.", "El portal me cerró la sesión a la mitad del formulario.", "Las categorías del portal son confusas."]),
    ("Otros", 6, 3.5, ["Sería útil un horario extendido los viernes.", "Propongo una sección de preguntas frecuentes.", "Todo bien en general.",
     "Podrían capacitar a los nuevos ingresos sobre cómo pedir apoyo.", "Me gustaría una encuesta más corta.", "Que haya alguien de guardia en vacaciones."]),
]
NAMED = ["Me atendió Mariana y resolvió todo en el momento, ¡gracias!", "Raúl de la mesa de servicio fue muy amable conmigo."]

def build_comments():
    rr = random.Random(77)
    out = []
    for tema, n, base, tpl in THEMES:
        for k in range(n):
            txt = tpl[k % len(tpl)]
            if tema == "Trato del personal" and k < 2: txt = NAMED[k]
            cal = max(1, min(5, int(xround(base + rr.uniform(-0.9, 0.9)))))
            out.append(dict(Region=rr.choice(REG), Mes=rr.choice(T3), Calificacion_1a5=cal, Comentario=txt, _tema=tema, _nombre=(tema == "Trato del personal" and k < 2)))
    rr.shuffle(out)
    for i, c in enumerate(out, 1): c["ID"] = f"C-{i:03d}"
    return out


def compute():
    raw, clean, true_out = build_rows()
    com = build_comments()
    K = {}
    q = lambda rows, ms: [r for r in rows if r["Mes"] in ms]
    c3, c2 = q(clean, T3), q(clean, T2)
    K["n_filas_raw"], K["n_filas_limpias"] = len(raw), len(clean)
    K["n_meses_region_3T"] = len(c3)
    for tag, rs in (("3T", c3), ("2T", c2)):
        K[f"rec_{tag}"] = sum(r["Solicitudes_recibidas"] for r in rs)
        K[f"ate_{tag}"] = sum(r["Solicitudes_atendidas"] for r in rs)
        K[f"pct_ate_{tag}"] = K[f"ate_{tag}"] / K[f"rec_{tag}"]
        tr = [r for r in rs if (r["Region"], r["Mes"]) != OUT[:2]]
        K[f"tiempo_{tag}"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in tr) / sum(r["Solicitudes_atendidas"] for r in tr)
        K[f"sat_{tag}"] = sum(r["Satisfaccion_1a5"] * r["Encuestas_respondidas"] for r in rs) / sum(r["Encuestas_respondidas"] for r in rs)
        K[f"pres_asig_{tag}"] = sum(r["Presupuesto_asignado"] for r in rs); K[f"pres_ej_{tag}"] = sum(r["Presupuesto_ejercido"] for r in rs)
        K[f"pres_pct_{tag}"] = K[f"pres_ej_{tag}"] / K[f"pres_asig_{tag}"]
        for g in REG:
            rg = [r for r in rs if r["Region"] == g]; tg = [r for r in rg if (r["Region"], r["Mes"]) != OUT[:2]]
            K[f"ate_{tag}_{g}"] = sum(r["Solicitudes_atendidas"] for r in rg)
            K[f"tiempo_{tag}_{g}"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in tg) / sum(r["Solicitudes_atendidas"] for r in tg)
            K[f"sat_{tag}_{g}"] = sum(r["Satisfaccion_1a5"] * r["Encuestas_respondidas"] for r in rg) / sum(r["Encuestas_respondidas"] for r in rg)
            K[f"pres_pct_{tag}_{g}"] = sum(r["Presupuesto_ejercido"] for r in rg) / sum(r["Presupuesto_asignado"] for r in rg)
    K["tiempo_delta"] = K["tiempo_3T"] - K["tiempo_2T"]; K["sat_delta"] = K["sat_3T"] - K["sat_2T"]
    K["peor_region"] = max(REG, key=lambda g: K[f"tiempo_3T_{g}"])
    K["regiones_bajo_meta_sat"] = [g for g in REG if K[f"sat_3T_{g}"] < META_SAT]
    # si no limpias
    r3 = q(raw, T3)
    K["ate_3T_sucio"] = sum(r["Solicitudes_atendidas"] for r in r3)
    K["tiempo_3T_sucio"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in r3) / sum(r["Solicitudes_atendidas"] for r in r3)
    c3o = [dict(r) for r in c3]
    for r in c3o:
        if (r["Region"], r["Mes"]) == OUT[:2]: r["Tiempo_respuesta_horas"] = OUT[2]
    K["tiempo_3T_solo_atipico"] = sum(r["Tiempo_respuesta_horas"] * r["Solicitudes_atendidas"] for r in c3o) / sum(r["Solicitudes_atendidas"] for r in c3o)
    dup = next(r for r in raw if (r["Region"], r["Mes"]) == DUP)
    K["dup_atendidas"] = dup["Solicitudes_atendidas"]; K["atipico"] = OUT[2]
    K["atipico_mediana_region"] = sorted(r["Tiempo_respuesta_horas"] for r in clean if r["Region"] == OUT[0] and (r["Region"], r["Mes"]) != OUT[:2])[4]
    # encuesta
    K["com_total"] = len(com)
    for tema, n, *_ in THEMES:
        cs = [c for c in com if c["_tema"] == tema]
        K[f"tema_n_{tema}"] = len(cs); K[f"tema_cal_{tema}"] = sum(c["Calificacion_1a5"] for c in cs) / len(cs)
    K["tema_pct_tiempo"] = K["tema_n_Tiempo de respuesta"] / K["com_total"]
    K["com_cal_prom"] = sum(c["Calificacion_1a5"] for c in com) / len(com)
    K["com_con_nombre"] = sum(1 for c in com if c["_nombre"])
    K["meta_tiempo"], K["meta_sat"] = META_TIEMPO, META_SAT
    K["tiempo_norte_jul"] = next(r["Tiempo_respuesta_horas"] for r in clean if r["Region"] == "Norte" and r["Mes"] == "2026-07")
    K["tiempo_norte_sep"] = next(r["Tiempo_respuesta_horas"] for r in clean if r["Region"] == "Norte" and r["Mes"] == "2026-09")
    return K, raw, clean, com


MINUS = "\u2212"
def sg(s): return s.replace("-", MINUS)
def num(x, d=0, sign=False): return sg(f"{x:+,.{d}f}" if sign else f"{x:,.{d}f}")
def pct(x, d=1, sign=False): return sg((f"{x*100:+.{d}f}" if sign else f"{x*100:.{d}f}") + " %")
def pesos(x): return sg(("-" if x < 0 else "") + f"${abs(x):,.0f}")
def mdp(x): return sg(("-" if x < 0 else "") + f"${abs(x)/1e6:,.1f} millones")
def hrs(x, sign=False): return sg((f"{x:+.1f}" if sign else f"{x:.1f}") + " h")


if __name__ == "__main__":
    K, raw, clean, com = compute()
    for k, v in K.items():
        print(k, f"{v:,.4f}" if isinstance(v, float) else v)
