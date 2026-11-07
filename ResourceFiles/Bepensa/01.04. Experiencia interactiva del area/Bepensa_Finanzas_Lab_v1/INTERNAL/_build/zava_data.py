"""Zava Bebidas: una sola base de datos ficticia para todo el laboratorio.
Todo archivo, checkpoint, respuesta y cifra del HTML sale de aquí."""
import random, datetime as dt

R = random.Random(20261109)
CEDIS = ["Norte", "Centro", "Golfo", "Península"]
CANALES = ["Tradicional", "Moderno", "Consumo en sitio"]
ESC = ["Real", "Presupuesto", "Año anterior"]
BANCOS = ["Banco Ceiba", "Banco Coral", "Banco Jade"]

# ---------------- Estado de resultados, octubre 2026 ----------------
VOL_PPTO = {
    ("Norte", "Tradicional"): 820000, ("Norte", "Moderno"): 410000, ("Norte", "Consumo en sitio"): 150000,
    ("Centro", "Tradicional"): 1050000, ("Centro", "Moderno"): 520000, ("Centro", "Consumo en sitio"): 210000,
    ("Golfo", "Tradicional"): 690000, ("Golfo", "Moderno"): 300000, ("Golfo", "Consumo en sitio"): 160000,
    ("Península", "Tradicional"): 760000, ("Península", "Moderno"): 380000, ("Península", "Consumo en sitio"): 230000,
}
VOL_REAL = {
    ("Norte", "Tradicional"): 801400, ("Norte", "Moderno"): 428900, ("Norte", "Consumo en sitio"): 146200,
    ("Centro", "Tradicional"): 1061300, ("Centro", "Moderno"): 541800, ("Centro", "Consumo en sitio"): 198700,
    ("Golfo", "Tradicional"): 642500, ("Golfo", "Moderno"): 291600, ("Golfo", "Consumo en sitio"): 150300,
    ("Península", "Tradicional"): 772900, ("Península", "Moderno"): 401200, ("Península", "Consumo en sitio"): 239100,
}
G_AA = {"Norte": 0.034, "Centro": 0.041, "Golfo": -0.021, "Península": 0.052}
G_AA_CANAL = {"Tradicional": 0.0, "Moderno": 0.02, "Consumo en sitio": -0.01}
P_BASE = {"Tradicional": 118.50, "Moderno": 104.20, "Consumo en sitio": 142.00}
F_CEDIS = {"Norte": 1.02, "Centro": 1.00, "Golfo": 0.98, "Península": 1.01}
DP_REAL = {"Tradicional": 0.012, "Moderno": -0.008, "Consumo en sitio": 0.020}
DP_CEDIS = {"Norte": 0.002, "Centro": 0.0, "Golfo": -0.004, "Península": 0.003}
AUMENTO_PRECIO_AA = 0.055

UC = {  # costo unitario por caja unidad (MXN), igual en todos los CEDIS y canales
    "Real": dict(azucar=22.90, pet=14.55, conc_usd=0.62, tc=18.65, otros=9.20),
    "Presupuesto": dict(azucar=21.40, pet=14.80, conc_usd=0.62, tc=18.20, otros=9.00),
    "Año anterior": dict(azucar=19.80, pet=14.20, conc_usd=0.60, tc=17.90, otros=8.70),
}
DIST = {  # gastos de distribución por CEDIS (MXN)
    "Real": {"Norte": 18_912_400, "Centro": 22_087_300, "Golfo": 17_236_800, "Península": 18_041_500},
    "Presupuesto": {"Norte": 18_600_000, "Centro": 22_400_000, "Golfo": 15_900_000, "Península": 17_800_000},
    "Año anterior": {"Norte": 17_706_200, "Centro": 21_154_900, "Golfo": 15_388_400, "Península": 16_532_700},
}
CORP = {  # gastos corporativos (MXN). Real = preliminar, antes de ajustes de conciliación
    "Administración": {"Real": 38_391_600, "Presupuesto": 39_050_000, "Año anterior": 36_820_300},
    "Comisiones y servicios bancarios": {"Real": 1_912_000, "Presupuesto": 1_950_000, "Año anterior": 1_804_500},
    "Mercadotecnia": {"Real": 38_204_700, "Presupuesto": 36_500_000, "Año anterior": 34_115_800},
}


