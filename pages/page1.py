import streamlit as st
# Mengatur tampilan halaman
st.set_page_config(
    page_title="Selamat Datang",
    layout="wide",
)

st.title("Selamat datang di remaja-ashabul-kahfi")

st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; margin-top: 50px;'>
        <p style='font-size: 24px;'>dipersembahkan oleh:</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style='text-align: center; font-size: 20px;'>
        <p>cevin</p>
        <p>yana</p>
        <p>hapis</p>
        <p>ucup</p>
    </div>
    """,
    unsafe_allow_html=True
)