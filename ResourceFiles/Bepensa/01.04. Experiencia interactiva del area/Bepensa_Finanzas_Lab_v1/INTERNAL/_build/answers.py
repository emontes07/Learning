"""Libro de respuestas maestro: calcula cada cifra del laboratorio a partir de zava_data."""
import json, os, datetime as dt
import zava_data as Z

MINUS = "\u2212"
import math
def xround(x): return int(math.floor(x + 0.5))

def sgn(s): return s.replace("-", MINUS)
def mdp(x, d=1, sign=False):
    s = f"{x/1e6:+,.{d}f}" if sign else f"{x/1e6:,.{d}f}"
    s = s.replace("+", "+$").replace("-", "-$") if sign else ("$" + s if x >= 0 else "-$" + s[1:])
    return sgn(s) + " millones"
def pesos(x, sign=False):
    s = f"{abs(x):,.2f}"
    pre = ("+" if x >= 0 else "-") if sign else ("" if x >= 0 else "-")
    return sgn(pre + "$" + s)
def num(x, d=0, sign=False):
    s = f"{x:+,.{d}f}" if sign else f"{x:,.{d}f}"
    return sgn(s)
def pct(x, d=1, sign=True):
    v = round(x * 100, d)
    s = f"{v:+.{d}f} %" if sign else f"{v:.{d}f} %"
    return sgn(s)
def pts(x, d=1): return sgn(f"{x*100:+.{d}f} pts")


