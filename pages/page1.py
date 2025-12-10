import streamlit as st
# Mengatur tampilan halaman
st.set_page_config(
    page_title="Selamat Datang",
    layout="wide",
)

st.title("Selamat datang di remaja-ashabul-kahfi")

st.markdown("---")

st.write("### Perkenalan")

st.markdown(
    """
    Situs ini dirancang sebagai sebuah platform informasi ekonomi yang menyajikan data penting mengenai perkembangan kondisi ekonomi Indonesia. Melalui tampilan yang sederhana, interaktif, dan mudah dipahami, situs ini bertujuan untuk membantu pengguna dalam memahami tiga indikator utama perekonomian, yaitu Indeks Harga Konsumen (IHK), Gini Ratio, dan Pertumbuhan Ekonomi.

    1. Indeks Harga Konsumen (IHK)

    Pada bagian IHK, situs ini menampilkan pergerakan harga barang dan jasa konsumsi rumah tangga dari waktu ke waktu. Informasi IHK digunakan untuk mengamati tingkat inflasi dan stabilitas harga. Melalui visualisasi data, pengguna dapat dengan cepat melihat tren kenaikan atau penurunan harga yang terjadi di Indonesia.

    2. Gini Ratio (Tingkat Ketimpangan)

    Situs ini juga menyajikan data Gini Ratio sebagai indikator ketimpangan pendapatan masyarakat. Melalui grafik dan informasi pendukung, pengguna dapat memahami perubahan tingkat kesenjangan ekonomi dari tahun ke tahun, sehingga dapat menjadi dasar analisis pemerataan pembangunan dan kesejahteraan.

    3. Pertumbuhan Ekonomi

    Pada bagian ini, situs menampilkan data pertumbuhan ekonomi yang diukur melalui Produk Domestik Bruto (PDB). Pengguna dapat melihat bagaimana laju pertumbuhan ekonomi Indonesia bergerak dari waktu ke waktu, serta memahami faktor-faktor yang memengaruhi dinamika ekonomi secara keseluruhan.

    Tujuan Pengembangan Situs

    Situs ini dikembangkan untuk:

    * Menyediakan informasi ekonomi yang akurat dan mudah diakses.

    * Membantu mahasiswa, peneliti, dan masyarakat luas memahami perkembangan kondisi ekonomi Indonesia.

    * Mendorong penggunaan data statistik resmi dalam analisis dan pengambilan keputusan.

    * Menjadikan data ekonomi lebih visual dan informatif melalui grafik, tabel, dan penjelasan yang ringkas.

    Sumber Data

    Seluruh data yang ditampilkan pada situs ini berasal dari Badan Pusat Statistik (BPS)—lembaga resmi penyedia data nasional—sehingga setiap informasi yang disajikan dapat dipertanggungjawabkan secara ilmiah dan akademik.
    """
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