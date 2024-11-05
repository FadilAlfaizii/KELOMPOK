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
            "https://drive.google.com/uc?export=view&id=1k55htE2BggSHYnJmioMNEy8LSEC0E43e",
            "https://drive.google.com/uc?export=view&id=1k66MfeRwdf_t4M4YrLqTDgjrlxxHho39",
            "https://drive.google.com/uc?export=view&id=1kF-KefyhohXYsC6ahiFKXUjy2BBO_Qkt",
            "https://drive.google.com/uc?export=view&id=1kFi_oOlZ9NbSTzNShn4_vaiIr5V19HGz",
            "https://drive.google.com/uc?export=view&id=1k9Bsm5rZAByQJ6ijurMR79KP_x4hC6VS",
            "https://drive.google.com/uc?export=view&id=11k4UAarQxu1SFLndZLhgssCrl0kNi1iO",
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
                "Kesan": "Keren abis",  
                "Pesan":"Semoga bisa kasih inspiratif ke adek tingkat"
            },
            {
                "Nama": "Pandra Insani Putra Azwar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "berwibawa",  
                "Pesan":"Semoga bisa kasih arahan ke adek tingkat"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagaralam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "cakep, baik",  
                "Pesan":"Semoga bisa kasih bimbingan kesekretarian ke adek tingkat yang membutuhkan"
            },
            {
                "Nama": " Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal": "Payakumbuh, Sumbar",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "keren, baik",  
                "Pesan":"Semoga bisa kasih bimbingan kesekretarian juga ke adek tingkat yang membutuhkan"
            },
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "Aura bendaharanya nampak",  
                "Pesan":"Semoga bisa kasih bimbingan kebendaharaan ke adek tingkat"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "kakanya agak pemalu",  
                "Pesan":"sehat-sehat kakak bendahara"
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jVcC1JWr5GJPixmkKiSqGRfTomIMJO4k",
            "https://drive.google.com/uc?export=view&id=1jYcwhHeaQhEVibebR79A5F4JX19e4lPD",
            "https://drive.google.com/uc?export=view&id=1joFf6qLTJjswbR4MUAQCqOeagkk3aQXI",
            "https://drive.google.com/uc?export=view&id=1j_3AsG2_e-JDwWBf7kmGylUNwJ21nZqX",
            "https://drive.google.com/uc?export=view&id=1jVjenA3Fex2Mx7tSznXpAZObJpHpwOhi",
            "https://drive.google.com/uc?export=view&id=1jU2XZLolJN4YTWW925GHuVhNwjdakBo8",
            "https://drive.google.com/uc?export=view&id=1jS8kaqdVj_I71Pf0mUMoysCVhibFjY_X",
            "https://drive.google.com/uc?export=view&id=1jw7_KfsWcgJ6aUFD2XsoqT4CZXnwWzkJ",
            "https://drive.google.com/uc?export=view&id=1CJLdgUh58X5hIXIQky47zlJ3CWkbfdR2",
            "https://drive.google.com/uc?export=view&id=1jlGP__WU-cUL7ZLR2TAiIpiSlX0QMMIM",
            "https://drive.google.com/uc?export=view&id=1k1ly0mGuraYa7IPIH2cVzSnfzt_Ic7QA",
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
                "Kesan": "wanita independen",  
                "Pesan":"semoga bisa nularin ilmunyaa"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tanggerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, Nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "kakaknya kalem",  
                "Pesan":"semangat kakak"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150 ",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "ramah, baikk",  
                "Pesan":"kalo ketemu senyum balik kak"
            },
            {
                "Nama": "Anisa Dini Amalia",
                "NIM": "121450081",
                "Umur": "21",
                "Asal":"Tanggerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "keren",  
                "Pesan":"sehat-sehat kakak keren"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "asik",  
                "Pesan":"semoga bisa ketemu lagi"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Batu Raja, Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "orang keren",  
                "Pesan":"info tutor prak alpro banh"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "cool,kece",  
                "Pesan":"ajarin jadi kece bang"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Sukabumi, Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka Ikut Tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "gamau foto kalo ga megang pohon",  
                "Pesan":"semoga kalo foto lagi yang dipegang iman dan takwa"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "121450156",
                "Umur": "22",
                "Asal":"Surakarta, Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "jago coding agaknya",  
                "Pesan":"semoga bisa kaya abangnya"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "lord prak alpro",  
                "Pesan":"info tambahan nilai banh"
            },
            {
                "Nama": "Berliana Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "suka senyum",  
                "Pesan":"sering-sering senyum kak, ibadah"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=154HDC-AuP-N6MRwykW5oVQ85H4REOe2z",
            "https://drive.google.com/uc?export=view&id=157cC-p5mO01TX7S9PEtYa8Ay3f0yhOPo",
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
                "Kesan": "Ilmu sama Pribadinya keren abiss",  
                "Pesan":  "Semoga bisa ngikutin kaya kakaknya"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "asik, baik",  
                "Pesan": "jangan cape kasih semangat & inspirasi ke adek tingkat bang "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UIJVOWmfWB20rtxZG7FLDJbo5zTFuM39",
            "https://drive.google.com/uc?export=view&id=1v1blI1qlILl0Ko-n46RVMFwix-AgVbVw",
            "https://drive.google.com/uc?export=view&id=1z3Baos565-fYU-RsQnhMu-vShKxp1niC",
            "https://drive.google.com/uc?export=view&id=1jLX_CkIcm52vXu0j2bNA2TONnRgZfnWb",
            "https://drive.google.com/uc?export=view&id=1Is38G6KrY1JXMNF4kozchRiY0P8X6sci",
            "https://drive.google.com/uc?export=view&id=1R-sNb2Nz1xeUnPxqtHYdOhddvhObpWHo",
            "https://drive.google.com/uc?export=view&id=1xrLD45bEisl9EpKWhQe0VOXZd3UoDLCT",
            "https://drive.google.com/uc?export=view&id=1ANuR7DNH8Wr3_knugJqqxZzTzyssPUcs",
            "https://drive.google.com/uc?export=view&id=1Sv8PprUkepv07YiFcN6TGoHhN-63k62M",
            "https://drive.google.com/uc?export=view&id=142c5krlEgHUr_XQczDEYQraUeNA1ZdQP",
            "https://drive.google.com/uc?export=view&id=1jM9FJyj9SjQR-yuSHGvVO30wETjSn6ne",
            "https://drive.google.com/uc?export=view&id=1T4lm8igAvcoCPR1MRAiHx_vK7myMrNNZ",
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
                "Kesan": "orang keren yang ngasi banyak inspirasi",  
                "Pesan":"sehat-sehat orang keren"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "cakep, kalem",  
                "Pesan": "jangan cape buat senyum kak"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "asikk",  
                "Pesan": "semoga bisa ikutan jadi orang yang asik"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "lebih cakep ketawa daripada jutek",  
                "Pesan": "sering-sering ketawa dong kak"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "cool",  
                "Pesan": "infokan cara jadi cowo cool banhh"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",  
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "lembut",  
                "Pesan":"tetap lembut dimanapun kakak berada"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "aura positif vibes",  
                "Pesan": "sering-sering senyum ya kak"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "aura islami",  
                "Pesan": "jangan cape nyebar kebaikan bang"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "lembut, kalem",  
                "Pesan": "semangat kakak jadi kuliahnya"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "kalem gitu",  
                "Pesan": "tetep kalem trus kak"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "abangnya ceria",  
                "Pesan": "trus sebarkan keceriaan bang"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "kalem, cool",  
                "Pesan": "info jadi cowo cool bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ofe7Wq9X-q5vdj3yCJN13jPNS0QPROZV",
            "https://drive.google.com/uc?export=view&id=1ohOv18tmmb7TfXI8caqVBT3eHWCaz2Xo",
            "https://drive.google.com/uc?export=view&id=1p2dgzYg7nL2AV2hwtjJldwzpLh1TaMe5",
            "https://drive.google.com/uc?export=view&id=1pRLWqzEg9z2GaWrP3ZqseyZiOK3rZx53",
            "https://drive.google.com/uc?export=view&id=1p1HpRgFqmnCbaOB2S-I8u3Lbq3ejHOnE",
            "https://drive.google.com/uc?export=view&id=1p-qAcvAVzA72jhqA7WWSxgF2GTtmXSk5",
            "https://drive.google.com/uc?export=view&id=1oyqpFOiuWUaIJS-MkFzHQv1PIdG8iG1y",
            "https://drive.google.com/uc?export=view&id=1pPnRq79gDUAYo8ud1KH0j-DJ_Ygo3iIt",
            "https://drive.google.com/uc?export=view&id=1p9E511gFo79HgsjJQ0inL1waZwE2BF6z",
            "https://drive.google.com/uc?export=view&id=1ng8yrGRUuMcM2JTcgJtiWszSDueCtfZK",
            "https://drive.google.com/uc?export=view&id=1ntqSebq1j_4fFmA5OnrjYj5yh_JiXfL3",
            "https://drive.google.com/uc?export=view&id=1oPvbW1O5hAhg7ojmvt5lIaI9VGm0ObMc",
            "https://drive.google.com/uc?export=view&id=1nuhuSmP_-O1HOS7wIeVzN21lvYXAJMAK",
            "https://drive.google.com/uc?export=view&id=1o63_gSkOxtaYBsYELuawYqBq2XoU3ZfA",
            "https://drive.google.com/uc?export=view&id=1nieAUQczUnq1U3Ri7PLGhiX-PHoQIlrR",
            "https://drive.google.com/uc?export=view&id=1nrIgiG3vcxWDpReUbJIgeCbbx7PbdLcg",
            "https://drive.google.com/uc?export=view&id=1oU3sabPPgfWFmpC0C1mu9Q9P19qCYFWN",
            "https://drive.google.com/uc?export=view&id=1nyPOHdIhnYCA9EPEvvu_XblWXjcImVYe",
            "https://drive.google.com/uc?export=view&id=1pTVL3js5Y_UFPLCxCeANU2553KZReLv7",
            "https://drive.google.com/uc?export=view&id=11scMMXZn8EKD-fqS6DrSdxiLeK9Vm0Bs",
            "https://drive.google.com/uc?export=view&id=19eV6wTH3lSmP0sC-hF4UdYKyO5bFqYGY",
            "https://drive.google.com/uc?export=view&id=11t60A7FMOkOcXj2mBnZ4He8Yfhe-eh3i",
            "https://drive.google.com/uc?export=view&id=11tp3orVqxtZu8FBVfgwaiP5BBAy7Cuwf",
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
                "Kesan": "publik speakingnya jago",  
                "Pesan": "ajarin publik speaking bang"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "asik orangnya",  
                "Pesan": "semangat kakak abet"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "keren kakanya",  
                "Pesan": "amankan kaderisasi kakk"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "bisa menyesuaikan diri dengan keadaan atau kondisi",  
                "Pesan": "senyum dong kak, ibadah"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "kakanya baik",  
                "Pesan": "jangan cape buat baik kak"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "asik, humornya seru",  
                "Pesan":"tetep asik dan seru bang der"
            },
            {
                "Nama": "Eksanty F. Sugma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "eksantyfebriana",
                "Kesan": "cakep, baik, asik",  
                "Pesan": "amankan nilai praktikum ads kak"
            },
            {
                "Nama": "Oktavia Nurwinda Puspitasari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@oktavianrwnda",
                "Kesan": "baik, lembut",  
                "Pesan": "jangan cape jadi orang baik kak"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "keren, kalem",  
                "Pesan": "semangat bang ferdy"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "asik, ada aja gebrakannya",  
                "Pesan":"sehat-sehat bang devan"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "cool",  
                "Pesan": "ajarin jadi cowo cool dong bang"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "orangnya aktif, capo suporteran",  
                "Pesan":"semangat jadi capo bang"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "pinterr",  
                "Pesan": "ajarin jadi orang pinter bang"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.",
                "Kesan": "tinggi, keren",  
                "Pesan": "infokan cara tubuh ideal bang"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "cantik, baik, asprak strukdat",  
                "Pesan": "bismillah nilai praktikum strukdat tinggi"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "cantik, pendiem",  
                "Pesan": "sehat-sehat kaka baik"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "kalem, keren",  
                "Pesan":"ajarin jadi orang keren bang"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "pinter, jago basket",  
                "Pesan":"jangan lelah transfer ilmu ke adek tingkat kak"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "baik, asik, tenang",  
                "Pesan": "ajarin jadi orang yang terlihat tenang bang"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "keanya suka suport adek tingkat abangnya",  
                "Pesan": "semangat bangg"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "cantik, baik, keren",  
                "Pesan": "jadi pembawa acara kader lagi dong kak, asik soalnya"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "asik, ngimbangin adek tingkat",  
                "Pesan": "semangat bang rafly"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "agak bingung bedain kakak ini sama kembarannya",  
                "Pesan":"semangat kaka kuliahnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mzK05vHqdzFliA0lxEm3I4vfdFNan1T_",
            "https://drive.google.com/uc?export=view&id=1n-do4ASUiykk5gM8f8q3CizNmvvrGD26",
            "https://drive.google.com/uc?export=view&id=1mdaWpep6GAasBOdXR-lGHreykhPK9Wjj",
            "https://drive.google.com/uc?export=view&id=1mpVbwdrciYspOO8ygO4R-t1uPRN7F1pi",
            "https://drive.google.com/uc?export=view&id=1mjrpP_hG601HmkOkQvqoY2pKJRTeVyLn",
            "https://drive.google.com/uc?export=view&id=1mypj0ewI1WWKoNcAkgFfOA1axa64215s",
            "https://drive.google.com/uc?export=view&id=19ebPvKwhjSoO7_NAdHLtt5Wr6e1gEGTo",
            "https://drive.google.com/uc?export=view&id=1mmFeqI-4Nc45z8MXIDAi_GZRDAOahVCI",
            "https://drive.google.com/uc?export=view&id=1mos3xnE2nl_T9Qb4pjYzeanmt4NY6mmL",
            "https://drive.google.com/uc?export=view&id=1mfu801M9q03vb-PJwWaIwFvjxd2vbTmd",
            "https://drive.google.com/uc?export=view&id=1nC0D2u_bZzAkagLJgXkr0wi_7psJ60_l",
            "https://drive.google.com/uc?export=view&id=1nH78J7pvRE1_GuoxUrQwIayQfpJDXL2P",
            "https://drive.google.com/uc?export=view&id=1nRBr8Y84v93FFQgn9SgIuWdfCTubFK4M",
            "https://drive.google.com/uc?export=view&id=1mZLNpiSNXos0VBuAOBwnOgs3N86CUCpG",
            "https://drive.google.com/uc?export=view&id=1mzQr6jfYPdmh1AOAa6uegGg9NiL2w6y5",
            "https://drive.google.com/uc?export=view&id=1n7wGiE2zR2Sv-57gmJdA3gmw5ZClCxDF",
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
                "Kesan": "abangnya perhatian",  
                "Pesan": "jangan cape kasi perhatian ke adek tingkat bang"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "logatnya orang lampung",  
                "Pesan": "tinggal di rajabasa sebelah mana kak"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "humornya receh abiss",  
                "Pesan":"stop kak, saya gatahan ketawa trus"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "baik kakanya",  
                "Pesan":"ajak ke kebun kaka dong"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@",
                "Kesan": "cantik, baik",  
                "Pesan":"ajarin main golf kak"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "baik, agak pemalu",  
                "Pesan": "ajak surving kak"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "cakep, baik",  
                "Pesan":"semangat kuliah kakak baik"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "kakaknya keren,",  
                "Pesan": "amankan nilai praktikum ads kak"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "gondrongnya keren",  
                "Pesan": "ajarin orang keren bangg"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "asik, baik",  
                "Pesan": "jangan cape baik ke adek tingkat kak"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "keren, stylis",  
                "Pesan": "moga bisa keikut jadi keren"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "asik, baik",  
                "Pesan": "semangat trus bang kuliahnya"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "kakanya agamis",  
                "Pesan": "tetep semangat kak jadi muslimin yang baik"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "keren, keliatan garang",  
                "Pesan":"semangat trus bang irvan"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "baik, care, asik",  
                "Pesan": "jangan lelah menjaga keseimbangan nilai praktikum dekting kak"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "satu sekolah sama kawan saya",  
                "Pesan": "jangan lupa senyum kak"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "baik, asik",  
                "Pesan":"semangat kuliahnya yak bang"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "asik, baik, ceria",  
                "Pesan": "kalo cape jangan lupa istirahat kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1mBL6g_P3ufzc1otL0Umw1VfcxUWl7y8y",
            "https://drive.google.com/uc?export=view&id=1mCj1DMHRHqb8vdBCuflBmAb-U7Nc1z_0",
            "https://drive.google.com/uc?export=view&id=1m8SZ4ipkeiuF-Z2wpuBpxwdePsSIDnuo",
            "https://drive.google.com/uc?export=view&id=1mWjSbeJXdBufM91NWKoDjg6vBM6JZg2n",
            "https://drive.google.com/uc?export=view&id=1mVSSo8v9PLeIBeCFAfF1RS1ffLVGfU_P",
            "https://drive.google.com/uc?export=view&id=1mNP6tcGprQzEaLAalTJKLUsrkFXfbVmj",
            "https://drive.google.com/uc?export=view&id=1mKT9Tm40kqDJ8GDhtNcJ8ntZyZMIoeJD",
            "https://drive.google.com/uc?export=view&id=1mDIxgy0yj26ZPUUMysVURo99ef2fwLco",
            "https://drive.google.com/uc?export=view&id=1m2JLrxaN-JzDRuOBePZRAixEufueGeAI",
            "https://drive.google.com/uc?export=view&id=1mUNML9d_I7T0_B46Ty63_KIm8W07J6J5",
            "https://drive.google.com/uc?export=view&id=1mKAcQeRxsUVPicyRU9l-HeaCq1jWl80t",
            "https://drive.google.com/uc?export=view&id=1mL-eo6Ks0F4GsHwKFfwxXAP3SdiEUYSm",
            "https://drive.google.com/uc?export=view&id=1mRDbp3f3Yz4IuWDpOSO24F8F0RA6ziXX",
            "https://drive.google.com/uc?export=view&id=1mC_TSO5Meu6QkngdLXsAixoCr3xQzxxU",
            "https://drive.google.com/uc?export=view&id=1lz7mWY2aLSICRBlOoL1s5MVyg-n1I3vw",
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
                "Kesan": "kalem, baik",  
                "Pesan": "trus jadi orang baik bang"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "cantik, manis",  
                "Pesan": "ajak masak dong kak"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "baik, kalem",  
                "Pesan": "sehat-sehat bang ahmad"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "baik, pinter",  
                "Pesan": "bantu nilai prak ads ku bang"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "agak susah bedain kaka sama kembarannya",  
                "Pesan": "semangat jalanin kuliahnya kak"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "baik, pinter",  
                "Pesan": "amankan nilai prak strukdat bang"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "cantik",  
                "Pesan": "info-info webinar kak"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "cantik, baik, lembut",  
                "Pesan": "jangan cape kak, kalo saya nanya trus pas prak"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "cantik, baik",  
                "Pesan": "semangat trus kaka cantik"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "aura orang pinter",  
                "Pesan": "amankan nilai kelompok 3 kak"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "baik,cantik, the best la",  
                "Pesan": "selesai kader main sama anak 67 kak"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "baik, pinter",  
                "Pesan": "ajarin ngoding bang"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "keren, jago speaking",  
                "Pesan": "ajarin publik speaking"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "cantik, lembut",  
                "Pesan": "bolehlah kak review journal ke saya"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "namanya baguss",  
                "Pesan": "semoga happy trus bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=150beoqJJRl_o8jkc3Tf9AjbKYdY43OfK",
            "https://drive.google.com/uc?export=view&id=14nuNAnci2ILp2ptfndjwy6LB_1nkmR4o",
            "https://drive.google.com/uc?export=view&id=14s0ORgTuhXVe3vU825OfvFeONW0Vi9_A",
            "https://drive.google.com/uc?export=view&id=14sbvWadxLwm6ZtOtY328Wx7E-A0vBQwm",
            "https://drive.google.com/uc?export=view&id=14y3Aon2moGOhX1wciKSS3JYmb733IXJp",
            "https://drive.google.com/uc?export=view&id=14wFlDHZp5eQjwXVMHYI_aFeGrvRxsEQu",
            "https://drive.google.com/uc?export=view&id=1CLtOmhUVevGRBifcqr4RqlCg3IU60x-_",
            "https://drive.google.com/uc?export=view&id=1Bw1aazSLaYutqaklNrgxtbTXRpU0lndf",
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
                "Kesan": "asik, publik speaking bagus",  
                "Pesan":"sehat-sehat bang andrian"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "cakep",  
                "Pesan":"ajak nonton film dong kak wkwk"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "banyak duit keanya kaka ini",  
                "Pesan":"bolehkah pinjam seratus"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "baik, orangnya aktif",  
                "Pesan":"ayo badminton bareng bang"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "baik, pinter, asik",  
                "Pesan":"ajak saya touring bang"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "badannya ideal",  
                "Pesan":"semangat bang pimpin suporteran"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "baik, kalem",  
                "Pesan":"ajarin produktif kak"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "baik, lembut",  
                "Pesan":"ajarin alat musik daerah kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kTocriiVEltnt_wCEHeqmYLk-e6NzDEO",
            "https://drive.google.com/uc?export=view&id=1lgOmWW2zDDY0MmjAPfPiScMuhTmn58Jk",
            "https://drive.google.com/uc?export=view&id=1knQpRwLU9RasZgtJ4ATYRHBZ6xq6SZVB",
            "https://drive.google.com/uc?export=view&id=1kkmekEOfgS7UHk2ZP8YdgUNa_45BiDwe",
            "https://drive.google.com/uc?export=view&id=1lLieK2M3KG6alDaPGMQsxPwAvyS2VnHE",
            "https://drive.google.com/uc?export=view&id=1kNefgmQfU8ZyvCas4l5c2_oKYIwk4oSf",
            "https://drive.google.com/uc?export=view&id=1ltROdOUWYTgq8iOdINo6DYJXJENVwaRv",
            "https://drive.google.com/uc?export=view&id=1kRYVEXFcwY6Sk_8z18SWjSlx93JXbLYd",
            "https://drive.google.com/uc?export=view&id=1l3xsOhyJyPP7rz_ibLtdKUPYKZ5x9azl",
            "https://drive.google.com/uc?export=view&id=1lTTOZ7Vm32ny611Ul4wNNv8RRvmC7kfV",
            "https://drive.google.com/uc?export=view&id=1lwYrzhW_YG835lo6ErQWFU9dz21sfSEX",
            "https://drive.google.com/uc?export=view&id=1ltuGqF4WiIYpMioLVcjsUXaTkGoLOHVj",
            "https://drive.google.com/uc?export=view&id=1lZcEpTztT7vgrKTHzTH-_IbNwdNvG1qn",
            "https://drive.google.com/uc?export=view&id=1l9iFhfltBh4Tj5m3Yoc3DW2ts1bBGUri",
            "https://drive.google.com/uc?export=view&id=1lYQcM4EXF6rvKbYogXhCqEfKEImdDVPH",
            "https://drive.google.com/uc?export=view&id=1koS5ZZ2b4vl-cw01ZRPmqWlxH3zkuguQ",
            "https://drive.google.com/uc?export=view&id=1kQrPBVhPnW1lSwNtv5iyudNsG_cWswiN",
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
                "Kesan": "keren, tegas",  
                "Pesan": "semoga bisa jadi pribadi yang tetap tegas"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "cantik, kalem",  
                "Pesan": "jangan lupa senyum kakaa"
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "cantik, baik, independen",  
                "Pesan": "semoga bisa niru inspirasi kakanya"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "cantik, tinggi",  
                "Pesan": "semangat kaka cantik"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "asik, lucu",  
                "Pesan": "tutor gamales baca buku kak"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "cantik, baik, pinter",  
                "Pesan": "ajak aku shopping kak"
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "asik, lucu, baik",  
                "Pesan": "jangan cape jadi orang asik sama lucu kak"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "baik, kalem",  
                "Pesan": "ajarin ngoding dong kak"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "keren, baik",  
                "Pesan": "makasih bang dah minjemin baju waktu riuh perdana"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "baik, kalem",  
                "Pesan": "ajak saya nonton kak"
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@gymnn.as",
                "Kesan": "keren, kalem, baik",  
                "Pesan": "info recomended komik bang"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "baik, cantik, kalem",  
                "Pesan": "info playlistnya kak"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "baik, kalem, lembut",  
                "Pesan": "sedih aja ya kak jangan nangis kalo nonton film"
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "baik, pinter",  
                "Pesan": "ajarin saya ngoding bang"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "baik, pinter, keren",  
                "Pesan": "tetep jadi orang asik sama baik bang"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "baik, pinter, asik",  
                "Pesan": "bolehlah pinjem novel Tere Liyenya bang"
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "baik, kalem, lucu",  
                "Pesan": "jadi orang yang kalem trus ya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()