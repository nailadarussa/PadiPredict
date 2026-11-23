
from pathlib import Path
import streamlit as st
import pandas as pd
import joblib
# ==========================================
# 1. KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="Prediksi | PadiPredict",
    page_icon="🌾",
    layout="wide"
)

# ==========================================
# 2. LOAD CSS
# ==========================================

ROOT_DIR = Path(__file__).resolve().parent.parent
CSS_PATH = ROOT_DIR / "assets" / "styles" / "style.css"

@st.cache_resource
def load_model():
    model_path = ROOT_DIR / "model_prediksi_padi_final_best.pkl"
    return joblib.load(model_path)

model = load_model()

if CSS_PATH.exists():
    st.markdown(
        f"<style>{CSS_PATH.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# 3. DATA KECAMATAN
# ==========================================

kecamatan_list = [
    "Ampelgading", "Bantur", "Bululawang", "Dampit",
    "Dau", "Donomulyo", "Gedangan", "Gondanglegi",
    "Jabung", "Kalipare", "Karangploso", "Kasembon",
    "Kepanjen", "Kromengan", "Lawang", "Ngajum",
    "Ngantang", "Pagak", "Pagelaran", "Pakis",
    "Pakisaji", "Poncokusumo", "Pujon", "Singosari",
    "Sumbermanjing", "Sumberpucung", "Tajinan",
    "Tirtoyudo", "Tumpang", "Turen", "Wagir",
    "Wajak", "Wonosari"
]

# ==========================================
# 4. HEADER
# ==========================================

st.title("🌾 Prediksi Produktivitas Padi")

st.write(
    """
    Masukkan informasi wilayah dan parameter agroklimat
    untuk melakukan estimasi produktivitas padi
    di Kabupaten Malang.
    """
)

st.divider()

# ==========================================
# 5. FORM INPUT
# ==========================================

st.subheader("📍 Informasi Wilayah")

with st.form("form_prediksi"):

    kecamatan = st.selectbox(
        "Pilih Kecamatan",
        options=kecamatan_list
    )

    tahun = st.number_input(
        "Tahun Pengamatan",
        min_value=2009,
        max_value=2100,
        value=2025,
        step=1
    )

    st.divider()

    st.subheader("🌤️ Parameter Agroklimat")

    col1, col2 = st.columns(2)

    with col1:
        tavg = st.number_input(
            "Suhu Rata-rata (TAVG)",
            min_value=0.0,
            max_value=50.0,
            value=24.0,
            step=0.1
        )

        rh_avg = st.number_input(
            "Kelembapan Rata-rata (RH_AVG)",
            min_value=0.0,
            max_value=100.0,
            value=78.0,
            step=0.1
        )

    with col2:
        rr = st.number_input(
            "Curah Hujan (RR)",
            min_value=0.0,
            value=20.0,
            step=0.1
        )

        ss = st.number_input(
            "Penyinaran Matahari (SS)",
            min_value=0.0,
            max_value=24.0,
            value=6.0,
            step=0.1
        )

    submit = st.form_submit_button(
        "🌱 Prediksi Produktivitas",
        use_container_width=True
    )


# ==========================================
# 5A. VALIDASI INPUT AGROKLIMAT
# ==========================================

if submit:

    rentang_data = {
        "TAVG": (23.28, 25.40, tavg),
        "RH_AVG": (75.52, 85.19, rh_avg),
        "RR": (4.23, 59.14, rr),
        "SS": (2.91, 7.72, ss)
    }

    parameter_di_luar = []

    for nama, (minimum, maksimum, nilai) in rentang_data.items():

        if nilai < minimum or nilai > maksimum:
            parameter_di_luar.append(
                f"{nama}: {nilai} "
                f"(rentang historis {minimum}–{maksimum})"
            )

    if parameter_di_luar:

        st.warning(
            "Beberapa parameter berada di luar rentang "
            "data historis penelitian:\n\n"
            + "\n".join(
                f"- {item}" for item in parameter_di_luar
            )
            + "\n\nMohon perhatikan interpretasi hasil prediksi."
        )



# ==========================================
# 6. HASIL PREDIKSI
# ==========================================

st.divider()
st.subheader("📊 Hasil Prediksi")

st.write(
    "Berikut adalah hasil estimasi produktivitas padi "
    "berdasarkan data wilayah dan parameter agroklimat."
)

if submit:

    st.success("Data input berhasil diterima!")

    # MENYIAPKAN DATA INPUT UNTUK MODEL
    input_data = pd.DataFrame([{
        "Kecamatan": kecamatan,
        "Tahun": int(tahun),
        "TAVG": tavg,
        "RH_AVG": rh_avg,
        "RR": rr,
        "SS": ss
    }])

    try:
        # MELAKUKAN PREDIKSI
        hasil_prediksi = float(model.predict(input_data)[0])

        col_result, col_location = st.columns([1.5, 1])

        # KARTU HASIL UTAMA
        with col_result:
            st.html(f"""
            <div style="
                background: linear-gradient(135deg, #205c45, #34835f);
                padding: 35px;
                border-radius: 20px;
                color: white;
                min-height: 245px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                box-shadow: 0 5px 18px rgba(0,0,0,0.08);
            ">
                <div style="
                    font-size: 14px;
                    font-weight: 600;
                    letter-spacing: 1px;
                ">
                    ESTIMASI PRODUKTIVITAS PADI
                </div>

                <div style="
                    font-size: 54px;
                    font-weight: 800;
                    margin: 18px 0 5px 0;
                ">
                    {hasil_prediksi:.2f}
                </div>

                <div style="font-size: 14px;">
                    Hasil estimasi berdasarkan model Linear Regression
                </div>

                <div style="
                    margin-top: 25px;
                    font-size: 13px;
                    opacity: 0.85;
                ">
                    🌾 PadiPredict | Kabupaten Malang
                </div>
            </div>
            """)

        # INFORMASI WILAYAH
        with col_location:

            st.metric(
                label="📍 Kecamatan",
                value=kecamatan
            )

            st.metric(
                label="📅 Tahun Prediksi",
                value=int(tahun)
            )

        # PARAMETER AGROKLIMAT
        st.divider()
        st.subheader("🌤️ Parameter Agroklimat")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("🌡️ Suhu Rata-rata", f"{tavg:.1f}")

        with col2:
            st.metric("💧 Kelembapan", f"{rh_avg:.1f}%")

        with col3:
            st.metric("🌧️ Curah Hujan", f"{rr:.1f}")

        with col4:
            st.metric("☀️ Penyinaran Matahari", f"{ss:.1f}")

        st.caption(
            "Nilai estimasi mengikuti satuan target "
            "RATA-RATA PRODUKSI pada dataset."
        )

    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")

else:

    st.info(
        "🌱 Silakan lengkapi formulir di atas dan tekan "
        "tombol Prediksi Produktivitas untuk melihat "
        "hasil estimasi."
    )


# ==========================================
# 7. FOOTER
# ==========================================

st.divider()

st.caption(
    "PadiPredict | Kelompok 19 Machine Learning"
)
