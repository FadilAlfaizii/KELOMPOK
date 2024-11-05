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
                "Pesan":"Semangat kuliah dan semoga dimudahkan TA bang"
            },
            {
                "Nama": "Pandra Insani Putra Azwar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "Abang ini asik dan seru ketika ngobrol bersama",  
                "Pesan":"Semangat dalam menghadapi masa akhir-akhir perkuliahan bang"
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
                "Pesan":"Coba nonton drama indosiar kak, siapa tau suka"
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
                "Pesan":"Semangat kak dengerin bang pandra main gitarnya"
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
                "Pesan":"Lagunya jangan yang galau kak"
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
                "Pesan":"Jangan pernah berhenti belajar dan berkembang ya kak !!!"
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
                "Kesan": "Kakaknya asik",  
                "Pesan":"Coba pesan kopi kak kalo lagi di coffe shop"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tanggerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, Nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "Kakaknya baik",  
                "Pesan":"Perbanyak membaca kurangi menonton kak"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150 ",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "Kakaknya keren",  
                "Pesan":"Semangat menyelesaikan drakor favoritnya kak"
            },
            {
                "Nama": "Anisa Dini Amalia",
                "NIM": "121450081",
                "Umur": "21",
                "Asal":"Tanggerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "Kakaknya keren",  
                "Pesan":"Semangat menamatkan dracinnya kak"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "Kakaknya baik",  
                "Pesan":"Referensi lagunya apa kak?"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Batu Raja, Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "Asik diajak ngobrol",  
                "Pesan":"Amankan nilai praktikum alpro bang"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "Baik dan keren",  
                "Pesan":"Jangan keseringan main kucing bang"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Sukabumi, Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka Ikut Tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "Kakaknya asik",  
                "Pesan":"Tips and trik jawab SKD kak"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "121450156",
                "Umur": "22",
                "Asal":"Surakarta, Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "Abangnya keren",  
                "Pesan":"Banyak betul hobinya bang"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "Abangnya keren dan pintar",  
                "Pesan":"Amankan nilai alpro bang"
            },
            {
                "Nama": "Berliana Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "Kakaknya baik",  
                "Pesan":"Semangat kuliahnya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YEURI7dXXxcGKgZwNP-faPOZd02MPbIi",
            "https://drive.google.com/uc?export=view&id=1z3-d1dapUoQDRqf-ouLZLDrkXrDLgV91",
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
                "Kesan": "Kakaknya keren dan sibuk orangnya",  
                "Pesan":  "Semangat terus kak"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "Abangnya keren",  
                "Pesan": "Semangat terus kuliah dan organisasinya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y521vZxCConqfI9IfS7jBfBnw4eCyPFu",
            "https://drive.google.com/uc?export=view&id=1pIYT5rXsfjgt1HNWcS7ctK6r3Ksb09HJ",
            "https://drive.google.com/uc?export=view&id=1WsiDXe-SF43SrYwBL5cRfVqwVrbKxc1W",
            "https://drive.google.com/uc?export=view&id=12-JlWggLTdx5iyfoQVnaxEgiop_LtKFH",
            "https://drive.google.com/uc?export=view&id=1pV50wQut08II8ggvb1ncv7JBiApAKfAA",
            "https://drive.google.com/uc?export=view&id=1b1Hw6HDSFeADJfTglJNKvr9uIVrKqco5",
            "https://drive.google.com/uc?export=view&id=1A2RAcfkiBUZ15Wn4kbZCIvSQse2in-P5",
            "https://drive.google.com/uc?export=view&id=1f95dDBNbQ68209ZtieDKqKUCJsixTus0",
            "https://drive.google.com/uc?export=view&id=1lK27rrqHQVWy7SKdyECsiqmnVlYOWEWG",
            "https://drive.google.com/uc?export=view&id=1OIYFF3Sm-zHPYZwnhAoOWK93oKZDeLP7",
            "https://drive.google.com/uc?export=view&id=1eU6Y3mqhjIGr2dsov4p_8weQq8U0386Q",
            "https://drive.google.com/uc?export=view&id=1MATqedErWJTdsxaPY_41EAX4hXfXeo_j",
        ]
        data_list = [
            {
                "Nama": "Dimas Rizky Ramadhani",
                "NIM": "121450027",
                "Umur": "20",
                "Asal": "Pamulang Tangsel",
                "Alamat": "Way Kandis (Kobam)",
                "Hobi": "Mancing Keributan",
                "Sosmed": "@dimzkry_",
                "Kesan": "Abangnya tegas dan keren",  
                "Pesan": "Jangan bosan-bosan jadi pelatih futsal bang"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "Kakaknya keren bisa jadi bendahara dan sekretaris",  
                "Pesan": "Semangat kak dah mau selesai kuliahnya"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "Abangnya suka ngobrol",  
                "Pesan": "Semangat bang kuliahnya dah mau selesai"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "Kakaknya ga banyak bicara",  
                "Pesan": "Semangat kuliahnya kak"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "Abangnya keren dan humble",  
                "Pesan": "Inpo tanggal perilisan lagunya bang"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "Kakaknya keren dan terlihat soleha",  
                "Pesan": "Semangat kak kuliahnya"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "Kakaknya keren dan ceria",  
                "Pesan": "Semangat kak kuliahnya"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "Soleh dan positive vibes",  
                "Pesan": "Kapan futsal lagi bang?"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "Kakaknya cantik ga banyak bicara",  
                "Pesan": "Semangat kak kuliahnya"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "Kakaknya cantik dan baik",  
                "Pesan": "Semangat kak kuliah dan berkebunnya kak"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "Abangnya baik dan keren",  
                "Pesan": "Semangat bang kuliahnya"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "Abangnya kalem dan gagah",  
                "Pesan": "Semangat semester akhirnya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19DBGSX4aHW_59u8YDxpBLi7XvoIAEXdu",
            "https://drive.google.com/uc?export=view&id=1ITXHtg9VALNjJtf3Z7bN8u9xSjPaLcO-",
            "https://drive.google.com/uc?export=view&id=1iIDMbkYAsCPmGUNAOlrJlnEwoUWDAWzi",
            "https://drive.google.com/uc?export=view&id=1aFcP8pgvobQUa3jd9zbrkVM_l5GJEdWw",
            "https://drive.google.com/uc?export=view&id=1zijW6N_aWXPFa6MTSBq3co_aybWmVjBq",
            "https://drive.google.com/uc?export=view&id=1SfWEIUAujzTn5YawY7qIxl3Q8dJtHhiD",
            "https://drive.google.com/uc?export=view&id=1QjICFFcoakt3aKQpQDZtgg4QaYp5LZ_H",
            "https://drive.google.com/uc?export=view&id=1eyuPHxjufd1MHKpdeFazq4Hw1ctcwwQP",
            "https://drive.google.com/uc?export=view&id=15L2htGt22gnlcq9TVXW7fDB-dLA5oRXB",
            "https://drive.google.com/uc?export=view&id=1VXSf7AarAaojFZBo7xE_ZUittIGk-yv8",
            "https://drive.google.com/uc?export=view&id=1ZgPc8eQhdiYf9Z3yg0jrFofmKkHDdvuB",
            "https://drive.google.com/uc?export=view&id=13W3-1yPn1_eTaCmTGenB2n3RTSZA9kRn",
            "https://drive.google.com/uc?export=view&id=1pFTk-qoV951PobMe_DV1ln2dzAhpoDsQ",
            "https://drive.google.com/uc?export=view&id=1eSNGrlOONzUxRELgwdk4RZs0g0dRTjsb",
            "https://drive.google.com/uc?export=view&id=12VJacwfN9baV8FNcKf5Ir3598juVVw4D",
            "https://drive.google.com/uc?export=view&id=1-JsulrZt9hW9UK3mIZbItQwLccPq-xg9",
            "https://drive.google.com/uc?export=view&id=1IYh1JOWdDyzjQhm_1PEejqqX8ipgsOOY",
            "https://drive.google.com/uc?export=view&id=1mvYI6npTrWxXVu1egVpT0GzyLHvf7nxM",
            "https://drive.google.com/uc?export=view&id=1AXwxQ5xdKyBgdMd_djBYjskpiVxpkeuB",
            "https://drive.google.com/uc?export=view&id=11xHgvSxTr8-Cj523XeWUVrAoW7zjxB8w",
            "https://drive.google.com/uc?export=view&id=1HVTxenkN3P19Il3kNhWRCK87rXo0FJob",
            "https://drive.google.com/uc?export=view&id=1m3Su2UYasj_JNeZEjrPgecKK2kr5ByCi",
            "https://drive.google.com/uc?export=view&id=1H1FhqoDUiCcVzDP9SdxVR5aFL1F6ENrc",
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
                "Kesan": "abangnya keren dan berwibawa",  
                "Pesan": "semangat menjalani masa-masa terakhir kuliahnya bang"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "cantik dan keren kakaknya",  
                "Pesan": "jangan sering-sering memancing keributan kak"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "kakaknya cantik dan berkharisma",  
                "Pesan": "semangat kak kuliah dan jadi kadivnya"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "kakaknya keren dan cantik",  
                "Pesan": "jangan bosan-bosan makan ayam kalasan kak"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "kakaknya keren dan cantik",  
                "Pesan": "info healing di padang kak"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "abangnya asik diajak ngobrol",  
                "Pesan":"tetap semangat bang riko"
            },
            {
                "Nama": "Eksanty F. Sugma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "eksantyfebriana",
                "Kesan": "kakaknya cantik dan pintar",  
                "Pesan": "tolong nilai praktikum ads kak"
            },
            {
                "Nama": "Oktavia Nurwinda Puspitasari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "kakaknya manis dan cantik",  
                "Pesan": "semangat kuliahnya kak"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "abangnya keren dan jago futsal",  
                "Pesan": "kapan futsal lagi bang?"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "abangnya keren terus jago basket",  
                "Pesan": "semangat menjalani masa-masa akhir kuliahnya bang"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "Abangnya keren dan cakep",  
                "Pesan": "Semangat kuliah bang dah mau selesai"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "Abangnya humble terus jago basket dan keren",  
                "Pesan": "Semoga tim basket menang lagi bang "
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "Abangnya keren dan jago ngoding",  
                "Pesan": "Ajarkan biar jago ngoding bang"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "Abangnya keren ",  
                "Pesan": "Inpo lomba futsal dalam waktu terdekat"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "Kakaknya cantik dan keren",  
                "Pesan": "Tolong nilai strukdat kak"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "kakaknya cantik cakep juga",  
                "Pesan": "Semangat kuliahnya kak"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "Abangnya baik dan peduli",  
                "Pesan": "Semangat bang kuliahnya"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "Kakaknya jago basket",  
                "Pesan": "Semoga IO menang ya kak"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "Abangnya keren dan baik",  
                "Pesan": "Semangat menolong siapapun bang"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "Abangnya tegap dan keren",  
                "Pesan": "Semangat menjalani masa-masa akhir kuliah bang"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "Kakaknya cantik ",  
                "Pesan": "Semangat kuliahnya kak"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "Abangnya keren dan tegap badannya",  
                "Pesan": "Semangat kuliahnya bang"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "Kakaknya cantik dan keren",  
                "Pesan": "Titip salam buat kembarannya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11RpH4Xm3kICyrBmxOjrYApyC3hJVEJQE",
            "https://drive.google.com/uc?export=view&id=1Bix7-z20g_soHfSnj7EpAjFjqb9depXA",
            "https://drive.google.com/uc?export=view&id=1M8LCL93COjSKRDpeHfswbQ2B3PaiTWHd",
            "https://drive.google.com/uc?export=view&id=1izoueZ4pk52zIOhdtkWf_knQcijn-CJe",
            "https://drive.google.com/uc?export=view&id=1uH2sMgk1xFyHdVJsD_cHAGVtTOguVZsE",
            "https://drive.google.com/uc?export=view&id=1mX4w0NbwgT6uHUgLkV1zXGlQ3W7Dkj_T",
            "https://drive.google.com/uc?export=view&id=1XQ_jgkhPZXg5Msyk38XnOSez0LctrzHu",
            "https://drive.google.com/uc?export=view&id=1MXmKMejwH7Sr2R3NVbErH2LKxCXDxJO1",
            "https://drive.google.com/uc?export=view&id=1ASK7XqXeo1kD5HaRLJmYM_OBY4b3AYEP",
            "https://drive.google.com/uc?export=view&id=1kViXLlNkfc-MXlj4mPdGPaULEiKS4peh",
            "https://drive.google.com/uc?export=view&id=1T_diZoN8M2U_tTWq-PP2LhAlLBJ7DfYf",
            "https://drive.google.com/uc?export=view&id=1yik-Erdbta7QSsk1WnbCGp0LeHrUiVIs",
            "https://drive.google.com/uc?export=view&id=1iI2997Dy0TE8weGkTBh5N1LIh19B8vmF",
            "https://drive.google.com/uc?export=view&id=1g9lnsfX19HWl0xt0lIaQ2WSuzTncfz2q",
            "https://drive.google.com/uc?export=view&id=1MBfSm5Yt95LiBbekTqui_kvA03lvU0CQ",
            "https://drive.google.com/uc?export=view&id=1L04rSRp1tWW-Z-cGhAy6nJHhHMA3eChf",
            "https://drive.google.com/uc?export=view&id=1TOqWYEXago9zLhg0ZbmINML7NMWh7TZW",
            "https://drive.google.com/uc?export=view&id=1mem5QHnlwTb1x2VJklakxGCCzYemqT-R",
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
                "Kesan": "Abangnya hebat dan keren",  
                "Pesan": "Semangat menjalani masa2 akhir kuliah bang"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "Kakaknya keren dan luar biasa ",  
                "Pesan": "Semangat tugas akhirnya kak"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "Positive vibes dan suka ngobrol",  
                "Pesan":"Semangat kak dah mau selesai kuliahnya"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "Orang minang cantik-cantiklah",  
                "Pesan":"Bolehlah singgah ke kampung kakaknya"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@",
                "Kesan": "Keren kak hobinya",  
                "Pesan":"Semangat kak akademik dan hobinya"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "Kakaknya keren dan luar biasa",  
                "Pesan": "Semangat kak kuliahnya"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "Cantik pol kakaknya",  
                "Pesan":"Semangat kuliahnya kak"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "Kakaknya keren dan pintar",  
                "Pesan": "Ajarin takraw kak"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "Keren,tegas,olahragawan dan luar biasa",  
                "Pesan": "Semoga bisa menang tur basket lagi bang"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "Kakaknya keren dan suka ngobrol",  
                "Pesan": "Semangat kuliah dan hobinya kak"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "Abangnya sibuk banget",  
                "Pesan": "Ajarin buat portofolio yang bagus bang"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "Aa bandung euy",  
                "Pesan": "Ajarkan bertani bang"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "Positive vibes banget",  
                "Pesan": "Tetap istiqomah kak "
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "Keren dan urang awak juga",  
                "Pesan": "Bolehlah ke kampung uda sekali-kali"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "Suaranya lantang dan bulat kak",  
                "Pesan": "Ajarkan rubik 3*3 kak"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "Positive vibes dan keren kakaknya",  
                "Pesan": "Istiqomah terus ngajinya kak"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "Abangnya terlihat berwawasan tinggi",  
                "Pesan":"Semangat bang ngikutin bang tobias larinya"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "Keren kak hobinya",  
                "Pesan": "Semangat kuliah dan hobinya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JbSoAInpWGGIwD0c2YWOsVoVrHSgaL-U",
            "https://drive.google.com/uc?export=view&id=1IWqhA4w5ITb1OpjP_NMyztnOmu5pmwT5",
            "https://drive.google.com/uc?export=view&id=1YAjAvqcJXd3B-wMbrYfTAKbK96zeWhe-",
            "https://drive.google.com/uc?export=view&id=1KEWfwm1ag1qZSoHZQlhqvxDCaaMFc-ZT",
            "https://drive.google.com/uc?export=view&id=1FNBX8wNJ76XXL7yIPcpEsvH8GrTGrIyX",
            "https://drive.google.com/uc?export=view&id=1JEsBkTtMXlv68gRL1-zuicLDCHO-R3Oh",
            "https://drive.google.com/uc?export=view&id=1y_yo4hTvVEXdyoJe9XKbitbaMsGj5RPR",
            "https://drive.google.com/uc?export=view&id=1i_jcVB4ZWj3JyWmMWG6b5NdiyrIUr19a",
            "https://drive.google.com/uc?export=view&id=1pppFus6n5gGEPkmr6c6DX9J1v6LN9nrU",
            "https://drive.google.com/uc?export=view&id=11wwAYjnVv4pRehbYiudnsBACO7QwLlKg",
            "https://drive.google.com/uc?export=view&id=1OHQ81-t0s7mOOdj5TqUHUS0SL5QIl9-k",
            "https://drive.google.com/uc?export=view&id=10D2NyUC20K5XB0BZJ2Gwp6XaOvKPKs3n",
            "https://drive.google.com/uc?export=view&id=1YeBK8kFTsCIgK0IfuxuzaU2NFVedMTAG",
            "https://drive.google.com/uc?export=view&id=1zR9abXK2iZzlc6fB4mA_8kkmoTX34RsG",
            "https://drive.google.com/uc?export=view&id=1zAhYU5LDoLIHHv8M8ikqshl02GQhyHAx",
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
                "Kesan": "Abangnya keren luar biasa",  
                "Pesan": "Kapan futsal lagi bang?"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "Cantik dan keren kakaknya",  
                "Pesan": "Semangat menjalani masa-masa akhir kuliah kak"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "Keren dan atletis",  
                "Pesan": "Ajarin voli bang"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "Abangnya pintar dan keren",  
                "Pesan": "Bantu nilai ads kami bang"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "Kakaknya cantik dan pintar",  
                "Pesan": "Dah berapa journal kak yang di review?"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "Abangnya jago dan pintar",  
                "Pesan": "Bantu nilai praktikum strukdat bang"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "Kakaknya cantik dan pintar",  
                "Pesan": "Semangat kuliahnya kak"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "Kakaknya pintar dan keren",  
                "Pesan": "Asiknya baca journal bu mika apa kak?"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "Kakaknya cantik dan pintar",  
                "Pesan": "Asik ya kak review journal bu mika?"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "Kakaknya pintar dan keren",  
                "Pesan": "Semangat kak menjadi pj tugas poisson"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "Cantik dan hobinya baru pertama kali dengarnya",  
                "Pesan": "Gimana tu kak hobinya?"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "Abangnya keren dan hebat",  
                "Pesan": "Semangat ngoding wisatanya bang"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "Abangnya cakep",  
                "Pesan": "Semangat ngoding wisatanya bang bareng bang aditya"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "Kakaknya keren apalagi hobinya",  
                "Pesan": "Berapa banyak journal yang sudah di review kak?"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "Abangnya keren dan hebat",  
                "Pesan": "Main game apa biasanya bang?"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15gfDupKjj4kqCHT0uPED6rwdZnuRgQF1",
            "https://drive.google.com/uc?export=view&id=1vjop1Alvj5bpyL-It6CkfnSy5E8vut0f",
            "https://drive.google.com/uc?export=view&id=1y1mFhs0nKAqwmgKrUBIpWdc8WSTnCxB1",
            "https://drive.google.com/uc?export=view&id=12kxtHhO2LoRHCqUkbcinlwf4gALFWfBM",
            "https://drive.google.com/uc?export=view&id=1fjvA2h2_PSlpe6RabwCON3JtAVGQl-oj",
            "https://drive.google.com/uc?export=view&id=1VUyzPY3Y6omMQZYeA-yZ4GgJLpQGu5k7",
            "https://drive.google.com/uc?export=view&id=134hy9-pRv7BRRARuVYcDfEnQsok9I-N_",
            "https://drive.google.com/uc?export=view&id=11b4MzsDc7kx9J2W-qczdXSI7XrvWOLfO",
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
                "Kesan": "Banyak fun fact abangnya",  
                "Pesan":"Semangat bang dah mau tamat kuliahnya"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "Kakaknya keren",  
                "Pesan":"Semangat semester tujuhnya kak"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "Kakaknya rajin ngitung duit",  
                "Pesan":"Semangat semester tujuhnya kak"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "Abangnya keren",  
                "Pesan":"Semangat kuliahnya bang"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "Abangnya jago menawarkan sesuatu",  
                "Pesan":"Semangat kuliahnya bang"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "Abangnya keren dan atletis",  
                "Pesan":"Sukses terus kedepannya bang"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "Kakaknya baik",  
                "Pesan":"Sukses terus kak"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "Kakaknya cantik dan suka ketawa",  
                "Pesan": "Semangat kak bermain alat musiknya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1j5OXJ30UYa81_YR32tvY25bDT6W-Sn1J",
            "https://drive.google.com/uc?export=view&id=1HQSzpAo6G1OURLzzEuHFiFayL8RPNdfy",
            "https://drive.google.com/uc?export=view&id=1z_FEDY8SlDfQzBoUYWD_HzwL3BSAW7mm",
            "https://drive.google.com/uc?export=view&id=1G9zK7PA2Bmd_MaGw8CoC-E1sDJvrDLHW",
            "https://drive.google.com/uc?export=view&id=1hbBhrXJQHhyWVvGgvf6qOqF24foJuBGa",
            "https://drive.google.com/uc?export=view&id=1bSlnhZY5pYLro5THzFSg_rWPHZMsjmrx",
            "https://drive.google.com/uc?export=view&id=1WSrDLcbLGSMDtZcZJTSkTXtPqwQgVUO4",
            "https://drive.google.com/uc?export=view&id=18pvZk_Gx49AY4iDBLcwXA38J1EIs5Jvs",
            "https://drive.google.com/uc?export=view&id=1Itc3N6qmRuZikfeqylMR8fuaKwWzsyW3",
            "https://drive.google.com/uc?export=view&id=1sy7D37zwakbL1h673DEzXVclCbIjxosG",
            "https://drive.google.com/uc?export=view&id=1yZNaepfaujWQAka1fzt_A2sjhWnYZqxY",
            "https://drive.google.com/uc?export=view&id=1fia6Pwb-owHxP3Ps-izmrSl1O97rF8Id",
            "https://drive.google.com/uc?export=view&id=1LeqP3K80iEAZZe_HZlrM9kKLbvfe6pyo",
            "https://drive.google.com/uc?export=view&id=1j2Zj5rFgZ01DnYFgumSj3mlCa1H84yPK",
            "https://drive.google.com/uc?export=view&id=1lZrdKIICNn31ipqsRiIqqvoAKTaERjxI",
            "https://drive.google.com/uc?export=view&id=1E1xyULlFxTbDPleRs17Q6preHPiVlzP2",
            "https://drive.google.com/uc?export=view&id=1ktqMELMV-02IeteWawq6DdpEgKlTxatk",
            "https://drive.google.com/uc?export=view&id=1sNrHtpFROZbT3leJim-KxqJqPb8tAP_H",
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
                "Kesan": "Serius dan bicara yang penting saja abangnya",  
                "Pesan": "Semangat menjalani masa-masa akhir kuliahnya bang"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "Kakaknya cantik dan keren",  
                "Pesan": "Semangat kuliah dan ngeditnya kak "
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "Senyuman kakaknya manis",  
                "Pesan": "Semangat menjalani masa-masa akhir kuliahnya kak"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "Kakaknya cantik dan atletis",  
                "Pesan": "Semangat kak ngegym nya"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "Kakaknya cantik juga keren dan ceria ",  
                "Pesan": "Semangat nulisnya kak"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "Positive vibes terus humble dan ceria",  
                "Pesan": "Tetap ceria dan semangat kak"
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "Kakaknya cantik dan keren",  
                "Pesan": "Tolong jagain adit kak"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "Kakaknya keren dan cantik juga",  
                "Pesan": "Semangat kak kuliah dan ngodingnya"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "Abangnya santai dan asik",  
                "Pesan": "Hobinya dah ketemu bang?"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "Kakaknya keren luar biasa",  
                "Pesan": "Dah berapa film kak yang ditonton?"
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@gymnn.as",
                "Kesan": "Terlihat keren dan soleh",  
                "Pesan": "Genre komiknya apa bang?"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "Kakaknya cantik dan keren",  
                "Pesan": "Inpo jj apa yang sering didengar kak"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "Kakaknya cantik dan baik",  
                "Pesan": "Jangan nangis terus kak"
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": "Abangnya terlihat tidak banyak bicara",  
                "Pesan": "Semangat bang dah mau tamat kuliahnya"
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "Abangnya keren terus jago ngoding dan ceria",  
                "Pesan": "Ajarkan biar jago ngoding bang"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "Abangnya pintar dan jago",  
                "Pesan": "Jagain fabio bangg"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "Abangnya keren personal brandingnya",  
                "Pesan": "Serial bumi dah tamat kah bang?"
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "Kakaknya baik dan ceria",  
                "Pesan": "Semangat kak kuliahnya dan sapu dulu sebelum ngepel"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()