def build_pl():
    rows = []
    for c in CEDIS:
        for ch in CANALES:
            pp = round(P_BASE[ch] * F_CEDIS[c], 2)
            pr = pp * (1 + DP_REAL[ch] + DP_CEDIS[c])
            pa = pp / (1 + AUMENTO_PRECIO_AA)
            va = round(VOL_REAL[(c, ch)] / (1 + G_AA[c] + G_AA_CANAL[ch]))
            for esc, vol, price in (("Real", VOL_REAL[(c, ch)], pr), ("Presupuesto", VOL_PPTO[(c, ch)], pp), ("Año anterior", va, pa)):
                u = UC[esc]
                ventas = round(vol * price)
                az, pet = round(vol * u["azucar"]), round(vol * u["pet"])
                conc = round(vol * u["conc_usd"] * u["tc"]); otros = round(vol * u["otros"])
                cv = az + pet + conc + otros
                rows.append(dict(Mes="2026-10" if esc != "Año anterior" else "2025-10", Escenario=esc, CEDIS=c, Canal=ch,
                                 Volumen_CU=vol, Ventas_netas=ventas, Costo_azucar=az, Costo_PET=pet,
                                 Costo_concentrado=conc, Otros_costos_produccion=cv - az - pet - conc,
                                 Costo_ventas=cv, Utilidad_bruta=ventas - cv))
    return rows


# ---------------- Bancos: estado de cuenta Banco Ceiba y auxiliar ----------------
def business_days(y, m, d0, d1):
    out, d = [], dt.date(y, m, d0)
    while d <= dt.date(y, m, d1):
        if d.weekday() < 5: out.append(d)
        d += dt.timedelta(days=1)
    return out

OCT = business_days(2026, 10, 1, 30)
SALDO_INICIAL_CEIBA = 41_250_000.00
DEP_TRANSITO = dict(fecha=dt.date(2026, 10, 30), ref="DEP-1030-PEN-05", concepto="Depósito cobranza CEDIS Península", importe=1_284_600.00)
COMISION = dict(fecha=dt.date(2026, 10, 30), ref="COM-OCT-26", concepto="Comisión por servicios de banca electrónica", importe=16_000.00, iva=2_560.00)
DUPLICADO = dict(fecha=dt.date(2026, 10, 22), ref="SPEI-PET-2210", concepto="Pago proveedor de preformas PET (Envases del Sureste Ficticio)", importe=2_436_900.00)
ERROR_CAPTURA = dict(fecha=dt.date(2026, 10, 14), ref="DEP-1014-GOL-02", concepto="Depósito cobranza CEDIS Golfo", banco=475_320.00, libros=457_320.00)


def build_bank():
    """Movimientos de Banco Ceiba (concentradora). Devuelve (banco, libros)."""
    rr = random.Random(77)
    common = []  # (fecha, ref, concepto, cargo, abono)
    for d in OCT:
        ds = d.strftime("%m%d")
        for k, ced in enumerate(rr.sample(CEDIS, 4)):
            ref = f"DEP-{ds}-{ced[:3].upper().replace('Í','I')}-{k+1:02d}"
            amt = round(rr.uniform(320_000, 1_900_000), -1) + rr.choice([0, 0.5, 0.25, 0.75]) * 0
            amt = round(amt, 2)
            common.append([d, ref, f"Depósito cobranza CEDIS {ced}", 0.0, amt])
        ref = f"SPEI-CAD-{ds}"
        common.append([d, ref, "SPEI cobranza cadenas de autoservicio (canal Moderno)", 0.0, round(rr.uniform(8_200_000, 13_900_000), 2)])
        if d.weekday() in (1, 3):
            common.append([d, f"TRF-COR-{ds}", "Traspaso a Banco Coral (pagos a proveedores)", round(rr.uniform(26_000_000, 30_000_000), -3), 0.0])
        if d.weekday() == 4:
            common.append([d, f"TRF-JAD-{ds}", "Traspaso a Banco Jade (nómina e impuestos)", round(rr.uniform(13_500_000, 15_500_000), -3), 0.0])
    common.append([dt.date(2026, 10, 8), "SPEI-PET-0810", DUPLICADO["concepto"], 2_391_450.00, 0.0])
    common.append([dt.date(2026, 10, 22), DUPLICADO["ref"], DUPLICADO["concepto"], DUPLICADO["importe"], 0.0])
    # error de captura: el depósito existe en ambos lados con distinto importe
    for row in common:
        if row[1] == ERROR_CAPTURA["ref"]: row[4] = ERROR_CAPTURA["banco"]
    if not any(r[1] == ERROR_CAPTURA["ref"] for r in common):
        common.append([ERROR_CAPTURA["fecha"], ERROR_CAPTURA["ref"], ERROR_CAPTURA["concepto"], 0.0, ERROR_CAPTURA["banco"]])
    common.sort(key=lambda r: (r[0], r[1]))
    bank = [list(r) for r in common]
    books = [list(r) for r in common]
    for r in books:
        if r[1] == ERROR_CAPTURA["ref"]: r[4] = ERROR_CAPTURA["libros"]
    # depósito en tránsito: sólo en libros
    if any(r[1] == DEP_TRANSITO["ref"] for r in books):
        raise SystemExit("ref colision")
    books.append([DEP_TRANSITO["fecha"], DEP_TRANSITO["ref"], DEP_TRANSITO["concepto"], 0.0, DEP_TRANSITO["importe"]])
    # comisión + IVA: sólo en banco
    bank.append([COMISION["fecha"], COMISION["ref"], COMISION["concepto"], COMISION["importe"], 0.0])
    bank.append([COMISION["fecha"], "IVA-" + COMISION["ref"], "IVA de comisión por servicios de banca electrónica", COMISION["iva"], 0.0])
    # cargo duplicado: sólo en banco (segunda vez)
    i = next(k for k, r in enumerate(bank) if r[1] == DUPLICADO["ref"])
    bank.insert(i + 1, [DUPLICADO["fecha"], DUPLICADO["ref"], DUPLICADO["concepto"], DUPLICADO["importe"], 0.0])
    bank.sort(key=lambda r: (r[0], 0 if r[4] else 1))
    books.sort(key=lambda r: (r[0], 0 if r[4] else 1))
    return bank, books


