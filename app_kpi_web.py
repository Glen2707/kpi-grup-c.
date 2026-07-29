import streamlit as st

# 1. Konfigurasi Halaman & Tampilan HP
st.set_page_config(page_title="Sistem Komando KPI 6 Goal - Grup C", page_icon="📊", layout="centered")

# Sembunyikan Bawaan Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stDeployButton {display:none;}
            div[data-testid="stToolbar"] {visibility: hidden; height: 0%; position: fixed;}
            div[data-testid="stDecoration"] {visibility: hidden; height: 0%; position: fixed;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 2. Header Utama
st.title("📊 MONITOR KPI & QUALITY GRUP C")
st.caption("Aplikasi Komando Evaluasi KPI, Reject, Defect PRI & BB, Absensi & K3 2026")
st.divider()

# 3. Database Utama 2026
DATA_UTAMA_2026 = {
    "Januari":  {"cw": 474402.00, "spb": 180637.00, "paid_karu": 1919.00, "paid_wt": 380.00, "real_cw": 37671, "rij_cw": 139, "real_spb": 15053, "rij_spb": 63, "polos": 4600050, "pri_pcs": 130180, "pri_pct": 2.83, "bb_pcs": 138281, "bb_pct": 3.01, "sd": 0, "alpa": 0, "hk_bulan": 312},
    "Februari": {"cw": 400056.00, "spb": 162814.00, "paid_karu": 1545.49, "paid_wt": 321.88, "real_cw": 30018, "rij_cw": 106, "real_spb": 13513, "rij_spb": 87, "polos": 3975075, "pri_pcs": 99774,  "pri_pct": 2.51, "bb_pcs": 136665, "bb_pct": 3.44, "sd": 0, "alpa": 0, "hk_bulan": 312},
    "Maret":    {"cw": 68277.60,  "spb": 24085.00,  "paid_karu": 224.00,  "paid_wt": 56.00,  "real_cw": 6987,  "rij_cw": 12,  "real_spb": 2999,  "rij_spb": 25, "polos": 817247,  "pri_pcs": 19041,  "pri_pct": 2.33, "bb_pcs": 29685,  "bb_pct": 3.63, "sd": 0, "alpa": 0, "hk_bulan": 312},
    "April":    {"cw": 346951.36, "spb": 152698.90, "paid_karu": 1484.00, "paid_wt": 324.00, "real_cw": 27505, "rij_cw": 85,  "real_spb": 12689, "rij_spb": 141, "polos": 3457645, "pri_pcs": 100271, "pri_pct": 2.90, "bb_pcs": 120199, "bb_pct": 3.48, "sd": 0, "alpa": 0, "hk_bulan": 312},
    "Mei":      {"cw": 465804.96, "spb": 273485.18, "paid_karu": 1913.00, "paid_wt": 374.50, "real_cw": 36763, "rij_cw": 81,  "real_spb": 22649, "rij_spb": 267, "polos": 4359224, "pri_pcs": 93723,  "pri_pct": 2.15, "bb_pcs": 245059, "bb_pct": 5.62, "sd": 2, "alpa": 0, "hk_bulan": 312},
    "Juni":     {"cw": 294099.44, "spb": 280349.40, "paid_karu": 1882.42, "paid_wt": 368.50, "real_cw": 23171, "rij_cw": 54,  "real_spb": 23225, "rij_spb": 203, "polos": 4422447, "pri_pcs": 87564,  "pri_pct": 1.98, "bb_pcs": 276311, "bb_pct": 6.25, "sd": 3, "alpa": 0, "hk_bulan": 312},
    "Juli":     {"cw": 380000.00, "spb": 210000.00, "paid_karu": 1600.00, "paid_wt": 310.00, "real_cw": 29172, "rij_cw": 50,  "real_spb": 17569, "rij_spb": 200, "polos": 4422447, "pri_pcs": 87564,  "pri_pct": 1.98, "bb_pcs": 276311, "bb_pct": 6.25, "sd": 3, "alpa": 0, "hk_bulan": 312},
}

# 4. Form Pilihan
col1, col2 = st.columns(2)
with col1:
    bulan = st.selectbox("🗓️ Pilih Bulan:", list(DATA_UTAMA_2026.keys()))
with col2:
    jabatan = st.selectbox("👤 Pilih Jabatan:", ["KARU - Muhammad Syahid", "KARU - Joko Sudiyono", "KASIE - Widodo"])

d = DATA_UTAMA_2026[bulan]

# 5. TAB NAVIGASI (5 TAB)
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎯 Goal 1: KPI", "📊 Goal 2: Reject Press", "🕳️ Goal 3: Defect PRI", "🧩 Goal 4: Defect BB", "🙋 Goal 5: Absensi"])

# --- TAB 1: GOAL 1 - EVALUASI KPI (BOBOT 25%) ---
with tab1:
    total_sj = d['cw'] + d['spb']
    if "KASIE" in jabatan:
        paid_hour = d['paid_karu'] + d['paid_wt']
        target_std = 287.92
    else:
        paid_hour = d['paid_karu']
        target_std = 342.00

    kpi_skor = total_sj / paid_hour if paid_hour > 0 else 0

    st.subheader(f"📋 Goal 1: Produktivitas Press & Molen - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `25%`")
    st.write(f"- **TK CW:** {d['cw']:,.2f} kg | **TK SPB:** {d['spb']:,.2f} kg")
    st.write(f"- **Total SJ Attb:** {total_sj:,.2f} kg")
    st.write(f"- **Summary Paid Hour:** {paid_hour:,.2f} jam")

    st.divider()
    if kpi_skor >= target_std:
        st.success(f"🔥 **GOAL 1 TERCAPAI!**\n\nSkor KPI {jabatan} Bulan {bulan}: **{kpi_skor:.2f}** (Target Standar: {target_std})")
    else:
        st.error(f"❌ **GOAL 1 TIDAK TERCAPAI**\n\nSkor KPI {jabatan} Bulan {bulan}: **{kpi_skor:.2f}** (Target Standar: {target_std})")

# --- TAB 2: GOAL 2 - REJECT PRESS (BOBOT 25%) ---
with tab2:
    real_cw = d['real_cw']
    rij_cw = d['rij_cw']
    pct_cw = (rij_cw / real_cw * 100) if real_cw > 0 else 0

    real_spb = d['real_spb']
    rij_spb = d['rij_spb']
    pct_spb = (rij_spb / real_spb * 100) if real_spb > 0 else 0

    total_real = real_cw + real_spb
    total_rij = rij_cw + rij_spb
    pct_total = (total_rij / total_real * 100) if total_real > 0 else 0

    st.subheader(f"🔍 Goal 2: Quality Reject TKP / Press - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `25%` | **Target Maksimal:** `0,60%`")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Reject TK CW", f"{pct_cw:.2f}%", f"{rij_cw:,} kg", delta_color="inverse")
    m2.metric("Reject TK SPB", f"{pct_spb:.2f}%", f"{rij_spb:,} kg", delta_color="inverse")
    m3.metric("Total Reject", f"{pct_total:.2f}%", f"{total_rij:,} kg", delta_color="inverse")

    st.divider()
    if pct_total <= 0.60:
        st.success(f"🔥 **GOAL 2 TERCAPAI!**\n\nTotal Reject Press Bulan {bulan}: **{pct_total:.2f}%** (Target Maksimal: 0,60%)")
    else:
        st.error(f"❌ **GOAL 2 TIDAK TERCAPAI**\n\nTotal Reject Press Bulan {bulan}: **{pct_total:.2f}%** (Target Maksimal: 0,60%)")

# --- TAB 3: GOAL 3 - DEFECT PORI-PORI / PRI (BOBOT 15%) ---
with tab3:
    pri_pct = d['pri_pct']
    pri_pcs = d['pri_pcs']
    polos = d['polos']
    target_pri = 6.00

    st.subheader(f"🕳️ Goal 3: Defect Pori-Pori (PRI) - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `15%` | **Target Maksimal:** `6,00%`")
    
    p1, p2 = st.columns(2)
    p1.metric("Barang Polos Diseleksi", f"{polos:,} Pcs")
    p2.metric("Defect PRI", f"{pri_pct:.2f}%", f"{pri_pcs:,} Pcs", delta_color="inverse")

    st.divider()
    st.write(f"📌 **Detail Rincian Formula ({bulan}):**")
    st.write(f"• **Rumus:** `(Pcs Defect PRI / Barang Polos) x 100%`")
    st.write(f"• **Hitungan:** `({pri_pcs:,} / {polos:,}) x 100% = {pri_pct:.2f}%`")

    if pri_pct <= target_pri:
        st.success(f"🔥 **GOAL 3 TERCAPAI (SANGAT BAIK)!**\n\nPersentase Defect PRI Bulan {bulan}: **{pri_pct:.2f}%** (Target Maksimal: 6,00%)")
    else:
        st.error(f"❌ **GOAL 3 TIDAK TERCAPAI**\n\nPersentase Defect PRI Bulan {bulan}: **{pri_pct:.2f}%** (Target Maksimal: 6,00%)")

# --- TAB 4: GOAL 4 - DEFECT BERUBAH BENTUK / BB (BOBOT 15%) ---
with tab4:
    bb_pcs = d['bb_pcs']
    bb_pct = d['bb_pct']
    polos = d['polos']
    target_bb = 5.00

    st.subheader(f"🧩 Goal 4: Defect Berubah Bentuk (BB) - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `15%` | **Target Maksimal:** `5,00%`")
    
    b1, b2 = st.columns(2)
    b1.metric("Barang Polos Diseleksi", f"{polos:,} Pcs")
    b2.metric("Defect BB", f"{bb_pct:.2f}%", f"{bb_pcs:,} Pcs", delta_color="inverse")

    st.divider()
    st.write(f"📌 **Detail Rincian Formula ({bulan}):**")
    st.write(f"• **Rumus:** `(Pcs Defect BB / Barang Polos) x 100%`")
    st.write(f"• **Hitungan:** `({bb_pcs:,} / {polos:,}) x 100% = {bb_pct:.2f}%`")

    if bb_pct <= target_bb:
        st.success(f"🔥 **GOAL 4 TERCAPAI!**\n\nPersentase Defect BB Bulan {bulan}: **{bb_pct:.2f}%** (Target Maksimal: 5,00%)")
    else:
        st.error(f"❌ **GOAL 4 TIDAK TERCAPAI**\n\nPersentase Defect BB Bulan {bulan}: **{bb_pct:.2f}%** (Target Maksimal: 5,00%)")

# --- TAB 5: GOAL 5 - ABSENSI TENAGA KERJA (BOBOT 10%) ---
with tab5:
    sd = d['sd']
    alpa = d['alpa']
    total_absensi = sd + alpa
    total_hk = d['hk_bulan']
    perf_absensi = ((total_hk - total_absensi) / total_hk) * 100 if total_hk > 0 else 100.0

    st.subheader(f"🙋 Goal 5: Presensi Tenaga Kerja - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `10%` | **Target Minimal:** `97,00%`")
    
    a1, a2, a3 = st.columns(3)
    a1.metric("Surat Dokter (SD)", f"{sd} Hari")
    a2.metric("Alpa (A)", f"{alpa} Hari")
    a3.metric("Performance Presensi", f"{perf_absensi:.2f}%")

    st.divider()
    if perf_absensi >= 97.0:
        st.success(f"🔥 **GOAL 5 TERCAPAI!**\n\nPresensi Operator Grup C Bulan {bulan}: **{perf_absensi:.2f}%** (Target Minimal: 97,00%)")
    else:
        st.error(f"❌ **GOAL 5 TIDAK TERCAPAI**\n\nPresensi Operator Grup C Bulan {bulan}: **{perf_absensi:.2f}%** (Target Minimal: 97,00%)")