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
            "https://drive.google.com/uc?export=view&id=1JeBs_SPXfVkxa3Sw121f_1-vAYCtuxuo",
            "https://drive.google.com/uc?export=view&id=12DBEABSGLlHvxIqS5nftxihwb55NSTmc",
            "https://drive.google.com/uc?export=view&id=1f-nG10A2EGc6j-t9gtalGeo73KdBR_6k",
            "https://drive.google.com/uc?export=view&id=1vOiRGpJkTwDGJIKC0UmIkeoXSugqfy6u",
            "https://drive.google.com/uc?export=view&id=11xjA7cCtiyabsNxk5QKcoIZAQzOTSdmO",
            "https://drive.google.com/uc?export=view&id=1I24f3K6yWhNwroKNr1uFlYSZ1vkt5ypv",
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
                "Kesan": "Abangnya berkharisma seperti namanya",  
                "Pesan":"Semangat untuk bang kahim yang udah mau selesai jabatannya"
            },
            {
                "Nama": "Pandra Insani Putra Azuar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "Abangnya sangat membaur",  
                "Pesan":"Semangat bang jadi sekjen"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagaralam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "Kakaknya Cantik",  
                "Pesan":"Semangat kak ngaspraknya"
            },
            {
                "Nama": "Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh, Sumatera Barat",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin Pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "Senyum kakaknya manis",  
                "Pesan":"Semangat lpjannya kak"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "Kakaknya palembang banget",  
                "Pesan":"Semangat kakak cantik"
            }, 
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "Vibes kakaknya bendahara banget",  
                "Pesan":"Semangat kak ngitung uangnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Z-b3YAadSr8B6w-kjZ8kvMrYzIVjwo90",
            "https://drive.google.com/uc?export=view&id=1AHtRPQ_cSesWbBMp2nr0n-WH-S7H0M9N",
            "https://drive.google.com/uc?export=view&id=1uIa43FOm0tgLM6BOUNDS_TUo7l61zsPt",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1_PDBlTkyQal2Y5GxDPG6C256e3R486NL",
            "https://drive.google.com/uc?export=view&id=1kWdaDw9A3Lv3QUIFWptvhtWiokV5KnON",
            "https://drive.google.com/uc?export=view&id=1YsT0cX6aDYrLjFzGCOiDh6w2Pd8SBIYg",
            "https://drive.google.com/uc?export=view&id=1_biCgoapsyG8O8S7h5TtAZNy-lOycaGR",
            "https://drive.google.com/uc?export=view&id=1wmz65dAU-03-jPWNCG-hPMCydynTcdc8",
            "https://drive.google.com/uc?export=view&id=11To7zk9x4r6fQwq6u3roXax5eFbhCb4V",
            "https://drive.google.com/uc?export=view&id=1yEPYkImeQFdSB7ggOR4O6xUpLVy3kJKh",
        ]
        data_list = [
            {
                "Nama": "Tri Murniya Ningsih",
                "NIM": "121450038",
                "Umur": "21",
                "Asal":"Bogor",
                "Alamat": "Raden  Saleh",
                "Hobi": "Kalo ke coffe shop pesen red velvet bukan kopi",
                "Sosmed": "@trimurniyaa",
                "Kesan": "Kakak berwibawa tapi lucu",  
                "Pesan":"Kak notis aku dong jadi ketua baleg"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tanggerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, Nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "Kakaknya soft bgt",  
                "Pesan":"Semangat kakak"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "Kakak nya humble",  
                "Pesan": "Kak notis aku dong masuk baleg "
            },
            {
                "Nama": "Annisa Dini Amaliya",
                "NIM": "121450081",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "Kakaknya cakep",  
                "Pesan": "Kak notis aku dong jadi bagian dari baleg"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger Lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "Kakaknya seru",  
                "Pesan":"Semangat kakak cantik"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal": "Batu Raja, Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca Buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "Senyum Abangnya manis banget",  
                "Pesan":"Bang bagusin nilai praktikum Alpro saya ya "
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main Kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "Abangnya riz banget mana ketceh lagi",  
                "Pesan":"Infokan film anime yang bagus bang"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Sukabumi, Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka Ikut Tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "Kakaknya baik mana gampang akrab lagi",  
                "Pesan":"Ajak aja itu bang jeremi berantem kak"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "121450156",
                "Umur": " 22",
                "Asal": "Surakarta, Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "Abangnya lucu suka ketawa",  
                "Pesan": "Tutor ngoding bang"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "Abang ini terlalu OP",  
                "Pesan": "Jangan jahat-jahat sama saya bang"
            },
            {
                "Nama": "Berlianda Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal": "Sumbar",
                "Alamat": "Way Huwi",
                "Hobi": "Main Game",
                "Sosmed": "@berlyyanda",
                "Kesan": "Suara Kakaknya kecil",  
                "Pesan": "Semangat kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "Kesan": "Kakaknya cakep, manis trus tomboy juga",  
                "Pesan": "Infokan cara lolos di senat km kak"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "Ternyata abang ini ketang 22",  
                "Pesan": "Jangan lupa senyum bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10mxHRivHmf9jpKGGxMxWk5JQeyHFFm5h",
            "https://drive.google.com/uc?export=view&id=1dwwKWAnjrA4Tj6FbAl-fDPVkwdDw_kpy",
            "https://drive.google.com/uc?export=view&id=1Rk8VGyL822qivEM6CAPufHS59DgEB_xh",
            "https://drive.google.com/uc?export=view&id=1Wms0qrVOhuWjvaR-6Gugky8zGLFH4GtM",
            "https://drive.google.com/uc?export=view&id=1NiGbrOLxb9hmfffXsQkn3JLQOwz5mji9",
            "https://drive.google.com/uc?export=view&id=1j3c3t9WKImhcAU5jEJ7-09XDRSX2QriQ",
            "https://drive.google.com/uc?export=view&id=1JYnLc3srP_W0Fi53xhEqedHAF7odek27",
            "https://drive.google.com/uc?export=view&id=1_rQyAaiaX8j3pZykycPo_ANNBbnCQn1d",
            "https://drive.google.com/uc?export=view&id=1WpEmpPTBmLbotq3uRBy1AbryPHzCQj1u",
            "https://drive.google.com/uc?export=view&id=1u2DgEAhPMWFViZVNF3Xeo1E1JWX6ky65",
            "https://drive.google.com/uc?export=view&id=1Vl3cL0IoYSIIIkbUK8rFiw5obb4yp85C",
            "https://drive.google.com/uc?export=view&id=1bsIAKEMfgG2MO4laVyUh0-LecvubCZdA",
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
                "Kesan": "Abangnya kocak bisa ngelucu",  
                "Pesan": "Semangat bang nugas mss nya"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "Kakaknya cantik dan kalem ",  
                "Pesan": "Semangat kak lpjan nya"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "Abangnya suka ketawa",  
                "Pesan": "Jangan lupa ketawa bang"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "Kak ranipu ternyata kalem yeah",  
                "Pesan": "Jangan galak2 kak ntr aku bilang kak elila nih, hehe"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "Abangnya keren",  
                "Pesan": "Semoga lagu abang viral yeah"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "Kakaknya manis banget",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "Kakaknya kek introvert tapi kadang ekstrovert ",  
                "Pesan": "Semangat kak ekstrovert"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "Abang ini islami bgt",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "Kakaknya cantik",  
                "Pesan": "Semangat kakak cantik"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "Kakaknya kalem  bgt",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "Abangnya  keren bgt",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "Abangnya orang batak tapi kalem bgt",  
                "Pesan": "Ayok jadi introvert bang kek orang batak pada umumnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xvN86ngbpUbK1qds-c9-zd0CvxFdQmOd",
            "https://drive.google.com/uc?export=view&id=1Yy0d0cuLVvaKMazQfQCLxPYAmfaRB5vI",
            "https://drive.google.com/uc?export=view&id=1tsrG9E3zkDm1mxHYYn5jDa3L15jBYTbc",
            "https://drive.google.com/uc?export=view&id=1jGYJcElFjmDc3vKPth_HQ-pAfrRP9FsO",
            "https://drive.google.com/uc?export=view&id=1xVDbRirqlgkKcFnrGi19czASDzfPUgRG",
            "https://drive.google.com/uc?export=view&id=1605fuNZJH_L1L4O94kkHL6c1WoyDgBtD",
            "https://drive.google.com/uc?export=view&id=1XodOkQmaAgZ1jsNWZOYlX6VW-NLzudot",
            "https://drive.google.com/uc?export=view&id=1LbEkuwO3DbJ4B_9l5KVv88zFmQLFSF8a",
            "https://drive.google.com/uc?export=view&id=1CZtzS6OLMCcf8EQugyEkD3ydQT1rgKZg",
            "https://drive.google.com/uc?export=view&id=1rSjiwOtlyiS-EY8pOxnO6UX07LSEp3eR",
            "https://drive.google.com/uc?export=view&id=1E_Mmm3StTubZ_e4SUnG4nOHKm90LdZkZ",
            "https://drive.google.com/uc?export=view&id=19SVV61gAkI_RIADgtsXzJJO_g5_v3rep",
            "https://drive.google.com/uc?export=view&id=13njBIO2trm2rBm9IpM9AcF1erFzgHKWy",
            "https://drive.google.com/uc?export=view&id=1-iPsz9NeCmJ3my1us0dCCF4EDD8rZkpw",
            "https://drive.google.com/uc?export=view&id=1s1RAsxD404QZMV1BVomvjXDuL7Tk3GUv",
            "https://drive.google.com/uc?export=view&id=1_HXkpzVBP0Rn20p9xZP8KZIIRLRGTwu_",
            "https://drive.google.com/uc?export=view&id=1s5OLUvW_uflDIDdp7Dj_UQaRi8VVvYH9",
            "https://drive.google.com/uc?export=view&id=1JFgnvKF5_-j84HkrBPmyhMGH7ap_4Ue7",
            "https://drive.google.com/uc?export=view&id=1c-ZV0BwE9iSlcCEgKPnMuRGKurdh-Wfl",
            "https://drive.google.com/uc?export=view&id=1F73h_GqL8DBX213OsX4YWS885nMhqD53",
            "https://drive.google.com/uc?export=view&id=1X-zmwk40MUmiB1KXNnQyd-NMtOzOaxgO",
            "https://drive.google.com/uc?export=view&id=13ZwvNtA9TEBDLHZ6eEF74uFEg8ixyyh-",
            "https://drive.google.com/uc?export=view&id=1U197AtKaosWAVuZdFevTsif2pFkwH5fM",
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
                "Kesan": "Publik speaking abang nya bagus banget",  
                "Pesan": "Jangan galak2 bang"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "Kakak cantik",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "Suara kakaknya khas bgt",  
                "Pesan": "Semangat kak afifah"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "Kak allya sering nahan senyum sama ketawa",  
                "Pesan": "Jangan lupa senyum kak"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "Kakaknya cantik",  
                "Pesan": "Semangat kakak cantik"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "Abangnya keren suka ngelucu",  
                "Pesan": "Semangat bang der"
            },
            {
                "Nama": "Eksanty F. Sukma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "eksantyfebriana",
                "Kesan": "Kak ashanty galak cuyy",  
                "Pesan": "Semoga langgeng sama anang ya kak"
            },
            {
                "Nama": "Oktavia Nurwenda Puspita Sari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "Kakak ini manis",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "Abang ini keren",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "Abang kocak yang lucu",  
                "Pesan": "Sehat-sehat bang biar bisa ngelucu"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "Abang  ini keren",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "Ternyata bang jo aksel cuy",  
                "Pesan": "Bang bagusin nilai prak alpro temen saya nim 046"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "Cewek abangnya cantik",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "Abang ini keren",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "Kakak ini imut",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "Marga abangnya kek temen saya",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "Abang nya keliatan galak",  
                "Pesan":"Semangat bang"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "Kakak keren",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "Ternyata ini bang ateng yang sering dibilang orang2",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "Nama abangnya lucu ada 'moana' nya",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "Kakak cantik",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "Abang ini keren",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "Kakak ini ternyata kembar kirain daftar dua divisi",  
                "Pesan": "Semangat kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Tz0ojUwXwEGO2bQeyq0eEHA7U59dVRGF",
            "https://drive.google.com/uc?export=view&id=1cBplLmelv7j7saWBqfGy_q4vETV4Ngpb",
            "https://drive.google.com/uc?export=view&id=15NaUCUOB6A_xxE-nJgg7XLV95vP969qT",
            "https://drive.google.com/uc?export=view&id=1iU3a8_r4n48NBdCKTUnEr8JTrzACB0AB",
            "https://drive.google.com/uc?export=view&id=1bZL-IXSVBsCW-XPFIsNdeZ3N1egN_NaK",
            "https://drive.google.com/uc?export=view&id=121xMNxgSvC1X1-CKbuoeoj9OwKr0ajlf",
            "https://drive.google.com/uc?export=view&id=1yvrY3_HmZXEZ0wcaR_fR9ZL0oKQpFl98",
            "https://drive.google.com/uc?export=view&id=1pz20AvSyIuuvF_ON1QYgiMmwRnuae8ny",
            "https://drive.google.com/uc?export=view&id=10sETq-xcq3PFvlsP_bn6xjwMdBUj9W2d",
            "https://drive.google.com/uc?export=view&id=12vgfECdpr8wQU0C_QXq1CNE34v01Zl4N",
            "https://drive.google.com/uc?export=view&id=1jGyaacfQd_IYJ-BA8QPOHDBDu1_0neE9",
            "https://drive.google.com/uc?export=view&id=1AExsyxOIDGNbBYRTl7Rmts9teumqGzat",
            "https://drive.google.com/uc?export=view&id=1DsCxDiT7_0I7X0Swx5fQno35TdFkQOOx",
            "https://drive.google.com/uc?export=view&id=1rAO4fRj3vUk_oTXdQB5JRJinJJHaDDTK",
            "https://drive.google.com/uc?export=view&id=1yirm9PAvRpOocPzOqfkeW82EjrMih6DN",
            "https://drive.google.com/uc?export=view&id=1KBqA5s-Us0_l4UwZ_vws0ix8HB5MQyLA",
            "https://drive.google.com/uc?export=view&id=1-P3YkR4nR3OcEPsDjwjGhDt4X4C__jyN",
            "https://drive.google.com/uc?export=view&id=1MwxS6wrmqKk8hPgPi356ZP73lmDrIazF",
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
                "Kesan": "Abangnya keren",  
                "Pesan": "Bang temen saya pengen masuk eksternal"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "Kakaknya cantik cuy",  
                "Pesan": "Semangat kakak cantik"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "Hobi kakaknya keren",  
                "Pesan": "Ajak saya  main golf kak"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "Kakak ini ternyata suka berkebun",  
                "Pesan": "Semangat kak berkebunnya"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@",
                "Kesan": "Kakaknya cantik",  
                "Pesan": "Semangat kak main golf nya"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "Kakaknya keren suka surving",  
                "Pesan": "Semangat kak survingnya"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "Kakaknya cantik trus manis senyumnya",  
                "Pesan": "Semangat kuliah kak cantik "
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "Kakanya baik cantik dan keren",  
                "Pesan": "Bagusin nilai prak ads ku ya kak"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "Ternyata abangnya kalem",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "Kakaknya seru suka",  
                "Pesan": "Jangan galak2 kak"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "Abangnya ganteng kata temen saya",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "Abangnya keren",  
                "Pesan": "Semangat bang kuliah nya"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "Nama kakak ya bagus beda dari yang lain",  
                "Pesan": "Semangat kak uyii"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "Abangnya baik dan keren",  
                "Pesan": "Semangat bang kuliah nya"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "Kak izza lucu trus kocak",  
                "Pesan": "Kak bagusin nilai prak ads temen2 saya ya kak"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "Masyaallah kakaknya suka ngaji",  
                "Pesan": "Semangat calon penghuni surga"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "Hobi abangnya baik banget",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "Kakaknya suka baca buku",  
                "Pesan": "Infokan judul buku yang bagus kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CJ3Gtr25K33tqcy9nMWEA545uvJjRvsB",
            "https://drive.google.com/uc?export=view&id=1r9Uu3Lx54ezt1DEo49tS6z04DLLyVaxv",
            "https://drive.google.com/uc?export=view&id=1EDiHusTdIEh-NEd8VHVv-umPPsQwVp-F",
            "https://drive.google.com/uc?export=view&id=1yPInVDRo82a_ZBMz2xTIroLJCkYxc7Yd",
            "https://drive.google.com/uc?export=view&id=1SSlOkeGKaSobDDsUFQCrIYqGxZ8t_PLW",
            "https://drive.google.com/uc?export=view&id=1IXM0HBLh7gDIbXSCQxumM2AOhR6Y_nO0",
            "https://drive.google.com/uc?export=view&id=1kM6Icr2zJDtPEfJ462RJwZ-tTfJzBbD4",
            "https://drive.google.com/uc?export=view&id=1BvaH44YSoasYDEUvKAFwWe_L7Y7l5fqh",
            "https://drive.google.com/uc?export=view&id=1FIOw8Mk7yaIs_xBMWqzVVkByG2wb8wWy",
            "https://drive.google.com/uc?export=view&id=1e8VqbXtQesYdC8ElOhr61A3euq6hOzO5",
            "https://drive.google.com/uc?export=view&id=1K9-BpN5CrmOqNg3nO03QQW3rt9lpuxqC",
            "https://drive.google.com/uc?export=view&id=1gyNecNuvuAxGMqH0hh85teRR1aDgGyXy",
            "https://drive.google.com/uc?export=view&id=10w-2tdNFWQU8kHEFDfstcPLqXY9OGYPM",
            "https://drive.google.com/uc?export=view&id=1n0p8TZCJmJCHtH_DLYT_lrnmCpQ2EAMl",
            "https://drive.google.com/uc?export=view&id=1_K6DoIGSU7MQPUqIz-T4jg_bLAafdWms",
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
                "Kesan": "Abangnya keren",  
                "Pesan": "Titip temen saya di mikfes bang"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "Kakaknya cantik bgt",  
                "Pesan": "Semangat kuliahnya kak"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "Abangnya sehat suka olahraga",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "Tulisan abangnya bagus",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "Kakaknya punya kembaran",  
                "Pesan": "Semangat kak cantikk"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "Hobi abangnya ml",  
                "Pesan": "Semangat bang ml nya"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "Kakaknya cantik",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "Kakaknya cantik trus baik",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "Kakaknya cantik manis",  
                "Pesan": "Semangat kakak cantik"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "Kakaknya kenal aku heheheh",  
                "Pesan": "Kak bagusin nilai kelompok aku ya"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "Hobi yang unik!",  
                "Pesan": "Semangat kak membangkitkan bilangan nya"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "Abangnya ganteng",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "Hobi abangnya keren",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "Hobi kakanya bisa dijadikan referensi ",  
                "Pesan": "Infokan tempat nyari jurnal yang kelaz kak"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "Nama abangnya happy pasti abangnya ketawa mulu",  
                "Pesan": "Happy fun bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1cXmJ23du2t2cbndHJwhHqePbwcgUbmP9",
            "https://drive.google.com/uc?export=view&id=15SqNyre9S2i7ay0uRDiAb7YWlbFgHBJx",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "Kesan": "Funfact abangnya banyak trus kocak",  
                "Pesan": "Semangat bang nyusun skripsi"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "Kakaknya cantik suka senyum",  
                "Pesan": "Semangat kk cantik"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "Hobi kakanya adalah hobi sejuta umat",  
                "Pesan": "Infokan duit yang mau di itung kak biar aku bantuin"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "Abangnya lucu suka ketawa",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "Abangnya baik",  
                "Pesan": "Bagusin nilai praktikum ads saya ya bang"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "Abangnya suka olahraga",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "Tulisan kk nya bagus",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Nabilah Andika Fitriati",
                "NIM": "121450139",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kedaton",
                "Hobi": "Bikin JJ",
                "Sosmed": "@nabilahanftr",
                "Kesan": "Kakaknya cantik",  
                "Pesan": "infokan jj yang gacor kak"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "Suara kk nya bagus",  
                "Pesan": "Semangat kak nyanyinya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "Kesan": "Abangnya galak dikit",  
                "Pesan": "Infokan masuk medkraf bang"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "Kalem banget trus suara kknya kecil ",  
                "Pesan": "Jangan lupa senyum kak"
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "Kakaknya manis",  
                "Pesan": "Semangat kak manies"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "Kakanya cantik pake C",  
                "Pesan": "Semangat kak cantik"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "Kakaknya lucu dan cantik",  
                "Pesan": "Semangat kak ngefangirl nya"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "Kakaknya cantik trus punya sumpipit",  
                "Pesan": "Yang nama natasya gausah ditanggepin kak:v"
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "Kak neli lucu titip teman ku ya kak di markov",  
                "Pesan": "Semangat kak jadi daplok markov"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "Kakaknya lucu",  
                "Pesan": "Tutor biar ngoding ga eror kak"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "Abangnya baik dan ganteng",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "Kakaknya cantik",  
                "Pesan": "Infokan film yang ga bosenin kak"
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@gymnn.as",
                "Kesan": "Abangnya ganteng",  
                "Pesan": "Rekomendasiin komik yang seru bang"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "Kakaknya baik dan cantik betul",  
                "Pesan": "Infokan jj yang gacor kak"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "Kakaknya baik banget mau direpotin tmn saya!",  
                "Pesan": "Semangat kak cantik"
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": "Abangnya keren pake K",  
                "Pesan": "Semangat bang"
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "Bang abit keren jago ngoding",  
                "Pesan": "Infokan cara ngoding tanpa gpt bang"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "Ternyata abang ini daplok bayesian",  
                "Pesan": "Bang bagusin nilai praktikum saya sama jangan jahatin kak elila saya bang"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "Abangnya baik trus kocak",  
                "Pesan": "Semangat kak"
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "Kakaknya lucu ",  
                "Pesan": "Semangat kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()