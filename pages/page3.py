import streamlit as st

st.title("👥 Profil Pembuat Website")

st.image(
    "PROFIL_BIGDATA.png",
    use_container_width=True,
    caption="Tim Pengembang Dashboard Praktikum Big Data"
)

st.markdown("---")

st.header("Tentang Tim Kami")
st.write("""
Website ini dikembangkan oleh kelompok **Pemuda Ashabul Kahfi** sebagai bagian dari proyek analisis 
data ekonomi Indonesia. Dashboard ini menampilkan informasi mengenai **Indeks Harga Konsumen (IHK)**, 
**Nilai Tukar (Kurs)**, serta **Data Impor Indonesia** dari tahun **2006 hingga 2025**.

Tujuan website ini adalah menyediakan visualisasi data ekonomi yang interaktif, informatif, dan mudah dipahami 
oleh mahasiswa, peneliti, maupun masyarakat umum.
""")

st.markdown("---")

st.header("🎯 Visi dan Misi")
st.success("""
**Visi:**  
Menyediakan visualisasi data ekonomi yang menarik, informatif, dan mudah dipahami oleh semua kalangan.

**Misi:**  
- 🔍 Mengolah data ekonomi Indonesia dengan akurat  
- 📊 Menyajikan grafik yang interaktif dan mudah diinterpretasi  
- 💡 Membantu mahasiswa dan masyarakat memahami kondisi ekonomi  
- 🌐 Membangun platform data yang modern dan mudah diakses  
""")

st.markdown("---")
st.header("😎 Anggota Tim")

anggota = {
    "Cevin Rizki Octavian": ("021002305005", "Ekonomi Pembangunan"),
    "Haizar Yusuf Fahrezzy": ("021002305020", "Ekonomi Pembangunan"),
    "Hafizh Alfani Rizqi": ("021002305016", "Ekonomi Pembangunan"),
    "Rizkyana Maharani": ("021002305010", "Ekonomi Pembangunan"),
}

cols = st.columns(4)

for col, (nama, data) in zip(cols, anggota.items()):
    with col:
        st.subheader(nama)
        st.write(f"""
        🆔 **NIM:** {data[0]}  
        🎓 **Program Studi:** {data[1]}
        """)
        if st.button(f"👋 Sapa {nama.split()[0]}", key=nama):
            st.toast(f"Halo dari {nama}! 👋")

st.markdown("---")

st.header("🧰Tools yang Digunakan")
st.write("""
**Bahasa & Library**
- 🐍 Python  
- 🟦 Pandas  
- 📈 Matplotlib  
- 📉 Plotly  

**Platform**
- 🟩 Streamlit  
- 📒 Jupyter Lab  
""")

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; font-size: 18px;'>
        <i>“Sebutlah namanya, tetap di jalannya. Kelak kau akan mengingat.”</i><br>
        <b>– Pemuda Ashabul Kahfi ♥</b>
    </div>
    """,
    unsafe_allow_html=True
)

st.success("Terima kasih telah mengunjungi halaman profil kami 🙏❤️")