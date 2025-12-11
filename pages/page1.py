import streamlit as st

st.set_page_config(
    page_title="Selamat Datang",
    layout="wide",
)

st.title("Selamat datang di remaja-ashabul-kahfi 🔐")

st.image("WELCOME_BIGDATA.png", use_container_width=True)

st.markdown("---")

st.write("### Perkenalan")

st.markdown(
    """
    Situs ini merupakan platform penyedia data ekonomi Indonesia yang menampilkan tiga indikator utama, yaitu **Indeks Harga Konsumen (IHK)**,
    **Kurs Rupiah**, dan **Nilai Impor Indonesia**. Data disajikan secara lengkap dari tahun **2006 hingga 2025**, 
    sehingga pengguna dapat memahami dinamika ekonomi nasional dalam jangka pendek maupun jangka panjang.

    ---
    ### Apa yang Disediakan Situs Ini?
    Website ini dirancang untuk menjadi pusat informasi dan analisis ekonomi yang mudah dipahami. 
    Dengan menyediakan data historis hampir dua dekade, pengguna dapat:
    - Menganalisis perkembangan inflasi melalui **IHK**
    - Memantau stabilitas nilai tukar melalui **data kurs Rupiah**
    - Mengamati tren impor Indonesia dari masa ke masa

    ---
    ## 📊 1. Indeks Harga Konsumen (IHK)
    IHK merupakan indikator utama untuk mengukur **inflasi**.  
    IHK menggambarkan perubahan harga barang dan jasa yang dikonsumsi masyarakat.

    Mengapa IHK penting?
    - menggambarkan tingkat inflasi bulanan maupun tahunan  
    - membantu pemerintah dan Bank Indonesia dalam menentukan kebijakan moneter  
    - memengaruhi daya beli, upah, dan kesejahteraan masyarakat  
    - menunjukkan tekanan harga dari sisi konsumsi rumah tangga  

    Data IHK dari 2006–2025 membantu pengguna melihat pola inflasi dari waktu ke waktu, termasuk periode krisis global, pandemi, hingga pemulihan ekonomi.

    ---
    ## 💱 2. Kurs Rupiah
    Nilai tukar Rupiah terhadap mata uang asing, khususnya USD, merupakan indikator penting bagi:
    - perdagangan internasional  
    - biaya impor  
    - stabilitas sektor keuangan  
    - aliran modal dan investasi  

    Dengan data kurs selama 2006–2025, pengguna dapat memahami dampak perubahan kebijakan, kondisi global, dan dinamika ekonomi internasional terhadap nilai tukar Rupiah.

    ---
    ## 🚢 3. Nilai Impor Indonesia
    Data impor digunakan untuk melihat kebutuhan Indonesia terhadap:
    - barang konsumsi  
    - bahan baku industri  
    - barang modal  

    Tren impor dapat menunjukkan:
    - kekuatan permintaan domestik  
    - ketergantungan industri terhadap bahan baku luar negeri  
    - kondisi pertumbuhan sektor manufaktur  
    - respon terhadap perubahan harga komoditas global  

    Data impor yang panjang (2006–2025) memberikan gambaran lengkap mengenai pola impor sebelum dan sesudah krisis global maupun pandemi.

    ---
    ## 🎯 Tujuan Website Ini
    Platform ini dibuat untuk:
    - analisis tren ekonomi  
    - riset akademik dan tugas kuliah  
    - pembuatan visualisasi grafik  
    - membantu masyarakat memahami dinamika ekonomi Indonesia  

    Dengan tampilan interaktif, filter dinamis, dan visualisasi yang informatif, situs ini diharapkan menjadi referensi data ekonomi yang mudah diakses oleh mahasiswa, peneliti, maupun publik umum.

    ---
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