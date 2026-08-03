import streamlit as st

# 1. Konfigurasi Halaman & Tampilan HP
st.set_page_config(page_title="Sistem Komando KPI 6 Goal - Grup C", page_icon="📊", layout="centered")

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

st.title("📊 MONITOR KPI 6 GOAL GRUP C")
st.caption("Aplikasi Komando Evaluasi KPI, Reject, Defect PRI & BB (Code KMS 44), Absensi & K3 2026")
st.divider()

# Database Utama 2026 Lengkap
DATA_UTAMA_2026 = {
    "Januari":  {"cw": 474402.00, "spb": 180637.00, "paid_karu": 1919.00, "paid_wt": 380.00, "real_cw": 37671, "rij_cw": 139, "real_spb": 15053, "rij_spb": 63, "polos": 4600050, "pri_pcs": 332058, "pri_pct": 7.22, "bb_pcs": 138281, "bb_pct": 3.01, "sd": 0, "alpa": 0, "hk_bulan": 312, "accident": 0},
    "Februari": {"cw": 400056.00, "spb": 162814.00, "paid_karu": 1545.49, "paid_wt": 321.88, "real_cw": 30018, "rij_cw": 106, "real_spb": 13513, "rij_spb": 87, "polos": 3975075, "pri_pcs": 264797, "pri_pct": 6.66, "bb_pcs": 136665, "bb_pct": 3.44, "sd": 0, "alpa": 0, "hk_bulan": 312, "accident": 0},
    "Maret":    {"cw": 68277.60,  "spb": 24085.00,  "paid_karu": 224.00,  "paid_wt": 56.00,  "real_cw": 6987,  "rij_cw": 12,  "real_spb": 2999,  "rij_spb": 25, "polos": 817247,  "pri_pcs": 50571,  "pri_pct": 6.19, "bb_pcs": 29685,  "bb_pct": 3.63, "sd": 0, "alpa": 0, "hk_bulan": 312, "accident": 0},
    "April":    {"cw": 346951.36, "spb": 152698.90, "paid_karu": 1484.00, "paid_wt": 324.00, "real_cw": 27505, "rij_cw": 85,  "real_spb": 12689, "rij_spb": 141, "polos": 3457645, "pri_pcs": 270773, "pri_pct": 7.83, "bb_pcs": 120199, "bb_pct": 3.48, "sd": 0, "alpa": 0, "hk_bulan": 312, "accident": 0},
    "Mei":      {"cw": 465804.96, "spb": 273485.18, "paid_karu": 1913.00, "paid_wt": 374.50, "real_cw": 36763, "rij_cw": 81,  "real_spb": 22649, "rij_spb": 267, "polos": 4359224, "pri_pcs": 339304, "pri_pct": 7.78, "bb_pcs": 245059, "bb_pct": 5.62, "sd": 2, "alpa": 0, "hk_bulan": 312, "accident": 0},
    "Juni":     {"cw": 294099.44, "spb": 280349.40, "paid_karu": 1882.42, "paid_wt": 368.50, "real_cw": 23171, "rij_cw": 54,  "real_spb": 23225, "rij_spb": 203, "polos": 4422447, "pri_pcs": 344396, "pri_pct": 7.79, "bb_pcs": 276311, "bb_pct": 6.25, "sd": 3, "alpa": 0, "hk_bulan": 312, "accident": 0},
    "Juli":     {"cw": 380000.00, "spb": 210000.00, "paid_karu": 1600.00, "paid_wt": 310.00, "real_cw": 29172, "rij_cw": 50,  "real_spb": 17569, "rij_spb": 200, "polos": 4422447, "pri_pcs": 344396, "pri_pct": 7.79, "bb_pcs": 276311, "bb_pct": 6.25, "sd": 3, "alpa": 0, "hk_bulan": 312, "accident": 0},
}

col1, col2 = st.columns(2)
with col1:
    bulan = st.selectbox("🗓️ Pilih Bulan:", list(DATA_UTAMA_2026.keys()))
with col2:
    jabatan = st.selectbox("👤 Pilih Jabatan:", ["KARU - Muhammad Syahid", "KARU - Joko Sudiyono", "KASIE - Widodo"])

