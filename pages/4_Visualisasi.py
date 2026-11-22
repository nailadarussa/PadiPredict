
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Visualisasi | PadiPredict",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# 2. LOAD CSS
# ==========================================

ROOT_DIR = Path(__file__).resolve().parent.parent
CSS_PATH = ROOT_DIR / "assets" / "styles" / "style.css"

if CSS_PATH.exists():
    st.markdown(
        f"<style>{CSS_PATH.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# 3. LOAD DATASET
# ==========================================

DATA_PATH = ROOT_DIR / "data" / "Data_Cropyield_Prediction.csv"

@st.cache_data
def load_data(path):
    return pd.read_csv(path)


st.title("📈 Visualisasi Data")

st.write(
    """
    Eksplorasi data produktivitas padi dan parameter
    agroklimat di Kabupaten Malang periode 2009–2024.
    """
)

st.divider()

if not DATA_PATH.exists():
    st.error(
        "Dataset tidak ditemukan. Pastikan file "
        "Data_Cropyield_Prediction.csv berada di folder data."
    )
    st.stop()

df = load_data(str(DATA_PATH))

# Kolom yang wajib tersedia
kolom_wajib = [
    "Kecamatan",
    "Tahun",
    "RATA-RATA PRODUKSI",
    "TAVG",
    "RH_AVG",
    "RR",
    "SS"
]

kolom_hilang = [
    kolom for kolom in kolom_wajib
    if kolom not in df.columns
]

if kolom_hilang:
    st.error(
        f"Kolom berikut tidak ditemukan dalam dataset: {kolom_hilang}"
    )
    st.stop()

# Konversi tipe data
kolom_numerik = [
    "Tahun",
    "RATA-RATA PRODUKSI",
    "TAVG",
    "RH_AVG",
    "RR",
    "SS"
]

for kolom in kolom_numerik:
    df[kolom] = pd.to_numeric(
        df[kolom],
        errors="coerce"
    )

df["Kecamatan"] = df["Kecamatan"].astype("string").str.strip()

df = df.dropna(
    subset=kolom_wajib
).copy()

df["Tahun"] = df["Tahun"].astype(int)

if df.empty:
    st.error("Dataset tidak memiliki data valid untuk divisualisasikan.")
    st.stop()

# ==========================================
# 4. RINGKASAN DATA
# ==========================================

st.subheader("📌 Ringkasan Data")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Jumlah Observasi",
    f"{len(df):,}"
)

c2.metric(
    "Jumlah Kecamatan",
    df["Kecamatan"].nunique()
)

c3.metric(
    "Rata-rata Produktivitas",
    f"{df['RATA-RATA PRODUKSI'].mean():.2f}"
)

c4.metric(
    "Periode Data",
    f"{df['Tahun'].min()}–{df['Tahun'].max()}"
)

st.divider()

# ==========================================
# 5. FILTER DATA
# ==========================================

st.subheader("🔎 Filter Visualisasi")

col1, col2 = st.columns(2)

with col1:
    tahun_tersedia = sorted(df["Tahun"].unique())

    tahun_pilihan = st.multiselect(
        "Pilih Tahun",
        options=tahun_tersedia,
        default=tahun_tersedia
    )

with col2:
    kecamatan_tersedia = sorted(
        df["Kecamatan"].dropna().unique().tolist()
    )

    kecamatan_pilihan = st.multiselect(
        "Pilih Kecamatan",
        options=kecamatan_tersedia,
        default=kecamatan_tersedia
    )

if not tahun_pilihan or not kecamatan_pilihan:
    st.warning("Pilih minimal satu tahun dan satu kecamatan.")
    st.stop()

data_filter = df[
    df["Tahun"].isin(tahun_pilihan)
    & df["Kecamatan"].isin(kecamatan_pilihan)
].copy()

if data_filter.empty:
    st.warning("Tidak ada data untuk kombinasi filter tersebut.")
    st.stop()