def running(rows, start):
    s, out = start, []
    for r in rows:
        s = round(s + r[4] - r[3], 2); out.append(r + [s])
    return out


# ---------------- Flujo de caja diario (3 bancos) ----------------
MINIMO = {"Banco Ceiba": 15_000_000, "Banco Coral": 10_000_000, "Banco Jade": 8_000_000}
LINEA_CREDITO = 150_000_000
NOV = business_days(2026, 11, 2, 13)


def build_cash(bank):
    rr = random.Random(5)
    cols = ["Cobranza", "Traspasos_recibidos", "Otros_ingresos", "Pagos_proveedores", "Nomina", "Impuestos", "Traspasos_enviados", "Comisiones"]
    rows = []
    # Ceiba = agregado diario del estado de cuenta
    s = SALDO_INICIAL_CEIBA
    for d in OCT:
        day = [r for r in bank if r[0] == d]
        v = dict.fromkeys(cols, 0.0)
        for r in day:
            if r[4]: v["Cobranza"] += r[4]
            elif r[1].startswith("TRF"): v["Traspasos_enviados"] += r[3]
            elif r[1].startswith("SPEI-PET"): v["Pagos_proveedores"] += r[3]
            else: v["Comisiones"] += r[3]
        fin = round(s + sum(v[k] for k in cols[:3]) - sum(v[k] for k in cols[3:]), 2)
        rows.append(dict(Fecha=d, Banco="Banco Ceiba", Saldo_inicial=s, **{k: round(x, 2) for k, x in v.items()}, Saldo_final=fin)); s = fin
    trf = {r[0]: r[3] for r in bank if r[1].startswith("TRF-COR")}
    trfj = {r[0]: r[3] for r in bank if r[1].startswith("TRF-JAD")}
    # Coral: pagos a proveedores
    s = 22_480_000.00
    for d in OCT:
        v = dict.fromkeys(cols, 0.0)
        v["Traspasos_recibidos"] = trf.get(d, 0.0)
        v["Cobranza"] = round(rr.uniform(900_000, 2_400_000), 2)
        pay = round(rr.uniform(7_500_000, 10_500_000), 2)
        if d.day in (15, 30): pay += 38_640_000.00  # azúcar quincenal
        v["Pagos_proveedores"] = pay
        fin = round(s + v["Cobranza"] + v["Traspasos_recibidos"] - pay, 2)
        rows.append(dict(Fecha=d, Banco="Banco Coral", Saldo_inicial=s, **v, Saldo_final=fin)); s = fin
    # Jade: nómina e impuestos
    s = 12_960_000.00
    for d in OCT:
        v = dict.fromkeys(cols, 0.0)
        v["Traspasos_recibidos"] = trfj.get(d, 0.0)
        v["Otros_ingresos"] = round(rr.uniform(150_000, 420_000), 2)
        if d.day in (15, 30): v["Nomina"] = 24_310_000.00 if d.day == 15 else 24_585_000.00
        if d.day == 16: v["Impuestos"] = 18_950_000.00
        fin = round(s + v["Otros_ingresos"] + v["Traspasos_recibidos"] - v["Nomina"] - v["Impuestos"], 2)
        rows.append(dict(Fecha=d, Banco="Banco Jade", Saldo_inicial=s, **v, Saldo_final=fin)); s = fin
    return rows


