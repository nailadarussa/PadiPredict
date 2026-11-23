import streamlit as st
import base64
from pathlib import Path

# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="PadiPredict | Smart Agriculture",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# 2. LOAD GLOBAL CSS + BACKGROUND IMAGE
# ==========================================

ROOT_DIR = Path(__file__).resolve().parent

def load_css():
    css_path = ROOT_DIR / "assets" / "styles" / "style.css"
    image_path = ROOT_DIR / "assets" / "images" / "rice-field-bg.jpeg"

    # Membaca file CSS
    css = css_path.read_text(encoding="utf-8")

    # Membaca dan mengubah gambar menjadi Base64
    image_base64 = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    # Mengganti placeholder gambar di CSS
    image_url = f"data:image/jpeg;base64,{image_base64}"
    css = css.replace("BACKGROUND_IMAGE", image_url)

    # Menerapkan CSS ke seluruh aplikasi
    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )


# Jalankan CSS
load_css()


# ==========================================
# 3. HERO SECTION
# ==========================================


st.markdown(
    """
    <div class="hero">
        <h1>🌾 PadiPredict</h1>
        <p style="font-size: 19px; font-weight: 600;">
            Smart Agriculture & Machine Learning
        </p>
        <p>
            Platform prediksi produktivitas padi berdasarkan parameter
            agroklimat di Kabupaten Malang.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ==========================================
# 4. INFORMASI PENELITIAN
# ==========================================

st.subheader("📊 Informasi Penelitian")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Wilayah Penelitian",
        "Kab. Malang"
    )

with col2:
    st.metric(
        "Jumlah Kecamatan",
        "33"
    )

with col3:
    st.metric(
        "Periode Dataset",
        "2009–2024"
    )

with col4:
    st.metric(
        "Jumlah Observasi",
        "528"
    )

st.divider()

# ==========================================
# 5. PENGENALAN APLIKASI
# ==========================================

st.header("Selamat Datang di PadiPredict")

st.write(
    """
    PadiPredict merupakan aplikasi berbasis Machine Learning
    yang dikembangkan untuk membantu memperkirakan
    produktivitas padi berdasarkan parameter agroklimat.

    Aplikasi ini menggunakan data historis wilayah
    Kabupaten Malang sebagai dasar eksplorasi dan
    pengembangan model prediksi.
    """
)

st.info(
    """
    **Tujuan Aplikasi**

    Memberikan gambaran estimasi produktivitas padi
    berdasarkan informasi suhu, kelembapan, curah hujan,
    penyinaran matahari, tahun, dan kecamatan.
    """
)

st.divider()

# ==========================================
# 6. FITUR APLIKASI
# ==========================================

st.subheader("🚀 Fitur PadiPredict")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 🔮 Prediksi Produktivitas")

        st.write(
            """
            Masukkan parameter agroklimat dan wilayah
            untuk mendapatkan estimasi produktivitas padi.
            """
        )

        st.caption("Menggunakan model Machine Learning.")

    with st.container(border=True):
        st.markdown("### 📊 Visualisasi Data")

        st.write(
            """
            Jelajahi tren produktivitas, distribusi data,
            perbandingan kecamatan, dan korelasi variabel.
            """
        )

        st.caption("Mendukung eksplorasi data historis.")

with col2:
    with st.container(border=True):
        st.markdown("### 📁 Dataset")

        st.write(
            """
            Lihat informasi dataset, variabel penelitian,
            dan data yang digunakan dalam pengembangan model.
            """
        )

        st.caption("Sumber data penelitian.")

    with st.container(border=True):
        st.markdown("### ℹ️ Tentang Aplikasi")

        st.write(
            """
            Pelajari tujuan penelitian, metode Machine Learning,
            ruang lingkup, dan informasi pengembangan aplikasi.
            """
        )

        st.caption("Informasi proyek PadiPredict.")

st.divider()

# ==========================================
# 7. ALUR PENGGUNAAN
# ==========================================

st.subheader("🧭 Cara Menggunakan PadiPredict")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 01. Eksplorasi Data")
    st.write(
        """
        Pelajari dataset dan karakteristik
        produktivitas padi melalui halaman Dataset
        dan Visualisasi.
        """
    )

with col2:
    st.markdown("### 02. Masukkan Parameter")
    st.write(
        """
        Pilih kecamatan, tahun, suhu, kelembapan,
        curah hujan, dan penyinaran matahari.
        """
    )

with col3:
    st.markdown("### 03. Lihat Hasil Prediksi")
    st.write(
        """
        Dapatkan estimasi produktivitas padi
        setelah model Machine Learning
        terintegrasi.
        """
    )

st.divider()

# ==========================================
# 8. METODE MACHINE LEARNING
# ==========================================

st.subheader("🧠 Metode Machine Learning")

st.write(
    """
    Proyek ini mengembangkan pendekatan regresi
    untuk memperkirakan produktivitas padi.
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Linear Regression**")
    st.caption("Model regresi linear sebagai baseline.")

with col2:
    st.markdown("**Decision Tree Regressor**")
    st.caption("Model berbasis struktur pohon keputusan.")

with col3:
    st.markdown("**Random Forest Regressor**")
    st.caption("Ensemble dari beberapa pohon keputusan.")

st.info(
    "Hasil prediksi akan tersedia setelah integrasi "
    "model Machine Learning dengan backend selesai."
)

# ==========================================
# 9. FOOTER
# ==========================================

st.divider()

st.caption(
    "PadiPredict | SKelompok 19 Machine Learning"
)

