import streamlit as st
import pandas as pd
from ui_helper import load_global_style

st.set_page_config(
    page_title="Dataset | PadiPredict",
    page_icon="📊",
    layout="wide"
)

# LOAD CSS
load_global_style()

# HEADER
st.title("📊 Dataset Penelitian")

st.write(
    """
    Halaman ini menyajikan informasi dataset yang digunakan
    dalam pengembangan model prediksi produktivitas padi
    di Kabupaten Malang.
    """
)

st.divider()

# RINGKASAN DATASET
st.subheader("📌 Ringkasan Dataset")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Data", "528")
c2.metric("Kecamatan", "33")
c3.metric("Periode", "2009–2024")
c4.metric("Jumlah Variabel", "9")

st.divider()

# SUMBER DATA
st.subheader("📚 Sumber Dataset")

st.write(
    """
    Dataset penelitian berasal dari Mendeley Data
    dengan judul *Rice Harvest and Climate Data in Indonesia*.
    """
)

st.markdown(
    "[Lihat sumber dataset di Mendeley Data](https://data.mendeley.com/datasets/xjbj2g5dbx/1)"
)

st.divider()

# INFORMASI VARIABEL
st.subheader("🔍 Informasi Variabel")

data_variabel = pd.DataFrame({
    "Variabel": [
        "Kecamatan",
        "Tahun",
        "LUAS PANEN",
        "RATA-RATA PRODUKSI",
        "PRODUKSI",
        "TAVG",
        "RH_AVG",
        "RR",
        "SS"
    ],
    "Keterangan": [
        "Nama kecamatan",
        "Tahun pengamatan",
        "Luas panen padi",
        "Target prediksi produktivitas",
        "Total produksi padi",
        "Suhu rata-rata",
        "Kelembapan rata-rata",
        "Curah hujan",
        "Lama penyinaran matahari"
    ],
    "Peran": [
        "Fitur",
        "Fitur",
        "Pendukung analisis",
        "Target (Y)",
        "Pendukung analisis",
        "Fitur",
        "Fitur",
        "Fitur",
        "Fitur"
    ]
})

st.dataframe(
    data_variabel,
    width="stretch",
    hide_index=True
)

st.divider()

# INFORMASI PENELITIAN
st.subheader("🌾 Fokus Penelitian")

st.write(
    """
    Penelitian ini berfokus pada prediksi produktivitas padi
    menggunakan parameter agroklimat dan karakteristik wilayah.
    """
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Variabel Input (X)**")
    st.write(
        "- Kecamatan\n"
        "- Tahun\n"
        "- Suhu rata-rata (TAVG)\n"
        "- Kelembapan (RH_AVG)\n"
        "- Curah hujan (RR)\n"
        "- Penyinaran matahari (SS)"
    )

with col2:
    st.markdown("**Variabel Target (Y)**")
    st.write("RATA-RATA PRODUKSI")

st.info(
    "LUAS PANEN dan PRODUKSI digunakan untuk analisis "
    "eksploratif, bukan sebagai fitur input model prediksi."
)

st.divider()

st.caption(
    "PadiPredict | Kelompok 19 Machine Learning"
)