def build_projection(cash):
    """Proyección 2 a 13 de noviembre. Coral cae bajo su mínimo el 12-nov (pago de azúcar)."""
    rr = random.Random(11)
    last = {b: [r for r in cash if r["Banco"] == b][-1]["Saldo_final"] for b in BANCOS}
    rows = []
    for b in BANCOS:
        s = last[b]
        for d in NOV:
            v = dict(Cobranza_esperada=0.0, Traspasos=0.0, Pagos_programados=0.0, Nomina=0.0, Impuestos=0.0)
            if b == "Banco Ceiba":
                v["Cobranza_esperada"] = round(rr.uniform(14_000_000, 18_500_000), -3)
                if d == dt.date(2026, 11, 2): v["Cobranza_esperada"] += DEP_TRANSITO["importe"]
                if d.weekday() in (1, 3): v["Traspasos"] = -22_000_000.0
                if d.weekday() == 4: v["Traspasos"] = -12_000_000.0
            elif b == "Banco Coral":
                v["Cobranza_esperada"] = round(rr.uniform(1_000_000, 2_000_000), -3)
                if d.weekday() in (1, 3): v["Traspasos"] = 22_000_000.0
                v["Pagos_programados"] = round(rr.uniform(9_000_000, 11_500_000), -3)
                if d == dt.date(2026, 11, 12): v["Pagos_programados"] += 41_200_000.0  # azúcar con nuevo precio
            else:
                v["Cobranza_esperada"] = round(rr.uniform(150_000, 400_000), -3)
                if d.weekday() == 4: v["Traspasos"] = 12_000_000.0
                if d == dt.date(2026, 11, 13): v["Nomina"] = 24_400_000.0
            fin = round(s + v["Cobranza_esperada"] + v["Traspasos"] - v["Pagos_programados"] - v["Nomina"] - v["Impuestos"], 2)
            rows.append(dict(Fecha=d, Banco=b, Saldo_inicial=round(s, 2), **v, Saldo_final=fin)); s = fin
    return rows


KPIS = [  # mes, cobranza real, meta, DSO total, DSO Tradicional, DSO Moderno, DSO Consumo, DPO, días inventario
    ("2026-07", 676_420_000, 684_000_000, 24.1, 8.2, 38.0, 21.5, 44.0, 18.2),
    ("2026-08", 668_910_000, 679_500_000, 24.6, 8.1, 39.1, 21.9, 43.6, 18.9),
    ("2026-09", 641_200_000, 657_300_000, 25.4, 8.3, 40.6, 22.4, 42.8, 19.6),
    ("2026-10", 0, 0, 26.3, 8.4, 43.0, 22.7, 41.9, 20.4),
]


# ---------------- Histórico de volumen y forecast ----------------
SEASON = [0.86, 0.88, 0.97, 1.05, 1.12, 1.10, 1.09, 1.08, 1.00, 0.97, 0.92, 1.04]
OUTLIER = dict(cedis="Golfo", mes="2026-07", factor=1.45)
PPTO_GROWTH_NOVDIC = 0.04
ESC_AZUCAR = 0.10
TC_SHOCK = 1.00
PET_USD_SHARE = 0.50


def build_history(pl):
    rr = random.Random(31)
    aa = {c: sum(r["Volumen_CU"] for r in pl if r["CEDIS"] == c and r["Escenario"] == "Año anterior") for c in CEDIS}
    re_ = {c: sum(r["Volumen_CU"] for r in pl if r["CEDIS"] == c and r["Escenario"] == "Real") for c in CEDIS}
    hist = {}
    for c in CEDIS:
        base = aa[c] / SEASON[9]
        g = re_[c] / aa[c] - 1
        for m in range(1, 13):
            v25 = aa[c] if m == 10 else round(base * SEASON[m - 1] * (1 + rr.uniform(-0.015, 0.015)))
            hist[(c, f"2025-{m:02d}")] = v25
        for m in range(1, 11):
            if m == 10: v26 = re_[c]
            else: v26 = round(hist[(c, f"2025-{m:02d}")] * (1 + g + rr.uniform(-0.01, 0.01)))
            hist[(c, f"2026-{m:02d}")] = v26
    hist[(OUTLIER["cedis"], OUTLIER["mes"])] = round(hist[(OUTLIER["cedis"], OUTLIER["mes"])] * OUTLIER["factor"])
    return hist


def build_all():
    pl = build_pl()
    bank, books = build_bank()
    cash = build_cash(bank)
    proj = build_projection(cash)
    hist = build_history(pl)
    return dict(pl=pl, bank=bank, books=books, cash=cash, proj=proj, hist=hist)