st.caption(
    f"Menampilkan {len(data_filter):,} baris data "
    f"dari {data_filter['Kecamatan'].nunique()} kecamatan."
)

# ==========================================
# DOWNLOAD DATA TERFILTER
# ==========================================

csv_download = data_filter.to_csv(
    index=False
).encode("utf-8-sig")

st.download_button(
    label="📥 Unduh Dataset Terfilter (CSV)",
    data=csv_download,
    file_name="PadiPredict_Dataset_Terfilter.csv",
    mime="text/csv",
    width="content"
)

st.divider()

# ==========================================
# 6. TREN PRODUKTIVITAS PER TAHUN
# ==========================================

st.subheader("📊 Tren Produktivitas Padi")

tren = (
    data_filter.groupby("Tahun", as_index=False)
    ["RATA-RATA PRODUKSI"].mean()
)

fig_tren = px.line(
    tren,
    x="Tahun",
    y="RATA-RATA PRODUKSI",
    markers=True,
    title="Rata-rata Produktivitas Padi per Tahun",
    labels={
        "Tahun": "Tahun",
        "RATA-RATA PRODUKSI": "Rata-rata Produktivitas"
    },
    template="plotly_white"
)

fig_tren.update_layout(
    hovermode="x unified",
    xaxis=dict(dtick=1)
)

st.plotly_chart(
    fig_tren,
    width="stretch"
)

st.divider()

# ==========================================
# 7. PERBANDINGAN PRODUKTIVITAS KECAMATAN
# ==========================================

st.subheader("📍 Perbandingan Produktivitas Kecamatan")

mode_kecamatan = st.radio(
    "Pilih tampilan perbandingan:",
    options=[
        "Semua Kecamatan",
        "10 Tertinggi",
        "10 Terendah"
    ],
    horizontal=True
)

per_kecamatan = (
    data_filter.groupby("Kecamatan", as_index=False)
    ["RATA-RATA PRODUKSI"].mean()
)

if mode_kecamatan == "10 Tertinggi":
    per_kecamatan = per_kecamatan.nlargest(
        10,
        "RATA-RATA PRODUKSI"
    )

elif mode_kecamatan == "10 Terendah":
    per_kecamatan = per_kecamatan.nsmallest(
        10,
        "RATA-RATA PRODUKSI"
    )

per_kecamatan = per_kecamatan.sort_values(
    "RATA-RATA PRODUKSI",
    ascending=True
)

fig_kecamatan = px.bar(
    per_kecamatan,
    x="RATA-RATA PRODUKSI",
    y="Kecamatan",
    orientation="h",
    title=f"Produktivitas Padi - {mode_kecamatan}",
    labels={
        "RATA-RATA PRODUKSI": "Rata-rata Produktivitas",
        "Kecamatan": "Kecamatan"
    },
    template="plotly_white"
)

fig_kecamatan.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(
    fig_kecamatan,
    width="stretch"
)

st.divider()

# ==========================================
# 8. DISTRIBUSI PRODUKTIVITAS
# ==========================================

st.subheader("📉 Distribusi Produktivitas")

nilai_rata_rata = data_filter[
    "RATA-RATA PRODUKSI"
].mean()

nilai_median = data_filter[
    "RATA-RATA PRODUKSI"
].median()

d1, d2 = st.columns(2)

d1.metric(
    "Rata-rata Produktivitas",
    f"{nilai_rata_rata:.2f}"
)

d2.metric(
    "Median Produktivitas",
    f"{nilai_median:.2f}"
)

fig_distribusi = px.histogram(
    data_filter,
    x="RATA-RATA PRODUKSI",
    nbins=25,
    title="Distribusi Nilai Produktivitas Padi",
    labels={
        "RATA-RATA PRODUKSI": "Produktivitas",
        "count": "Jumlah Observasi"
    },
    template="plotly_white"
)

# Garis rata-rata
fig_distribusi.add_vline(
    x=nilai_rata_rata,
    line_dash="dash",
    line_width=2,
    annotation_text=f"Rata-rata: {nilai_rata_rata:.2f}",
    annotation_position="top"
)