d = DATA_UTAMA_2026[bulan]

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🎯 Goal 1", "📊 Goal 2", "🕳️ Goal 3", "🧩 Goal 4", "🙋 Goal 5", "⛑️ Goal 6"])

# --- TAB 1: GOAL 1 ---
with tab1:
    total_sj = d['cw'] + d['spb']
    paid_hour = (d['paid_karu'] + d['paid_wt']) if "KASIE" in jabatan else d['paid_karu']
    target_std = 287.92 if "KASIE" in jabatan else 342.00
    kpi_skor = total_sj / paid_hour if paid_hour > 0 else 0

    st.subheader(f"📋 Goal 1: Produktivitas Press & Molen - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `25%` | **Target:** `>={target_std} kg/paidhour`")
    st.write(f"- **TK CW:** {d['cw']:,.2f} kg | **TK SPB:** {d['spb']:,.2f} kg")
    st.write(f"- **Total SJ Attb:** {total_sj:,.2f} kg")
    st.write(f"- **Summary Paid Hour:** {paid_hour:,.2f} jam")

    st.divider()
    if kpi_skor >= target_std:
        st.success(f"🔥 **GOAL 1 TERCAPAI!**\n\nSkor KPI {jabatan} Bulan {bulan}: **{kpi_skor:.2f}** (Target Standar: {target_std})")
    else:
        st.error(f"❌ **GOAL 1 TIDAK TERCAPAI**\n\nSkor KPI {jabatan} Bulan {bulan}: **{kpi_skor:.2f}** (Target Standar: {target_std})")

# --- TAB 2: GOAL 2 (TERDAPAT RINCIAN PRODUKSI REAL TKP & REJECT) ---
with tab2:
    real_cw, rij_cw = d['real_cw'], d['rij_cw']
    pct_cw = (rij_cw / real_cw * 100) if real_cw > 0 else 0
    
    real_spb, rij_spb = d['real_spb'], d['rij_spb']
    pct_spb = (rij_spb / real_spb * 100) if real_spb > 0 else 0
    
    total_real = real_cw + real_spb
    total_rij = rij_cw + rij_spb
    pct_total = (total_rij / total_real * 100) if total_real > 0 else 0

    st.subheader(f"🔍 Goal 2: Quality Reject TKP / Press - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `25%` | **Target Maksimal:** `0,60%`")
    
    # Indikator Persentase & Nilai Reject
    m1, m2, m3 = st.columns(3)
    m1.metric("Reject TK CW", f"{pct_cw:.2f}%", f"{rij_cw:,} kg", delta_color="inverse")
    m2.metric("Reject TK SPB", f"{pct_spb:.2f}%", f"{rij_spb:,} kg", delta_color="inverse")
    m3.metric("Total Reject", f"{pct_total:.2f}%", f"{total_rij:,} kg", delta_color="inverse")

    st.divider()
    
    # Rincian Produksi Real TKP yang Ditambahkan
    st.write(f"📌 **Detail Produksi Real vs Reject TKP ({bulan}):**")
    st.write(f"• **TK CW:** Produksi Real = `{real_cw:,} kg` | Reject = `{rij_cw:,} kg` (**{pct_cw:.2f}%**)")
    st.write(f"• **TK SPB:** Produksi Real = `{real_spb:,} kg` | Reject = `{rij_spb:,} kg` (**{pct_spb:.2f}%**)")
    st.write(f"• **TOTAL TKP:** Total Produksi Real = `{total_real:,} kg` | Total Reject = `{total_rij:,} kg` (**{pct_total:.2f}%**)")

    st.divider()
    if pct_total <= 0.60:
        st.success(f"🔥 **GOAL 2 TERCAPAI!**\n\nTotal Reject Press Bulan {bulan}: **{pct_total:.2f}%** (Target Maksimal: 0,60%)")
    else:
        st.error(f"❌ **GOAL 2 TIDAK TERCAPAI**\n\nTotal Reject Press Bulan {bulan}: **{pct_total:.2f}%** (Target Maksimal: 0,60%)")

