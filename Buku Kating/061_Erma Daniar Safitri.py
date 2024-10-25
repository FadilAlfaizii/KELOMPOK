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
            "Departemen MEDKRAF",
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
            "people-fill",
        ],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#144259"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#3FBAD8",
            },
            "nav-link-selected": {"background-color": "#ffa500"},
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
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"NIM: {data_list[i]['NIM']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobi: {data_list[i]['Hobi']}")
            st.write(f"Sosial Media: {data_list[i]['Sosmed']}")
            st.write(f"Kesan: {data_list[i]['Kesan']}")
            st.write(f"Pesan: {data_list[i]['Pesan']}")
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
            "https://drive.google.com/uc?export=view&id=1rUlFycgljYeyz4ua9QghMisTyqD2dxH0",
            "https://drive.google.com/uc?export=view&id=1rTjpexeGwkHNX2gQSYt4zs6LT1nJEVML",
        ]
        data_list = [
            {
                "Nama": "Kharisma Gumilang",
                "NIM": "121450142",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Way Kandis",
                "Hobi": "Mendengarkan musik",
                "Sosmed": "@gumilangkharisma",
                "Kesan": "Kakak ini bijak banget!!",  
                "Pesan":"semoga cepat wisuda ya kak!!"# 1
            },
            {
                "Nama": "Pandra Insani Putra Azuar ",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "Kakak ini asik dan seru banget!!",  
                "Pesan":"Tetap berpegang teguh pada prinsip dan tujuan ya kak !!!"# 1
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "21",
                "Asal":"Pagaralam",
                "Alamat": "Kota Baru",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "Kakak ini seru dan periang banget!",  
                "Pesan":"semangat terus kak buat kedepannya !!!"# 1
            },
            {
                "Nama": "Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh, Sumatera barat",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "Kak putri lucu dan asik banget!",  
                "Pesan":"semangat terus kak buat kedepannya !!!"# 1
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "Kak hartiti baik banget ",  
                "Pesan":"semangat terus buat kuliahnya !!!"# 1
            },
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kota Baru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "Kak nadilla baik dan seru banget orangnya!!",  
                "Pesan":"jangan pernah berhenti belajar dan berkembang ya kak !!!"# 1
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
                "Nama": "Tri Murniya Ningsih",
                "NIM": "121450038",
                "Umur": "21",
                "Asal":"Bogor",
                "Alamat": "Raden Saleh",
                "Hobi": "Kalo ke coffe shop pesen red velvet bukan kopi",
                "Sosmed": "@trimurniyaa",
                "Kesan": "Kakak ini asik dan positive vibes banget!!",  
                "Pesan":"Terus jadi pribadi yang menebarkan energi positif ya kak !!!"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tangerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, Nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "Kakak ini humble sekali!!",  
                "Pesan":"semangat terus kak buat kuliahnya !!!"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "Kak wulan aktif banget!!",  
                "Pesan":"Jangan ragu untuk mengambil langkah besar, karena disanalah kamu akan menemukan peluang yang luar biasa "
            },
            {
                "Nama": "Annisa Dini Amaliya",
                "NIM": "121450079",
                "Umur": "21",
                "Asal":"Tangerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "Kakak ini seru dan ceria banget!!",  
                "Pesan":"semangat terus buat menyelesaikan studi dan mencapai impian nya !!!"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger Lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "Kakak ini sangat ramah!!",  
                "Pesan":"jangan berhenti berkembang dan belajar !!!"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Batu Raja, Sumatera Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "Kakak ini sangat inspiratif!!",  
                "Pesan":"Semoga sukses dalam setiap langkah yang diambil kedepannya !!!"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "kakak ini sangat lucu dan ramah banget!!",  
                "Pesan":" Jangan pernah berhenti berkarya untuk meraih lebih banyak lagi prestasi!!!"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Sukabumi, Jawa Barat",
                "Alamat": "Natar",
                "Hobi": "Suka ikut tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "kak dhea lucu bangett!!",  
                "Pesan":" Semoga kakak selalu menghadirkan inovasi baru yang bermanfaat!!!"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "121450156",
                "Umur": "22",
                "Asal":"Surakarta, Jawa Tengah",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film, dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "kakak ini sangat mengayomi",  
                "Pesan":" Jangan berhenti untuk terus berkontribusi di bidang yang kakak geluti"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "kakak ini sangat humoris!!",  
                "Pesan":" Tetaplah menjadi panutan yang baik"
            },
            {
                "Nama": "Berlianda Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Main Game",
                "Sosmed": "@berlyyanda",
                "Kesan": "kakak ini sangat ramah dan sopan",  
                "Pesan":" Dalam kesibukan yang ada, jangan lupa untuk selalu menjaga kesehatan ya kak!!"# 1
            },
        ]          
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11hywXX8apCbAdS3KcJOYXg4TxVC0tFmF",
            "https://drive.google.com/uc?export=view&id=11i9vZHyLLnTzny7umkmYXaC0wUWgmvG1",
        ]
        data_list = [
            {
                "Nama": "Anissa Luthfi Alifia",
                "NIM": "121",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat ramah",  
                "Pesan":"Kakak sangat inspiratif, semoga saya bisa seperti kakak"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat bertanggungjawab",  
                "Pesan":"Semoga kekeluargaan dan semangat yang kakak tunjukkan terus terjaga!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "Dimas Rizky Ramadhani",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Orang yang sangat ramah",  
                "Pesan":"Semoga sukses di masa depan"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat seru",  
                "Pesan":"Semoga tetap rendah hati dan tetap semangat"
            },
            {
                "Nama": "Akbar Resdika",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat humble dan seru",  
                "Pesan":"Tetaplah menjadi panutan yang luar biasa"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat ramah",  
                "Pesan":"Jadilah pribadi yang berkembang dan selalu rendah hati"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat berwibawa",  
                "Pesan":"Tetaplah berjuang meraih cita-cita tanpa melupakan prinsip"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat ramah dan baik hati",  
                "Pesan":"Tetaplah menjadi pribadi yang terus menginspirasi"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Baik dan humble",  
                "Pesan":"Semoga tetap rendah hati dan selalu semangat dalam berkarya"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat ramah",  
                "Pesan":"Tetap menjadi pribadi yang rendah hati dan tulus"
            },
            {
                "Nama": "Dearni Monica Br Manik",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sosok yang bertanggungjawab ",  
                "Pesan":"Semoga tetap menjadi pribadi yang dapat bertanggungjawab"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat ramah",  
                "Pesan":"Tetap menjadi pribadi yang rendah hati dan penuh semangat"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat seru dan asik",  
                "Pesan":"Semoga bisa menjadi sosok yang inspiratif"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "Sangat baik hati",  
                "Pesan":"Tetaplah memberi inspirasi untuk generasi berikutnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=128yynqvz4CmtBRrHTRN2O4ug8c23-RaM",
            "https://drive.google.com/uc?export=view&id=1132zsyGXlz92uW5EpboIy_Ps-UboObs7O",
            "https://drive.google.com/uc?export=view&id=11j1ls01RlrSVzKM76ANQH2VSYbVMWCS_",
            "https://drive.google.com/uc?export=view&id=11sJNkeXn_1dpZh23B75fM0LDm2erQquM",
            "https://drive.google.com/uc?export=view&id=11vs3PUfEmevhWgzsqS5XjE_fWxSJ71MT",
            "https://drive.google.com/uc?export=view&id=11w-bZKkb7Kkm6SjMBzCPXf8LSOQHf2PD",
            "https://drive.google.com/uc?export=view&id=11sRjPGbnPSw8mEbB2FTHLtU7RFhHq1hw",
            "https://drive.google.com/uc?export=view&id=11t-v3wNikgB0MoNG78cOqOjvgqn4r7tj",
            "https://drive.google.com/uc?export=view&id=11wwS_n9t_WbVPsmb_DnTVEW8kTL0zTL-",
            "https://drive.google.com/uc?export=view&id=12G98bFwlL5J0QIBKf0t1UrxHj1l_JnEC",
            "https://drive.google.com/uc?export=view&id=12_xjs8EQzz2eBEJkdIVl_6gKVIF0uHd2",
            "https://drive.google.com/uc?export=view&id=12ThCuLXHDtTHvKP8iQU9tkbmji-W1rUo",
            "https://drive.google.com/uc?export=view&id=12XbC1dHXx0vY1xq0TvcfqSSpd14Xpyv2",
            "https://drive.google.com/uc?export=view&id=12dx_CO2KJiN80HoLNohk-TJYR-QHVzlc",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=12RIAj5P9dmWyqcuvX-M1cMKgCjzqoDad",
            "https://drive.google.com/uc?export=view&id=12Iu0WBOtCVAFVZUJTDjbSOHo9aJyMdeJ",
            "https://drive.google.com/uc?export=view&id=130-d7hon8SkXwN1jUGI4A_OfOcV73WEN",
            "https://drive.google.com/uc?export=view&id=12yrM8W3w6eRMhXPHhWAC80Xpc-1cxCpZ",
            "https://drive.google.com/uc?export=view&id=136A2jnAbi74NuEOSaudzlvvmLkUgTvdc",
            "https://drive.google.com/uc?export=view&id=13-BiuLujFSjuiKaK4CUDzNjCwU-L0UlA",
            "https://drive.google.com/uc?export=view&id=12xCkz96kszReeyGja7S2L2w79tLeLRdA",
        ]
        data_list = [
            {
                "Nama": "Ericson Chandra Sihombing",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Elisabeth Claudia Simanjuntak",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Eksanty F. Sukma Islamiaty",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Oktavia Nurwenda Puspita Sari",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Presilia",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Gede Moana",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "",
                "NIM": "",
                "Umur": "",
                "Asal":"",
                "Alamat": "",
                "Hobi": "",
                "Sosmed": "",
                "Kesan": "",  
                "Pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

# Tambahkan menu lainnya sesuai kebutuhan