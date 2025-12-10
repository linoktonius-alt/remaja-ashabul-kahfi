import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(layout="wide", page_title="Dashboard Data Ekonomi Indonesia")

FILE_PATH = "bigdata_kelompok.csv"

@st.cache_data
def load_data():
    return pd.read_csv(FILE_PATH)

df = load_data()

st.sidebar.title("📊 Menu Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Tabel Data", "Visualisasi"])

st.sidebar.write("---")

warna_grafik = st.sidebar.color_picker("🎨 Pilih Warna Grafik", "#1f77b4")

size = st.sidebar.slider("Ukuran Grafik", 4, 15, 7)

st.sidebar.subheader("Filter Data")

if "Tahun" in df.columns:
    tahun_opsi = sorted(df["Tahun"].unique())
    tahun_pilih = st.sidebar.multiselect("Pilih Tahun:", tahun_opsi, default=tahun_opsi)
    df = df[df["Tahun"].isin(tahun_pilih)]

if "Bulan" in df.columns:
    bulan_opsi = sorted(df["Bulan"].unique())
    bulan_pilih = st.sidebar.multiselect("Pilih Bulan:", bulan_opsi, default=bulan_opsi)
    df = df[df["Bulan"].isin(bulan_pilih)]

if page == "Tabel Data":
    st.title("📋 Tabel Data Ekonomi Indonesia")

    st.write("### Data Lengkap Setelah Filter")
    st.dataframe(df, use_container_width=True)

    if st.checkbox("Tampilkan Statistik Deskriptif"):
        st.write(df.describe())

elif page == "Visualisasi":
    st.title("📈 Visualisasi Data Ekonomi")

    num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(num_cols) == 0:
        st.error("Tidak ada kolom numerik untuk divisualisasikan.")
    else:
        kolom_grafik = st.selectbox("Pilih Kolom untuk Grafik:", num_cols)

        jenis = st.radio("Jenis Grafik:", ["Line Chart", "Bar Chart", "Area Chart"])

        fig, ax = plt.subplots(figsize=(size, size))

        if jenis == "Line Chart":
            ax.plot(df[kolom_grafik], color=warna_grafik)
        elif jenis == "Bar Chart":
            ax.bar(df.index, df[kolom_grafik], color=warna_grafik)
        elif jenis == "Area Chart":
            ax.fill_between(df.index, df[kolom_grafik], color=warna_grafik, alpha=0.4)

        ax.set_title(f"{jenis}: {kolom_grafik}")
        ax.set_xlabel("Bulan")
        ax.set_ylabel(kolom_grafik)
        plt.xticks(rotation=45)

        st.pyplot(fig)