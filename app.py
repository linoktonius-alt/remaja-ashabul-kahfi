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

with st.sidebar:
    st.markdown("## 📊 Praktikum Big Data")
    st.caption("Eksplorasi & Visualisasi Data Ekonomi")
    st.markdown("---")

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
    st.caption("💡 *Data tells a story.*")
    st.caption("© 2025 | REMAJA ASHABUL KAHFI")

st.caption("© 2025 | REMAJA ASHABUL KAHFI")

pg.run()