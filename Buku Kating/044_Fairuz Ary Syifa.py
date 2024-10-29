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
    def Kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sIo4zZ6OuJiN4JRxJZsKjvtOpVNcL59K",
            "https://drive.google.com/uc?export=view&id=1guddUupaxGocduw7775UTqo-4Q8SkPMh",
            "https://drive.google.com/uc?export=view&id=1uTDeqc0KapHFO9uwdb4F2jsEqWdZR-1a",
            "https://drive.google.com/uc?export=view&id=1ZXob1YYiSK-fc18EkBNmasIR1DBYtamH",
            "https://drive.google.com/uc?export=view&id=1tzqehnfhrhFc57Cgix0bzb1GuSCFCmlE",
            "https://drive.google.com/uc?export=view&id=1wI28a99rNeHg_W8oH7BEgd60fyWGpqC7",
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
                "Kesan": "abang ini asik saya suka belajar dengan blio",  
                "Pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "Nama": "Pandra Insani Putra Azuar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "abangnya asik",  
                "Pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagaralam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "Kakak ini baikk",  
                "Pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "Nama": "Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh, Sumbar",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "Kakak nya pendiem",  
                "Pesan":"semangat terus kuliahnya kakak !!!!"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "Kakak seruu",  
                "Pesan":"semangat terus kuliahnya kakak !!!!"
            },
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "Kakak ini asikk bngt",  
                "Pesan":"semangat terus kuliahnya kakak !!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YdH2EBMoLqJszKf6q70R6xIOaWWiEUO5",
            "https://drive.google.com/uc?export=view&id=16zXe_v-TZYljbaJVBkiGdfm2_xXA6EYu",
            "https://drive.google.com/uc?export=view&id=1vB54gb6cSTlURF83fkvH1qua6gv9kl-e",
            "https://drive.google.com/uc?export=view&id=1lyybLO0c0rGekx4hKxyFr2tLGLbI13XA",
            "https://drive.google.com/uc?export=view&id=1HTit1EmT0BnVSoyqcHWnt0F9j4mJ_XWI",
            "https://drive.google.com/uc?export=view&id=1lUkyfrklUPfoQ4SdfBPmqzdmFZ3vz0li",
            "https://drive.google.com/uc?export=view&id=1HmfxaV4oX4bA5CTrJIILIhLyBqarOLlL",
            "https://drive.google.com/uc?export=view&id=1utfzJv0yDe2jGH5rkVArycMIQ_GBbINm",
            "https://drive.google.com/uc?export=view&id=1ZXkIXBvTghLxRkBwj4bOl81mJW3b71oQ",
            "https://drive.google.com/uc?export=view&id=1wRItEBqUHeQJGuhwe72TVDIiv8WFsby8",
            "https://drive.google.com/uc?export=view&id=1IUdVL-xPS2rRB1tEFN10c_drdVGNzFZH",
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
                "Kesan": "Kakaknya lucuu, semangat terus",  
                "Pesan":"semangat terus kuliahnya kakak !!"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tanggerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, Nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "Kakak nya baiik",  
                "Pesan":"semangat terus kuliahnya kakak !!"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150 ",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "agak pendiemm si, cakepp",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Annisa Dini Amaliya",
                "NIM": "121450081 ",
                "Umur": "20",
                "Asal":"Tanggerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "Kakak ini asikk",  
                "Pesan":"semangat terus kuliahnya kakak !!!"# 1
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079  ",
                "Umur": "21",
                "Asal":"Bandaar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger Lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "kakanya pendiem",  
                "Pesan":"jangan sering diem diem kakk"# 1
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087  ",
                "Umur": "20",
                "Asal":"Batu Raja, SumselMedan",
                "Alamat": "Way Kandis",
                "Hobi": "Baca Buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "abangnya asik seruu",  
                "Pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118 ",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main Kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "abangnya mantapp",  
                "Pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004  ",
                "Umur": "20",
                "Asal":"Sukabumi, Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka Ikut Tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "Kakak nya humble, sunda banget ",  
                "Pesan":"semangat terus kuliahnya kaaa !!!"# 1
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "121450156 ",
                "Umur": "22",
                "Asal":"Surakarta, Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "abangnya keren",  
                "Pesan":"semangat terus kuliahnya bang !!!"# 1
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022 ",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "abangnya kocakk",  
                "Pesan":"semangat terus kuliahnya bangg !!!"# 1
            },
            {
                "Nama"  : "Berlianda Enda Putri",
                "NIM"   : "122450065",
                "Umur"  : "21",
                "Asal"  : "Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi" : "Main Game",
                "Sosmed": "@berlyyanda",
                "Kesan" : "kakaknya aga pendiem",  
                "Pesan" : "kedepannnya jangan terlalu pendiem kakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14Jq6FYAkU9agLGuEsd9E7JvOERgWFGc1",
            "https://drive.google.com/uc?export=view&id=1I7990ho8BZdr2cZJ3ADCaBIj0ZLjwVe2",
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
                "Kesan": "kakanya keren banget, wanita karir vibes",  
                "Pesan":  "semangat kakakk, jangan lupa istirahat"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "abangnya keren",  
                "Pesan": "semangat bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10YuF3qbXXJsaZ5gbA-bkUcb7_Dx6yKQG",
            "https://drive.google.com/uc?export=view&id=1TsqlOoIwukVFjXd8onBC60dTzOCUlFMe",
            "https://drive.google.com/uc?export=view&id=1Ebig3fiRxy6Bbd8zVSHCpp4KXq6EsEaf",
            "https://drive.google.com/uc?export=view&id=1EyZPf2MA7CMFEvyamIOeyi1_6sQUo-pC",
            "https://drive.google.com/uc?export=view&id=1BZ83nkhfrWvFzh04Fd63_eziO8zDWEId",
            "https://drive.google.com/uc?export=view&id=11MNPai0x1RYuXMxz0fpXzal3FmfRwh47",
            "https://drive.google.com/uc?export=view&id=1FU3ZmlmsmLXwtqc0RQOeWbS0HxGsc4M_",
            "https://drive.google.com/uc?export=view&id=1i8stJwVhVBOOsbi7jNOHzyRAvCXpmqrb",
            "https://drive.google.com/uc?export=view&id=1bTNQgvbYLsICGf0W8PrgKpYlHthN5-6h",
            "https://drive.google.com/uc?export=view&id=1IBtFq3gb_o2Boh8riHGqT3IlsHtY3-gC",
            "https://drive.google.com/uc?export=view&id=1z1KRe7vNqLYSyyKTdTNfVrob6rz3QEcY",
            "https://drive.google.com/uc?export=view&id=11jksyBvwLzhnjaSTvavyGmSczx0Toavu",
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
                "Kesan": "abangnya humble asikk",  
                "Pesan":"semangat semester tua bang"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "kakanya baikk",  
                "Pesan": "semangatt kaka"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "abangnya asikk",  
                "Pesan": "semangat teruss bang"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "kakanya asikk",  
                "Pesan": "semangatt kakaa kuliahnya"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "abangnya humble, asikk",  
                "Pesan": "semangat terus bang apapun cuacanya"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "kakanya kalemm",  
                "Pesan":"terus semangat"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "kakanya lucuu",  
                "Pesan": "semangat kakakkk"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "abangya ramahh",  
                "Pesan": "terus menjadi orang yang ramah bang"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "kakanya asikk",  
                "Pesan": "selalu semangatt"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "kakanya pendiem",  
                "Pesan": "jangan diem2 an kak"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "abangnya mantap",  
                "Pesan": "semangat bang mantap"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "abangnya asikk ",  
                "Pesan": "asikin terus bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vyWMQE8tc_r8Hb-xNAdisq0TCdRgwIfI", #econ
            "https://drive.google.com/uc?export=view&id=1suKPe7xSDSlykcLdXT04xAMgQwG1dBwR", #elisabeth
            "https://drive.google.com/uc?export=view&id=1CjqFDwc_ADB-ZbY8OeTr4EDgVc00M5-R", #nisrina
            "https://drive.google.com/uc?export=view&id=1pZ-UIgpE0TptTmmqiHrdDlO-kpDJWqUb", #allya
            "https://drive.google.com/uc?export=view&id=1tywSqlRHShsCoFnZFT-C4kcp6zP28tlp", #farahanum
            "https://drive.google.com/uc?export=view&id=1dIeqcrvLIyLsnp8-__s-OeJ7dadQ_5uf", #deriansyah
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #eksanty
            "https://drive.google.com/uc?export=view&id=12BGICPFQbl3LlBNMY29GR_yk3sd7MNr5", #oktavia
            "https://drive.google.com/uc?export=view&id=1S71VruffDiOqBv0AnCtcagvaI5wG_hb5", #ferdy kevin
            "https://drive.google.com/uc?export=view&id=16sU7Y-L-Ae-05JpIPA0NgKpxqyVnnM9c", #devyan
            "https://drive.google.com/uc?export=view&id=1mKIwYXQuRx9341fQDMDmwSCM0KebOx0p", #ibnu farhan
            "https://drive.google.com/uc?export=view&id=1dmkrXk26InWNp1cVTQPPTVCzxxrhGX8q", #johannes
            "https://drive.google.com/uc?export=view&id=1_l2P_9hDC-mif0pmhw9ItqM2UfXii2zj", #kemas
            "https://drive.google.com/uc?export=view&id=1YO8Nf5bcax8vozMYRRCYn0XVtc_Co2it", #leonard
            "https://drive.google.com/uc?export=view&id=1n0gH3sThp_mydF2CCkQpHi0MlEWpF0ze", #presilia
            "https://drive.google.com/uc?export=view&id=1ao5pTsql-7wERT46xRWRINl5tPfFr1SC", #rafa aqilla
            "https://drive.google.com/uc?export=view&id=1ibdly6oRexQ797LErs6Y6ye0XH_1vf5i", #sahid
            "https://drive.google.com/uc?export=view&id=1yRt10NJZQuRurw_k99E79lLW6HgSPYR_", #vanessa
            "https://drive.google.com/uc?export=view&id=1K6mOjE7_zG5qSVyMER-JFj0jeTtRWl35", #ateng
            "https://drive.google.com/uc?export=view&id=19IySE8ywrqGcWk5brBPJIahaX-pvUhV9", #gede
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", #jaclin
            "https://drive.google.com/uc?export=view&id=1A18lYORDv0jaXLiLi6yVgrA5Kh51d9zC", #rafly
            "https://drive.google.com/uc?export=view&id=1qrdIllLbY37TexFgHNIljjCMrbu7l0xc", #syalaisha
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
                "Kesan": "Mantap",  
                "Pesan": "Terus menjadi orang yang mantap bang"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "Kakanya semangat banget",  
                "Pesan": "Terus semangat ya kak"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "Kakaknya keren banget, beribawa",  
                "Pesan": "semangat terus buat kakaknya"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "kakaknya tegas",  
                "Pesan": "Semangat terus kak membina kita angkatan 23"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "cakepp kalem",  
                "Pesan": "semangatt kakaak"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "seru abangnya",  
                "Pesan":"Seru seru bang"
            },
            {
                "Nama": "Eksanty F. Sukma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "eksantyfebriana",
                "Kesan": "positif vibes banget",  
                "Pesan": "nular ya kak positif vibes nyaa"
            },
            {
                "Nama": "Oktavia Nurwenda Puspita Sari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "kakanya kalemm",  
                "Pesan": "semangat mengkaderin akt 23 kaa"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "abangnya diem",  
                "Pesan": "jangan terlalu diem bangh"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "abangnya lawakk",  
                "Pesan":"selalu bahagia bang"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "abangnya cool",  
                "Pesan": "jangan terlalu cool bang"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "abangnya profesional",  
                "Pesan":"semangat terus bang "
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "pinter koding",  
                "Pesan": "semoga nular ke saya pintarnya bang"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "abangnya pendiem",  
                "Pesan": "jangan terlalu diem2 bang"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "kakanya caekeepp",  
                "Pesan": "semangat kakak"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "baik, cakep",  
                "Pesan": "semangat selaluu kak"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "humbel banget",  
                "Pesan":"semangat terus kuliahnya bang"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "energetic girl",  
                "Pesan":"semangatt kakak"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "wawasan abangnya luas",  
                "Pesan": "semangat terus bang"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "abangnya mantap ",  
                "Pesan": "semangat bang"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "kakaknya jarang liat",  
                "Pesan": "semangat terus kak, jangan lupa istirahat"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "abangnya keren",  
                "Pesan": "terus semangatt"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "kaget kakanya muncul di dua deparetemen rupanya beda orang",  
                "Pesan":"kompak selalu kakk sama kembarannya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LfOo1dCQouWSPJhfnpSidr4edSTISSGt",
            "https://drive.google.com/uc?export=view&id=1R2iAtdfmBvaMDMWFGZcWw6J-O4ys8fsf",
            "https://drive.google.com/uc?export=view&id=1LSHfv9Izj3_6ptNZhVm84fSRyaZQGV_i",
            "https://drive.google.com/uc?export=view&id=1qkZ8dhKT_SjldBjIs5t6bxCM-rYSGjaG",
            "https://drive.google.com/uc?export=view&id=1EuNWYVZDThrYKtD9aPY5V0N9lXaRdOpy",
            "https://drive.google.com/uc?export=view&id=1rlp8fJ0ovWGvBoadE52agV0z51qExwSD",
            "https://drive.google.com/uc?export=view&id=1XN2hNv0LOvyHZoNew3iIbuDwdPhGvmml",
            "https://drive.google.com/uc?export=view&id=19UNGETUvPStE5P5ocmDT6cZAub4hDZYa",
            "https://drive.google.com/uc?export=view&id=14s-okp9f9Cpw0OBKXvGW4YuZqB6MtITx",
            "https://drive.google.com/uc?export=view&id=1asBYPLHBHoFN-BE-KZdzLMZD8_c-90yt",
            "https://drive.google.com/uc?export=view&id=1lkzWHoO4lasNoNnsCc5RB--uGAg6nuzx",
            "https://drive.google.com/uc?export=view&id=1lkzWHoO4lasNoNnsCc5RB--uGAg6nuzx", #arafi
            "https://drive.google.com/uc?export=view&id=16mBlHz1qvG1BVtLuXM5JF4na-GOHHDgu",
            "https://drive.google.com/uc?export=view&id=1lkzWHoO4lasNoNnsCc5RB--uGAg6nuzx", #irvan
            "https://drive.google.com/uc?export=view&id=1JMxixZkgd7C-9J7YVYhY9b9Vw4A4X-x8",
            "https://drive.google.com/uc?export=view&id=1wfIXdY_CzbIcXuHHsZXJ37WyF4iF4MW-",
            "https://drive.google.com/uc?export=view&id=1N3LdvHErwDGwSVvHFlFJoEd5aEcz7zPr",
            "https://drive.google.com/uc?export=view&id=1yBB2zE94zyW3uVSAYmHEXT9bpnW9QM5o",
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
                "Kesan": "wawasannya luass",  
                "Pesan": "seamngat tidurnya bangg, menyala"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "kakanya ceriaa",  
                "Pesan": "ajak kita jalan-jalan dong kakk"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "kakanya asiik",  
                "Pesan":"semangat kuliahnya kakk, semoga jadi atlit golf"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "kakaknya asikk",  
                "Pesan":"semoga kakanya punya kebun gede aamiin"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@esteriars",
                "Kesan": "kakaknnya assik ",  
                "Pesan":"semoga jadi atlit golf ya kakk"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "kakaknya baikk kerenn",  
                "Pesan": "lanjutkan survingnya kakk, jangan lupa istirahat"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "kakaknya caekkpp",  
                "Pesan":"semangat kuliahnya kakak"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "positif vibes bangett",  
                "Pesan": "jangan lupa istirahat kakk"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "abangnya humble, kocakk",  
                "Pesan": "terus menjadi org humble bang, moga nular ke orang2 yang pendiam"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "kakanya kereen amay",  
                "Pesan": "semangat mengkaderkan kita akt 23 kakk"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "abangnya kereen ",  
                "Pesan": "lanjutkan terus hobinya bang, keren bngt"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "abangnya mantap",  
                "Pesan": "semoga di masa depan punya tempat bertani luass buat nyalurin hobinya"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "kakaknya Masya Allah banget",  
                "Pesan": "semangat dan terus istiqomah kakkk"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "minang banget ",  
                "Pesan":"semoga menjadi menajadi konten creator bang, supaya tidak menjadi penonton saja"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "energetic girl, independent women",  
                "Pesan": "kakak jangan lupa istirahat, semoga pinternya nualr ke akuu aamiin"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "kakaknya cakeupp",  
                "Pesan": "semnangat meraih cita-citanya kakk"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "abangnya baik dan aga kalem",  
                "Pesan":"sukses selalu bangg"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "cheerful",  
                "Pesan": "semangat terus kakakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vWu9EKEXqyjm1xPXq2L_DRPWdAxHGC06",
            "https://drive.google.com/uc?export=view&id=1-VU2FY10AZl5w6t6lSTsFKCUjBMhLR20",
            "https://drive.google.com/uc?export=view&id=1ucKa7LRrov1WlLxitH7SHwbNM7AfhmTS",
            "https://drive.google.com/uc?export=view&id=1vzGGGvmRKZqbmbwKolEWUKxjHoSVT5dQ",
            "https://drive.google.com/uc?export=view&id=1QF5Y5v-rbo4zU-P5KQsvxDuzj7Y68L5a",
            "https://drive.google.com/uc?export=view&id=1vzGGGvmRKZqbmbwKolEWUKxjHoSVT5dQ", 
            "https://drive.google.com/uc?export=view&id=1-T0OwaI1mJyhcayBUZ7oLPtwsLgBllsJ", #deva
            "https://drive.google.com/uc?export=view&id=1YBd__IC5d_c5Jp2eKHxp5BCAv-qc_1je", 
            "https://drive.google.com/uc?export=view&id=17NHJrUiG4NtwRJAx8xH6JJzfxJIFEyf2",
            "https://drive.google.com/uc?export=view&id=1Gz6QHO-cioHpf75NCYlil4AIHxO_657o",
            "https://drive.google.com/uc?export=view&id=1DqS-ZInVkBUCOka77AmeYjChJ-7Ht0mg",
            "https://drive.google.com/uc?export=view&id=12Jsm7ZaZ9s_v_wkSYRIde2cOWA-ZAc_2",
            "https://drive.google.com/uc?export=view&id=18HFjVQTsiYKmyOzCMYv49WE7WKjynOzZ",
            "https://drive.google.com/uc?export=view&id=1ykT_fh25pDxk9c-_1PmAvBwQeHBTRPxl",
            "https://drive.google.com/uc?export=view&id=1GxuJkzWq0gMn9OMvYMGYdRQTccHs0vB0", 
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
                "Kesan": "abangnya mantapp",  
                "Pesan": "semangat semester tua nya bangg"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "kakanya kalem",  
                "Pesan": "terus memasakk, let her cook"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "abangnya pendiem",  
                "Pesan": "terus semnangat kuliahnya bang"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "keren bgt bisa nge-mc",  
                "Pesan": "tutor kan kita ADS dong bang"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "lucu banget punya kembaran",  
                "Pesan": "mangatt kak nge review jurnaal nya bu mika"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "abangnya profesional",  
                "Pesan": "semangat bang kuliahnya"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "kakaknya hebatt",  
                "Pesan": "terus menjadi pribadi yang menjadi lebih baik kedepannya kak"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "kakaknya hobinya keren banget",  
                "Pesan": "jangan lupa istirahat kak"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "kakaknya pinterr, cantiknyaa",  
                "Pesan": "moga pintarnya nular, jangan lupa istirahat kak"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "kakaknya ramah, asikk",  
                "Pesan": "semoga terbayarkan semua apa yang kakak usahakan"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "kakaknya kalemm",  
                "Pesan": "semoga lulus tepat waktu  kak"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "abangnya keren abis",  
                "Pesan": "semangat terus, tetap menjadi org yang keren abng"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "pinter banget",  
                "Pesan": "semoga nular kepintarannya dan terus semangat mengasprak nya bang"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "kakaknya baikk, ramah",  
                "Pesan": "jangan lupa istirahat kak, terus semangat kuliahnya"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "abangnya aga pendiem",  
                "Pesan": "tetap menjadi pribadi yang happy sesuai namanya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1WcK1n_gbuLyemnWkio7zlgP9qIuZgEhI",
            "https://drive.google.com/uc?export=view&id=13Ac84DkrSoUHau7P8UQwyDJcCiqkb8Cn",
            "https://drive.google.com/uc?export=view&id=1Y9SjwPQtNCtBy-WHWIbf4-Nj2GXpixLF",
            "https://drive.google.com/uc?export=view&id=1rRmbcsF_zNU7kn2mwgDUacgkjqZv9r1N",
            "https://drive.google.com/uc?export=view&id=1ZCwhRDTsng19vCZUaFSluF4R0fHLuUfF",
            "https://drive.google.com/uc?export=view&id=133ptAQuZZKPngwsa5iYQhOr612jVrfxP",
            "https://drive.google.com/uc?export=view&id=1IvX8pE5xcSeu78ivk0NA0vlVLUti37YD",
            "https://drive.google.com/uc?export=view&id=1J-WsStYWRrNmlCsnqhkivEkt3NnyqI2m",
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
                "Kesan": "humble, banyak betul funfact nya",  
                "Pesan":"lanjutkan pencarian hobii nya bang"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "kakaknya asikk",  
                "Pesan":"semangat terus kuliahnya kakk"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "kakaknya bendahara banget",  
                "Pesan":"moga ga cuman ngitung duit aja, tapi juga pemilik duitnya kak "
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "abangnya aga pendiem",  
                "Pesan":"jangan terus2an diem bang, smangat"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "humble parah",  
                "Pesan":"semangat terus bang, next harga stiker nya 10k dapat 4 ya bang"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "abangnya keren",  
                "Pesan":"tetap menjadi pribadi yang slalu semangat bang"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "kakaknya ramahh",  
                "Pesan":"terus menjadi kakak yang ramah, semoga bisa menjadi penulis yang menerbitkan banyak buku best seller"
            },
            {
                "Nama": "Nabilah Andika Fitriati",
                "NIM": "121450139",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kedaton",
                "Hobi": "Bikin JJ",
                "Sosmed": "@nabilahanftr",
                "Kesan": "kakanya baikk, ramah",  
                "Pesan":"selalu semangat kak, smoga lulus tepat waktu"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "kakaknya keren bisa main alat musik dan menyanyi",  
                "Pesan":"pengen denger suara emsa kakaknya deh, semangat kuliahnya kakakkuh"
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
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@gymnn.as",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "",  
                "Pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()