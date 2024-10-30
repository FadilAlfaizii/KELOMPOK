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
            "https://drive.google.com/uc?export=view&id=1JOJKirMg43VjeJ89KTa6R7UOQ48wzgf9",
            "https://drive.google.com/uc?export=view&id=1tp1dQWZjTgqSlp-Xxk9JjhflNmfJFgTA",
            "https://drive.google.com/uc?export=view&id=1nbNrrGDqCnL6mQ8K2MuFmoRwvJXHKX2Z",
            "https://drive.google.com/uc?export=view&id=1oRol0ew-nR47akHR7zdguqH1wcvDufGT",
            "https://drive.google.com/uc?export=view&id=1GUa9lHI8xklNZ6O9m_Ll9w6kCgief8vJ",
            "https://drive.google.com/uc?export=view&id=1pnbcF66NOSYJ2EnLnYatjc2JXLwi_-Cx",
        ]
        data_list = [
            {
                "Nama": "Kharisma Gumilang",
                "NIM": "121450142",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Way Kandis",
                "Hobi": "Mendengarkan Musik",
                "Sosmed": "@gumilangkharisma",
                "Kesan": "bijak dan berkharisma sekali",  
                "Pesan":"semangat dan inspiratif bagi semua bang"
            },
            {
                "Nama": "Pandra Insani Putra Azuar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "mudah bergaul dan ramah",  
                "Pesan":"tetap bahagia aja bang meskipun gajadi kahim"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagaralam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "Kakaknya suka senyum",  
                "Pesan":"pertahankan kinerja dan tetap semangat kak"
            },
            {
                "Nama": "Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh, Sumatera Barat",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin Pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "ramah dan baik",  
                "Pesan":"tetap konsisten kak"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "kakanya lembut kalo ngobrol",  
                "Pesan":"semangat itung duitnya kak"
            }, 
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "komunikasi kakanya bagus",  
                "Pesan":"semangat juga kak itung"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1scjNsDLUzRIpcjZXXP3oGqnlJQ9_Ste2",
            "https://drive.google.com/uc?export=view&id=1W15LiSJvAIrbog8QySO_CJAhKl5iydPh",
            "https://drive.google.com/uc?export=view&id=1wb3BCvxriYx1EkUTUNyYN4dVvUse1cMM",
            "https://drive.google.com/uc?export=view&id=1f-enJNQ7M8nE3iD0i4HH9SJuib632sm6",
            "https://drive.google.com/uc?export=view&id=1A2z2YPTLGFAdwhR2oHSSeh_QkNUg7f1o",
            "https://drive.google.com/uc?export=view&id=1WXTPiEPXPbt7Mlja9dWeCJR_q5b3-oP5",
            "https://drive.google.com/uc?export=view&id=136gozrgMq3Zy71BOr-3EFDwQuRQYafUx",
            "https://drive.google.com/uc?export=view&id=17tGbdfu5k5K1oGzbFi2VDLsLr_msnu_Y",
            "https://drive.google.com/uc?export=view&id=1iAvtaqCEHYsIwsCZ1IXtwEQ3-Za3Y7xu",
            "https://drive.google.com/uc?export=view&id=1wi1_W_ZRXp13NQ0jZKHxnXrtQbj7muSZ",
            "https://drive.google.com/uc?export=view&id=1hHM_Q5tjoeIddwIkibuuhI8BNkiPEpYV",
        ]
        data_list = [
            {
                "Nama": "Tri Murniya Ningsih",
                "NIM": "121450038",
                "Umur": "21",
                "Asal":"Bogor",
                "Alamat": "Raden Saleh",
                "Hobi": "Kalo ke coffee shop pesen red velvet bukan kopi",
                "Sosmed": "@trimurniyaa",
                "Kesan": "Kakakny asik banget",  
                "Pesan":"semangat kakkk"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tangerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "Kakanya pendengar yang baik",  
                "Pesan":"semoga sukses kak"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "Kakanya ramah ",  
                "Pesan":"makasi bimbingannya kak"
            },
            {
                "Nama": "Annisa Dini Amaliya",
                "NIM": "121450081",
                "Umur": "20",
                "Asal":"Tangerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "kakanya panutan yang baik",  
                "Pesan":"semoga bisa terus belajar bersama kak"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "kakanya ramah",  
                "Pesan":"semoga studinya lancar kak"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "abangnya humoris",  
                "Pesan":"jaga kesehatan bang"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "abangnya menyenangkan",  
                "Pesan":"semoga bertemu lagi di kesempatan berikutnya bang"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka ikut tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "Kakak lucu",  
                "Pesan":"semoga terus bisa menginspirasi kak"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "122450156",
                "Umur": "22",
                "Asal":"Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin musik, nonton film, dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "abangnya humoris",  
                "Pesan":"jangan lelah ngebimbing kami bang"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "abangnya mudah diajak ngobrol",  
                "Pesan":"semangat dalam kepanitiaan bang"
            },
            {
                "Nama": "Berlianda Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumbar",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "kakanya aktif",  
                "Pesan":"semangat kuliahnya kaka"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TRJk0pLgA-o_v0SsPCBidba09zEYjNED",
            "https://drive.google.com/uc?export=view&id=1TzEE20y1vsHQDDLanJHpIgJezdkr_17v",
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
                "Kesan": "cara kakanya nyampein sesuatu bagus banget",  
                "Pesan":  "sehat kak"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "abangnya tegas",  
                "Pesan": "semangat ngumpulin aspirasinya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KRlqjorJ2pZGJxMbWDs-TmZUSr60rhap",
            "https://drive.google.com/uc?export=view&id=15AepJrLW6bSKU0oLDMDDBcIm4NvbrlRm",
            "https://drive.google.com/uc?export=view&id=1ipkoE_-Apgkh8PxwaVBIP1Qc3rj7ulCe",
            "https://drive.google.com/uc?export=view&id=1qs3BF1TIHZ6GUnCDyyllauXGMIidzpnv",
            "https://drive.google.com/uc?export=view&id=1gGNQMrtJMzCWkpZfG5FPvr9F7FJd86eG",
            "https://drive.google.com/uc?export=view&id=1hJbZ9s3slHrR3NJZWK3_k-Cbxz-ZMpZa",
            "https://drive.google.com/uc?export=view&id=1DRYKsJlGxFy4x7WpgF8DTKNIkGIc5B5x",
            "https://drive.google.com/uc?export=view&id=1WhTLl6EVpzr4PGnmYOdBIJcfJnPOUoQd",
            "https://drive.google.com/uc?export=view&id=18iW-nmQZVOHTBZUVRyZ0HtfBSYMSjG3p",
            "https://drive.google.com/uc?export=view&id=1fH3REqQU3O_WPA8LvF2mCpJuc6jfXchV",
            "https://drive.google.com/uc?export=view&id=1lDYk7OLiE9FE7RgkW_Y_vx7UhJJ1N21M",
            "https://drive.google.com/uc?export=view&id=1CrCHSgCBnh6Vl5UmhOUQ-Y44EPhJV_Gg",
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
                "Kesan": "Abangnya mudah berbaur dan asik",  
                "Pesan":"Jangan sering sering mancing keributannya bang"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "Kakanya tenang dan berwibawa",  
                "Pesan": "Semangat bikin suratnya kaa"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "abangnya asikkk",  
                "Pesan": "Semanagat ngoding dari gptnya bang"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "Suara kakanya lembut",  
                "Pesan": "Bikin spotify dari musik yang sering kaka denger dong ka"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "Abangnya bagus banget kalo nge MC",  
                "Pesan": "Semangat bikin lagunya bang"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "Kakanya ramah dan baik",  
                "Pesan":"Semoga IPKnya bagus kaaa"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "Mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "Kakanya ramah sekaliii",  
                "Pesan": "Semangat kuliahnya kaa"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "Abangnya ganteng dan agamis",  
                "Pesan": "Semangat futsalnya bangg"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "Kakanya mudah berbaurr",  
                "Pesan": "Makin rajin kak membacanyaa"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "Kakanya suka senyum",  
                "Pesan": "Semangat kak berkebunnya"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "Abangnya baik dan pendengar yang baik",  
                "Pesan": "Semangat bang nyanyinya"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "Abangnyaa suka senyum",  
                "Pesan": "Spill dong bang film yang baguss"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1uTVP1mnYMXcVHpdrkhLzvh5X5mOQ0dvt",
            "https://drive.google.com/uc?export=view&id=1UVSj3eSfISRiq4SWsAKwiqlM-cbQuVkN",
            "https://drive.google.com/uc?export=view&id=15KjBjiTKtmTnEYVWnlxO2OC99LVfntEe",
            "https://drive.google.com/uc?export=view&id=18valVfE0ZJiv1K-AvN9IriWgvQsdVfYF",
            "https://drive.google.com/uc?export=view&id=1uUUbRZ18FHbkhyQpASoJD7RjoEv5XFeR",
            "https://drive.google.com/uc?export=view&id=172N98S_LbDu7z2wnpvxL27SOJQPUKN4r",
            "https://drive.google.com/uc?export=view&id=1lDKcU-KdpvPAbXKsg2smxpiOfF_gsmzm",
            "https://drive.google.com/uc?export=view&id=1EexUPfLpYihG6nRAVuik1idtgRnyr0_K",
            "https://drive.google.com/uc?export=view&id=1Cm3J9o22T1MuwMO6f49tDkZBdVijQCTg",
            "https://drive.google.com/uc?export=view&id=1yB1_WyCzeJeAz12cmKvQkx3Eq9GNRx3E",
            "https://drive.google.com/uc?export=view&id=1QOJEqu26PNso2-iILtb2a7N8vY1MutZy",#gifari
            "https://drive.google.com/uc?export=view&id=1QzIg5ml1n2EU8nGSZVTQCNEEkCFpxbTS",#jo
            "https://drive.google.com/uc?export=view&id=1WLxB1g4QlwjJm1k2Y4TNbHQ24_WFIyy9",#kemas
            "https://drive.google.com/uc?export=view&id=1qKlfVa7NupLa5q8QcIfsYUz0prPFsrqv",#leonard
            "https://drive.google.com/uc?export=view&id=177hS2s5BoZN_KO8z0x6qsuMeEaOw2UvB",#presilia
            "https://drive.google.com/uc?export=view&id=1gROfWU9i_5bW2xBQlxbfiChfPINzR2YR",#rafa
            "https://drive.google.com/uc?export=view&id=1qnDg3f0U8CX59Z8swgQHvgMRXXimuRDS",#sahid
            "https://drive.google.com/uc?export=view&id=17XkpEv4TcL2GetS9UxE4dD-j9sGZwT8U",#vanesa
            "https://drive.google.com/uc?export=view&id=1SPUmjtD6PAh8vJgESWSb84sLB8KnKQmg",#farhan
            "https://drive.google.com/uc?export=view&id=1VDu00ogr6bWyf9KfBX6kyqnusbqxfZpS",#gede
            "https://drive.google.com/uc?export=view&id=1E2IakmBnLqw6DlltgSc0X-qRkszv_eHg",#jaclin
            "https://drive.google.com/uc?export=view&id=1Oy0sIn6GG-WXmN4x0_2vdSCSZbtAI0HT",#rafly
            "https://drive.google.com/uc?export=view&id=16Rf_wPvw1QXh-Ht342Rq1c0Nv07_lp5e",#andini
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
                "Kesan": "Abangya tegas",  
                "Pesan": "Sehat selalu bang"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "Kakanya lucu",  
                "Pesan": "Semangat kuliahnya kak"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "Kakanya cantik bangettt",  
                "Pesan": "Semangat kuliahnya kak"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "Kakanya tegas",  
                "Pesan": "Semangat nanti kknnya kak"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "Kakanya ramah",  
                "Pesan": "Jangan capek ngebimbing kami kak"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "Abangnya baik",  
                "Pesan":"Semangat ya bang kuliahyaaa"
            },
            {
                "Nama": "Eksanty F. Sukma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "@eksantyfebriana",
                "Kesan": "Kakanya ramahh",  
                "Pesan": "Jaga kesehatannya kak"
            },
            {
                "Nama": "Oktavia Nurwenda Puspita Sari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "Kakanya baikk",  
                "Pesan": "Semoga IPK nya bagus kak"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "Abangnya murah senyum",  
                "Pesan": "Semoga lulus tepat waktu bang"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "Lucu banget abangnyaaa",  
                "Pesan":"Semangat dan sehat selalu bangg"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "Adem banget abangnyaa",  
                "Pesan": "Sehat selalu bangg"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "Abangnya ramah juga yaa",  
                "Pesan":"Tambah semanagat lagi bang supporterannya"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "Abangnya pinterrr",  
                "Pesan": "Semangat bang belajarnyaaa"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "Abangnya kece deh",  
                "Pesan": "Makin rajin bang ibadahnya"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "Kakanya adem bangettt",  
                "Pesan": "Sehat selalu kak"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "Kakanya cantik bangettt",  
                "Pesan": "Jangan lupaistirahat kak"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "Abangnya baik bangetttt",  
                "Pesan":"Semangat kepanitiaannya bang"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "Kece banget kakanya",  
                "Pesan":"Semangat baskeetnya kak"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "Abangnya asik bangett",  
                "Pesan": "Semoga lulus tepat waktu bangg"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "Abangnya balance antara belajar dan main",  
                "Pesan": "Semanagat bang belajar dan mainnya"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "Kakanya ramah dan suka senyum",  
                "Pesan": "Semangat kuliahnya kak, semoga lulus tepat waktu"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "Abangnya agak pendiem",  
                "Pesan": "Sehat selalu bangg"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "Kakanya adem dan ramah",  
                "Pesan":"Selalu positive vibe kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LsPqPgeK_N0sGIhMw7j9DycTwlMcidB0",#yogi
            "https://drive.google.com/uc?export=view&id=1tvMg66iZY2tGN5HzT3opmn4vEHK7Ljs0",#ramadhita
            "https://drive.google.com/uc?export=view&id=1q3hMXRVbRrxTWxcg_SBqwt1Norisay-4",#naswa
            "https://drive.google.com/uc?export=view&id=1UurQ39OZNgleANiTYCIAwLfzmyArunx_",#dea
            "https://drive.google.com/uc?export=view&id=18gjMiF68y_rlh4LVIznUG1nWYAjh4UtE",#esteria
            "https://drive.google.com/uc?export=view&id=1C4yKA34MNDkNzU5tAEMVvO48NtThobwl",#natasya
            "https://drive.google.com/uc?export=view&id=1lq6GGAKiQ6FCdiKM5MCkaYZbuhiE2uRe",#novelia
            "https://drive.google.com/uc?export=view&id=14szhm6XaYloHIAwhHBXYaLt9ZkiZIBLi",#ratu
            "https://drive.google.com/uc?export=view&id=1OaP0POFw4wpFJJ-98PR8q3Gp6KhLOBXg",#tobias
            "https://drive.google.com/uc?export=view&id=1qnSFetXPoqDm62oBHFFuNaYvzkYku-GN",#yohana
            "https://drive.google.com/uc?export=view&id=1MEHsWHxutq5zMsqFskNCNZ5eEWpCeNuZ",#rizki
            "https://drive.google.com/uc?export=view&id=1j1P3GMqXgqRIsMtGSMSvwXbyKCranaOf",#arafi
            "https://drive.google.com/uc?export=view&id=1e6D0d7E67hlsRT0XNfcbYmQC6lrTI-Nq",#asa
            "https://drive.google.com/uc?export=view&id=1qGlGcCxKBcX1cE4jPAMf1gcegOO1POvv",#irvan
            "https://drive.google.com/uc?export=view&id=1PkAz7bsazb_HL1DasV6S8Zyydip5bKk4",#izza
            "https://drive.google.com/uc?export=view&id=1fAuqxxqRCROvPoY1k4cL7IbWvF7kBIv7",#khalisah
            "https://drive.google.com/uc?export=view&id=1BW0VdwEeJ_nBsQ5NIl-adU1jo2BxXOpl",#raid
            "https://drive.google.com/uc?export=view&id=1BJ3I6nrSSTyX52F3Lvfk2O056_DS7Bfb",#tria
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
                "Kesan": "Abangnya sangat mudah bersosialisasi",  
                "Pesan": "Yang nyenyak bang tidurnya"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "Kakanya tegass",  
                "Pesan": "Ayo jalan-jalan bareng kak"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "Kakanya baikk",  
                "Pesan":"Semangat main golfnya kak"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "Kakanya sangat menginspirasi",  
                "Pesan":"Semangat kak berkebunnya"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@esteriars ",
                "Kesan": "Kakanya ramah bangettt ",  
                "Pesan":"Ayo kak main golf bareng"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "Kakanya lucuuu",  
                "Pesan": "Semangat survingnya kak"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "Kakanya cantik bangettt",  
                "Pesan":"Semangat kuliahnya kaaa"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "Kakanya cantik dan asik bangett",  
                "Pesan": "Semangat jadi BPHnya kaaa"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "Abangnya asikkk",  
                "Pesan": "Semangat kuliahnya banggg"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "Kakanyaa baik dan ramahh",  
                "Pesan": "Semoga lulus tepat waktu kaa"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "Abangnya ganteng",  
                "Pesan": "Semangat bikin fortofolionya bang"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "Abangnya seruuu ",  
                "Pesan": "Semangat bertaninya bang"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "Vibe kakanya agama bangettt",  
                "Pesan": "Dilancarin semua urusannya kaa"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "Abangnya asiikkk dan ramahh",  
                "Pesan":"Semoga IPKnya naik bangg"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "Kakanyaaaa asikkk dan heboh",  
                "Pesan": "Ajarin main rubik dong kaa"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "Kakanyaaa cantikkk",  
                "Pesan": "Ayo kak ngaji barengg"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "Abangnyaa ramahh",  
                "Pesan":"Ikut dong bang nemenin bang tobias lari"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "Kakanya sangat menginspirasi",  
                "Pesan": "Spill buku yang baggus dong kaaa"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sSs7Id58pYDF-_5xU1NeOk5xPgV5Ok_4",
            "https://drive.google.com/uc?export=view&id=1DyPZfGyK0pxGFxLxxgLM08TllfuUIRTY",
            "https://drive.google.com/uc?export=view&id=1lbuPo6vgBme7gMQ-vxBHepHIN2bc_np3",
            "https://drive.google.com/uc?export=view&id=18LLK4R4EtnViq01INIKFIvhCcDsrP3fw",
            "https://drive.google.com/uc?export=view&id=1By8yJTuHZVLS_a6Bn39AUkrIdT-kAI9J",
            "https://drive.google.com/uc?export=view&id=1-O99g8g3wP0oEVbjMWavleHgUBxhsYA7",
            "https://drive.google.com/uc?export=view&id=1LsFg1XcYxsKpy_M5S6P8wQS3GFnZtZ83",
            "https://drive.google.com/uc?export=view&id=1wL-iz3VrFctI-fWw8iUHJ_jIbbcRcRY6",
            "https://drive.google.com/uc?export=view&id=1H6Iawa1_gYeNMMNGtIFQPyt6yI7hrNao",
            "https://drive.google.com/uc?export=view&id=1t5SWOo5wDGkbjYSmCyWM0omc4wS84ZxA",
            "https://drive.google.com/uc?export=view&id=17MBtFgAq4nVjq93HD10OGOfMfl15PR0R",
            "https://drive.google.com/uc?export=view&id=1cANV0ZF61pcIOrtZTeiC5hBWyl3hKQvq",
            "https://drive.google.com/uc?export=view&id=1_PLyJeOVmEca1addzXyGH6TAOmCbbXHD",
            "https://drive.google.com/uc?export=view&id=10UjhnqrYA-M2aeI8wyQfhldZsc02UJ_F",
            "https://drive.google.com/uc?export=view&id=1zhKXmORTfOqb46VpN2cZZmKIURZoJJ67",
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
                "Kesan": "Muka abangnya kek orang pinterr",  
                "Pesan": "Semanagt olahraganya bangg"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "Kakaknya lucuuu",  
                "Pesan": "Semangat masaknya kakk"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "Abangnya ramahhh",  
                "Pesan": "Semangat olahraganya banggg"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "Abang dutaaa",  
                "Pesan": "Semangat ngaspraknya baangg"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "Kaka kembarrrr",  
                "Pesan": "Semangat review journal bu mikanya kak"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "Abangnya serius bangettt",  
                "Pesan": "Semangat belajar Ml nya bang"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "kakanya pinterrr",  
                "Pesan": "Semangat kak resume webinarnya"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "Kakanya baikkk",  
                "Pesan": "Semangat baca jurnalnya kaaa"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "Kakanya cantikkk",  
                "Pesan": "Semangat review jurnalnya kak"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "Kakanya baik bangettt",  
                "Pesan": "Semanagat menghitung akurasinya kaaa"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "kakanyaaa murah senyummm",  
                "Pesan": "semangat membangkitkan bilangannya kak"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "Abang ganteng",  
                "Pesan": "semangat ngodingnya bangg"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "Abangnya pinterrr",  
                "Pesan": "Semangat ngodingnya banggg"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "Kakany asikkk",  
                "Pesan": "Semangat kak review jurnalnya"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "Abangnya happpy",  
                "Pesan": "Semangat main gamenya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16hLCx-ZF0fVq2a0T3_IsEmu__z296MlQ",
            "https://drive.google.com/uc?export=view&id=1J7bZU52_wyybo8G6iybdCNItpr-GtW1c",
            "https://drive.google.com/uc?export=view&id=1zOWVOC4LMIbbbXYZr15YNP8xU65sBoaG",
            "https://drive.google.com/uc?export=view&id=1GugHZtZ7FZ85oN-9_KTRzgKxvsZtCAvH",
            "https://drive.google.com/uc?export=view&id=1kt79SfnyBax-gmaQJguHY_4yYmZW48Tf",
            "https://drive.google.com/uc?export=view&id=1aC9O7IG8MmNq6L860SfFkVN7-LvVzKwH",
            "https://drive.google.com/uc?export=view&id=1GnfqtGwnocxjZDklfQ0tvW376_1ZgF4w",
            "https://drive.google.com/uc?export=view&id=1d-5zwEKhve2o15jhve0AuIBUuqM6y7JL",
            "https://drive.google.com/uc?export=view&id=1Zyhlc2ojVgkh-V8xSrjFuMqHkyXjftDz",
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
                "Kesan": "Abangnya sangat berduitt",  
                "Pesan":"Sangat menginspirasi"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "Kakanya cantikk",  
                "Pesan":"Ayo nonton bareng kaa "
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "Kakanya ramahhh",  
                "Pesan":"Semangat kak ngitung duitnyaa"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "Abangnya minang nih",  
                "Pesan":"Semangat bang badmintoonnya"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "Abangnya lucuuu",  
                "Pesan":"Ayo bang touring bareng"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "Abang gantengg",  
                "Pesan":"Semangat bang olahraganya"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "Kakanya asikk",  
                "Pesan":"Gimana tuh kak hobi rajin nuliss"
            },
            {
                "Nama": "Nabilah Andika Fitriati",
                "NIM": "121450139",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kedaton",
                "Hobi": "Bikin JJ",
                "Sosmed": "@nabilahanftr",
                "Kesan": "Kakanya kecee ",  
                "Pesan":"Spill template jj dong kaa"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "Kakanya humble",  
                "Pesan":"Semangat nyanyi dan main musiknya kaa"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kpZXRHEhqT3jpBgK76hxhM4Pj4jxVNzf",
            "https://drive.google.com/uc?export=view&id=1_ElkLW5t5_n89PIfUPEvGOyuv_aWyhcc",
            "https://drive.google.com/uc?export=view&id=12t1oKeS-9x-NP5Ooa9DaO4JHGR6lrX4e",
            "https://drive.google.com/uc?export=view&id=1Ykd7t1l_-4ILNxmGtj5YbuZ4E3BUgaJk",
            "https://drive.google.com/uc?export=view&id=1g42mzBPYcpZ9O97x4Dq70yhUtGXB4TKq",
            "https://drive.google.com/uc?export=view&id=1vAFKzbsu_EC2mm4K38ieJemM0LdwYNYn",
            "https://drive.google.com/uc?export=view&id=1zEQGSVZpixKT3xGCkQoey_4ig35gUUui",
            "https://drive.google.com/uc?export=view&id=1n94loSJngeecUVPbME_XexjeUe_8qPYO",
            "https://drive.google.com/uc?export=view&id=1U5z3fw6obBzJ2-YmNldiFzMx4vzarOtV",
            "https://drive.google.com/uc?export=view&id=1FBnH5eAiN7kcarrcBA1F_AGFuMkD6tnl",
            "https://drive.google.com/uc?export=view&id=1eyQY3Pn9vCOJns2RIQ-evOcTbhoH_RPw",
            "https://drive.google.com/uc?export=view&id=1jkl9ESgX076YbvUZDxriEJ6Q_Phjpn2K",
            "https://drive.google.com/uc?export=view&id=1y5s7WtPVIDGIcMOuXqxj5A6DWbLYmQjX",
            "https://drive.google.com/uc?export=view&id=18s89m8B0MucNaCoAB8lwDq8jxkjFPL4F",
            "https://drive.google.com/uc?export=view&id=1MC8Rs9XBocyHwWsA3Z1odOqMM-d2HBZD",
            "https://drive.google.com/uc?export=view&id=1bW_UUJBdX40iY3AlD-EcTtf3nx5B3Hi2",
            "https://drive.google.com/uc?export=view&id=1xJWEd4Nqp5VZ9ODLjp2M5GatShPZF3kR",
            "https://drive.google.com/uc?export=view&id=15KxVMyErXSwGfnFj_nVb3EGNFBFvH1-E",
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
                "Kesan": "Abangnya berwibawa",  
                "Pesan": "Seoga lulus tepat waktu bang"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "Kakanya cantik bangettt",  
                "Pesan": "Semangat ngaspraknya kaa"
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "Kakanya lucuuu",  
                "Pesan": "Semangat ngontennya kaaa"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "Make up kakanya baguss",  
                "Pesan": "Semangat kak ngegymnya"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "kakanyaaa mudah berbaur",  
                "Pesan": "Semangat ka nulis dan bacanya"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "Kakanya lucu dan asik",  
                "Pesan": "Semangat kuliahnya kaaa"
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "Kakanya ramahhhh",  
                "Pesan": "Semangat ka jadi daploknya"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "Kakanyaa pinterrr",  
                "Pesan": "Semangat ka ngodingnyaa"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "Abangny berwibawaa",  
                "Pesan": "Semoga hobinya cepet ketemu bang"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "Kakanya murah senyum",  
                "Pesan": "Semoga IPKnya naik kak"
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@gymnn.as",
                "Kesan": "Abangnya murah senyum",  
                "Pesan": "Spill dong bang komik yang asik"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "Kakanya humble",  
                "Pesan": "Apatuh kak musik jj yng asik"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "Kakanya ngasi contoh yang baik",  
                "Pesan": "Jangan sering-sering nonton yang bikin nangis kak"
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": "Abangnya pembimbing yang baik",  
                "Pesan": "Semangat bang ngaspraknya"
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "Abangnya pinter ngoding nih",  
                "Pesan": "Semangat bang ngodingnya"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "Abangnya rendah hati dan ramah",  
                "Pesan": "Semangat jadi daploknya bang"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "Abangnya ramah dan mudah berbaur",  
                "Pesan": "Semangat kuliahnya bangg"
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "Kakaknya lucuuu",  
                "Pesan": "Semanagt kak ngepelnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()