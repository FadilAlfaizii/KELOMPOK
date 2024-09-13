import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#144259"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#ffa500"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_" #FOTO KELOMPOK
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ovvdqpZioDWr6MVH6wlsGCi8MvZwrC-g", #Palu mas anif
            "https://drive.google.com/uc?export=view&id=17TIBv9RbaAwW1S4-OnPzXjLHWBm3Elm5", #Bulu bu olla
            "https://drive.google.com/uc?export=view&id=1Uijfmrjt0dGVZLvRlkX0qO1br5gGmap5", #Mhs1 pak padil
            "https://drive.google.com/uc?export=view&id=1-6NqsjR-9VHys1Zt2wxrOBiRvrCjIt2E", #Mhs2 pak dzikra
            "https://drive.google.com/uc?export=view&id=17xHrv4LCWpw6m0FWuIbNt3QGCSLA8D9e", #Mhs3 pak zai
            "https://drive.google.com/uc?export=view&id=17xHrv4LCWpw6m0FWuIbNt3QGCSLA8D9e", #Mhs4 razka
            "https://drive.google.com/uc?export=view&id=17xHrv4LCWpw6m0FWuIbNt3QGCSLA8D9e", #Mhs5 vany
            "https://drive.google.com/uc?export=view&id=11HG7Igmw9kT9R3km6OXUNPxCX-F_FVR_", #Mhs6 hafsa
            "https://drive.google.com/uc?export=view&id=17xHrv4LCWpw6m0FWuIbNt3QGCSLA8D9e", #Mhs7 ilmi
            "https://drive.google.com/uc?export=view&id=17xHrv4LCWpw6m0FWuIbNt3QGCSLA8D9e", #Mhs8 fai
            "https://drive.google.com/uc?export=view&id=1xYyX3zU4EJJrEdKracegtZR5MtTncjdU", #Mhs9 daniar
            "https://drive.google.com/uc?export=view&id=1JIZjUV3P4vuVLsUEpXSx63IFvBhg-jWr", #Mhs10 wulan
        ]
        data_list = [
            {
                "nama": "Muhammad Hanif Dzaky Arifin",
                "sebagai": "Pak Lurah",
                "nim": "123450064",
                "fun_fact": "main game ama futsal",
                "motto_hidup": "MU separuh jiwaku.",
            },
            {
                "nama": "Fabiolla Charissa Putri",
                "sebagai": "Anggota",
                "nim": "122450044",
                "fun_fact": "ga ssuka makan kerupuk",
                "motto_hidup": "Ya apa ya",
            },
            {
                "nama": "Muhammad Fadil Alfaizi",
                "sebagai": "Anggota",
                "nim": "122450124",
                "fun_fact": "cepet inget, cepet lupa",
                "motto_hidup": "don't be long where you don't belong",
            },
            {
                "nama": "Muhammad Dzikra",
                "sebagai": "Anggota",
                "nim": "123450046",
                "fun_fact": "bisa tidur dimana saja",
                "motto_hidup": "suicide is a sin",
            },
            {
                "nama": "Zailani Satria",
                "sebagai": "Anggota",
                "nim": "123450022",
                "fun_fact": "ga suka buah",
                "motto_hidup": "belum kepikiran.",
            },
            {
                "nama": "Gusti Putu Ferazka",
                "sebagai": "Anggota",
                "nim": "123450111",
                "fun_fact": "nyemilin es",
                "motto_hidup": "jalanin azza",
            },
            {
                "nama": "Vany Salsabila Putri",
                "sebagai": "Anggota",
                "nim": "123450022",
                "fun_fact": "suka kopi tapi nggak suka nasi",
                "motto_hidup": "yang penting hidup",
            },
            {
                "nama": "Hafsa Fazila Arradhi",
                "sebagai": "Anggota",
                "nim": "123450079",
                "fun_fact": "nyemilin es",
                "motto_hidup": "gatau",
            },
            {
                "nama": "Khazanatil Ilmi",
                "sebagai": "Anggota",
                "nim": "123450111",
                "fun_fact": "nyemilin es",
                "motto_hidup": "jalanin aja",
            },
            {
                "nama": "Fairuz Ary Syifa",
                "sebagai": "Anggota",
                "nim": "123450053",
                "fun_fact": "suka jajan",
                "motto_hidup": "married is scary",
            },
            {
                "nama": "Erma Daniar Safitri",
                "sebagai": "Anggota",
                "nim": "123450053",
                "fun_fact": "suka jajan",
                "motto_hidup": "married is scary",
            },
            {
                "nama": "Wulan Lumbantoruan",
                "sebagai": "Anggota",
                "nim": "123450053",
                "fun_fact": "suka jajan",
                "motto_hidup": "married is scary",
            },
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