# --- TAB 3 ---
with tab3:
    pri_pct, pri_pcs, polos = d['pri_pct'], d['pri_pcs'], d['polos']
    target_pri = 6.00

    st.subheader(f"🕳️ Goal 3: Defect Pori-Pori (PRI - KMS 44) - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `15%` | **Target Maksimal:** `6,00%`")
    st.caption("📌 *Acuan Resmi: Laporan Harian Analisa Kualitas KW II, III, IV (Code KMS 44)*")
    
    p1, p2 = st.columns(2)
    p1.metric("Barang Polos Diseleksi", f"{polos:,} Pcs")
    p2.metric("Defect PRI (KMS 44)", f"{pri_pct:.2f}%", f"{pri_pcs:,} Pcs", delta_color="inverse")

    st.divider()
    st.write(f"📌 **Detail Rincian Formula ({bulan}):**")
    st.write(f"• **Rumus:** `(Pcs Defect PRI Code 44 / Barang Polos) x 100%`")
    st.write(f"• **Hitungan:** `({pri_pcs:,} / {polos:,}) x 100% = {pri_pct:.2f}%`")

    if pri_pct <= target_pri:
        st.success(f"🔥 **GOAL 3 TERCAPAI!**\n\nPersentase Defect PRI (KMS 44) Bulan {bulan}: **{pri_pct:.2f}%** (Target Maksimal: 6,00%)")
    else:
        st.error(f"❌ **GOAL 3 TIDAK TERCAPAI**\n\nPersentase Defect PRI (KMS 44) Bulan {bulan}: **{pri_pct:.2f}%** (Target Maksimal: 6,00%)")

# --- TAB 4 ---
with tab4:
    bb_pcs, bb_pct, polos = d['bb_pcs'], d['bb_pct'], d['polos']
    target_bb = 5.00

    st.subheader(f"🧩 Goal 4: Defect Berubah Bentuk (BB - KMS 44) - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `15%` | **Target Maksimal:** `5,00%`")
    st.caption("📌 *Acuan Resmi: Laporan Harian Analisa Kualitas KW II, III, IV (Code KMS 44)*")
    
    b1, b2 = st.columns(2)
    b1.metric("Barang Polos Diseleksi", f"{polos:,} Pcs")
    b2.metric("Defect BB (KMS 44)", f"{bb_pct:.2f}%", f"{bb_pcs:,} Pcs", delta_color="inverse")

    st.divider()
    st.write(f"📌 **Detail Rincian Formula ({bulan}):**")
    st.write(f"• **Rumus:** `(Pcs Defect BB Code 44 / Barang Polos) x 100%`")
    st.write(f"• **Hitungan:** `({bb_pcs:,} / {polos:,}) x 100% = {bb_pct:.2f}%`")

    if bb_pct <= target_bb:
        st.success(f"🔥 **GOAL 4 TERCAPAI!**\n\nPersentase Defect BB (KMS 44) Bulan {bulan}: **{bb_pct:.2f}%** (Target Maksimal: 5,00%)")
    else:
        st.error(f"❌ **GOAL 4 TIDAK TERCAPAI**\n\nPersentase Defect BB (KMS 44) Bulan {bulan}: **{bb_pct:.2f}%** (Target Maksimal: 5,00%)")

# --- TAB 5 ---
with tab5:
    sd, alpa = d['sd'], d['alpa']
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

# --- TAB 6 ---
with tab6:
    acc = d['accident']
    st.subheader(f"⛑️ Goal 6: Keselamatan Kerja (Zero Accident) - {bulan}")
    st.write(f"- **Bobot Evaluasi:** `10%` | **Target Utama:** `0% / Zero Accident`")
    
    k1, k2 = st.columns(2)
    k1.metric("Jumlah Kecelakaan Kerja", f"{acc} Kasus")
    k2.metric("Status Zero Accident", "100% AMAN 🛡️")

    st.divider()
    st.write(f"📌 **Identifikasi Potensi & Penggunaan APD ({bulan}):**")
    st.write(f"• **Laporan Kecelakaan Kerja:** `0 Kasus (NIL)`")
    st.write(f"• **Implementasi Program Inisiatif K3:** `100% Terlaksana`")
    st.write(f"• **Penggunaan APD Operator:** `Lengkap & Sesuai Standar`")

    st.success(f"🔥 **GOAL 6 TERCAPAI SANGAT BAIK!**\n\nBagian Bahan Baku Grup C Berhasil Mempertahankan **Zero Accident (0% Kecelakaan Kerja)** Pada Bulan {bulan} 2026!")