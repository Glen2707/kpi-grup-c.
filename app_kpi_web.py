import streamlit as st

# 1. Konfigurasi Halaman & Styling
st.set_page_config(page_title="Sistem Komando KPI Grup C", page_icon="📊", layout="centered")

# Sembunyikan Header, Footer, dan Tombol Deploy Streamlit
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
st.title("📊 MONITOR KPI GRUP C")
st.caption("Aplikasi Komando Rekapitulasi KPI Bahan Baku 2026")
st.divider()

# 3. Database Rekapitulasi KPI 2026 (Sangat Mudah Di-update Nanti!)
DATA_KPI_2026 = {
    "Januari":  {"cw": 474402.00, "spb": 180637.00, "paid_karu": 1919.00, "paid_wt": 380.00},
    "Februari": {"cw": 400056.00, "spb": 162814.00, "paid_karu": 1545.49, "paid_wt": 321.88},
    "Maret":    {"cw": 68277.60,  "spb": 24085.00,  "paid_karu": 224.00,  "paid_wt": 56.00},
    "April":    {"cw": 346951.36, "spb": 152698.90, "paid_karu": 1484.00, "paid_wt": 324.00},
    "Mei":      {"cw": 465804.96, "spb": 273485.18, "paid_karu": 1913.00, "paid_wt": 374.50},
    "Juni":     {"cw": 294099.44, "spb": 280349.40, "paid_karu": 1882.42, "paid_wt": 368.50},
    # Nanti bulan Juli & seterusnya tinggal tambahkan baris baru di sini!
}

# 4. Form Pilihan Dropdown
col1, col2 = st.columns(2)
with col1:
    bulan = st.selectbox("🗓️ Pilih Bulan:", list(DATA_KPI_2026.keys()))
with col2:
    jabatan = st.selectbox("👤 Pilih Jabatan:", ["KARU - Muhammad Syahid", "KARU - Joko Sudiyono", "KASIE - Widodo"])

# 5. Kalkulasi Otomatis
d = DATA_KPI_2026[bulan]
total_sj = d['cw'] + d['spb']

if "KASIE" in jabatan:
    paid_hour = d['paid_karu'] + d['paid_wt']
    target_std = 287.92
else:
    paid_hour = d['paid_karu']
    target_std = 342.00

kpi_skor = total_sj / paid_hour if paid_hour > 0 else 0

# 6. Tampilan Ringkasan Produksi
st.subheader("📋 Ringkasan Data Produksi")
st.write(f"- **TK CW:** {d['cw']:,.2f} kg")
st.write(f"- **TK SPB:** {d['spb']:,.2f} kg")
st.write(f"- **Total SJ Attb:** {total_sj:,.2f} kg")
st.write(f"- **Paid Hour (Terpisah Otomatis):** {paid_hour:,.2f} jam")

st.divider()

# 7. Tampilan Hasil Evaluasi KPI
if kpi_skor >= target_std:
    st.success(f"🔥 **STATUS: TERCAPAI!**\n\nSkor KPI {jabatan} Bulan {bulan}: **{kpi_skor:.2f}** (Target Standar: {target_std})")
else:
    st.error(f"❌ **STATUS: TIDAK TERCAPAI**\n\nSkor KPI {jabatan} Bulan {bulan}: **{kpi_skor:.2f}** (Target Standar: {target_std})")