fig_distribusi.update_layout(
    bargap=0.08
)

st.plotly_chart(
    fig_distribusi,
    width="stretch"
)

st.caption(
    "Histogram menunjukkan sebaran nilai produktivitas. "
    "Garis putus-putus menunjukkan nilai rata-rata."
)

st.divider()

# ==========================================
# 9. HUBUNGAN AGROKLIMAT DENGAN PRODUKTIVITAS
# ==========================================

st.subheader("🌤️ Hubungan Parameter Agroklimat")

nama_parameter = {
    "TAVG": "Suhu Rata-rata (TAVG)",
    "RH_AVG": "Kelembapan Rata-rata (RH_AVG)",
    "RR": "Curah Hujan (RR)",
    "SS": "Penyinaran Matahari (SS)"
}

col1, col2 = st.columns(2)

with col1:
    parameter = st.selectbox(
        "Pilih Parameter Agroklimat",
        options=list(nama_parameter.keys()),
        format_func=lambda x: nama_parameter[x]
    )

with col2:
    warna_kecamatan = st.checkbox(
        "Bedakan warna berdasarkan kecamatan",
        value=False
    )

fig_hubungan = px.scatter(
    data_filter,
    x=parameter,
    y="RATA-RATA PRODUKSI",
    color="Kecamatan" if warna_kecamatan else None,
    hover_data=["Tahun", "Kecamatan"],
    title=f"Hubungan {nama_parameter[parameter]} dengan Produktivitas Padi",
    labels={
        parameter: nama_parameter[parameter],
        "RATA-RATA PRODUKSI": "Produktivitas"
    },
    template="plotly_white"
)

fig_hubungan.update_layout(
    legend_title_text="Kecamatan"
)

st.plotly_chart(
    fig_hubungan,
    width="stretch"
)

st.caption(
    "Grafik menunjukkan pola hubungan pada data historis "
    "dan tidak secara langsung membuktikan hubungan sebab-akibat."
)

st.divider()

# ==========================================
# 10. HEATMAP KORELASI
# ==========================================

st.subheader("🔗 Korelasi Antarvariabel")

st.write(
    """
    Heatmap digunakan untuk melihat kekuatan dan arah hubungan
    linear antarvariabel numerik dalam dataset.
    """
)

# Variabel target dan fitur yang direncanakan untuk model
kolom_korelasi = [
    "Tahun",
    "TAVG",
    "RH_AVG",
    "RR",
    "SS",
    "RATA-RATA PRODUKSI"
]

matriks_korelasi = data_filter[
    kolom_korelasi
].corr(method="pearson")

fig_korelasi = px.imshow(
    matriks_korelasi,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    title="Heatmap Korelasi Parameter Agroklimat dan Produktivitas",
    labels={
        "x": "Variabel",
        "y": "Variabel",
        "color": "Korelasi"
    }
)

st.plotly_chart(
    fig_korelasi,
    width="stretch"
)

st.caption(
    """
    Interpretasi umum:
    +1 menunjukkan korelasi positif sempurna,
    0 menunjukkan tidak adanya korelasi linear,
    dan -1 menunjukkan korelasi negatif sempurna.
    Korelasi tidak membuktikan hubungan sebab-akibat.
    """
)

st.info(
    """
    Catatan: Heatmap ini berfokus pada tahun, parameter agroklimat,
    dan variabel target. Variabel LUAS PANEN dan PRODUKSI tidak
    dimasukkan karena keduanya tidak direncanakan sebagai fitur
    """
)

st.divider()


# ==========================================
# 11. RINGKASAN INSIGHT OTOMATIS
# ==========================================

st.subheader("💡 Ringkasan Insight Data")

st.write(
    """
    Berikut merupakan ringkasan informasi yang dihasilkan
    secara otomatis berdasarkan data dan filter yang dipilih.
    """
)

