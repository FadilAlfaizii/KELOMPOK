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
            "https://drive.google.com/uc?export=view&id=1Ag_ecQRLCCmoLE1NMW00vVhqkU9PtJKC",
            "https://drive.google.com/uc?export=view&id=1rQYEYfWfxm7XL2H_ne4wglMHHRqwxBM1",
            "https://drive.google.com/uc?export=view&id=1uBn9cL9NXrcCGyHSkIikCOVfbFKz6ed8",
            "https://drive.google.com/uc?export=view&id=1wahRrrguyn3AHKpkGUr3OBNX3d4mp2f5",
            "https://drive.google.com/uc?export=view&id=16L4muoTW8AsmDFp-BukRubmXrzPiCwra",
            "https://drive.google.com/uc?export=view&id=1zA0UkiBjHXd91ZF3RHWDwSKsIdBUu4FU",
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
                "Kesan": "Abangnya memiliki ilmu yang luas terkait organisasi",  
                "Pesan":"semangat kuliah dan segera TA bang !!!"
            },
            {
                "Nama": "Pandra Insani Putra Auzar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "Abang ini asik dan seru ketika ngobrol bersama",  
                "Pesan":"semangat dalam menghadapi masa akhir-akhir perkuliahan"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagaralam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "Kakaknya keren dan luar biasa",  
                "Pesan":"sukses selalu kedepannya kak"
            },
            {
                "Nama": "Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh, Sumatera Barat",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"#1
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
    kesekjenan()
elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-CMb2830hBRQWO88LlsWyUt9HDxpzfBJ",
            "https://drive.google.com/uc?export=view&id=1ejGHQHQgrWOTq3CvRPdh5JkaAjUq_N_-",
            "https://drive.google.com/uc?export=view&id=1MA5uwPHe7IJwKYNWaI7DD3iZqvu3W3Ob",
            "https://drive.google.com/uc?export=view&id=1f_jjj8DvnYVhUDUtw6UPx-p6NCGxUziJ",
            "https://drive.google.com/uc?export=view&id=1c5vzevlo0XQD4EYcavWrVV0rsQYh_iac",
            "https://drive.google.com/uc?export=view&id=1f4PRXrFTJ-EBFnVi97UOjSiAaiVb1HTj",
            "https://drive.google.com/uc?export=view&id=13NmueKkXwe1PV-pSyTWmZn71iQ2AZYBC",
            "https://drive.google.com/uc?export=view&id=1k6FRItvS12EuAbP0b1v1EJaJF5wbKZBt",
            "https://drive.google.com/uc?export=view&id=1Wiv2YJx07DHb7XmIEwFpILoRuf8gd-8A",
            "https://drive.google.com/uc?export=view&id=1Dj-eTymm6v55JeYmX8fvSEsfq1Umo3wk",
            "https://drive.google.com/uc?export=view&id=1cboVbcPDQTVKXWmMcX24_mPduo_v5u6o",
        ]
        data_list = [
                    {
                "Nama": "Tri Murniya Ningsih",
                "NIM": "121450038 ",
                "Umur": "21",
                "Asal":"Bogor",
                "Alamat": "Raden Saleh",
                "Hobi": "Kalo ke coffe shop pesen red velvet bukan kopi",
                "Sosmed": "@trimurniyaa",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tanggerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, Nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150 ",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Annisa Dini Amaliya",
                "NIM": "121450081",
                "Umur": "21",
                "Asal":"Tanggerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Batu Raja, Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Sukabumi, Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka Ikut Tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "121450156",
                "Umur": "22",
                "Asal":"Surakarta, Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Berlianda Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "",  
                "Pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Senator":
    def senator():
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
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
           
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
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
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