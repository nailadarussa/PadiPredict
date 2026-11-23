import streamlit as st
from ui_helper import load_global_style

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

load_global_style()

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

st.markdown("---")

st.markdown(
    '<h2 class="section-title">Tim Pengembang</h2>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="section-description">'
    'PadiPredict dikembangkan oleh Kelompok 19 '
    'sebagai bagian dari proyek Pembelajaran Mesin.'
    '</p>',
    unsafe_allow_html=True
)

st.markdown("### Kelompok 19")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-label">Anggota 1</div>
            <div class="info-value">Naiya Humaira Rusydi</div>
            <div class="result-note">J0404241014</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-label">Anggota 2</div>
            <div class="info-value">Al Fariz Muhammad Zibril</div>
            <div class="result-note">J0404241036</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-label">Anggota 3</div>
            <div class="info-value">Naila Darussalamah</div>
            <div class="result-note">J0404241059</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# 10. FOOTER
# ==========================================

st.divider()

st.caption(
    "PadiPredict | Kelompok 19 Machine Learning"
)
