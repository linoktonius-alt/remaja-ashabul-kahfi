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
    st.metric("Indikator Utama", "IHK", "Inflasi")
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
        Data mencakup tingkat inflasi bulanan (*m-to-m*) yang bersumber dari laporan resmi BPS.
        """
    )

with tab2:
    st.markdown(
        """
        **Kurs Rupiah terhadap USD** mencerminkan stabilitas ekonomi dan keuangan nasional.
        Data historis ini mencakup fluktuasi nilai tukar harian dan bulanan.
        """
    )

with tab3:
    st.markdown(
        """
        **Nilai Impor Indonesia** menunjukkan volume perdagangan barang luar negeri (Migas & Non-Migas) 
        dalam satuan Juta USD.
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
        """
    )

st.markdown("---")

st.subheader("📚 Sumber Data Resmi")
st.info("Seluruh data yang disajikan dalam dashboard ini diperoleh dari sumber terpercaya berikut:")

col_src1, col_src2, col_src3 = st.columns(3)

with col_src1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/28/Lambang_Badan_Pusat_Statistik_%28BPS%29_Indonesia.svg", width=50)
    st.markdown("**Data Impor Indonesia**")
    st.caption("Nilai Impor Migas & Non-Migas (Juta USD)")
    st.link_button("Buka Data BPS", "https://www.bps.go.id/id/statistics-table/2/MTc1NCMy/nilai-impor-migas-nonmigas--juta-us--.html")

with col_src2:
    st.markdown("### 📊")
    st.markdown("**Kurs USD/IDR**")
    st.caption("Data Historis Nilai Tukar Rupiah (Investing.com)")
    st.link_button("Buka Data Investing", "https://id.investing.com/currencies/usd-idr-historical-data")

with col_src3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/28/Lambang_Badan_Pusat_Statistik_%28BPS%29_Indonesia.svg", width=50)
    st.markdown("**Inflasi (IHK)**")
    st.caption("Tingkat Inflasi Konsumen Nasional Bulanan")
    st.link_button("Buka Data BPS", "https://www.bps.go.id/en/statistics-table/1/OTEzIzE=/tingkat-inflasi-harga-konsumen-nasional-bulanan--m-to-m----sup-1--sup---2022-100-.html")

st.markdown("---")

st.info("👉 Gunakan menu di sidebar untuk mulai melihat **Tabel Data** dan **Visualisasi Grafik**.")

st.markdown(
    """
    <div style='text-align: center; margin-top: 50px;'>
        <p style='font-size: 22px;'><b>Dipersembahkan oleh:</b></p>
        <p style='font-size: 18px;'>Cevin • Kiana • Hapis • Ucup</p>
        <p style='font-size: 14px;'>Tim Praktikum Big Data</p>
    </div>
    """,
    unsafe_allow_html=True
)