# Rata-rata produktivitas setiap kecamatan
insight_kecamatan = (
    data_filter.groupby("Kecamatan")["RATA-RATA PRODUKSI"]
    .mean()
    .sort_values(ascending=False)
)

# Rata-rata produktivitas setiap tahun
insight_tahun = (
    data_filter.groupby("Tahun")["RATA-RATA PRODUKSI"]
    .mean()
    .sort_values(ascending=False)
)

# Korelasi parameter terhadap target
parameter_korelasi = ["TAVG", "RH_AVG", "RR", "SS"]

hasil_korelasi = (
    data_filter[parameter_korelasi + ["RATA-RATA PRODUKSI"]]
    .corr()["RATA-RATA PRODUKSI"]
    .drop("RATA-RATA PRODUKSI")
    .dropna()
)

# Menentukan kecamatan tertinggi dan terendah
kecamatan_tertinggi = insight_kecamatan.idxmax()
nilai_kecamatan_tertinggi = insight_kecamatan.max()

kecamatan_terendah = insight_kecamatan.idxmin()
nilai_kecamatan_terendah = insight_kecamatan.min()

# Menentukan tahun tertinggi dan terendah
tahun_tertinggi = insight_tahun.idxmax()
nilai_tahun_tertinggi = insight_tahun.max()

tahun_terendah = insight_tahun.idxmin()
nilai_tahun_terendah = insight_tahun.min()

# Menentukan parameter dengan korelasi absolut terbesar
if not hasil_korelasi.empty:
    parameter_terkuat = hasil_korelasi.abs().idxmax()
    nilai_korelasi_terkuat = hasil_korelasi[parameter_terkuat]
else:
    parameter_terkuat = None
    nilai_korelasi_terkuat = None

# Tampilan kartu insight
col1, col2 = st.columns(2)

with col1:
    st.success(
        f"""
        **🏆 Produktivitas Kecamatan Tertinggi**

        {kecamatan_tertinggi}

        Rata-rata: {nilai_kecamatan_tertinggi:.2f}
        """
    )

    st.info(
        f"""
        **📅 Tahun Produktivitas Tertinggi**

        {tahun_tertinggi}

        Rata-rata: {nilai_tahun_tertinggi:.2f}
        """
    )

with col2:
    st.warning(
        f"""
        **📉 Produktivitas Kecamatan Terendah**

        {kecamatan_terendah}

        Rata-rata: {nilai_kecamatan_terendah:.2f}
        """
    )

    st.info(
        f"""
        **📅 Tahun Produktivitas Terendah**

        {tahun_terendah}

        Rata-rata: {nilai_tahun_terendah:.2f}
        """
    )

st.divider()

if parameter_terkuat is not None:
    arah_korelasi = (
        "positif"
        if nilai_korelasi_terkuat > 0
        else "negatif"
    )

    st.markdown(
        f"""
        **🔬 Korelasi Parameter Agroklimat**

        Parameter dengan korelasi linear absolut terbesar
        terhadap produktivitas adalah **{parameter_terkuat}**,
        dengan koefisien korelasi **{nilai_korelasi_terkuat:.3f}**
        ({arah_korelasi}).
        """
    )
else:
    st.warning(
        "Korelasi belum dapat dihitung dari data yang dipilih."
    )

st.caption(
    """
    Catatan: Insight ini merupakan ringkasan statistik deskriptif.
    Korelasi tidak membuktikan hubungan sebab-akibat dan bukan
    merupakan hasil prediksi model machine learning.
    """
)

st.divider()

# ==========================================
# 11. TABEL DATA
# ==========================================

with st.expander("📋 Lihat Data yang Digunakan"):

    st.dataframe(
        data_filter.sort_values(
            ["Tahun", "Kecamatan"]
        ),
        width="stretch",
        hide_index=True
    )

# ==========================================
# 12. FOOTER
# ==========================================

st.divider()

st.caption(
    "PadiPredict | Data Exploration & Visualization"
)
