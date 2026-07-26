import streamlit as st

# 1. Konfigurasi Halaman & Mode Tampilan HP
st.set_page_config(page_title="Sistem Komando KPI & Reject Grup C", page_icon="📊", layout="centered")

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

# 2. Header Utama Aplikasi
st.title("📊 MONITOR KPI & REJECT GRUP C")
st.caption("Aplikasi Komando Rekapitulasi Produksi, KPI & Quality Press 2026")
st.divider()

# 3. Database Rekapitulasi KPI & Reject 2026
DATA_UTAMA_2026 = {
    "Januari":  {"cw": 474402.00, "spb": 180637.00, "paid_karu": 1919.00, "paid_wt": 380.00, "real_cw": 37671, "rij_cw": 139, "real_spb": 15053, "rij_spb": 63},
    "Februari": {"cw": 400056.00, "spb": 162814.00, "paid_karu": 1545.49, "paid_wt": 321.88, "real_cw": 30018, "rij_cw": 106, "real_spb": 13513, "rij_spb": 87},
    "Maret":    {"cw": 68277.60,  "spb": 24085.00,  "paid_karu": 224.00,  "paid_wt": 56.00,  "real_cw": 6987,  "rij_cw": 12,  "real_spb": 2999,  "rij_spb": 25},
    "April":    {"cw": 346951.36, "spb": 152698.90, "paid_karu": 1484.00, "paid_wt": 324.00, "real_cw": 27505, "rij_cw": 85,  "real_spb": 12689, "rij_spb": 141},
    "Mei":      {"cw": 465804.96, "spb": 273485.18, "paid_karu": 1913.00, "paid_wt": 374.50, "real_cw": 36763, "rij_cw": 81,  "real_spb": 22649, "rij_spb": 267},
    "Juni":     {"cw": 294099.44, "spb": 280349.40, "paid_karu": 1882.42, "paid_wt": 368.50, "real_cw": 23171, "rij_cw": 54,  "real_spb": 23225, "rij_spb": 203},
    "Juli":     {"cw": 380000.00, "spb": 210000.00, "paid_karu": 1600.00, "paid_wt": 310.00, "real_cw": 29172, "rij_cw": 50,  "real_spb": 17569, "rij_spb": 200},
}

# 4. Form Pilihan Utama
col1, col2 = st.columns(2)
with col1:
    bulan = st.selectbox("🗓️ Pilih Bulan:", list(DATA_UTAMA_2026.keys()))
with col2:
    jabatan = st.selectbox("👤 Pilih Jabatan:", ["KARU - Muhammad Syahid", "KARU - Joko Sudiyono", "KASIE - Widodo"])

d = DATA_UTAMA_2026[bulan]

# 5. TAB NAVIGASI APLIKASI
tab1, tab2 = st.tabs(["🎯 Evaluasi KPI", "📊 Analisis Reject Press"])

# --- TAB 1: EVALUASI KPI ---
with tab1:
    total_sj = d['cw'] + d['spb']
    if "KASIE" in jabatan:
        paid_hour = d['paid_karu'] + d['paid_wt']
        target_std = 287.92
    else:
        paid_hour = d['paid_karu']
        target_std = 342.00

    kpi_skor = total_sj / paid_hour if paid_hour > 0 else 0

    st.subheader(f"📋 Ringkasan Produksi - Bulan {bulan}")
    st.write(f"- **TK CW:** {d['cw']:,.2f} kg")
    st.write(f"- **TK SPB:** {d['spb']:,.2f} kg")
    st.write(f"- **Total SJ Attb:** {total_sj:,.2f} kg")
    st.write(f"- **Summary Paid Hour:** {paid_hour:,.2f} jam")

    st.divider()

    if kpi_skor >= target_std:
        st.success(f"🔥 **STATUS: TERCAPAI!**\n\nSkor KPI {jabatan} Bulan {bulan}: **{kpi_skor:.2f}** (Target Standar: {target_std})")
    else:
        st.error(f"❌ **STATUS: TIDAK TERCAPAI**\n\nSkor KPI {jabatan} Bulan {bulan}: **{kpi_skor:.2f}** (Target Standar: {target_std})")

# --- TAB 2: ANALISIS REJECT ---
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

    st.subheader(f"🔍 Performansi Quality Press - Bulan {bulan}")
    
    # KARTU INDIKATOR UTAMA
    m1, m2, m3 = st.columns(3)
    m1.metric("Reject TK CW", f"{pct_cw:.2f}%", f"{rij_cw:,} kg", delta_color="inverse")
    m2.metric("Reject TK SPB", f"{pct_spb:.2f}%", f"{rij_spb:,} kg", delta_color="inverse")
    m3.metric("Total Reject", f"{pct_total:.2f}%", f"{total_rij:,} kg", delta_color="inverse")

    st.divider()
    st.write(f"📌 **Detail Produksi Real vs Reject ({bulan}):**")
    st.write(f"• **TK CW:** Real = `{real_cw:,} kg` | Reject = `{rij_cw:,} kg` (**{pct_cw:.2f}%**)")
    st.write(f"• **TK SPB:** Real = `{real_spb:,} kg` | Reject = `{rij_spb:,} kg` (**{pct_spb:.2f}%**)")
    st.write(f"• **TOTAL:** Real = `{total_real:,} kg` | Reject = `{total_rij:,} kg` (**{pct_total:.2f}%**)")