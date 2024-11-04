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
            "https://drive.google.com/uc?export=view&id=1vmN6Vz9LjnGjEEkf8zt9xsPb8c2BoxkV",
            "https://drive.google.com/uc?export=view&id=1dKyYAUEpeo3GJUC3kOozEupww6mbcd4i",
            "https://drive.google.com/uc?export=view&id=1KpKx7tofkFaI7k5taS-TLLsbjPO9c0VJ",
            "https://drive.google.com/uc?export=view&id=1DQKLUAkW6kb0m6LgWosBMvu3od-zgpD1",
            "https://drive.google.com/uc?export=view&id=1YunvNhAGx2OcMWlZmqsWTPkXaQGoZEge",
            "https://drive.google.com/uc?export=view&id=1t5GofN-oS0Y7vBbznVIt_10sQKK-GZZb",
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
                "Kesan": "Abangnya asik klo ngobrol",  
                "Pesan":"Semangat bang kedepannya, sukses terus!"
            },
            {
                "Nama": "Pandra Insani Putra Azuar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "Abangnya keren",
                "Pesan":"Gokil bang!"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagar Alam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "Kakaknya gercep",  
                "Pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "Nama": "Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin Pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "Kakaknya tegas",  
                "Pesan":"Semangat kak ngatur jadwalnya"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "Santai tapi calm",  
                "Pesan":"Semangat kak jadi bendaharanya"
            },
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "Kakak ini katanya galak klo urusan duit",  
                "Pesan":"semangat kak urus duitnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sNfF4x9HvomciVYQci59GRUxmoCPDDso",
            "https://drive.google.com/uc?export=view&id=1dm0NiWWsc5voIF4TDx6quSDKPHy6bzNj",
            "https://drive.google.com/uc?export=view&id=1hQ5CofdHgmBZNvR-QeWCJ0ZYDzhLiIp8",
            "https://drive.google.com/uc?export=view&id=1c9zxm67fF5B9dLHLmWCD-aNzrYBjY7tq",
            "https://drive.google.com/uc?export=view&id=1vd0kc17vHbIXNfXbqGg-eSAK0YdVyWWc", 
            "https://drive.google.com/uc?export=view&id=1Qq4uUHipod8ff_ouR2_o95GZ1ICUWcEx", 
            "https://drive.google.com/uc?export=view&id=1_ohAdgLM4WfSW3vd8eKGL31gQl--43X-", 
            "https://drive.google.com/uc?export=view&id=1TqSUgwKk6oeXGMA8lb_GBrNCrARU23X4", 
            "https://drive.google.com/uc?export=view&id=1DCB735WmlFkXZMCyptPkcB7-rxNU11fb", 
            "https://drive.google.com/uc?export=view&id=1L-nR3ez8HzP1rYs1W6WkpVUJJVrwduBj", 
            "https://drive.google.com/uc?export=view&id=15iUMaWyfP4fRFVmNm11n0j5jESDNuLdY", 
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
                "Kesan": "energik kakaknya",  
                "Pesan":"semangat kak kuliahnya, semoga cepet wisuda"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tangerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "Kakak ini asikk",  
                "Pesan":"semangat terus kuliahnya kakak !!!"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "Kakak memiliki business insight yang kuat",  
                "Pesan":"semangat teruus kak berbisnis dan kuliahnya"
            },
            {
                "Nama": "Annisa Dini Amaliya",
                "NIM": "121450081",
                "Umur": "20",
                "Asal":"Tangerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "kakak ini kerern",  
                "Pesan":"semangat terus kak kuliahnya"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "pendiem",  
                "Pesan":"semangat kak belajarnya"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "abang ini pinter ngoding",  
                "Pesan":"semangat bang ngasprak alpro nyaa"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "kacamata abang ini keren",  
                "Pesan":"semangat bang"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka ikut tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "kakak ini pinter skd",  
                "Pesan":"semangat kak tesnya"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "122450156",
                "Umur": "22",
                "Asal":"Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin musik, nonton film, dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "abangnya sangat humble",  
                "Pesan":"teruskann banggg"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "abangnya pinter",  
                "Pesan":"semangat juga bang asprak alpronya"
            },
            {
                "Nama": "Berlianda Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumbar",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "kakak ini lucu",  
                "Pesan":"semangat kak kuliahnya, jangan keseringan main game"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1P14XSPKbh_C3TfVDAGEdUnohkr8jTJv6",
            "https://drive.google.com/uc?export=view&id=1Otnd6qW73ep49fmYwhU7Lxn90XtWiBSR",
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
                "Kesan": "Kakakya tegas, cocok keren jadi senator",  
                "Pesan":  "Kakaknya inspiratif banget"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "Bang Bintang kritis banget",  
                "Pesan": "jangan lupa istirahat bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Y3va9-ATSWE86260Iu96hcSYiulTvPO2",
            "https://drive.google.com/uc?export=view&id=1XqkI6IfcIyT24_rk21OiLeZiqnzPDumm",
            "https://drive.google.com/uc?export=view&id=1G48CHuneBO296f0wcR0Vu_HLHnRtcRD-",
            "https://drive.google.com/uc?export=view&id=1YBu7gShU9BQqsnVOMSfSZ6jSvGnDz-ql",
            "https://drive.google.com/uc?export=view&id=1Y26cu-FRE_iyAi6FENKJxfciKgYDjxFk",
            "https://drive.google.com/uc?export=view&id=18DKP9BhU8pj8qkdew5Ug5dSZ9F12bed4",
            "https://drive.google.com/uc?export=view&id=1Y8hH_xPvPkrqbcUTcYONlh7NmK72SDEG",
            "https://drive.google.com/uc?export=view&id=1XmQN1tRX0n98dtnB5IwWST4eTEAJrCnK",
            "https://drive.google.com/uc?export=view&id=1XPgoTWY76HSFcwSu3-4iyMDumt_st4p9",
            "https://drive.google.com/uc?export=view&id=1XOvtnC0Jv6e8fsdD0W2_SqLHcwhXd2sd",
            "https://drive.google.com/uc?export=view&id=1Xd7MxoToVZObtEyKykX870AhtBbW_Pw-",
            "https://drive.google.com/uc?export=view&id=1XSaXrbjlc7HYHTvSCPl0uJqw9_cGFjOi",
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
                "Kesan": "bang dim ramah abiss",  
                "Pesan":"semoga sukses bang, dan semoga kita bisa kerja bareng ya bang"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "kak catherine orangnya calm",  
                "Pesan": "jangan lupa semangat kuliah kak"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "bang akbar ada aja gebrakannya",  
                "Pesan": "abang jangan lupa semangat belajar gptnya bang"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "kak rani skena abis",  
                "Pesan": "jangan lupa bayar bulanan spotifynya kak"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "bang rendra insightful",  
                "Pesan": "bang infokan cara buat laguu"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "kak salwa baik banget",  
                "Pesan":"semangat kak nonton filmnya"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "kak renta lucu banget",  
                "Pesan": "jangan mancing keributan terus kak"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "bang sigit keren banget klo under pressure, calm and collected banget",  
                "Pesan": "jangan lupa bersyukut bang"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "Kak mei outgoing dan friendly orangnya",  
                "Pesan": "jangan lupa baca alquran kakk"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "kak azizah baik banget",  
                "Pesan": "jangan keseringan megang kecoa kak"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "bang rendi pinter banget",  
                "Pesan": "semangat bang mssnya"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "bang josua calm and colleted juga kayak bang sigit",  
                "Pesan": "jangan lupa olahraga bangg"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16SH5NeHEVevat8_4KWqcLAh95ECYro7D",
            "https://drive.google.com/uc?export=view&id=15a8svzn8x4gfdHQBKRRZPtc5OBjwYIIp",
            "https://drive.google.com/uc?export=view&id=169NpoFA07erUoBqPqLSuGtdIdB8tC0yg",
            "https://drive.google.com/uc?export=view&id=15lLbYwtBaYcG4qN8qwTBJGrPjfso3rUX",
            "https://drive.google.com/uc?export=view&id=15x5SIhNJmyopA9YxJMwDpCM049jv13B0",
            "https://drive.google.com/uc?export=view&id=15Y-J5HOB4VUjAJtj-B7jufVxIGo94USB",
            "https://drive.google.com/uc?export=view&id=160xTkMvcbGApTEgAfVzFfmacs8YxHiY2",
            "https://drive.google.com/uc?export=view&id=15jV43pVsQYyRiavQoiJ-yZs_NXsPFNCS",
            "https://drive.google.com/uc?export=view&id=15l58gI2g9dd3SkawtqAGL4uNEyAQEkyR",
            "https://drive.google.com/uc?export=view&id=16cjHFcfLij9Ugq0NSgRLe8951mPX9gXi",
            "https://drive.google.com/uc?export=view&id=16ergiUkXfL2FKs2r77LEgDiMQ2q3vom3",
            "https://drive.google.com/uc?export=view&id=16IjLAw7uC4h9buvyoYoHrNcICpoJHr5X",
            "https://drive.google.com/uc?export=view&id=16PmPIqu5LcyYIG7lbGOj-BN0T1DfO_8Y",
            "https://drive.google.com/uc?export=view&id=16MWtSrcQBCm3X2JFzwGUywfPXLLL5MmY",
            "https://drive.google.com/uc?export=view&id=16UAtGlZVsFaZLUw2aJNnVw2YGpKWEXYG",
            "https://drive.google.com/uc?export=view&id=16pip7CcujF83QwfwaE3q-95h_vldvs1C",
            "https://drive.google.com/uc?export=view&id=16Slgy6K5a5F9Kkc0WKCWzJsFgX2FpRRK",
            "https://drive.google.com/uc?export=view&id=16Loc3qm2jylhEdHoXzSAxZCZmK58UU-m",
            "https://drive.google.com/uc?export=view&id=16A2jz0KLUwcCjsMoNUnWWelzeiGdwXn9", 
            "https://drive.google.com/uc?export=view&id=16Eb-n8ri4QyNFeRbyYO3RUCr4b6LhKnY", 
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_", 
            "https://drive.google.com/uc?export=view&id=16BQC3sy09DBsl3qA9syg46zV_OO98hJW", 
            "https://drive.google.com/uc?export=view&id=16mei0q34KsJ5uOYzEjPZffSBprtSSW7E", 
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
                "Kesan": "abang ini pinter banget klo memberikan ide",  
                "Pesan": "tetap semangat bang, jangan lupa istirahat bang"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "kak abeth keren kak",  
                "Pesan": "semangat mancing keributannya kak"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "cantik kaya orang arab",  
                "Pesan": "semoga harinya dijauhi panas terik ITERA ya kak"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "kakaknya profesional",  
                "Pesan": "semangat kak mengkader kami yang sering salah ini"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "kak hanum mirip kawan smp saya",  
                "Pesan": "jangan keseringan gangguin kak allya kak"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "bang der chill abis orangnya",  
                "Pesan":"semangat bang kuliahnya, jangan keseringan push rank (gas bang login)"
            },
            {
                "Nama": "Eksanty F. Sukma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "@eksantyfebriana",
                "Kesan": "kak eksanty baik banget klo praktikum ADS",  
                "Pesan": "semangat kak asprak ADS kelas RB (tolong kak)"
            },
            {
                "Nama": "Oktavia Nurwenda Puspita Sari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "kak okta orangnya observant",  
                "Pesan": "jangan lupa senyum kak"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "bang kevin diem-diem insightful",  
                "Pesan": "semangat bang kuliahnya, semoga sukses kita"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "bang dey lucu bgt dah kalo ngelawak, tapi tetep profesional",  
                "Pesan":"jangan lupa bernafas bang, teruskan bang outgoingnya"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "bang ibnu jarang ngomong, tapi ramah",  
                "Pesan": "jangan lupa belajar bang"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "bang jo juga profesionalitasnya keren",  
                "Pesan":"jangan lupa beli kalkulator bang"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "bang kemas pinter bgt dah klo soal programming dan statistika",  
                "Pesan": "semoga kita bisa kerja bareng yaa"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "bang leo pendiem juga, tapi keliatannya ramah",  
                "Pesan": "Teruskan bang hobi belajarnya"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "kak presil cantik banget",  
                "Pesan": "jangan lupa bangun tidur kak"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "kak rafa juga manis banget",  
                "Pesan": "jangan lupa bedakan dunia nyata dan webtoon kak"

            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "bang sahid orangnya baik, keren, profesional juga",  
                "Pesan":"nonton gadgetin juga bang"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "kak vaness jago banget dah basketnya",  
                "Pesan":"semangat terus kak hobi belajarnya"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "bang ateng kharismatik",  
                "Pesan": "teruskan bang hobi menolongnya"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "bang gede asik banget diajak ngobrol",  
                "Pesan": "jangan lupa bang prioritaskan belajar bang"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "kak jaclin murah senyum",  
                "Pesan": "hati-hati kak kalo berenang"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "bang rafly pendiem, tapi kalo ngomong serius",  
                "Pesan": "jangan lupa belajar bang"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "kak dini pinter banget",  
                "Pesan": "jangan lupa bersyukur kak dan belajar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QF0u1WMzDKcZI3nxVM0GmnXUkZLgezX6",
            "https://drive.google.com/uc?export=view&id=1QFBTIQRo4-Q0F9aHzKa_Q4qZUWeEzDdm",
            "https://drive.google.com/uc?export=view&id=1QvWjqIdVpukAje5x-G7_6Uge5mzsk3o0",
            "https://drive.google.com/uc?export=view&id=1QxrIkh8HzxmbGy5MN3LCPPslWxLM0c0R",
            "https://drive.google.com/uc?export=view&id=1R2RnFrL94BM435cbqKAYaVTf4xjICmzF",
            "https://drive.google.com/uc?export=view&id=1QgprcUV9DGTDp0BLDXZN6c7esgsqC5ag",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1QnlfOEyLPhqtLjUDVfLUcMUTOBtxDIfQ",
            "https://drive.google.com/uc?export=view&id=1QqQeVsOCLFuW5yJgislN3E_bnIwIuVVL",
            "https://drive.google.com/uc?export=view&id=1QzgTg0yL-b5pIlYxYYvKVjkTDwmv0qhB",
            "https://drive.google.com/uc?export=view&id=1YefMjC1dQtYrMdBolM2VX81cJLRldCFd",
            "https://drive.google.com/uc?export=view&id=1QOUohMWlU1ES804Td7NB0m_0XgK1YdKX",
            "https://drive.google.com/uc?export=view&id=1QAr_j7j1OsRFlxVe2RDdfpoks4CZSmaz",
            "https://drive.google.com/uc?export=view&id=1QI1dLBKZZE1gsVuGmzyF_MQutjxjiRxA",
            "https://drive.google.com/uc?export=view&id=1P26PgHMZe2LdsaKsq2S5wiWGuOiiE64j",
            "https://drive.google.com/uc?export=view&id=1P33HMqMUQ5-JGmP6zejAKcVTsn4zQLMt",
            "https://drive.google.com/uc?export=view&id=1Q7HFI5bNLCqO-Q3tsF52Pdv5n-upcytT",
            "https://drive.google.com/uc?export=view&id=1R3VeIGNylPwYYnR-cSclsSr-BOEOqkCh",
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
                "Kesan": "bang yogy baik banget semenjak sdm",  
                "Pesan": "semangat bang skripsinya"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "kakaknya keliatan sibuk",  
                "Pesan": "infokan lokasi jalan-jalan yang murmer kak"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "kakaknya suka ngelawak",  
                "Pesan":"Golfnya di mana kak"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "kak dea outgoing",  
                "Pesan":"tips and trick berkebun kakk"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@esteriars",
                "Kesan": "kak ester manis banget",  
                "Pesan":"kaka main golfnya bareng kak nazwa juga ya"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surfing",
                "Sosmed": "@nateee__15",
                "Kesan": "kak  natasya lucu banget",  
                "Pesan": "ajarin saya surfing kakk"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "saya gk ketemu kakak, tapi kayaknya kakak baik",  
                "Pesan":"jangan keseringan tidur kak"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "kak mine baik banget pas ADS",  
                "Pesan": "tolong bantu ADS saya kakk"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "bang tobb keliatan galak, tapi lembut ternyata",  
                "Pesan": "gass bang long run barengg"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "kak yohanaa tegas orangnya",  
                "Pesan": "player favorit bulu tangkis kak"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "bang benno kharismatik abis",  
                "Pesan": "infokan projek buat porto bangg"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "bang arafi keren lawakannya",  
                "Pesan": "semangat bang,  kita harus jadi petani yang sukses"

            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "kak uyii ramah banget",  
                "Pesan": "jangan lupa istirahat dan minum air putih kak"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "bang irvan keren banget, apalagi pas sdm",  
                "Pesan":"sering-sering senyum bangg, nular soalnyaa"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "kak izza orangnya positif vibes banget",  
                "Pesan": "kak izza jangan lupa istirahatt"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "kakaknya kyknya agamis yaa",  
                "Pesan": "semoga bisa kerja bareng ya kakk"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "bang raid baik tapi jarang ngomong",  
                "Pesan":"gas bang long runn"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "kak yuna ramah banget dari semenjak pplk",  
                "Pesan": "semangat kak kuliahnya biar bisa pergi ke Yunani"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PDWaoDNMJBlyU8RMa_awMW0LKa-xy2Pm",
            "https://drive.google.com/uc?export=view&id=1PSXQm-3nU4c3yUb__4LYkh0kQXU4zHEX",
            "https://drive.google.com/uc?export=view&id=1P9-MOlR0UBKfLeAO4kq7RN5ka9WAuhAY",
            "https://drive.google.com/uc?export=view&id=1PxIDAVrLw_HiEE9UuTI2A2PLCq2C5IHY",
            "https://drive.google.com/uc?export=view&id=1Po5Ji6xBDbTyWJP-kMG9pQ_iF8iN6QWF",
            "https://drive.google.com/uc?export=view&id=1PR655j9HKlv5YG1juRX_MQKZARrEIrPM",
            "https://drive.google.com/uc?export=view&id=1Ydc5NdHMvjYf6xWfobldwE4A1R0sji57",
            "https://drive.google.com/uc?export=view&id=1PPpnl5HT0noCU7w_JVP8Iab7J9GCid8T",
            "https://drive.google.com/uc?export=view&id=1PIKi-H6lYhbjN-4p1KKRRuqlfwQYSirL",
            "https://drive.google.com/uc?export=view&id=1Phs8dyRKlhnzS40WeQZlaH98ml-DMWGD",
            "https://drive.google.com/uc?export=view&id=1PeXFAGRvi0zsCbGmhnfjgY3ol8WH49Hl",
            "https://drive.google.com/uc?export=view&id=1PdQRQm-8Fmhav9plcn5X10dDT_9q8h0P",
            "https://drive.google.com/uc?export=view&id=1Pad6-8-Ktfl_CbrrUW9DbilXDqJK10jR",
            "https://drive.google.com/uc?export=view&id=1PKTeya33X5d8Hlr2jmyS1MrmzHxMvgqn",
            "https://drive.google.com/uc?export=view&id=1Pj28GvOAbA191xmsOjfQSEWKg1ArTdof",
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
                "Kesan": "baik, positif abangnya",  
                "Pesan": "yahh gk kerja bareng kita bang"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "kakanya rajin",  
                "Pesan": "jangan lupa minum air putih kak"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "bang sahid asikk",  
                "Pesan": "semangat bang volinya"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "bang regi ramah,baik,dan kharismatik",  
                "Pesan": "bang tolong ADS sayaa"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "baru tauu kakaknya kembar",  
                "Pesan": "minta notulensi journal bu mika kak"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "bang anwar pinter banget",  
                "Pesan": "bang ajarin machine learning"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "kak deva baik dan ramah bangett",  
                "Pesan": "kak jangan lupa bersyukur dan minum air putihh"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "kak dinda tegas banget orangnya",  
                "Pesan": "infokan journal favorit bu mika kakak"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "kak eta cantikk",  
                "Pesan": "jangan keseringan review journal kak"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "kak nita pj tugas kelompok saya",  
                "Pesan": "kak nita bagusin nilai kelompok poisson ya kak"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "kakaknya baik banget",  
                "Pesan": "semangat ya kak, kita bisa lulus"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "abangnya keren bisa sql",  
                "Pesan": "ajarin sql dong bang"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "abang tercoding se sains data",  
                "Pesan": "semangat bang ngodingnya btw tutor caari yang error bang"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "kakaknya cantik",  
                "Pesan": "seamangat kak cantik"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "abangnya suka senyum",  
                "Pesan": "jangan luntur ya bang senyumnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BYW6bUofLOVC3i3AzyCDif7gkDjy2sN8",
            "https://drive.google.com/uc?export=view&id=16nAQhEu5BU0zVsZVkeUZ9s7MMYKkySZy",
            "https://drive.google.com/uc?export=view&id=1AJU488_Hqa6u70imcEEGtMSg5IPXJYNS",
            "https://drive.google.com/uc?export=view&id=1SRRL2cAeod5WahV5ApEaL2K_ky22ETRf",
            "https://drive.google.com/uc?export=view&id=1YnLq1geDMixI0IuEI_lvKyBWKWs_12hi",
            "https://drive.google.com/uc?export=view&id=19ScsN4dJ_wRrZG03yfkBwFmBsPmen-Vs",
            "https://drive.google.com/uc?export=view&id=1m_MhrszHosVI915rpiXTrUBMod6wLF4X",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1nL8-je9YSR_6DhUTJscdNb5sWBBbg7Zm",
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
                "Kesan": "abangnya insightful",  
                "Pesan":"abangnya klo ngomong jangan cepet banget bang"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "behel kakak lucuu",  
                "Pesan":"semangat kak kuliahnya"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "kakaknya lucu banget",  
                "Pesan":"jangan keseringan ngitung duit kak"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "abangnya  keren",  
                "Pesan":"infokan perbadmintonan"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "abangnya humble",  
                "Pesan":"hati-hati bang touringnya"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "bang farel keren banget dan kharismatik",  
                "Pesan":"jangan lupa cutting bang"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "kak tessa inspiratif",  
                "Pesan":"jangan lupa bersyukur kakk"
            },
            {
                "Nama": "Nabilah Andika Fitriati",
                "NIM": "121450139",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kedaton",
                "Hobi": "Bikin JJ",
                "Sosmed": "@nabilahanftr",
                "Kesan": "kak nabilah tegas",  
                "Pesan":"semangat kak kuliahnyaa"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "kak mey keren banget",  
                "Pesan":"senyum terus kakk"
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Bm3M7Ov60_x5DA8uoEAxLM4SmhHiClKG",
            "https://drive.google.com/uc?export=view&id=1BPLxc5B8qBhmK-Q51yUwSJ4xnF9WoWfl",
            "https://drive.google.com/uc?export=view&id=1Bzw4XmWXoWWIKQqW560MmbfnTItcMyeS",
            "https://drive.google.com/uc?export=view&id=1BYYt1k72yVD_ckARwnjpMiX1YChEgcsd",
            "https://drive.google.com/uc?export=view&id=1BbDxwinm5G4H7QQigUs7h7ZX5CqzETL0",
            "https://drive.google.com/uc?export=view&id=1C0orVWlVdp6tUhZ4tvJL7SvuTutd47QC",
            "https://drive.google.com/uc?export=view&id=1BJmvSqkLMPpje1WBrXxjkePzCbThIcDJ",
            "https://drive.google.com/uc?export=view&id=1BsPzD7UNsMYF08C1lnDYjQyfkwgllyUN",
            "https://drive.google.com/uc?export=view&id=1BYPTgReGCX_mTqJaAIw-XtYRQuasL6nJ",
            "https://drive.google.com/uc?export=view&id=1BVjCWXYPV-EtFE_Nj4rV6YiBJGZU8HZL",
            "https://drive.google.com/uc?export=view&id=1B89Sdt3lmmyR-pHirsjgBrICPWedw9uf",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1BY09GqJmrGsVeMCCP1Q54rP1q0RoTLpy",
            "https://drive.google.com/uc?export=view&id=1BVu3YhNHcW_CRbqtiT1RGSr_5G19PkFL",
            "https://drive.google.com/uc?export=view&id=1BgflYoNsYuuwFnV9GyxyW4RP8VuAgLd9",
            "https://drive.google.com/uc?export=view&id=1BRYvg_nEv6aszy5auxjg-vNRcbRHGG6a",
            "https://drive.google.com/uc?export=view&id=1Bsp8W0hBVdadq4MC92WTWHRMLDDxn3EU",
            "https://drive.google.com/uc?export=view&id=1Bh9PSUMR1TzXV8h6ehgXEF1O3BaTHGUZ",
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
                "Kesan": "abangnya berwibawa",  
                "Pesan": "semangat bang nontonya"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "kakaknya cantik",  
                "Pesan": "semangat ngeditnya kak"
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "Keren kak ngonten",  
                "Pesan": "semangat kak ngontennya"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "gokil kak ngegym",  
                "Pesan": "infokan gym yang bagus kak"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "kak juju baikk",  
                "Pesan": "fangirling siapa kakk"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "kak cia baik banget",  
                "Pesan": "shopping  di mana kakk"

            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "kak nelii ramah banget",  
                "Pesan": "suka merk mobil apa kak"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "keren kak ngoding",  
                "Pesan": "infokan projek kakk"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "abangnya asikk",  
                "Pesan": "hobinya klo dh nemu ajakin saya bangg"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "kakaknya baikk",  
                "Pesan": "infokan film thriller kak"
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@gymnn.as",
                "Kesan": "bang gym gokill",  
                "Pesan": "semangatt bangg"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "Kakaknya outgoing",  
                "Pesan": "infokan preset JJ kak"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "kak priska lucu",  
                "Pesan": "nonton yang bikin seneng aja kak"
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": "kacamata bang arsal bagus bang",  
                "Pesan": "infokan permabaran bang"
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "bang abit keren banget bang, baik juga",  
                "Pesan": "ajarin bang ngoding full stack"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "bang akmal orangnya pendiem tapi asik",  
                "Pesan": "jangan keseringan main hp bang"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "bang mawan kharismatik banget",  
                "Pesan": "novel nya bang mawan bagus banget"

            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "kak nun juga outgoing",  
                "Pesan": "semangat terus kak kuliah dan ngepelnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()