def compute(D=None):
    D = D or Z.build_all()
    pl = D["pl"]
    K = {}
    def T(esc, k, c=None, ch=None):
        return sum(r[k] for r in pl if r["Escenario"] == esc and (c is None or r["CEDIS"] == c) and (ch is None or r["Canal"] == ch))
    # ---------- Ejercicio 1: caja ----------
    cash, proj = D["cash"], D["proj"]
    fin = {b: [r for r in cash if r["Banco"] == b][-1]["Saldo_final"] for b in Z.BANCOS}
    K["caja_ceiba"], K["caja_coral"], K["caja_jade"] = fin["Banco Ceiba"], fin["Banco Coral"], fin["Banco Jade"]
    K["caja_total"] = round(sum(fin.values()), 2)
    K["caja_minimos_total"] = sum(Z.MINIMO.values())
    K["caja_excedente_minimos"] = round(K["caja_total"] - K["caja_minimos_total"], 2)
    oct22 = next(r for r in cash if r["Banco"] == "Banco Ceiba" and r["Fecha"] == dt.date(2026, 10, 22))
    oct08 = next(r for r in cash if r["Banco"] == "Banco Ceiba" and r["Fecha"] == dt.date(2026, 10, 8))
    K["atipico_22oct_pagos"] = oct22["Pagos_proveedores"]; K["pago_pet_08oct"] = oct08["Pagos_proveedores"]
    coral = {r["Fecha"]: r["Saldo_final"] for r in proj if r["Banco"] == "Banco Coral"}
    K["coral_12nov"] = coral[dt.date(2026, 11, 12)]; K["coral_13nov"] = coral[dt.date(2026, 11, 13)]
    K["coral_faltante_12nov"] = round(Z.MINIMO["Banco Coral"] - K["coral_12nov"], 2)
    K["coral_traspaso_necesario"] = round(Z.MINIMO["Banco Coral"] - K["coral_13nov"], 2)
    K["pago_azucar_12nov"] = 41_200_000.0
    ceiba = {r["Fecha"]: r["Saldo_final"] for r in proj if r["Banco"] == "Banco Ceiba"}
    K["ceiba_11nov"] = ceiba[dt.date(2026, 11, 11)]
    k = Z.KPIS
    K["cobranza_oct_real"], K["cobranza_oct_meta"] = 641_846_000, 667_200_000
    K["cobranza_oct_cumpl"] = K["cobranza_oct_real"] / K["cobranza_oct_meta"]
    K["dso_moderno_jul"], K["dso_moderno_oct"] = k[0][5], k[3][5]
    K["dso_moderno_delta"] = round(K["dso_moderno_oct"] - K["dso_moderno_jul"], 1)
    K["dso_total_oct"] = k[3][3]
    # ---------- Ejercicio 2: conciliación ----------
    b, l = D["bank"], D["books"]
    K["conc_saldo_inicial"] = Z.SALDO_INICIAL_CEIBA
    K["conc_saldo_banco"] = round(Z.SALDO_INICIAL_CEIBA + sum(r[4] - r[3] for r in b), 2)
    K["conc_saldo_libros"] = round(Z.SALDO_INICIAL_CEIBA + sum(r[4] - r[3] for r in l), 2)
    K["conc_mov_banco"], K["conc_mov_libros"] = len(b), len(l)
    K["dep_transito"] = Z.DEP_TRANSITO["importe"]
    K["comision"], K["comision_iva"] = Z.COMISION["importe"], Z.COMISION["iva"]
    K["comision_total"] = Z.COMISION["importe"] + Z.COMISION["iva"]
    K["duplicado"] = Z.DUPLICADO["importe"]
    K["error_banco"], K["error_libros"] = Z.ERROR_CAPTURA["banco"], Z.ERROR_CAPTURA["libros"]
    K["error_dif"] = Z.ERROR_CAPTURA["banco"] - Z.ERROR_CAPTURA["libros"]
    K["conc_ajustado_banco"] = round(K["conc_saldo_banco"] + K["dep_transito"] + K["duplicado"], 2)
    K["conc_ajustado_libros"] = round(K["conc_saldo_libros"] + K["error_dif"] - K["comision_total"], 2)
    K["conc_diferencia_inicial"] = round(K["conc_saldo_libros"] - K["conc_saldo_banco"], 2)
    assert abs(K["conc_ajustado_banco"] - K["conc_ajustado_libros"]) < 0.005
    # ---------- Ejercicio 3: cierre ----------
    for e, tag in (("Real", "r"), ("Presupuesto", "p"), ("Año anterior", "a")):
        K[f"vol_{tag}"] = T(e, "Volumen_CU"); K[f"ventas_{tag}"] = T(e, "Ventas_netas")
        K[f"cv_{tag}"] = T(e, "Costo_ventas"); K[f"ub_{tag}"] = T(e, "Utilidad_bruta")
        K[f"mb_{tag}"] = K[f"ub_{tag}"] / K[f"ventas_{tag}"]
        K[f"precio_{tag}"] = K[f"ventas_{tag}"] / K[f"vol_{tag}"]
        for m, col in (("azucar", "Costo_azucar"), ("pet", "Costo_PET"), ("conc", "Costo_concentrado"), ("otros", "Otros_costos_produccion")):
            K[f"{m}_{tag}"] = T(e, col); K[f"{m}_cu_{tag}"] = K[f"{m}_{tag}"] / K[f"vol_{tag}"]
        K[f"dist_{tag}"] = sum(Z.DIST[e].values())
        K[f"corp_{tag}"] = sum(v[e] for v in Z.CORP.values())
        K[f"ebitda_{tag}"] = K[f"ub_{tag}"] - K[f"dist_{tag}"] - K[f"corp_{tag}"]
        for c in Z.CEDIS:
            K[f"vol_{tag}_{c}"] = T(e, "Volumen_CU", c); K[f"ventas_{tag}_{c}"] = T(e, "Ventas_netas", c)
            K[f"ub_{tag}_{c}"] = T(e, "Utilidad_bruta", c); K[f"dist_{tag}_{c}"] = Z.DIST[e][c]
        for ch in Z.CANALES:
            K[f"vol_{tag}_{ch}"] = T(e, "Volumen_CU", ch=ch); K[f"ventas_{tag}_{ch}"] = T(e, "Ventas_netas", ch=ch)
    K["ebitda_ajuste"] = -Z.COMISION["importe"]
    K["ebitda_r_aj"] = K["ebitda_r"] + K["ebitda_ajuste"]
    K["mb_r_aj"] = K["mb_r"]
    for x in ("vol", "ventas", "ub", "ebitda", "dist", "corp", "cv"):
        rr = K[f"{x}_r_aj"] if x == "ebitda" else K[f"{x}_r"]
        K[f"{x}_var_p"] = rr - K[f"{x}_p"]; K[f"{x}_varpct_p"] = rr / K[f"{x}_p"] - 1
        K[f"{x}_var_a"] = rr - K[f"{x}_a"]; K[f"{x}_varpct_a"] = rr / K[f"{x}_a"] - 1
    for c in Z.CEDIS:
        for x in ("vol", "ventas", "ub", "dist"):
            K[f"{x}_var_p_{c}"] = K[f"{x}_r_{c}"] - K[f"{x}_p_{c}"]; K[f"{x}_varpct_p_{c}"] = K[f"{x}_r_{c}"] / K[f"{x}_p_{c}"] - 1
            K[f"{x}_varpct_a_{c}"] = K[f"{x}_r_{c}"] / K[f"{x}_a_{c}"] - 1
    K["mb_var_p_pts"] = K["mb_r"] - K["mb_p"]; K["mb_var_a_pts"] = K["mb_r"] - K["mb_a"]
    K["precio_varpct_p"] = K["precio_r"] / K["precio_p"] - 1; K["precio_varpct_a"] = K["precio_r"] / K["precio_a"] - 1
    # puente de ventas
    cells = [(r["CEDIS"], r["Canal"]) for r in pl if r["Escenario"] == "Real"]
    get = {(r["Escenario"], r["CEDIS"], r["Canal"]): r for r in pl}
    pavg_p = K["ventas_p"] / K["vol_p"]
    at_pp = sum(get[("Real", c, ch)]["Volumen_CU"] * get[("Presupuesto", c, ch)]["Ventas_netas"] / get[("Presupuesto", c, ch)]["Volumen_CU"] for c, ch in cells)
    K["ef_volumen"] = (K["vol_r"] - K["vol_p"]) * pavg_p
    K["ef_mezcla"] = at_pp - K["vol_r"] * pavg_p
    K["ef_precio"] = K["ventas_r"] - at_pp
    assert abs(K["ef_volumen"] + K["ef_mezcla"] + K["ef_precio"] - K["ventas_var_p"]) < 0.01
    # puente de costos
    for m in ("azucar", "pet", "conc", "otros"):
        cp = K[f"{m}_p"] / K["vol_p"]
        K[f"cost_vol_{m}"] = (K["vol_r"] - K["vol_p"]) * cp
        K[f"cost_tarifa_{m}"] = K[f"{m}_r"] - K["vol_r"] * cp
        K[f"{m}_var_p"] = K[f"{m}_r"] - K[f"{m}_p"]
        K[f"{m}_cu_varpct_p"] = K[f"{m}_cu_r"] / K[f"{m}_cu_p"] - 1
    K["cost_vol_total"] = sum(K[f"cost_vol_{m}"] for m in ("azucar", "pet", "conc", "otros"))
    K["cost_tarifa_total"] = sum(K[f"cost_tarifa_{m}"] for m in ("azucar", "pet", "conc", "otros"))
    K["corp_mkt_var_p"] = Z.CORP["Mercadotecnia"]["Real"] - Z.CORP["Mercadotecnia"]["Presupuesto"]
    K["corp_adm_var_p"] = Z.CORP["Administración"]["Real"] - Z.CORP["Administración"]["Presupuesto"]
    K["comisiones_prelim"] = Z.CORP["Comisiones y servicios bancarios"]["Real"]
    K["comisiones_aj"] = K["comisiones_prelim"] + Z.COMISION["importe"]
    # ---------- Ejercicio 4: forecast ----------
    H = D["hist"]
    oc, om = Z.OUTLIER["cedis"], Z.OUTLIER["mes"]
    K["atipico_vol"] = H[(oc, om)]
    K["atipico_reemplazo"] = xround((H[(oc, "2026-06")] + H[(oc, "2026-08")]) / 2)
    K["atipico_exceso"] = K["atipico_vol"] - K["atipico_reemplazo"]
    adj = dict(H); adj[(oc, om)] = K["atipico_reemplazo"]
    price_oct = {c: K[f"ventas_r_{c}"] / K[f"vol_r_{c}"] for c in Z.CEDIS}
    price_pp = {c: K[f"ventas_p_{c}"] / K[f"vol_p_{c}"] for c in Z.CEDIS}
    ucr = K["azucar_cu_r"] + K["pet_cu_r"] + K["conc_cu_r"] + K["otros_cu_r"]
    K["costo_cu_r"] = ucr
    nd_vol = nd_ventas = ppto_nd_vol = ppto_nd_ventas = 0
    for c in Z.CEDIS:
        s26 = sum(adj[(c, f"2026-{m:02d}")] for m in range(1, 11)); s25 = sum(adj[(c, f"2025-{m:02d}")] for m in range(1, 11))
        g = s26 / s25 - 1; K[f"fc_g_{c}"] = g
        graw = sum(H[(c, f"2026-{m:02d}")] for m in range(1, 11)) / s25 - 1; K[f"fc_graw_{c}"] = graw
        for m in (11, 12):
            v = xround(H[(c, f"2025-{m:02d}")] * (1 + g)); K[f"fc_vol_{c}_{m}"] = v
            pv = round(H[(c, f"2025-{m:02d}")] * (1 + Z.PPTO_GROWTH_NOVDIC)); K[f"pp_vol_{c}_{m}"] = pv
            nd_vol += v; nd_ventas += v * price_oct[c]; ppto_nd_vol += pv; ppto_nd_ventas += round(pv * price_pp[c])
            K[f"pp_ventas_{c}_{m}"] = round(pv * price_pp[c])
        K[f"precio_oct_{c}"] = price_oct[c]
    K["fc_nd_vol"], K["fc_nd_ventas"] = nd_vol, nd_ventas
    K["fc_nd_ub"] = nd_ventas - nd_vol * ucr
    K["fc_q4_vol"] = K["vol_r"] + nd_vol
    K["fc_q4_ventas"] = K["ventas_r"] + nd_ventas
    K["fc_q4_ub"] = K["ub_r"] + K["fc_nd_ub"]
    K["pp_q4_vol"] = K["vol_p"] + ppto_nd_vol
    K["pp_q4_ventas"] = K["ventas_p"] + ppto_nd_ventas
    K["fc_q4_vol_vs_pp"] = K["fc_q4_vol"] / K["pp_q4_vol"] - 1
    K["fc_q4_ventas_vs_pp"] = K["fc_q4_ventas"] / K["pp_q4_ventas"] - 1
    K["fc_g_total_raw"] = sum(H[(c, f"2026-{m:02d}")] for c in Z.CEDIS for m in range(1, 11)) / sum(H[(c, f"2025-{m:02d}")] for c in Z.CEDIS for m in range(1, 11)) - 1
    K["fc_g_total_adj"] = sum(adj[(c, f"2026-{m:02d}")] for c in Z.CEDIS for m in range(1, 11)) / sum(adj[(c, f"2025-{m:02d}")] for c in Z.CEDIS for m in range(1, 11)) - 1
    u = Z.UC["Real"]
    K["esc_azucar_cu"] = u["azucar"] * Z.ESC_AZUCAR
    K["esc_azucar"] = -nd_vol * K["esc_azucar_cu"]
    K["esc_tc_conc_cu"] = u["conc_usd"] * Z.TC_SHOCK
    K["esc_tc_pet_cu"] = u["pet"] * Z.PET_USD_SHARE * (Z.TC_SHOCK / u["tc"])
    K["esc_tc"] = -nd_vol * (K["esc_tc_conc_cu"] + K["esc_tc_pet_cu"])
    K["esc_comb"] = K["esc_azucar"] + K["esc_tc"]
    K["esc_ub_base"] = K["fc_nd_ub"]; K["esc_ub_comb"] = K["fc_nd_ub"] + K["esc_comb"]
    K["esc_comb_pct_ub"] = K["esc_comb"] / K["fc_nd_ub"]
    K["tc_real"], K["tc_esc"] = u["tc"], u["tc"] + Z.TC_SHOCK
    return K


if __name__ == "__main__":
    K = compute()
    for k, v in K.items():
        if not any(s in k for s in ("_Norte", "_Centro", "_Golfo", "_Península", "_Tradicional", "_Moderno", "_Consumo")):
            print(f"{k:28s} {v:,.4f}" if isinstance(v, float) else f"{k:28s} {v:,}")
