import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

pages = [
    st.Page(page="pages/page1.py", title="Home", icon="🏠"),
    st.Page(page="pages/page2.py", title="Data Masyarakat", icon="🍕"),
    st.Page(page="pages/page3.py", title="Profil Pembuat", icon="🍪",)
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)
st.write("Tugas Praktikum Big Data")

pg.run()