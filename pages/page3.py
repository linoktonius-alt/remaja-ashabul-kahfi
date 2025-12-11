import streamlit as st

st.title("👥 Profil Pembuat Website")
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

st.header("Anggota Tim")
st.write("Berikut adalah anggota yang terlibat dalam pembuatan website ini:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Cevin Rizki Octavian")
    st.write("""
    **NIM:021002305005**  
    **Program Studi:** Ekonomi Pembangunan   
    """)

with col2:
    st.subheader("Haizar Yusuf Fahrezzy")
    st.write("""
     🆔 **NIM:021002305020**  
    🎓**Program Studi:** Ekonomi Pembangunan    
    """)

with col3:
    st.subheader("Hafizh Alfani Rizqi")
    st.write("""
    **NIM:021002305016**  
    **Program Studi:** Ekonomi Pembangunan   
    """)

with col4:
    st.subheader("Rizkyana Maharani")
    st.write("""
    **NIM:021002305010**  
    **Program Studi:** Ekonomi Pembangunan   
    """)

st.markdown("---")

st.header("Tools yang Digunakan")
st.write("""
- Python  
- Pandas  
- Matplotlib  
- Plotly  
- Streamlit  
- Jupyter Lab  
""")

st.markdown("---")

# ====== QUOTES ======
st.info("“Sebutlah Namanya Tetap di Jalannya, Kelak Kau Meningat” – Pemuda Ashabul Kahfi ♥")

