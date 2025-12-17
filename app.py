import streamlit as st

st.set_page_config(
    page_title="Praktikum Big Data",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Praktikum Big Data")
st.caption("Aplikasi interaktif untuk eksplorasi data dan visualisasi")

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
st.caption("© 2025 | Praktikum Big Data")

pg.run()
