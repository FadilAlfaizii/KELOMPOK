import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rBy7haERpdkiLtRRUTaOVnLAjavTx_ss",
            "https://drive.google.com/uc?export=view&id=1rVvTqwFkMPViz3saDK6dn5GI0Xzlvi0V",
            "https://drive.google.com/uc?export=view&id=1rLtiAvVUlZ5IbDNxe6z7X38KP_Xg_I3_",
            "https://drive.google.com/uc?export=view&id=1f6ddHSmvpkmfIzikLm160sU-vVLb7Irr",
            "https://drive.google.com/uc?export=view&id=1rTjpexeGwkHNX2gQSYt4zs6LT1nJEVML",
            "https://drive.google.com/uc?export=view&id=1rUlFycgljYeyz4ua9QghMisTyqD2dxH0",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Way Kandis",
                "hobbi": "Mendengarkan musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Kakak ini bijak banget!!",  
                "pesan":"semoga cepat wisuda ya kak!!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azuar",
                "nim": "121450137",
                "umur": "21",
                "asal":"Lampung Utara",
                "alamat": "Sukarame",
                "hobbi": "Main gitar",
                "sosmed": "@pndrinsani27",
                "kesan": "Kakak ini asik dan seru banget!!",  
                "pesan":"Tetap berpegang teguh pada prinsip dan tujuan ya kak !!!"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "21",
                "asal":"Pagaralam",
                "alamat": "Kota Baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak ini seru dan periang banget!",  
                "pesan":"semangat terus kak buat kedepannya !!!"# 1
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin pandra main gitar",
                "sosmed": "@ptrimaulidas_",
                "kesan": "Kak putri lucu dan asik banget!",  
                "pesan":"semangat terus kak buat kedepannya !!!"# 1
            },
            {
                "nama": "Nadilla Andhara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "@nadilaandr26",
                "kesan": "Kak nadilla baik dan seru banget orangnya!!",  
                "pesan":"jangan pernah berhenti belajar dan berkembang ya kak !!!"# 1
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kak hartiti baik banget ",  
                "pesan":"semangat terus buat kuliahnya !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rcktYkcJwugxd5xNIFK1xQFZ9pIXh3UG",
            "https://drive.google.com/uc?export=view&id=1rrGHaFbvLC8zbh_Kt4Vg6uimqrf1TAAo",
            "https://drive.google.com/uc?export=view&id=1rmd1MoJugHcDk-U2wKNmwfcUfY479QhJ",
            "https://drive.google.com/uc?export=view&id=1roDgT3uZAj96_wawsqEB2kR11N6pbgrx",
            "https://drive.google.com/uc?export=view&id=1ru7FdU70j6r7OukziTDSqTSjjx-IiQPQ",
            "https://drive.google.com/uc?export=view&id=1rZjwvNxAZMCfrgADWsxJ6nK-ftIx55BB",
            "https://drive.google.com/uc?export=view&id=1rcTm-xC8Mwbzc2RjPBAVTw7z_TmAQpnJ",
            "https://drive.google.com/uc?export=view&id=1rfYqgB7cNmhWXnI8dhEJ4iI_tFsjLyAY",
            "https://drive.google.com/uc?export=view&id=1rwefpfPMwmA0VUFqVWxxSSOga4rgfN7H",
            "https://drive.google.com/uc?export=view&id=1rgDkCA0h6QVuoIDvtY_80FJCRgveRIVS",
            "https://drive.google.com/uc?export=view&id=1s50beAtpw9TKbFUkwRE7sciUOAQEw6u3",
        ]
        data_list = [
            {
                "nama": "Tri Murniya Ningsih",
                "nim": "121450038",
                "umur": "21",
                "asal":"Bogor",
                "alamat": "Raden Saleh",
                "hobbi": "Kalo ke coffe shop pesen red velvet bukan kopi",
                "sosmed": "@trimurniyaa",
                "kesan": "Kakak ini asik dan positive vibes banget!!",  
                "pesan":"Terus jadi pribadi yang menebarkan energi positif ya kak !!!"
            },
            {
                "nama": "Annisa Cahyani Surya",
                "nim": "121450114",
                "umur": "21",
                "asal":"Tangerang Selatan",
                "alamat": "Way Huwi",
                "hobbi": "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan": "Kakak ini humble sekali!!",  
                "pesan":"semangat terus kak buat kuliahnya !!!"# 1
            },
            {
                "nama": "Wulan Sabina",
                "nim": "121450150",
                "umur": "21",
                "asal":"Medan",
                "alamat": "Raden Saleh",
                "hobbi": "Nonton drakor",
                "sosmed": "@wlnsbn0",
                "kesan": "Kak wulan aktif banget!!",  
                "pesan":"Jangan ragu untuk mengambil langkah besar, karena disanalah kamu akan menemukan peluang yang luar biasa "# 1
            },
            {
                "nama": "Annisa Dini Amaliya",
                "nim": "121450079",
                "umur": "21",
                "asal":"Tangerang",
                "alamat": "Jati Agung",
                "hobbi": "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan": "Kakak ini seru dan ceria banget!!",  
                "pesan":"semangat terus buat menyelesaikan studi dan mencapai impian nya !!!"# 1
            },
            {
                "nama": "Renisha Putri Giani",
                "nim": "122450079",
                "umur": "21",
                "asal":"Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Denger Lagu",
                "sosmed": "@fleurnsh",
                "kesan": "Kakak ini sangat ramah!!",  
                "pesan":"jangan berhenti berkembang dan belajar !!!"# 1
            },
            {
                "nama": "Feryadi Yulius",
                "nim": "122450087",
                "umur": "20",
                "asal":"Batu Raja, Sumatera Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Baca buku",
                "sosmed": "@fer_yulius",
                "kesan": "Kakak ini sangat inspiratif!!",  
                "pesan":"Semoga sukses dalam setiap langkah yang diambil kedepannya !!!"# 1
            },
            {
                "nama": "Mirzan Yusuf Rabbani",
                "nim": "122450118",
                "umur": "20",
                "asal":"Jakarta",
                "alamat": "Korpri",
                "hobbi": "Main kucing",
                "sosmed": "@myrrinn",
                "kesan": "kakak ini sangat lucu dan ramah banget!!",  
                "pesan":" Jangan pernah berhenti berkarya untuk meraih lebih banyak lagi prestasi!!!"# 1
            },
            {
                "nama": "Dhea Amelia Putri",
                "nim": "122450004",
                "umur": "20",
                "asal":"Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi": "Suka ikut tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan": "kak dhea lucu bangett!!",  
                "pesan":" Semoga kakak sellau menghadirkan inovasi baru yang bermanfaat!!!"# 1
            },
            {
                "nama": "Muhammad Fahrul Aditya",
                "nim": "121450156",
                "umur": "22",
                "asal":"Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film, dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan": "kakak ini sangat mengayomi",  
                "pesan":" Jangan berhenti untuk terus berkontribusi di bidang yang kakak geluti"# 1
            },
            {
                "nama": "Jeremia Susanto",
                "nim": "122450022",
                "umur": "20",
                "asal":"Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi": "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan": "kakak ini sangat humoris!!",  
                "pesan":" Tetaplah menjadi panutan yang baik"# 1
            },
            {
                "nama": "Berlianda Enda Putri",
                "nim": "122450065",
                "umur": "21",
                "asal":"Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi": "Main Game",
                "sosmed": "@berlyyanda",
                "kesan": "kakak ini sangat ramah dan sopan",  
                "pesan":" Dalam kesibukan yang ada, jangan lupa untuk selalu menjaga kesehatan ya kak!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "nama": "Kakak D",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak E",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak D",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
            "https://drive.google.com/uc?export=view&id=",
        ]
        data_list = [
            {
                "nama": "Kakak D",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "nama": "Kakak E",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "nama": "Kakak D",
                "nim": "122450000",
                "umur": "18",
                "asal":"Bekasi",
                "alamat": "Gg.sakum",
                "hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhann
