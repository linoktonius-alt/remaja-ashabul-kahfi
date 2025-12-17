import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Praktikum Big Data",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Praktikum Big Data")
st.caption("Aplikasi interaktif untuk eksplorasi data dan visualisasi")

jam = datetime.now().hour

if jam < 11:
    st.success("🌤️ Selamat pagi, selamat belajar Big Data!")
elif jam < 15:
    st.info("☀️ Selamat siang, semangat eksplorasi data!")
elif jam < 18:
    st.warning("🌥️ Selamat sore, tetap fokus ya!")
else:
    st.error("🌙 Selamat malam, jangan lupa istirahat!")


pages = [
    st.Page("pages/page1.py", title="Home", icon="🏠"),
    st.Page("pages/page2.py", title="Data Masyarakat", icon="📈"),
    st.Page("pages/page3.py", title="Profil Pembuat", icon="👤"),
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

with st.sidebar:
    st.markdown("### 🔍 Informasi Aplikasi")
    st.info(
        """
        **Mata Kuliah**: Big Data  
        **Fungsi**:  
        - Eksplorasi data  
        - Visualisasi  
        - Analisis sederhana  
        """
    )

    st.markdown("---")

    mode = st.radio(
        "🎨 Mode Tampilan",
        ["Standar", "Fokus"]
    )

if mode == "Fokus":
    st.markdown(
        "<style>footer {visibility: hidden;}</style>",
        unsafe_allow_html=True
    )
    st.success("Mode fokus aktif — tampilan lebih bersih 👀")

st.markdown("---")
st.caption("© 2025 | REMAJA ASHABUL KAHFI")

pg.run()
