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
                "Pesan":"semoga cepat wisuda ya kak!!"
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
            "https://drive.google.com/uc?export=view&id=11i9vZHyLLnTzyn7umkmYXaC0wUWgmvG1",
        ]
        data_list = [
            {
                "Nama": "Anissa Luthfi Alifia",
                "NIM": "121450093",
                "Umur": "22",
                "Asal": "Lampung Tengah",
                "Alamat": "Kost Putri Rahayu",
                "Hobi": "Bernyanyi",
                "Sosmed": "@anissaluthfi_",
                "Kesan": "Sangat ramah sekali",  
                "Pesan":  "Semoga kakak sukses dalam segala hal yang dikerjakan"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "Sangat menginspirasi",  
                "Pesan": "Semoga rasa kekeluargaan yang sudah dibangun tetap terjaga"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16YTPu3GnLDG2WJmj6ss6kbtETpsEAFuk",
            "https://drive.google.com/uc?export=view&id=16b-ThTEEkflmh9S3Cj3j7rfCHlHUT2Q6",
            "https://drive.google.com/uc?export=view&id=16fNze1dbN4TJ1PlcbXXT-tQ_RAmAq2Tu",
            "https://drive.google.com/uc?export=view&id=16RsK3rwfR2BYkViPl0cGMdNovnZusoH_",
            "https://drive.google.com/uc?export=view&id=16iECT5D5UVPLHVwqdZfoiUta9Q2obzfX",
            "https://drive.google.com/uc?export=view&id=16v03QW2cOybh-blWBB8u-jKdZAf3MAyK",
            "https://drive.google.com/uc?export=view&id=16b3rlSHD6wJHtwBQ7tobE8W90eIAc1mP",
            "https://drive.google.com/uc?export=view&id=16Z-InHM7KHWIpu71swYMkVieYroWEonU",
            "https://drive.google.com/uc?export=view&id=16xToTBXBV2BtOLBGAiqA-OxXf_xMtFvA",
            "https://drive.google.com/uc?export=view&id=17--OH23jS98aG3vlC_Mp1wdr9KpGLr-g",
            "https://drive.google.com/uc?export=view&id=171ncktWkp-Y8nNZUfGFTQSu3BXfpwFmV",
            "https://drive.google.com/uc?export=view&id=16dAZ1vG_rfmIeZIvxB7NiDTcbU974mSn",
        ]
        data_list = [
            {
                "Nama": "Dimas Rizky Ramadhani",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Pamulang Tangsel",
                "Alamat": "Way Kandis (Kobam)",
                "Hobi": "Mancing Keributan",
                "Sosmed": "@dimzkry_",
                "Kesan": "Baik dan humble sekali",  
                "Pesan":"Tetap menjadi pribadi yang akan terus berkembang"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "Sangat baik dan ramah",  
                "Pesan": "Teruslah menjadi sosok yang inspiratif bagi orang lain"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "Baik sekali",  
                "Pesan": "Semoga studinya lancar sampai wisuda ya kak"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "Sangat ramah",  
                "Pesan": "Tetap semangat dan rendah hati"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "Sangat ceria",  
                "Pesan": "Tetap menjadi pribadi yang terus berkembang dan berkarya"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "Sangat ramah",  
                "Pesan":"Tetaplah menjadi pribadi yang baik dan menginspirasi"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "Kakak ini sangat seru dan asik",  
                "Pesan": "Tetaplah berjuang meraih impian tanpa melupakan prinsip"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "Sangat ramah sekali",  
                "Pesan": "Jadilah pribadi yang akan terus berkembang dan selalu rendah hati"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "Sangat ramah dan membantu sekali",  
                "Pesan": "Tetaplah menjadi panutan yang luar biasa bagi orang lain"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "Kakak ini ramah dan agak sedikit pendiam",  
                "Pesan": "Semoga lancar terus ya kak dalam menjalani masa studinya"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "Sangat bertanggung jawab dalam setiap tugasnya",  
                "Pesan": "Jangan pernah menyerah dalam segala hal"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "Sangat humble",  
                "Pesan": "Tetap menjadi pribadi yang bisa membawa suasana positif"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=128yynqvz4CmtBRrHTRN2O4ug8c23-RaM",
            "https://drive.google.com/uc?export=view&id=132zsyGXlz92uW5EpboIy_Ps-UboObs7O",
            "https://drive.google.com/uc?export=view&id=11j1ls01RlrSVzKM76ANQH2VSYbVMWCS_",
            "https://drive.google.com/uc?export=view&id=11sJNkeXn_1dpZh23B75fM0LDm2erQquM",
            "https://drive.google.com/uc?export=view&id=11w-bZKkb7Kkm6SjMBzCPXf8LSOQHf2PD",
            "https://drive.google.com/uc?export=view&id=11t-v3wNikgB0MoNG78cOqOjvgqn4r7tj",
            "https://drive.google.com/uc?export=view&id=11vs3PUfEmevhWgzsqS5XjE_fWxSJ71MT",
            "https://drive.google.com/uc?export=view&id=11wwS_n9t_WbVPsmb_DnTVEW8kTL0zTL-",
            "https://drive.google.com/uc?export=view&id=11sRjPGbnPSw8mEbB2FTHLtU7RFhHq1hw",
            "https://drive.google.com/uc?export=view&id=12G98bFwlL5J0QIBKf0t1UrxHj1l_JnEC",
            "https://drive.google.com/uc?export=view&id=12_xjs8EQzz2eBEJkdIVl_6gKVIF0uHd2",
            "https://drive.google.com/uc?export=view&id=12ThCuLXHDtTHvKP8iQU9tkbmji-W1rUo",
            "https://drive.google.com/uc?export=view&id=12XbC1dHXx0vY1xq0TvcfqSSpd14Xpyv2",
            "https://drive.google.com/uc?export=view&id=12dx_CO2KJiN80HoLNohk-TJYR-QHVzlc",
            "https://drive.google.com/uc?export=view&id=12u_noQAfdOZs5jL9DE2EswWozkT3DBXI",
            "https://drive.google.com/uc?export=view&id=16RDPTdCCycZu-PfrDVVpzfGbcCQaGdv6",
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
                "NIM": "121450026",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Kobam",
                "Hobi": "Nambal Ban",
                "Sosmed": "@ericsonchandra99",
                "Kesan": "Sangat menginspirasi",  
                "Pesan": "Tetap menjadi panutan yang dapat menjadi inspirasi bagi orang lain"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "Kakak ini lucu banget",  
                "Pesan": "Jangan lupa jaga kesehatan dan terus menjadi sosok yang ceria ya kak"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "Kakak ini selalu bersikap positif dalam menghadapi masalah",  
                "Pesan": "Tetap menjadi pribadi yang optimis dan memotivasi bagi orang lain ya kak"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "Kakak selalu menunjukkan cara berpikir yang dewasa",  
                "Pesan": "Tetap semangat dan semoga dilancarkan segala urusan dan kuliahnya ya kak"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "Kakak ini orang yang rendah hati dan sabar",  
                "Pesan": "Tetap menjadi pribadi yang rendah hati ya kak"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "Kakak ini selalu menunjukkan sikap sopan dalam berkomunikasi",  
                "Pesan":"Tetap semangat dalam menjalani hari-harinya ya kak"
            },
            {
                "Nama": "Eksanty F. Sukma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "eksantyfebriana",
                "Kesan": "Kakak ini selalu memberikan arahan dengan jelas",  
                "Pesan": "Semoga kakak bisa menjadi sosok yang dapat memotivasi bagi orang lain"
            },
            {
                "Nama": "Oktavia Nurwenda Puspita Sari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "Kakak ini adalah sosok pengamat yang baik",  
                "Pesan": "Tetap menjadi orang yang selalu percaya diri dalam segala hal positif ya kak"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "Kakak ini selalu menjadi pendengar yang baik",  
                "Pesan": "Semangat kak dalam menjalani masa studinya"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "Kakak ini punya cara yang baik dalam menyampaikan pendapat",  
                "Pesan":"Tetap menjadi pribadi yang berkembang dan penuh semangat ya kak"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "Kakak ini sangat baik sekali",  
                "Pesan": "Semangat terus ya kak kuliahnya"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "Kakak ini selalu menujukkan pentingnya menghargai waktu",  
                "Pesan":"Tetap menjadi panutan yang baik bagi kami semua ya kak"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "Kakak ini selalu menujukkan sikap disiplin dalam belajar",  
                "Pesan": "Semoga bisa wisuda tepat waktu ya kak"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "Kakak ini sangat ramah dan baik sekali",  
                "Pesan": "Tetap menjadi sosok yang ramah ya kak"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "Kakak ini sangat ramah dan lucu",  
                "Pesan": "Saya berharap bisa belajar banyak hal positif dari kakak"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "Kakak ini selalu memberikan contoh sikap positif",  
                "Pesan": "Saya berharap bisa berbagi pengalaman dengan kakak"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "Kakak ini adalah sosok yang inspiratif",  
                "Pesan":"Semoga tetap menjadi sosok yang terus menginspirasi bagi orang lain ya kak"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "kakak ini sangat aktif",  
                "Pesan":"Jangan lupa untuk jaga kesehatan dan tetap semangat ya kak"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "Kakak ini Memiliki kemampuan problem-solving yang baik",  
                "Pesan": "Semoga bisa terus memberikan arahan yang baik bagi orang lain"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "Kakak ini sangat ramah",  
                "Pesan": "Tetap semangat dalam menjalani masa perkuliahannya ya kak"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "Kakak ini memiliki semangat yang luar biasa",  
                "Pesan": "Semoga diberikan kemudahan dalam segala hal ya kak"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "Kakak ini sangat baik sekali",  
                "Pesan": "SEmoga kita bisa bekerja sama dengan baik ya kak"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "Kakak ini selalu  memberi motivasi untuk terus berkembang",  
                "Pesan":"Tetap semangat dan terus menjadi pribadi yang berkembang ya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17JMG7bGeeuOBDyqcItdmGoL7NeHNf8rJ",
            "https://drive.google.com/uc?export=view&id=19zC_Xgh8OQLNQJpD2OYRdfJnwdOrY6vO",
            "https://drive.google.com/uc?export=view&id=1ABktP8f48a07fl-16hpVRuJJF0H3BDT1",
            "https://drive.google.com/uc?export=view&id=17MdEbPm-oiXdNZIOgx58nhuLy0_OVHCv",
            "https://drive.google.com/uc?export=view&id=1AIKVxB7o3naHdA65xKnYUs7gBljme_8C",
            "https://drive.google.com/uc?export=view&id=17NUX0lxxHDVTtHb_4zjrOQ0WEQSebzkA",
            "https://drive.google.com/uc?export=view&id=1AEtmD8Wmsd1FybsesPYkWVk8jVZpZ4VC",
            "https://drive.google.com/uc?export=view&id=1AMYlriLmwc-jtkQ3UtzwtnRWC6eHRgcY",
            "https://drive.google.com/uc?export=view&id=17BySoMVv8aWDry--33BouBn4FwZdFZXT",
            "https://drive.google.com/uc?export=view&id=1AXXyygbfXKQGLyW69CuvSDdhYn9HpFPe",
            "https://drive.google.com/uc?export=view&id=1AcgpXYXyhey5XnpoViUvy5WiuclYqFUW",
            "https://drive.google.com/uc?export=view&id=1AclVBWjkM7VrVcEf9vvxKAQjh-23C6W4",
            "https://drive.google.com/uc?export=view&id=1Ahyuumc7sGnx4YtlDn_ROBlHEqXYqYQk",
            "https://drive.google.com/uc?export=view&id=1AioX0wtB41VH7gERN9K8EGIDRQJOjnS1",
            "https://drive.google.com/uc?export=view&id=17AMKGzHwr0fF2tRKmosCQ39TrYsty5UO",
            "https://drive.google.com/uc?export=view&id=1AodDsLorQw18XTZEpFnx0y8NQTwcInMJ",
            "https://drive.google.com/uc?export=view&id=1ArHtx2uG3C8B1mEV9-tU87FiY11Cp_zi",
            "https://drive.google.com/uc?export=view&id=1AwGveWEQy6xOq01GUqTnfdxKn1aS0pMM",
        ]
        data_list = [
            {
                "Nama": "Yogy Sae Tama",
                "NIM": "121450041",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Jatimulyo",
                "Hobi": "Tidur",
                "Sosmed": "@yogyst",
                "Kesan": "Kakak ini sangat ramah sekali",  
                "Pesan": "Tetap menjadi sosok yang positif bagi orang lain ya kak"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "Kakak ini selalu menunjukkan sikap positif",  
                "Pesan": "Terus berkarya dan tetap semangat ya kak"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "Kakak ini sangat rendah hati",  
                "Pesan":"Tetap menjadi pribadi yang rendah hati ya kak"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "Kakak ini selalu menunjukkan sikap profesional dalam setiap kegiatan",  
                "Pesan":"Tetap menjadi pribadi yang akan terus berkembang dimana pun itu ya kak"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@esteriars",
                "Kesan": "Kakak ini sangat ramah",  
                "Pesan":"Semangat terus ya kak kuliahnya"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "Kakak ini sangat seru sekali",  
                "Pesan": "Semoga diberi kelancaran dalam setiap urusannya ya kak"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "Kakak ini sangat asik sekali",  
                "Pesan":"Tetap menjadi pribadi yang ramah dan rendah hati ya kak"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "Kakak ini sangat menginspirasi sekali",  
                "Pesan": "Saya harap hubungan baik ini akan terus terjaga hingga akhir masa kuliah ya kak"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "Kakak ini sangat berwibawa",  
                "Pesan": "tetap menjadi pribadi yang selalu berpegang teguh pada prinsip ya kak"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "Kakak ini sangat ramah",  
                "Pesan": "Semoga sukses selalu ya kak"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "Kakak ini baik sekali",  
                "Pesan": "Tetap semangat dalam menjalani masa perkuliahannya ya kak"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "Kakak ini sangat rajin sekali",  
                "Pesan": "Jangan lupa untuk terus jaga kesehatan ya kak"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "Kakak ini baik sekali dan sedikit pendiam",  
                "Pesan": "Sukses terus dan tetap rendah hati"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alfaritziirvan",
                "Kesan": "Kakak ini sangat ramah dan asik",  
                "Pesan":"Semoga tetap menjadi panutan yang baik dan penuh motivasi"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "Kakak ini sangat seru dan asik",  
                "Pesan": "Terus berkarya dimana pun kakak berada"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "Kakak ini Sangat Ramah",  
                "Pesan": "Semangat terus ya kak dalam meraih cita-citanya"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "Kakak ini sangat baik dan sopan",  
                "Pesan":"Semoga kakak selalu sukses dalam setiap langkah dan keputusan yang diambil"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "Kakak ini selalu memberi masukan yang membangun",  
                "Pesan": "Tetap menjadi sosok yang selalu memberi arahan dan solusi terbaik bagi orang lain ya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1B-BYV2-DlVUzFlydgiYtXKsKuaOM7j2D",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1B1Gba9HT72XjDmrsvT2OfViIgGzUHwAU",
            "https://drive.google.com/uc?export=view&id=1B5wLAHaRJ6HEjHS7vrYNvmWWqv9dUq7U",
            "https://drive.google.com/uc?export=view&id=1BBLsbxZk0fxVZCO_8xCZVTkvh28v-zIA",
            "https://drive.google.com/uc?export=view&id=1DSyEApOSdqz_Ma-iVtGlm8rC40d66OhN",
            "https://drive.google.com/uc?export=view&id=1BFZbclPxm5CpDalbcVOx-GkgOW3a6GOV",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1BHnSUpnF1eeGnEwmxG9IJiJ1ezdczBsc",
            "https://drive.google.com/uc?export=view&id=1BJ8CmZn_Tpq7xlAcZW1xfwxNQee1K0wt",
            "https://drive.google.com/uc?export=view&id=1BN4T7HNTJE77xi-AcZl5Hntex32dIiG9",
            "https://drive.google.com/uc?export=view&id=1DdOzfe6a5TPEEnz8vducis8Qp-9-tD2Q",
            "https://drive.google.com/uc?export=view&id=1BN6OS4W0xu1b9xxIXOqXRDwC_iLDu_ZB",
            "https://drive.google.com/uc?export=view&id=1BXt-VWkDKzAxTXa3JFuzejfR0rX2rI80",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "Rafi Fadhlillah",
                "NIM": "121450143",
                "Umur": "21",
                "Asal": "Sumatera selatan",
                "Alamat": "Jl. Nangka 4",
                "Hobi": "Olahraga",
                "Sosmed": "@rafadhlillahh13",
                "Kesan": "Kakak ini sangat ramah sekali",  
                "Pesan": "Semangat terus yea kak kuliahnya"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "Kakak ini selalu membawa aura positif",  
                "Pesan": "Tetap semangat menjalani studinya ya kak"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "Kakak ini sangat bertanggungjawab dalam menjalankan semua tugas",  
                "Pesan": "Jangan lupa jaga kesehatan ya kak"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "Kakak ini sangat seru dan aktif",  
                "Pesan": "Jangan lupakan tujuan utama selama berkuliah"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "Kakak ini sangat baik sekali",  
                "Pesan": "Saya berharap bisa berbagi pengalaman bersama kakak"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "Kakak ini sangat profesional",  
                "Pesan": "Jangan lupa berdoa untuk setiap langkah yang akan diambil ya kak"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "Kakak ini sangat ramah dan rajin",  
                "Pesan": "Semoga menjadi pribadi yang akan terus belajar dan berkembang"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "Kakak ini hobi sekali membaca buku",  
                "Pesan": "Jangan terlalu diforsir ya kak belajarnya"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "Kakak ini sangat asik dan lucu",  
                "Pesan": "Semangat terus kak kuliahnya"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "Kakak ini sangat baik dan ramah sekali",  
                "Pesan": "Semoga bisa lulus tepat waktu dengan nilai terbaik ya kak"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "Kakak ini sangat ramah",  
                "Pesan": "Tetap menjadi pribadi yang ramah ya kak"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "Kakak ini sangat baik",  
                "Pesan": "Semangat terus ya kak kuliahnya"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "Kakak ini humble sekali",  
                "Pesan": "Tetap semangat dan jaga kesehatan ya kak"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "Kakak ini sangan asik dan seru sekali",  
                "Pesan": "Tetap menjadi pribadi yang rendah hati"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "Kakak ini sangat baik sekali",  
                "Pesan": "Tetap semangat meneruskan studinya ya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17PLsGp0nKMoGKhG273k4qSQnI2QCHmFP",
            "https://drive.google.com/uc?export=view&id=17QJPt-44xCKGRT_1cfks1RS-RDwXqKNj",
            "https://drive.google.com/uc?export=view&id=17UtVBucvKW6NZ-GnxtChnR5SUOTazWrJ",
            "https://drive.google.com/uc?export=view&id=17WKPFtzSJZJuEmWyxLf1G8Cz4bouCFH1",
            "https://drive.google.com/uc?export=view&id=17_EDbUeA8Rbz_z_SbzrCI6L1UX200mnW",
            "https://drive.google.com/uc?export=view&id=17cTeG-1rP45PqK80SFG9WPKhKscWhQKS",
            "https://drive.google.com/uc?export=view&id=17cq4sL86f7QsfpR-yDHE9shwi1YGuERD",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=17hgPpeRWy--gkm0qjnovR0CMOgjtDA-l",
        ]
        data_list = [
            {
                "Nama": "Andrian Agustinus Lumbangaol",
                "NIM": "121450090",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Belwis",
                "Hobi": "Nyari hobi",
                "Sosmed": "@andrianlgaol",
                "Kesan": "Kakak ini sangat humble dan aktif",  
                "Pesan":"Semoga bisa menjadi sosok panutan yang baik ya kak"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "Kakak ini sangat ramah dan baik",  
                "Pesan":"Semangat terus ya kak kuliahnya"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "Kakak ini sangat humoris",  
                "Pesan":"Semangat terus ya kak kuliahnya"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "Kakak ini sangat ramah dan sedikit pendiam",  
                "Pesan":"Ayo kak mencoba untuk lebih aktif lagi yaa"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "Kakak ini sangat humble dan asik",  
                "Pesan":"Jangan lupa jaga kesetahan ya kak"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "Kakak ini sangat berwibawa",  
                "Pesan":"Tetaplah menjadi sosok yang dapat memotivasi bagi orang lain"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "Kakak ini seru banget",  
                "Pesan":"Tetap menjadi orang yang rendah hati ya kak"
            },
            {
                "Nama": "Nabilah Andika Fitriati",
                "NIM": "121450139",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kedaton",
                "Hobi": "Bikin JJ",
                "Sosmed": "@nabilahanftr",
                "Kesan": "Kakak ini selalu membawa suasana yang positif dan seru",  
                "Pesan":"Semoga kakak diberi kemudahan untuk setiap langkah yang diambil"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "Kakak ini pandai menyanyi",  
                "Pesan":"Saya harap bisa mendengarkan kakak bernyanyi setiap hari"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1BaKiHZkVn7f7sUwe0BCRSs6AzEKeeuoK",
            "https://drive.google.com/uc?export=view&id=1BfvyP--mP_XZRsw6qPyqzQnjle2S-tGP",
            "https://drive.google.com/uc?export=view&id=1BijOiRQwvyFMa_FLbOJJWu0z-RxXb3SF",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1Bk4JBhgN6dmVYCbFCzJUCJgnV29gpwax",
            "https://drive.google.com/uc?export=view&id=1BnlQzOW1qtcZOA6XEomP7ouO17lZlW70",
            "https://drive.google.com/uc?export=view&id=1BsBFsyFQBGpPOzQPYCr-JDJtyo1ykHxL",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1BtZgYHvEMWhtLWEOdPXk5gtYl3QykIOO",
            "https://drive.google.com/uc?export=view&id=1BtsN4TlDbaHrLFwbBUSqNIxi-9bOzm-e",
            "https://drive.google.com/uc?export=view&id=1BtzUV_C7n9ozCqN2s8LLDVjiFTn__KGh",
            "https://drive.google.com/uc?export=view&id=1BviitGHx8knSrB415NdL6w6ieeIvAip8",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1C53MpUOun_7XjexJFVu9N9TzDwhKWVpY",
            "https://drive.google.com/uc?export=view&id=1CJzp8IXT5D22bzUUSxnj4utxPJfvaPey",
            "https://drive.google.com/uc?export=view&id=1CSwH0i8LnxoR_wbUqYJBfaWEs5yse2V_",
            "https://drive.google.com/uc?export=view&id=1Ca4PDyOYsAJXltLBwY2u-6zz7ZL7koTH",
        ]
        data_list = [
            {
                "Nama": "Wahyudiyanto",
                "NIM": "121450040",
                "Umur": "22",
                "Asal": "Makasar",
                "Alamat": "Sukarame",
                "Hobi": "Nonton",
                "Sosmed": "@wahyulaja",
                "Kesan": "Kakak ini sosok yang bijaksana",  
                "Pesan": "Semangat terus ya kak kuliahnya"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "Kakak ini selalu memberi ide yang kreatif",  
                "Pesan": "Semoga kita bisa bekerja sama ya kak dalam suatu kegiatan"
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "Kakak ini ramah sekali",  
                "Pesan": "Semoga studi kakak lancar dan sukses"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "Kakak ini sangat baik dan ramah sekali",  
                "Pesan": "Tetap semangat kuliahnya ya kak"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "Kakak ini baik sekali",  
                "Pesan": "Tetap berpegang teguh pada pendirian ya kak"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "Kakak ini sangat humble dan asik",  
                "Pesan": "Semoga sukses selalu ya kak"
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "Kakak ini baik dan sangat asik",  
                "Pesan": "Semangat kak kuliahnya"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "Kakak ini sangat ramah",  
                "Pesan": "Tetap semangat meraih cita-citanya ya kak"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "@dino_rapet",
                "Kesan": "Saya terkesan dengan cara kakak menyampaikan pendapat",  
                "Pesan": "Saya sangat mengapresiasi semua dukungan kakak"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "Kakak selalu menjadi pendengar yang baik",  
                "Pesan": "Saya sangat terkesan dengan semangat kakak"
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@jimnn.as",
                "Kesan": "Kakak ini selalu menunjukkan empati yang tinggi",  
                "Pesan": "Terimakasih atas semua motivasi dan ilmu yang kakak berikan"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "Kakak ini selalu punya solusi kreatif",  
                "Pesan": "Saya belajar banyak dari sikap dan pola pikir kreatif kakak"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "Kakak ini selalu menunjukkan sikap yang baik",  
                "Pesan": "Saya sangat menghargai dedikasi kakak"
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": "Kakak ini sangat ramah sekali",  
                "Pesan": "Semangat terus kuliahnya ya kak"
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "Kakak ini sangat aktif dan seru",  
                "Pesan": "Terimakasih atas semua arahan dan ilmu yang kakak berikan"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "Kakak sangan kritis dalam berpikir",  
                "Pesan": "Saya merasa termotivasi setiap kali berbicara dengan kakak"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "Kakak ini sangat humble",  
                "Pesan": "Terimakasih atas semua ilmu yang telah diberikan ya kak "
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "Kakak ini baik sekali dalam menyampaikan pendapat",  
                "Pesan": "Semangat terus menjalanii masa studinya ya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()