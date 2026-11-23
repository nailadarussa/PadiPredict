
from pathlib import Path
import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Tentang | PadiPredict",
    page_icon="🌾",
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
# 3. HEADER
# ==========================================

st.title("🌾 Tentang PadiPredict")

st.write(
    """
    Mengenal lebih jauh aplikasi, tujuan penelitian,
    dan teknologi yang digunakan dalam pengembangan PadiPredict.
    """
)

st.divider()

# ==========================================
# 4. PROFIL APLIKASI
# ==========================================

st.subheader("🌱 Apa Itu PadiPredict?")

st.write(
    """
    **PadiPredict** merupakan aplikasi berbasis Machine Learning
    yang dikembangkan untuk memperkirakan produktivitas padi
    berdasarkan parameter agroklimat dan karakteristik wilayah
    kecamatan di Kabupaten Malang.

    Aplikasi ini dirancang sebagai sarana pemanfaatan data
    pertanian dan iklim untuk menghasilkan estimasi produktivitas
    yang dapat membantu memberikan gambaran mengenai kondisi
    produktivitas padi di suatu wilayah.
    """
)

st.divider()

# ==========================================
# 5. TUJUAN PENELITIAN
# ==========================================

st.subheader("🎯 Tujuan Pengembangan")

tujuan = [
    (
        "Analisis Data",
        "Mengidentifikasi pola hubungan antara parameter "
        "agroklimat dan produktivitas padi."
    ),
    (
        "Prediksi Produktivitas",
        "Mengembangkan model Machine Learning untuk "
        "memperkirakan produktivitas padi."
    ),
    (
        "Pemanfaatan Teknologi",
        "Menyediakan aplikasi sederhana untuk mencoba "
        "estimasi berdasarkan parameter yang dimasukkan."
    )
]

cols = st.columns(3)

for col, (judul, deskripsi) in zip(cols, tujuan):
    with col:
        with st.container(border=True):
            st.markdown(f"### {judul}")
            st.write(deskripsi)

st.divider()

# ==========================================
# 6. CAKUPAN PENELITIAN
# ==========================================

st.subheader("📍 Cakupan Penelitian")

c1, c2 = st.columns(2)

with c1:
    st.markdown("**Wilayah Penelitian**")
    st.write("Kabupaten Malang, Jawa Timur")

    st.markdown("**Jumlah Wilayah**")
    st.write("33 kecamatan")

with c2:
    st.markdown("**Periode Dataset**")
    st.write("2009–2024")

    st.markdown("**Target Prediksi**")
    st.write("RATA-RATA PRODUKSI")

st.divider()

# ==========================================
# 7. METODE MACHINE LEARNING
# ==========================================

# ==========================================
# 7. METODE MACHINE LEARNING
# ==========================================

st.subheader("🤖 Metode Machine Learning")

st.write(
    """
    PadiPredict menggunakan pendekatan regresi
    untuk memperkirakan produktivitas padi berdasarkan
    parameter agroklimat dan karakteristik wilayah.
    """
)

metode = [
    (
        "Linear Regression",
        "Model regresi linear yang dipilih sebagai model final "
        "berdasarkan hasil perbandingan performa pada data testing."
    ),
    (
        "Decision Tree Regressor",
        "Model pembanding berbasis pohon keputusan."
    ),
    (
        "Random Forest Regressor",
        "Model pembanding berbasis ensemble pohon keputusan "
        "yang juga diuji melalui hyperparameter tuning."
    )
]

for nama, deskripsi in metode:
    with st.expander(nama):
        st.write(deskripsi)

st.success(
    "Model final PadiPredict: Linear Regression."
)

st.caption(
    "Pemilihan model didasarkan pada hasil evaluasi "
    "performa model pada data testing."
)

# ==========================================
# 8. BATASAN APLIKASI
# ==========================================

st.subheader("ℹ️ Batasan Aplikasi")

st.warning(
    """
    Hasil prediksi merupakan estimasi berdasarkan pola
    yang dipelajari dari dataset penelitian.

    Akurasi estimasi bergantung pada kualitas data dan
    karakteristik model. Faktor lain seperti varietas,
    kondisi tanah, irigasi, pemupukan, dan serangan hama
    belum seluruhnya tercakup dalam variabel penelitian.
    """
)

st.divider()

# ==========================================
# 9. TIM PENGEMBANG
# ==========================================

st.subheader("👥 Tim Pengembang")

st.write(
    """
    PadiPredict dikembangkan secara berkelompok sebagai
    bagian dari proyek mata kuliah Pembelajaran Mesin.
    """
)

st.info(
    "Nama anggota dan pembagian kontribusi tim dapat "
    "ditambahkan setelah disepakati bersama kelompok."
)

# ==========================================
# 10. FOOTER
# ==========================================

st.divider()

st.caption(
    "PadiPredict | Kelompok 19 Machine Learning"
)
