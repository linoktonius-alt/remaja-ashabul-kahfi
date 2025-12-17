import streamlit as st

st.set_page_config(
    page_title="Selamat Datang | Dashboard Ekonomi Indonesia",
    layout="wide",
)

st.title("🔐 Selamat Datang di *remaja-ashabul-kahfi*")
st.caption("Dashboard Interaktif Data Ekonomi Indonesia (2006–2025)")

st.image("WELCOME_BIGDATA.png", use_container_width=True)

st.markdown("---")

st.subheader("📌 Ringkasan Indikator Utama")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Indikator", "IHK", "Inflasi")
with col2:
    st.metric("Nilai Tukar", "Kurs Rupiah", "USD/IDR")
with col3:
    st.metric("Perdagangan", "Nilai Impor", "Juta USD")

st.markdown("---")

st.subheader("📖 Perkenalan")

st.markdown(
    """
    Website ini merupakan **platform penyedia data ekonomi Indonesia** yang dirancang secara interaktif 
    untuk membantu pengguna memahami dinamika ekonomi nasional.

    Data yang ditampilkan mencakup **periode 2006–2025**, sehingga sangat relevan untuk:
    - analisis jangka pendek  
    - analisis tren jangka panjang  
    - kebutuhan akademik dan riset  
    """
)

st.markdown("---")
st.subheader("📊 Indikator yang Disediakan")

tab1, tab2, tab3 = st.tabs(["📈 IHK", "💱 Kurs Rupiah", "🚢 Impor Indonesia"])

with tab1:
    st.markdown(
        """
        **Indeks Harga Konsumen (IHK)** merupakan indikator utama untuk mengukur **inflasi**.

        **Mengapa IHK penting?**
        - Menggambarkan tingkat inflasi bulanan dan tahunan  
        - Menjadi dasar kebijakan moneter Bank Indonesia  
        - Berpengaruh terhadap daya beli dan kesejahteraan masyarakat  

        Data IHK 2006–2025 memungkinkan analisis:
        - krisis global  
        - periode pandemi  
        - fase pemulihan ekonomi
        """
    )

with tab2:
    st.markdown(
        """
        **Kurs Rupiah terhadap USD** mencerminkan stabilitas ekonomi dan keuangan nasional.

        Kurs berperan penting dalam:
        - perdagangan internasional  
        - biaya impor  
        - investasi dan arus modal  

        Dengan data historis panjang, pengguna dapat melihat pengaruh:
        - kebijakan moneter  
        - gejolak global  
        - kondisi ekonomi internasional
        """
    )

with tab3:
    st.markdown(
        """
        **Nilai Impor Indonesia** menunjukkan kebutuhan ekonomi terhadap barang luar negeri.

        Impor mencakup:
        - barang konsumsi  
        - bahan baku  
        - barang modal  

        Tren impor membantu memahami:
        - kekuatan permintaan domestik  
        - ketergantungan industri  
        - kondisi sektor manufaktur
        """
    )

st.markdown("---")
with st.expander("🎯 Tujuan Pembuatan Website", expanded=False):
    st.markdown(
        """
        Platform ini dikembangkan untuk:
        - analisis tren ekonomi Indonesia  
        - riset akademik dan tugas kuliah  
        - pembuatan visualisasi data  
        - meningkatkan literasi ekonomi masyarakat  

        Dengan **filter dinamis**, **grafik interaktif**, dan **interpretasi data otomatis**, 
        website ini diharapkan menjadi referensi yang mudah diakses oleh:
        - mahasiswa  
        - peneliti  
        - masyarakat umum
        """
    )

st.markdown("---")
st.info("👉 Gunakan menu di sidebar untuk mulai melihat **Tabel Data** dan **Visualisasi Grafik**.")

st.markdown(
    """
    <div style='text-align: center; margin-top: 50px;'>
        <p style='font-size: 22px;'><b>Dipersembahkan oleh:</b></p>
        <p style='font-size: 18px;'>cevin • yana • hapis • ucup</p>
    </div>
    """,
    unsafe_allow_html=True
)
