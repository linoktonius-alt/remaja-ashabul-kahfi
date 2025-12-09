import streamlit as st
# Mengatur tampilan halaman
st.set_page_config(
    page_title="Selamat Datang",
    layout="wide",
)

st.title("Selamat datang di remaja-ashabul-kahfi")

st.markdown("---")

st.write("### Perkenalan")

st.write(
    "Selamat datang di Website Monitoring Perkembangan Ekonomi Indonesia.
Situs ini dibuat untuk memberikan informasi yang ringkas, akurat, dan mudah dipahami mengenai kondisi ekonomi Indonesia dari waktu ke waktu.

Dalam website ini, Anda dapat menemukan berbagai indikator ekonomi penting yang menjadi dasar dalam analisis makroekonomi nasional, antara lain:

Inflasi – menggambarkan tingkat kenaikan harga barang dan jasa.

Suku Bunga – mencerminkan kebijakan moneter dan memengaruhi aktivitas kredit serta konsumsi.

Kurs Rupiah – menunjukkan nilai tukar rupiah terhadap mata uang asing yang berdampak pada perdagangan dan stabilitas harga.

Produk Domestik Regional Bruto (PDRB) – mengilustrasikan kinerja ekonomi di tingkat daerah.

Pertumbuhan Ekonomi – memberikan gambaran mengenai ekspansi atau perlambatan aktivitas ekonomi nasional.

Website ini dirancang untuk membantu mahasiswa, peneliti, pembuat kebijakan, maupun masyarakat umum dalam memahami kondisi ekonomi terkini berbasis data yang tersusun secara visual dan informatif."
)

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