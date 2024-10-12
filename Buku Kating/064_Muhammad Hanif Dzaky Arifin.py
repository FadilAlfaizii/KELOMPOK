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
            st.write(f"Nama: {data_list[i]['Nama']}")
            st.write(f"NIM: {data_list[i]['NIM']}")
            st.write(f"Umur: {data_list[i]['Umur']}")
            st.write(f"Asal: {data_list[i]['Asal']}")
            st.write(f"Alamat: {data_list[i]['Alamat']}")
            st.write(f"Hobbi: {data_list[i]['Hobbi']}")
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
        ]
        data_list = [
            {
                "Nama": "Kharisma Gumilang",
                "NIM": "121450142",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Way Kandis",
                "Hobbi": "Mendengarkan Musik",
                "Sosmed": "@gumilangkharisma",
                "Kesan": "Abangnya memiliki ilmu yang luas terkait organisasi",  
                "Pesan":"semangat kuliah dan segera TA bang !!!"# 1
            },
            {
                "Nama": "Pandra Insani Putra Auzar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobbi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "Abang ini asik dan seru ketika ngobrol bersama",  
                "Pesan":"semangat dalam menghadapi masa akhir-akhir perkuliahan"# 1
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagaralam",
                "alamat": "Kotabaru",
                "hobbi": "Nonton Drakor",
                "sosmed": "@wulandarimeliza",
                "Kesan": "Kakaknya keren dan luar biasa",  
                "Pesan":"sukses selalu kedepannya kak"# 1
            },
            {
                "Nama": "Putri Maulida Chairani",
                "NIM": "121450050",
                "umur": "21",
                "Asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "Hobbi": "Dengerin pandra main gitar",
                "sosmed": "@ptrimaulidas_",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "Nama": "Kakak D",
                "NIM": "122450000",
                "umur": "18",
                "Asal":"Bekasi",
                "alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "Nama": "Kakak D",
                "NIM": "122450000",
                "umur": "18",
                "Asal":"Bekasi",
                "alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "sosmed": "@i",
                "Kesan": "Kakaknya keren ",  
                "Pesan":"semangat di masa-masa terakhir kuliah kak"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "...",
                "NIM": "122450000",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "Sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "Nama": "...",
                "NIM": "122450000",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "Sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "...",
                "NIM": "122450000",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "Sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "Nama": "Kakak D",
                "NIM": "122450000",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "Sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "Nama": "Kakak E",
                "NIM": "122450000",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "Sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Kakak D",
                "NIM": "122450000",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "Sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
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
                "Nama": "Kakak D",
                "NIM": "122450000",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "Sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "Nama": "Kakak E",
                "NIM": "122450000",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "Sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Kakak D",
                "NIM": "122450000",
                "Umur": "18",
                "Asal":"Bekasi",
                "Alamat": "Gg.sakum",
                "Hobbi": "Mainn Bola, Belajar",
                "Sosmed": "@i",
                "Kesan": "Kakak ini asik saya suka belajar dengan dia",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
