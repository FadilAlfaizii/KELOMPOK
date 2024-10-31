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
            "https://drive.google.com/uc?export=view&id=1FlkHgMsYz-989GVpwbv61n1UUwPkjZlv",
            "https://drive.google.com/uc?export=view&id=1FgF1JmbqCHIii07WC1w0fWOZ0VmmHdTJ",
            "https://drive.google.com/uc?export=view&id=1FcC8_i9v7OLYC6B9JM8b1C_F8yklpmCv",
            "https://drive.google.com/uc?export=view&id=1FvWmr0pCYUWiMhPsuOI6uHCud1f1NiNp",
            "https://drive.google.com/uc?export=view&id=17iHOHoBoEKIvkm0LEyrPxc47hTtgi5IP",
            "https://drive.google.com/uc?export=view&id=1FeHQKQlMPa5bTi7he-96h6psI-MF2UA3",
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
                "Kesan": "rizz abis",  
                "Pesan":"abang ini keren"
            },
            {
                "Nama": "Pandra Insani Putra Azuar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "suka anuin rambut",  
                "Pesan":"semangatt ngatur jadwalnya bangg"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagaralam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "manisss",  
                "Pesan":"semanagat bikin proposalnya kakak maniss"
            },
            {
                "Nama": " Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh, Sumbar",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "kerenn",  
                "Pesan":"semoga ipk nya 4"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "kakak ini hawanya serius",  
                "Pesan":"semangat nagihin duitnya kakk"
            },
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "lucukk",  
                "Pesan":"semangatt ngitung duitnya kakk"
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1kqxtEpljTKlvtNTdDpmehVHNgIXStclF",
            "https://drive.google.com/uc?export=view&id=1hnAmLE6y37xF55_3gmxyiyuGE5SnVSHO",
            "https://drive.google.com/uc?export=view&id=1j71OuSkh04cIOj_VTN9LvT2p8QF9DPJQ",
            "https://drive.google.com/uc?export=view&id=1R2EK_02HSYhuVRyQU5NzqjNv9Ooh1H80",
            "https://drive.google.com/uc?export=view&id=1l7sakgXKarrJyxD85cRHw7DZbt1VaN62",
            "https://drive.google.com/uc?export=view&id=13Ip7KZN_hy9epaZf0V_KOoSO4hk5w6eD",
            "https://drive.google.com/uc?export=view&id=1mLD71KoQwGrp3N_d5lzVjIuuZlfM0M_h",
            "https://drive.google.com/uc?export=view&id=18RqdV4vurtQxrZUqxQdY6sxXEvLRuxFa",
            "https://drive.google.com/uc?export=view&id=1tqXahZkwQytdhnkK-C4J6Tasoave0FLh",
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
                "Kesan": "teteh Bandung",  
                "Pesan":"notice vany salsabila putri dr kelompok poisson di baleg dong kakk"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150 ",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "kaka ini cantik aku suka",  
                "Pesan":"sehat sehat kakak cantikk"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "kakak ini baikk banget",  
                "Pesan":"semoga lulus tepat waktu"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Batu Raja, Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "kerenn",  
                "Pesan":"bang bagusin nilai praktikum vany salsabila banh"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "abang ini spt orang jepang",  
                "Pesan":"bang notice vany banh"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Sukabumi, Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka Ikut Tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "kakak ini maniss",  
                "Pesan":"kapan mau tes SKD lagi kakk?"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "121450156",
                "Umur": "22",
                "Asal":"Surakarta, Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "chill abiiez",  
                "Pesan":"keren keren trs bang"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "kiyay lampung pasti ini",  
                "Pesan":"sehat sehat bang"
            },
            {
                "Nama": "Berlianda Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "kirain galak, ternyata baik",  
                "Pesan":"semangatt kuliahnya kakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Mm1jhvF7EENlwOLgLRRTQqrCGVQb1zCs",
            "https://drive.google.com/uc?export=view&id=1MspIP3Sk14aVONZV6nJAExcfSA1JvkGb",      
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
                "Kesan": "Keren banget berkharismatik",  
                "Pesan": "Sehat sehat kakak senat"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "Tegas abangnya",  
                "Pesan": "Infokan konser kak Luthfi bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ZqdG8keYxsBdugtTuyRE9EiYEEKk8-PX",
            "https://drive.google.com/uc?export=view&id=1RGmVXFS2RKdDyfUSPCpkAy4zOIb17yJq",
            "https://drive.google.com/uc?export=view&id=1Zz040Lg1Ko2Mw7o9Z7CChTL1Xt-DBOAZ",
            "https://drive.google.com/uc?export=view&id=1_77-NtNhjrwyaD4sYuXU4uFPdE1FvATf",
            "https://drive.google.com/uc?export=view&id=1_5C6umhwBZLDnX5yooAtDS6ArcVoqJRX",
            "https://drive.google.com/uc?export=view&id=1RezM3e35vwcb5Esf9ga9C1W11QRxGhtP",
            "https://drive.google.com/uc?export=view&id=1RZWCHsj_V2eunXtskXzASAB1H7hJW2nR",
            "https://drive.google.com/uc?export=view&id=1RmtakBeFLhQwwsbNFYIjfedA3v9Di4UA",
            "https://drive.google.com/uc?export=view&id=1Rp4CfcteZxmEu5giTLPTqr6x2am3bxRn",
            "https://drive.google.com/uc?export=view&id=1KhO3ozxFLv2VxMqLGdFfExqPEi7aXgcj",
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
                "Kesan": "Chill banget abangnya",  
                "Pesan": "Jangan mancing keributan terus ya bang, 3x sehari gapapa"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "Sangat anggunly sangat slay",  
                "Pesan": "Semangat kuliahnya kakak cantik"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "Kakanya seperti tomboi",  
                "Pesan": "Titip kak Elila kesayangan Poisson yeah kak"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "Abangnya sangat ceria",  
                "Pesan": "Praktikum saya 100 kan bang?"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "Kakanyaa soft sekalie",  
                "Pesan": "Jangan lupa makan kak"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "Abang ini sangat soft",  
                "Pesan": "Spar sama Hanip bang"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "Kakaknya imutt",  
                "Pesan": "Jangan lupa minum air putih yang banyak kak"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "Sangat islami",  
                "Pesan": "Infokan hasil kebun kak"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "Abangnya humble banget",  
                "Pesan": "Infookal jadwal konser bang"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "Tegas rahangnya",  
                "Pesan": "Rekomendasi film bagus selain horror bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NCkb896ckY8NLMEOp0Y1p7S8tlQzoemB",
            "https://drive.google.com/uc?export=view&id=1LgV6kas9R68zkJqeNFP4uDlwZlyhFlem",
            "https://drive.google.com/uc?export=view&id=1Lv4Mo5H1Ar5lBQCWkKFyor-6XoUxNVC-",
            "https://drive.google.com/uc?export=view&id=1M1EVtR-htaRoz17CvEBssrycGtJGNYzh",
            "https://drive.google.com/uc?export=view&id=1Lrd6jVsDJI1Tsy4jSK5akvX8PVk-U694",
            "https://drive.google.com/uc?export=view&id=1Lq1w1DgaityGr9AzM-3_qwZKkuLZhjku",
            "https://drive.google.com/uc?export=view&id=1LhQkr9EgtWRAviNnYGFFAyH4JOwjVTIL",
            "https://drive.google.com/uc?export=view&id=1LkZRNcDcExWrFGZWpuNb3IykhRRgUk7w",
            "https://drive.google.com/uc?export=view&id=1LzvBgg0W2TixuOKW4AbIBMiDTZFNp-me",
            "https://drive.google.com/uc?export=view&id=1_S8LxTcKRAMfdMvh3pHTmhPqH9pKjt-0",
            "https://drive.google.com/uc?export=view&id=1N6dCCI3wp4zUj7H8jVaNk5siAMvbVVWO",
            "https://drive.google.com/uc?export=view&id=1NUKrqOsBnfyPiUzmnFTXoReuWarVNcbW",
            "https://drive.google.com/uc?export=view&id=1NkQVoA4wqmvAH8V9QWzDBP9uazO9n-Xo",
            "https://drive.google.com/uc?export=view&id=1NQ9SwdmKbGFyOAZ2dPp0hfQnWPoKLlck",
            "https://drive.google.com/uc?export=view&id=1NEYC52pNcMYtoltAvcPp9K-kgl66VtiC",
            "https://drive.google.com/uc?export=view&id=1LfWHDUTPyX_lVawyrSfF7UquQd7lyom-",
            "https://drive.google.com/uc?export=view&id=1Ndln9itYGAOGbJJ47VBkeQFS9jgFaXZ_",
            "https://drive.google.com/uc?export=view&id=1NkN3fvay62LegiT2OIrM3PKP8SZh8-YF",
            "https://drive.google.com/uc?export=view&id=1M4RWG96NlGV9Xwh3UHVmXoangqUYVBoH",
            "https://drive.google.com/uc?export=view&id=1M7V-pB3X31hoH-o5agF-MymzDPwXjXV_",
            "https://drive.google.com/uc?export=view&id=1LfKeYaqZ_U89G7KPmfdnB4i6XU6IlY00",
            "https://drive.google.com/uc?export=view&id=1M8B8-IJyU6y-_IPrpjCUJmmyVyfL_5PW",
            "https://drive.google.com/uc?export=view&id=1M8jfLLkms40lSeD5aBY3-o_KFOPOVnkp",
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
                "Kesan": "Wow anak dulidu",  
                "Pesan": "Infokan jadwal buka bengkel bang"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "Kakaknya humble",  
                "Pesan": "infokan umpan mancing keributan kak"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "Cantik kaya orang Arab",  
                "Pesan": "Liptintnya pake apa kak?"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "Kakak komdis",  
                "Pesan": "Rate rasa ayam kalasan warboy kak"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "Gemess kalo senyum matanya ilang",  
                "Pesan": "Jangan lupa istirahat kak"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "Tukang parkir",  
                "Pesan": "Udah winstreak belum bang hari ini?"
            },
            {
                "Nama": "Eksanty F. Sukma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "@eksantyfebriana",
                "Kesan": "Asik kakaknya",  
                "Pesan": "Sabar sabar ngajarin pani ya kak"
            },
            {
                "Nama": "Oktavia Nurwenda Puspita Sari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "Paling galak di ika? ternyata tidak",  
                "Pesan": "Istirahat yang cukup ya kak"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "Abangnya jarang senyum",  
                "Pesan": "Senyum itu ibadah bang"
            }, 
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "Abangnya lucuu",  
                "Pesan":"P adu keong"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "Abang ini manis",  
                "Pesan": "P mabar"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "Galak, pembully",  
                "Pesan": "Pretest saya 100 kan bang?"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "Ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "Rapih orangnya",  
                "Pesan": "Udah berapa kali ngeprint hello dunia hari ini bang?"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "Abangnya diem aja",  
                "Pesan": "Jangan lupa minum air putih bang"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "Cantik kakaknya",  
                "Pesan": "Semoga sukses kak"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "Ini juga kakak cantik",  
                "Pesan": "Semoga setiap baca webtoon happy end terus"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "Ramah, bintang 5",  
                "Pesan": "Semangat abang daplok"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "Ketchee bgt brow",  
                "Pesan": "Tolong notice ak di barisan supporter itu kak :3"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "Sangat positive vibes",  
                "Pesan": "Semoga dibalas berkali lipat tiap menolong ya bang"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "Abangnya baik",  
                "Pesan": "Sukses selalu ya bang"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "Kakak mc",  
                "Pesan": "semoga selalu dipertemukan dengan situasi yang menyenangkan ya kak"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "Abangnya kerenn",  
                "Pesan": "Semoga win terus tiap main game bang"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "Kakak kembarrr?!",  
                "Pesan": "Infokan tutor bedain kakak sama kembaran kakak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WZOpnFD-4V_IyQ5iFHJa9H45oP50Xilr",
            "https://drive.google.com/uc?export=view&id=1X0QclOhJFXyBmGxnXqDTOjW0V3apV3oM",
            "https://drive.google.com/uc?export=view&id=1WpOAeC5ZklqZw3VXXnujMp9jdKHlSNTk",
            "https://drive.google.com/uc?export=view&id=1WhirqMcMUgLw4T1IrNGUKOTmePM9R8UL",
            "https://drive.google.com/uc?export=view&id=1Wp_o6EvGWtaA-GjydgvRphvNJknQuTGb",
            "https://drive.google.com/uc?export=view&id=1WsfEJA7zYXVdJJf5Ekl5NClWvhbcMd6u",
            "https://drive.google.com/uc?export=view&id=1_NNvQJx3Y6e--bTdzb-nVR7OrXx_DOjG",
            "https://drive.google.com/uc?export=view&id=1Wn-DD0xjoala5b4nzY4sByFR8TA45Y84",
            "https://drive.google.com/uc?export=view&id=1WicI5Bmy0KNDPs5tWdBcvJ8ttx1gi472",
            "https://drive.google.com/uc?export=view&id=1Wf4G_nJB4K9hXKetRvgPTSsFpeWrSXth",
            "https://drive.google.com/uc?export=view&id=1YmmQxO9DaWhBWhLWUXpqyQfBKYelilwW",
            "https://drive.google.com/uc?export=view&id=1WVajN4tb2NnVOT9mKrwROd3OwqvP7cl8",
            "https://drive.google.com/uc?export=view&id=1WZAqGrZPKSgy9Wp2cW4m9pmflWesUJzk",
            "https://drive.google.com/uc?export=view&id=1WUlRdy2yy6YaCp-IhfAQ-TnKx6xh37db",
            "https://drive.google.com/uc?export=view&id=1WLyBZ5qt2hTHhSXDkPCWFMs2FmeaNzN5",
            "https://drive.google.com/uc?export=view&id=1WJogI5b5p2Y8eRAkydWJU5maoJomo9YN",
            "https://drive.google.com/uc?export=view&id=1WTY2NzIOkxyyN35Yw5E5YPFtvFlyRYn4",
            "https://drive.google.com/uc?export=view&id=1WTFwsEUm1CURTXoQ_SZaSLbhPFhHxAml",
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
                "Kesan": "Abangnya kece banget",  
                "Pesan": "Semangat ngurus 1 departemen bang"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "Ramahh banget kakaknyaa",  
                "Pesan": "Semoga lulu tepat waktu ya kak!"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "Lucuu kakaknyaa",  
                "Pesan": "Infokan tempat main golfnya kak"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "Auranya orang ceria",  
                "Pesan": "Semoga moodnya oke terus ya kak"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@esteriars",
                "Kesan": "Kakaknya gemesss",  
                "Pesan": "Semangat kuliahnya kak"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "Kakak inni kiyowo",  
                "Pesan": "Tutor surving kak"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "Seperti wanita karir",  
                "Pesan": "Jangan lupa jaga kesehatan kak!"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "Kakak ini ramee",  
                "Pesan": "Tutor main sepak takraw kak"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "Abang yang jago basket",  
                "Pesan": "Kok hobinya bukan basket bang?"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "Marganya kaya ridho",  
                "Pesan": "Diajakin main bultang kak sama Hasfa"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "Manis abang ini",  
                "Pesan": "Semangat bikin portofolionya bang"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "Ramahh banget",  
                "Pesan": "Infokan hasil bertaninya bang"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "Bulunya kak Lilaa",  
                "Pesan": "Sehat sehat kak"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "Sangat humblee",  
                "Pesan": "Nonton mukbang juga ga bang?"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "Kakaknya seruu",  
                "Pesan": "Semangat ngampusnya kak"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "Maniss bangett aww",  
                "Pesan": "Senyum terus kak, biar orang pada diabet :p"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "Abangnya baik",  
                "Pesan": "Semoga sukses selalu bang"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "Kakaknya mancung, cakep",  
                "Pesan": "Jangan lupa jaga kesehatan ya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OO0yjiPAzR4pues_I7LQB-vHBFootLc_",
            "https://drive.google.com/uc?export=view&id=1O1tyy0gRk4DsRW2oYPoPE_6uTYz84FKW",
            "https://drive.google.com/uc?export=view&id=1OLAoNKCCZiIyf4NOD3dUeUziL4VbbKyJ",
            "https://drive.google.com/uc?export=view&id=1OH2FVD2AZUvQWEb2LNutdQO4UZxRAR6J",
            "https://drive.google.com/uc?export=view&id=1OIq2PJjLrMYcckYP1oLMo_NkZzgmyzLQ",
            "https://drive.google.com/uc?export=view&id=1O29ODVnlI4171Poziomeie3QG7gb6Gn0",
            "https://drive.google.com/uc?export=view&id=1__t3p_nnFqf0_zIqZ-S7MPv6YDxLfGDM",
            "https://drive.google.com/uc?export=view&id=1NvfNTrszyTt2kNhlTBfhDQUE0ZorJgfI",
            "https://drive.google.com/uc?export=view&id=1OCSUijBF-Pju_UvMDgswmbK0Ggdg87Vh",
            "https://drive.google.com/uc?export=view&id=1NvxxU0v-Fff0e4OUpK6pJpqr_3eoJaL2",
            "https://drive.google.com/uc?export=view&id=1OB0qvGORgnPNKNa_mH9MdvneKoXBUcUK",
            "https://drive.google.com/uc?export=view&id=1O2C0wm4waCoRN4bHjD0_oBYkfzI-BZTA",
            "https://drive.google.com/uc?export=view&id=1NvGHoO6BzETqE2SAXMtYpiQ6vu1FSSGE",
            "https://drive.google.com/uc?export=view&id=1_Zgb1WDBJ3gOwFkbS0ULOmOfM3LEB83z",
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
                "Kesan": "Abang ini berkharismatik",  
                "Pesan": "Semoga sukses terus ya"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "Hawanya hawa orang sibuk",  
                "Pesan": "Stay happy stay healthy kak"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "Abangnya lucuu",  
                "Pesan": "Sukses selalu bang"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "Berwibawa abangnya",  
                "Pesan": "Betah betah ngasprak ADS terus ya bang"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "Kakaknya kembarr",  
                "Pesan": "Trimzie sudah sering membantu prak. ADS saya kakak <3"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "Auranya spt orang pintar",  
                "Pesan": "Mending mole bang daripada ML"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "Kakak ini soft sekali",  
                "Pesan": "Semangat resume webinarnya kak"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "Kakak ini gemass",  
                "Pesan": "Bahagia selalu kak"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "Kembaranku kata bg Johan :3",  
                "Pesan": "Gimana journal bu Mika nya kak?"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "Namanya susah",  
                "Pesan": "Sukses membangkitkan bilangannya kak"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "Bagus banget tulisannya?!",  
                "Pesan": "Tips tulisan bagus dan rapih bang"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "Muka sangat ramah",  
                "Pesan": "Semangat  ngoding wisatanya bang"

            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "woww orangnya",  
                "Pesan": "yaa okee lah"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "Diem banget abangnya",  
                "Pesan": "Semoga happy terus seperti namanya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MIIZDP3O8C5_ztuj13EhEfNIzse9NXt6",
            "https://drive.google.com/uc?export=view&id=1MKs-iSb-yUk_4LZPTmKioGQeAQi0TCJM",
            "https://drive.google.com/uc?export=view&id=1MWaA_h6L0OJ2c57wXeRdlcKyKTYIL1g-",
            "https://drive.google.com/uc?export=view&id=1MTPrWZ-xcsh7DjI3Fs9OqdwI8UbEzZnz",
            "https://drive.google.com/uc?export=view&id=1MKL8FdVlbhWyHR6Y5FqgWsASuvvvxM6J",
            "https://drive.google.com/uc?export=view&id=1MTIyNoZrsTBuJtJ3kQa4fheD5h0vgIxa",
            "https://drive.google.com/uc?export=view&id=1McwIw8HgZIlDC-atZi3kH6v1rLLbPwpz",
            "https://drive.google.com/uc?export=view&id=1XEwSE3iqco4QUaUSBwLqK3VdrCrQs7c-",
            "https://drive.google.com/uc?export=view&id=1X8MdEp4CAwL4eiMnZUB7jpEWTVIIF34k",

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
                "Kesan": "Seruu abangnyaa",  
                "Pesan": "Semangat nyari hobinya bang"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "Maniss banget kalo senyum?!",  
                "Pesan": "Jangan bikin orang diabetes ah kak"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "Cantik banget kaya orang arab",  
                "Pesan": "Semangat ngitung duitnya kak"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal": "Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "Pasti orang padang",  
                "Pesan": "semangat badmintonnya"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "Abang ini ramee",  
                "Pesan": "Semangat touringnya abang"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "Abang ini keren",  
                "Pesan": "Ati-sti pp Bogor-Lampungnya bang"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "Kakanyaa gemess",  
                "Pesan": "Semangat menulisnya kak"
            },
            {
                "Nama": "Nabilah Andika Fitriati",
                "NIM": "121450139",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kedaton",
                "Hobi": "Bikin JJ",
                "Sosmed": "@nabilahanftr",
                "Kesan": "Kakaknya kerenn",  
                "Pesan": "Ditunggu hasil JJ nya kakk"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "Lucuu, kalo senyum matanya ilang",  
                "Pesan": "Infokan jadwal kakak konser"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LMrZ5WEgmmC19sUDQhtBovFnVQ6F8X_j",
            "https://drive.google.com/uc?export=view&id=1KuZuFM3Vgn1qc2OBgteiWP38vHrqCq9B",
            "https://drive.google.com/uc?export=view&id=1LRZWzDRE-AH48nOjx7zHS3rMi_XbWXW- ",
            "https://drive.google.com/uc?export=view&id=1LNn9r5dXuGCgkXWVDC52Qa5hBaAhT5pC",
            "https://drive.google.com/uc?export=view&id=1KmI-JUOErpNedB8laYthwwQU3EItwFNp",
            "https://drive.google.com/uc?export=view&id=1LRttc-4JmNnBMj51ERx72iH0aZDlpNvN",
            "https://drive.google.com/uc?export=view&id=1_marnzo4OFJkly1L1mi28VXctjQXUZmX",
            "https://drive.google.com/uc?export=view&id=1L3kn0czwRRVMaCgt-Lb6ffebY-v68fmY",
            "https://drive.google.com/uc?export=view&id=1_khC9Y1Xs3L36NXceVyoWZMfgxSQhOjk",
            "https://drive.google.com/uc?export=view&id=1Klv3zjwgUTGu6x4XiL1ThgfCWCmgEiaJ",
            "https://drive.google.com/uc?export=view&id=1YlghW_YHcPDVt2fUtWeNmyqtj_DgAgOf",
            "https://drive.google.com/uc?export=view&id=1KpFAipVh2gkDAaMgJizCW7GfON1pSmwl",
            "https://drive.google.com/uc?export=view&id=1L4J50-wMUYjGpzmTR5c-AGWrQr0kf4s2",
            "https://drive.google.com/uc?export=view&id=1LIHoD2XbP3zCXII8-BClwOl6m09vLki1",
            "https://drive.google.com/uc?export=view&id=1KzKTmMTvN4Ea8XNxHxGvtrV7tCGtnw8k",
            "https://drive.google.com/uc?export=view&id=1LUo42bnyU1xssZzrbGxj_bmXPW_6_FNF",
            "https://drive.google.com/uc?export=view&id=1LObtfmZayC4NKmN5uy_suQi4dxFYA3do",
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
                "Kesan": "Keren abang ini",  
                "Pesan": "Sukses terus bang"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "Cantik banget pls",  
                "Pesan": "Semoga IPK nya 4"
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "Ramah kakak ini",  
                "Pesan": "Semangat ngontennya kak"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "Kaya model",  
                "Pesan": "Semangat ngegymnya kak"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "Kakaknnya kiyowo",  
                "Pesan": "Diajak fangirling sama Daniar kak"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "Si manis berlesung pipit <3",  
                "Pesan": "Semangat ngaspraknya kak ciakk"
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "Sangat terkesan",  
                "Pesan": "Semangat selalu"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "Sepertinya kakak ini baik",  
                "Pesan": "Semangat ngodingnya kak"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "Keren namanya kaisar",  
                "Pesan": "Semoga cepet dapet hobi ya bang"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "Kakak ini menggemaskan",  
                "Pesan": "Ayo kita nonton film hantu kak"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "Kakak ini keren",  
                "Pesan": "Pulang ke Bekasi bareng ayo kak"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "Ramah  banget", 
                "Pesan": "Titip kak elila ya kak"
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": " Abang ini seperti gamer",  
                "Pesan": "Semoga winstreak"
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "Abang gemoy",  
                "Pesan": "Semangat ngodingnya bang"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "Abang ini pendiem",  
                "Pesan": "jangan bikin kesel daplok saya ya bang"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "Abang ini yang pernah bohongin saya",  
                "Pesan": "Titip kak elilanya poisson ya bang"
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "Kakak ini tegas",  
                "Pesan": "Semangat kuliahnya kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()