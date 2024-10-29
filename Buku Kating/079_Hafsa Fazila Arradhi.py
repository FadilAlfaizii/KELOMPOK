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
            "https://drive.google.com/uc?export=view&id=1ajUSYcVZW7YQq6TZSgAur4Ml8BPd7mRG",
            "https://drive.google.com/uc?export=view&id=1Xph4eYYCqxR1ZUOMvZuO6RE5U_sM0bY-",
            "https://drive.google.com/uc?export=view&id=10v9v2wwZaE30EI-maMYXmsVorG7fy9Uy",
            "https://drive.google.com/uc?export=view&id=18U8ZIyQPiX9S-MZ6wqE2lcsrhjwEJUjh",
            "https://drive.google.com/uc?export=view&id=1ya074gua4JDhkoqMgLS5xLZ9Tb3kVyk2",
            "https://drive.google.com/uc?export=view&id=1A2uk7IJ9v7U6hOyTacgSPD0L1UYjVm7C",
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
                "Kesan": "abangnya bijak",  
                "Pesan": "semangat bang mimpin himpunannya!"
            },
            {
                "Nama": "Pandra Insani Putra Azuar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "abangnya seruu",  
                "Pesan": "Semangat ngurus himpunannya bang!"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagaralam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "kakaknya periang",  
                "Pesan": "semangat kakk ngurus surat-suratnyaa!"
            },
            {
                "Nama": "Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh, Sumbar",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "kakaknya kalem",  
                "Pesan": "semangat kakakk nagih uangnyaa!"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "kakaknya ramah",  
                "Pesan": "semangat ngurusin uangnya kak!"
            }, 
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "kakaknya asik",  
                "Pesan": "semangat lpjan kakakk!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1w8XfA5_PGzINIKr6iRaAa5BJoPyvYXr0",
            "https://drive.google.com/uc?export=view&id=1jMvItsDOtevzKu2xkqiFxT7kpL4I1EtI",
            "https://drive.google.com/uc?export=view&id=1bEDeU-NNaB_XMIBKnqdzg3fTxTrVRAWp",
            "https://drive.google.com/uc?export=view&id=1zRuyIV9a1IxrBo2jQcwMq7dK5vjdUL9i",
            "https://drive.google.com/uc?export=view&id=1JoIraEo8X-Zb1rEByKSztot1kolMAl_6",
            "https://drive.google.com/uc?export=view&id=1V3fV10lXuGZ_tTlD_Ei-FWZwYXloL5j1",
            "https://drive.google.com/uc?export=view&id=1TUNLLjar2ShkRF_dkf-ZAD-5JDVpm8mI",
            "https://drive.google.com/uc?export=view&id=1BXMZkytreGITrqaS7sp5nG6UCd6k6hRH",
            "https://drive.google.com/uc?export=view&id=1dxiL40p-Kamcn42H9hw9VtXNOELdXraZ",
            "https://drive.google.com/uc?export=view&id=17Sk4eNPCPoYuoOCPa0RuahInkcJ5AsVE",
            "https://drive.google.com/uc?export=view&id=1vA6vUUnkvQFkFDHnlotFVK3vsM9dJjyO",
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
                "Kesan": "kakaknya ceria banget",  
                "Pesan": "tetap jadi pribadi yang menyenangkan ya kak!"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tanggerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, Nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "kakaknya ramah",  
                "Pesan": "semangat ngurus komisinya kak!"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150 ",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "kak wulan cantikk!",  
                "Pesan": "suksess terus kak!"
            },
            {
                "Nama": "Annisa Dini Amaliya",
                "NIM": "121450081",
                "Umur": "21",
                "Asal":"Tanggerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "kakaknya interaktif",  
                "Pesan": "semangat kuliahnya kakakk!"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "kakak nim akuu",  
                "Pesan": "bahagia terus kakk!"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Batu Raja, Sumsel",
                
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "abangnya asik",  
                "Pesan": "semangat kuliahnya kakk!"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "abangnyaa pendiem",  
                "Pesan": "sukses bangg!"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Sukabumi, Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka Ikut Tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "kakaknyaa lucu",  
                "Pesan": "sehat-sehat kakk!"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "121450156",
                "Umur": "22",
                "Asal":"Surakarta, Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "abangnyaa asik bangett",  
                "Pesan": "Semangat buat terus berkembang bang!"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "abangnya lucu",  
                "Pesan": "sabar bang, jangan marah-marah"
            },
            {
                "Nama": "Berlianda Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "kakaknya asikk",  
                "Pesan": "semangat menjalani kesibukan kakk!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vOS-JDXqTydamnDXem8m_WPgWRvCOUJ2",
            "https://drive.google.com/uc?export=view&id=14Qm8nycjQ5ZzBBx5ZyGG0ybO-8reiDcQ",
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
                "Kesan": "kakaknya inspiratif bangett",  
                "Pesan": "tetap jaga kesehatan ya kak!"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "abangnya keren banget",  
                "Pesan": "tetap menginspirasii banyak orang bangg!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=148thEYioDZF9qC-GzGEAIxxexViOwylG",
            "https://drive.google.com/uc?export=view&id=1l6J4sPF1FWGtt_-2Lq0Hgr95IsU5_9Qo",
            "https://drive.google.com/uc?export=view&id=1J7l0Uj46PLL47pUjBSWyR_B7uwrmuRUt",
            "https://drive.google.com/uc?export=view&id=11l7XgraGzy5qhu0_8B20fKioqBP45VzW",
            "https://drive.google.com/uc?export=view&id=1AvUjdSO7y6mUEj-wWpkG9sWweDDmHo7c",
            "https://drive.google.com/uc?export=view&id=1cnwUf59zaTDfEkL0oOveBdBbOHdyaYkG",
            "https://drive.google.com/uc?export=view&id=1QK4G1y45G6D6r19peVV0MMCazWI670ch",
            "https://drive.google.com/uc?export=view&id=1eEZ5c0UvrT43ORRBXg4esMKgo_TjmlC8",
            "https://drive.google.com/uc?export=view&id=1OctfGWGbECoQWY3CxuTmUSuQYonigP0f",
            "https://drive.google.com/uc?export=view&id=18CEDQ6UtDvqPVFfpxftOXv2XP7Wz6dzb",
            "https://drive.google.com/uc?export=view&id=1KWQgHQMYiIsqOu0tWHt9DgLIMbOZnhCq",
            "https://drive.google.com/uc?export=view&id=1d01oRP60W0vCk0G9J768IcjezCKDGbKe",

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
                "Kesan": "abangnya humble bangett",  
                "Pesan": "jangan lupa istirahat bang!"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "kakaknyaa manis",  
                "Pesan": "tetap semangat kakk!"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "abangnyaa asik",  
                "Pesan": "semoga bisa ngoding tanpa gpt ya bang!"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "ternyata ga galak",  
                "Pesan": "titip ka elil ya kakk!"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "abangnya baik bangett",  
                "Pesan": "semangat ngaspraknya bangg!"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "kakaknya pendiem",  
                "Pesan": "semangat kuliahnya kakak cantikk!"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "kakaknya ramah",  
                "Pesan": "semangat jadi pribadi yang lebih baikk kak!"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "abangnya positif vibes bgt",  
                "Pesan": "semangat ngebimbing anggotanya bang!"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "kakaknya ramah",  
                "Pesan": "semoga lancar kak kuliahnya!"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "agak pendiem",  
                "Pesan": "semangatt terus kakak!"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "abangnyaa murah senyum",  
                "Pesan": "semoga semua tujuan nya tercapai!"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "abangnya ramah",  
                "Pesan": "semangat mss nya bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eIHmgPsz0OnT8bEIYTThxkQ7U94-nJxk",
            "https://drive.google.com/uc?export=view&id=13zsKaP2sOmPdUFH8wPr3UOoqBf_JO1qd",
            "https://drive.google.com/uc?export=view&id=13hh_2Sxggn4Qa2QOqRByyh_kwAzcHTFM",
            "https://drive.google.com/uc?export=view&id=12oplL46H6eceYaCJlZWUhanpsT_CDMfm",
            "https://drive.google.com/uc?export=view&id=1Z7wykgvt0PAULw8bxw0YrJopFEEGvRYZ",
            "https://drive.google.com/uc?export=view&id=1hy7Fx8JEMVy2qcxqPkN7CylI2TzapuI9",
            "https://drive.google.com/uc?export=view&id=1AHNT2UmMTXa-V2vFWd66pewDCSpALLXm",
            "https://drive.google.com/uc?export=view&id=1dhGPClssHAe2pUF6Sw5bBd-2rsepu8y_",
            "https://drive.google.com/uc?export=view&id=1jkhC0es0167thF_LGxBKi6PWGZIsxboa",
            "https://drive.google.com/uc?export=view&id=1-79In_ucsZ5US8U-p8NUIzL7PpxGfHLB",
            "https://drive.google.com/uc?export=view&id=1lqzzC1xB6gFgC3EG_Q4oEpajeIrbk9RW",
            "https://drive.google.com/uc?export=view&id=19-_VLzsFnHQabvjZ8rlLesGrXhPMz3tY",
            "https://drive.google.com/uc?export=view&id=1oodvymkOfcGbNS6FgSGoNyTuK3gFhpaB",
            "https://drive.google.com/uc?export=view&id=1jB_yqjSKbBf-sgzXRgr0gr0pLqPyzv7z",
            "https://drive.google.com/uc?export=view&id=1TtaA297QfdRZrd-_weox9ceUTtb28-jv",
            "https://drive.google.com/uc?export=view&id=1XZIHmN5OEbSWDlTv77gUjuOx_OD1s9nJ",
            "https://drive.google.com/uc?export=view&id=1kl033NSP61kA2dzNO5jJMi3LTPPPj--6",
            "https://drive.google.com/uc?export=view&id=1ZiFHRLYIB2j3C6CISbpugBJnKpK0B3_p",
            "https://drive.google.com/uc?export=view&id=1yOKcRMfpcbg5UyawNQisHoqI5xOzomXE",
            "https://drive.google.com/uc?export=view&id=17CwiizaP12_9T_KEz2vVDDzgE1dn9CS0",
            "https://drive.google.com/uc?export=view&id=1uR75zeJSgIgb9mnr1TBVwrhlmnNanKJV",
            "https://drive.google.com/uc?export=view&id=1VHLFUPiYtRFpZ_f81rwh_VLj1siXvKq2",
            "https://drive.google.com/uc?export=view&id=1hr1o9_NLdHs0UQB_xO6HnTTwflo5ouOb",

          
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
                "Kesan": "abangnya tegas dan inspiratif",  
                "Pesan": "tetap selalu membimbing dan menginspirasi banyak orang bang!"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "kakaknya asikk",  
                "Pesan": "semangat kak jadi sekrenya!"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "maniss banget",  
                "Pesan": "tetep jadi pribadi yang menginspirasi kak!"
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
                "Pesan": "semoga kuliahnya lancar kak!"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "kakaknyaa rendah hati",  
                "Pesan": "sukses terus kak!"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "abangnya asik",  
                "Pesan": "semangat terus bang!"
            },
            {
                "Nama": "Eksanty F. Sukma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "eksantyfebriana",
                "Kesan": "kakaknya pinterr",  
                "Pesan": "semoga bisa terus berkembang lagi kakk!"
            },
            {
                "Nama": "Oktavia Nurwenda Puspita Sari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "kakaknya baik banget",  
                "Pesan": "tetap jadi pribadi yang baik dan ramah kak!"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "abangnya ramah",  
                "Pesan": "semangat menjalani kesibukannya bang!"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "abangnya lucu dan asik banget",  
                "Pesan": "tetap jadi pribadi yang periang bang!"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "abangnya pendiem",  
                "Pesan": "suksess teruss kak!"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "abangnya humble banget",  
                "Pesan": "tetap rendah hati bang!"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "abangnya baik dan sabar",  
                "Pesan": "makasi bang bimbingannya!"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "abangnya ga banyak omong",  
                "Pesan": "semangat capai cita-cita bang!"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "cantikk banget kak",  
                "Pesan": "semangat kakak cantik!"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "kakaknya kalem banget",  
                "Pesan": "sukses terus kakk!"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "abangnya sopan dan ramah",  
                "Pesan": "tetap jadi pribadi yang ramah dan riang bang!"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "kakaknya aktif dan ekspresif",  
                "Pesan": "semangat skripsiannya kakk!"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "abangnya asik bangett",  
                "Pesan": "semangat ngejalanin prokernya bang!"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "abangnya baik bangett",  
                "Pesan": "pantang menyerah bang, semangat!"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "kakaknya maniss",  
                "Pesan": "sehat selalu kak!"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "abangnya pendiem",  
                "Pesan": "semangat bangg ngejalanin hari-hari!"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "mirip sama kakak mikfess",  
                "Pesan": "akur-akur ya kak sama kembarannya!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19zccYx3hjOVkyRuBbehMuwfwkz_NfWFT",
            "https://drive.google.com/uc?export=view&id=1cdRR3tByTofHGSU-ZmLW3fzIdurH5JAp",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "",  
                "Pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14NkKIMivxAmtg-vX1yKib_CL9VZz-uYU",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1WcMIDSIPIcJ_3MvHJN9eC5zfUXtJ_90c",
            "https://drive.google.com/uc?export=view&id=1gcvWtgAi24I2V5Q01hI-apFux0CqYvjI",
            "https://drive.google.com/uc?export=view&id=1xFy5cEB8jsHg5BhPN5xgU_nwvVu_5B3N",
            "https://drive.google.com/uc?export=view&id=1QuhhBfzl6DLEkJVkqrAUaRcJSdw7j-ta",
            "https://drive.google.com/uc?export=view&id=11UItGXJnOE6O3M6xaPkILrtl2ELGUN4z",
            "https://drive.google.com/uc?export=view&id=1iKhQu1Cz5nzM1w1sg_Y4dcoj9BKZWEeS",
            "https://drive.google.com/uc?export=view&id=1WeaIR4GjngAHpfNgBGB7oShwYyakCyKe",
            "https://drive.google.com/uc?export=view&id=1ivNuyIQs_QhYN2d5B9zC2QacRJcsXBfZ",
            "https://drive.google.com/uc?export=view&id=1PetLwatsyQ8gC7Wc1plEIfQXK6LywSqD",
            "https://drive.google.com/uc?export=view&id=1CgPcgTkzKPIN4FG1d_YiBqWMT8ccaWK4",
            "https://drive.google.com/uc?export=view&id=1h0I-ERmsg34F6YQUcGUohgzjWlI8xxJB",
            "https://drive.google.com/uc?export=view&id=1_dRCDHw6FiLy1hGHXHfmjlw17wy2DeQv",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
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
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "",  
                "Pesan": ""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_CGhpgV7tOiI7-w54m-j4LxV16bUvNAq",
            "https://drive.google.com/uc?export=view&id=1KEzETTwmWAMnbaZ_a0mhE65SyjBWGTUa",
            "https://drive.google.com/uc?export=view&id=1kW0g_UInspzA10OC7bpPLlaKpT0_mXej",
            "https://drive.google.com/uc?export=view&id=1CwjB97eofBduA6rPZcjmjXVhJdKK7_ur",
            "https://drive.google.com/uc?export=view&id=19dyZz2dM2fgwJTuNIyKUKpw2K2EKXfE9",
            "https://drive.google.com/uc?export=view&id=1cmIOx2qxV-xOzUZbpKeWM-sg2pbp4HOa",
            "https://drive.google.com/uc?export=view&id=1Jr4k5P7RKDM9E278tyjJxwxdeAYWamTs",
            "https://drive.google.com/uc?export=view&id=18GTogXvs30RKYhrh6r89HtyZAYK6Y-5G",
            "https://drive.google.com/uc?export=view&id=1SLIwF_CIvoaQk2aYLkbu33K_3KIXb7W0",
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
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Nabilah Andika Fitriati",
                "NIM": "121450139",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kedaton",
                "Hobi": "Bikin JJ",
                "Sosmed": "@nabilahanftr",
                "Kesan": "",  
                "Pesan":""
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "",  
                "Pesan":""
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lLN_GkI3XfDZ2V_TidNiPlvmYYCw1f3S",
            "https://drive.google.com/uc?export=view&id=1xXg40LZ8wx8reg5NYyOKDQj0GK-vTetD",
            "https://drive.google.com/uc?export=view&id=1OW1rsmzaDJzcedLxtuShiwtTTItE74tw",
            "https://drive.google.com/uc?export=view&id=1dqUT8Oc7xYOlJw4Nuj3yS5RzTTR26Uka",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1liJkb7R4N9SSI7HK7SyqVo5sjkQ7KY4q",
            "https://drive.google.com/uc?export=view&id=1ZdPsNVw3Zu98kjC_njjaDiwAoxIGdK25",
            "https://drive.google.com/uc?export=view&id=14syEOudb9BTT4OmE9p-EFpbEgbOoYhzD",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1eX1MYNLJvI3WvGZta1g3JinggFpldmJv",
            "https://drive.google.com/uc?export=view&id=1k2emZYOl9lAyQWnV9UpO328RK5bhAbSG",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1sxLcXNWyNTUHtT-7VI9QLBny-CxDKMCz",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1I4yU38rBssJFDSZ07RomKlYQPtL-hrfH",
            "https://drive.google.com/uc?export=view&id=1Cq6PJABy_ApCiNI8nJrvYQs-VNsjtkT6",
            "https://drive.google.com/uc?export=view&id=1UMx2S0YpICMXWPkl7V3uhclulb2Dz_d_",
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