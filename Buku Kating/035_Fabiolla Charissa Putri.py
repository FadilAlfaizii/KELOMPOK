
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
           "https://drive.google.com/uc?export=view&id=1jwN8b5TMRlpEb3QQJymeyI-3fVQZBBHt",
           "https://drive.google.com/uc?export=view&id=1vpBI2mEejcE8v4yTWB-46KjtBgDG16g6",
           "https://drive.google.com/uc?export=view&id=1BrBXmBv4-dqpMBIZBCZzwljBUcz8JAaI",
           "https://drive.google.com/uc?export=view&id=1iWZieXaEyG1Wwuocw0qTF6Yh279Bp4Ct",
           "https://drive.google.com/uc?export=view&id=17_Pkihk4lNxR_ATyRv5fZyTe3Ed5GNB9",
           "https://drive.google.com/uc?export=view&id=1Uio4VTeM3cs-w5s21ejmIjkEqet-99Wz",
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
                "Kesan": "Abangnya asik",  
                "Pesan":"semangat terus kuliahnya bang !!!"
            },
            {
                "Nama": "Pandra Insani Putra Azwar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "Abangnya asik juga",  
                "Pesan":"Lancar selalu kuliahnya bang"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagaralam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "Kakaknya baik dan gercep",  
                "Pesan":"Semangats kakak"
            },
            {
                "Nama": " Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh, Sumbar",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "Kakaknya baik",  
                "Pesan":"Semangat Kuliah nya kakak, jangan kasih kendor"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "Kakak baik sekali",  
                "Pesan":"Semangat Kakak Cantik"
            },
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "12145003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@hrtfdlh",
                "Kesan": "Kakaknya asik",  
                "Pesan":"sehat selalu kakak"
            }, 
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fbFBlUbWaQXOvkNGxfrl5gZPsB0i2EEU",
            "https://drive.google.com/uc?export=view&id=1UMCSVhtn8bOmJjKyzW_g6gO-ggdJix_I",
            "https://drive.google.com/uc?export=view&id=10enx6CcLkNJYLmKQ8b5GQQtF7y9EgkMB",
            "https://drive.google.com/uc?export=view&id=1IDcOt1rfAC9B6d4mFC49ei3oJFotAaKT",
            "https://drive.google.com/uc?export=view&id=1O5GAvbzMWjknz1_IYe5S46O9ZcaclB4C",
            "https://drive.google.com/uc?export=view&id=1tzebvqEF_sLvwzAe-ENIG8lFwhs-FWGU",
            "https://drive.google.com/uc?export=view&id=1mc-fyWrO3nh0ECSKZCqf4whNTY61etmS",
            "https://drive.google.com/uc?export=view&id=1bYIgdU64EUnn-e4Mq-XNdnhqCT9jGYpZ",
            "https://drive.google.com/uc?export=view&id=1MnPfGhlP8TjKp9XE4y7AEg8TuSKBJYA2",
            "https://drive.google.com/uc?export=view&id=1O5GAvbzMWjknz1_IYe5S46O9ZcaclB4C",
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
                "Kesan": "Kakaknya geulis pisan",  
                "Pesan":"Semangat terus kakak, selalu jadi inspirasi banyak orang ya kak"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tanggerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, Nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "Kakaknya asik dan cantik",  
                "Pesan":"semangat kuliah nya kak, jangan kasih kendor"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150 ",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "Kakaknya cantik, dan suka senyuum",  
                "Pesan":"Semangat terus kakak manis"
            },
            {
                "Nama": "Anisa Dini Amalia",
                "NIM": "121450081",
                "Umur": "21",
                "Asal":"Tanggerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "Kakakny seru",  
                "Pesan":"Sehat selalu kakak"
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
                "Pesan":"jaga semangat ya kak"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Batu Raja, Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "abangnya asik dan baik",  
                "Pesan":"Lancar terus kuliahnya bang"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "Abangnya baik",  
                "Pesan":"jaga semangat ya bang"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Sukabumi, Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka Ikut Tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "Kakaknya seru, dan asik",  
                "Pesan":"Semoga dapet A kakakss cantik"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "Abangnya ramah, baik, asik, dan seru",  
                "Pesan":"Semangat ngaspraknya bang"
            },
            {
                "Nama": "Berliana Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "Kakaknya baik",  
                "Pesan":"Semangat kakak baik"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EKjTXJBKXD3cl1npRr6sgg0lHVkQJNi2",
            "https://drive.google.com/uc?export=view&id=1M2XBlhhpt7-GBQAsX7c-4e5_Z_M3yGra",
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
                "Kesan": "kakaknya intelektual vibes bangett, keren puooll kakaak",  
                "Pesan":"semangats kakak kereen"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "abangnya asik diajak ngobrol",  
                "Pesan":"sehat sehat bang Bintang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1nii36cr-bRy57pz4_05knxzALK1NoBR6",
            "https://drive.google.com/uc?export=view&id=1N8g443FYa4cGiW9ZAlknFqS4RhyOB2bc",
            "https://drive.google.com/uc?export=view&id=1rWo7sUr5aI55Yl7Zc4ocpb_iZLaCPSd7",
            "https://drive.google.com/uc?export=view&id=1y7bs6xC9I7NRxReoOPMD-rTvIKVwkRZo",
            "https://drive.google.com/uc?export=view&id=1wZS7pjkBlCQFZ_ge6SGTo_wPsbDXQpNB",
            "https://drive.google.com/uc?export=view&id=1QKYe2VGtzOTDh1D_t-3sBrXty-VXRk9y",
            "https://drive.google.com/uc?export=view&id=1kGG0FaI8MbMBdrLulFC1tDUDPNuL239B",
            "https://drive.google.com/uc?export=view&id=1LDwU6tjLNk0b7Nfu7QLhv6irf_lSRzGv",
            "https://drive.google.com/uc?export=view&id=1Ai8HdM-TJv0eW234Vhz_zMAoPPDRZfK1",
            "https://drive.google.com/uc?export=view&id=1uwc7BhyPhLHkwtvLqpUsJDMgcymjdubH",
            "https://drive.google.com/uc?export=view&id=1HFF5GtNeN7FSlmSqWmqkl1X1Q5NPj7Yl",
            "https://drive.google.com/uc?export=view&id=1eDAGQ1LSO50TwrHQl-EMAL5M2-IPTazb",
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
                 "Kesan": "abangnya seru deh",  
                "Pesan":"Mending mancing ikan di Pahawang bang mwehehee"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "kakaknya anggunly sekali",  
                "Pesan":"semangat coolyeah nya kakak, lancar selalu yaps"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "abangnya baik",  
                "Pesan":"Semangat ngodingnya bang mwehehe"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "Kakaknya baik",  
                "Pesan":"sehat selalu kak Ranii"
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
                "Pesan":"Mau denger lagu ala bang Rendra"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan" : "Kakaknya bikin terkejoet karena ternyata rumah kita deketan cuma beda blok aja",
                "Pesan" : "Semangat kak salwaa cantik"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "kakaknya inspiratif",  
                "Pesan":"semangat kakak keren"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "Abangnya vibesnya adem banget",  
                "Pesan":"semangat bang"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "Kakaknya anggunly, lembut dan baik sekaly",  
                "Pesan":"semangat kuliahnya kak Meira, semoga A ya kak"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "Kakaknya vibes juga adem",  
                "Pesan":"mangatss kak jangan kasih kendor"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "Abangnya keren",  
                "Pesan":"semangat terus bang"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "Abangnya keren dan asik",  
                "Pesan":"semangat terus bang, jangan kasih kendor"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LSrCOE455OpBlhD26vAzouaQv7U-atkD",
            "https://drive.google.com/uc?export=view&id=1sX4y5Fx9q-cJ6zZM8UQPiAZCYsreoYl1",
            "https://drive.google.com/uc?export=view&id=1xp4ecz_6UF7Dc7e6rukmMvcy4vmUENpj",
            "https://drive.google.com/uc?export=view&id=1L6WGJ0N7f79u8kUKoQ6ASZbYwlOstoYa",
            "https://drive.google.com/uc?export=view&id=1MaBCZoqX3kV7GNgL2eD3K7SfET3KnR8N",
            "https://drive.google.com/uc?export=view&id=1MaBCZoqX3kV7GNgL2eD3K7SfET3KnR8N",
            "https://drive.google.com/uc?export=view&id=11M-l48C1jhxMbGfNW7aGGQ42tU6n9JBT",
            "https://drive.google.com/uc?export=view&id=1JyD6crsWZbAxP3GeEtm3U-Sxxi8jWNbD",
            "https://drive.google.com/uc?export=view&id=1pFUF0KQKRBFyBYMbcTRw3XmG-y1lL4YJ",
            "https://drive.google.com/uc?export=view&id=1tlmeLEPp-2QPfki5ONWmgcUpDHGVw732",
            "https://drive.google.com/uc?export=view&id=1fFVCWetjc85v2E9gqbegklrRQQBhW_PZ",
            "https://drive.google.com/uc?export=view&id=1ai_1HsuXTZb3MTuCUW28TWi_wDej8bYm",
            "https://drive.google.com/uc?export=view&id=1BR3RF2SVyQT6iT0c2uFq3_6owodb20d5",
            "https://drive.google.com/uc?export=view&id=1qnh3bc5C3Zg_f8kkp7VSFfBpR-4YEaZz",
            "https://drive.google.com/uc?export=view&id=1IQlS1WkBXiTygEAVM_owDBi_UFjtg54e",
            "https://drive.google.com/uc?export=view&id=1XLtCIw7pqkp8O15NnE33ae5k-zMhAV-c",
            "https://drive.google.com/uc?export=view&id=1IvT8SUOQSeE7llsz-Mnttl3HhDUENEfI",
            "https://drive.google.com/uc?export=view&id=12KlWc_GBe_Yj10Mxuu0KR-6MKtIWdFeU",
            "https://drive.google.com/uc?export=view&id=1kWjCE8kY3Ihyek1FAXb3-5spxpjaNBhu",
            "https://drive.google.com/uc?export=view&id=1Q5mZ7UCC71vebgI5H1w7dI-LqidYm0YE",
            "https://drive.google.com/uc?export=view&id=1Qz_9PwXvXrSUxXEdgigbD8pol-QlzR9T",
            "https://drive.google.com/uc?export=view&id=1cUO9RwHM3z6IJRPDCi9U3EL-iutOP0eQ",
            "https://drive.google.com/uc?export=view&id=15PSxvZHcIj_8aR0Ya3rTY5uNAn02b9gH",
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
                "Kesan": "Bang Econ keren banget apa lagi kalo lagi ngisi materi",  
                "Pesan":"Tetep keren dan selalu semangat bang"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "Kak Abeth cantiik dan kereeen",  
                "Pesan":"semangat kuliahnya kak Abeth, sukses terus"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "Kak Fifaah cuantiik puoool, kewren pokoknyaa",  
                "Pesan":"Mangats kak Fifah, sukses terus ya kak"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "Kak Allya cantik, apalagi kalo lagi senyum",  
                "Pesan":"Keep smile kak Allya, sehat selalu ya kak"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "Kak Hanum keren dan kece",  
                "Pesan":"Semangat kak Hanum"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                 "Kesan": "Abangnya baik, dan suka menghibur",  
                "Pesan":"Sukses selalu bang"

            },
            {
                "Nama": "Eksanty F. Sugma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "@eksantyfebriana",
                "Kesan": "Kak Eksanty baik sama sabar banget deh suka bantu codingan error di Praktikum ADS",  
                "Pesan":"Semnagat ngaspraknya kak Eksanty, sukses terus kak"
            },
            {
                "Nama": "Oktavia Nurwinda Puspitasari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "Kakaknya baik ",  
                "Pesan":"Sukses selalu kakak"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "Abangnya kereen",  
                "Pesan":"Sukses dan sehat selalu bang"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "Abangnya kereen, baik, dan suka bikin ngakaak",  
                "Pesan":"Jangan pernah hilngkan positif vibes nya baang. Sukses terusss bang"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                 "Kesan": "Abangnya baik",  
                "Pesan":"sehat selalu bang"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "Bang Jo adalah si paling energik kalo udah suporteran bikin tambah seru",  
                "Pesan":"Sukses dan sehat selalu bang Jo"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "Pasti bang Kemas jagooo banget ngodingnya",  
                "Pesan":"Ingpoo tutor ngoding biar ga eror terus dong bang hehehe"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                 "Kesan": "Abangnya kereen",  
                "Pesan":"Sukses dan sehat selalu bang"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "Kakaknya anggunly dan cantik banget",  
                "Pesan":"Semangat kakak, semoga sukses selalu "
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "Kakaknya cantik",  
                "Pesan":"Sehat selalu kak, semnagat kuliahnya"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "Bang Sahid baik dan keren",  
                "Pesan":"Sukses dan sehat selalu bang, semangat teruss"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "Kakak nya energik vibes banget, kereeen puolll",  
                "Pesan":"Semangat kak, sukses terus ya kak"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "Abangnya enjoy, asik diajak ngobrol",  
                "Pesan":"Bang spill dong bang kenapaa bisa dipanggil Ateng, bang" 
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "Abangnya asik",  
                "Pesan":"jangan lupa jaga kesehatan ya bang"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "Kak Jaclin cantiiik banget dan positive vibes",  
                "Pesan":"Semangaaat kaaak, sukses terus yapsss"  
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "Abangnya keren",  
                "Pesan":"Sukses terus bang" 
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "Waah ternyata kakanya kembar, terus vibes kakaknya sama-sama kalem",  
                "Pesan":"Semangaaat kaakak kereen"

            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1BN4CWyDqq__L9eIL8RNcVqU0itYfBUMG",
            "https://drive.google.com/uc?export=view&id=1oJYQHl2KmLYVNvrZenGhZ5uQsQfIKva-",
            "https://drive.google.com/uc?export=view&id=1vYsiw59dRSNCmAvgwSE_IVU9BzBrY6sH",
            "https://drive.google.com/uc?export=view&id=1O5tBFhhENWu2e74T6TGFdBcxbChClGYe",
            "https://drive.google.com/uc?export=view&id=1FzCs90Bu7kMYnDf-hG1lJzuTMB398BR7",
            "https://drive.google.com/uc?export=view&id=1izxoBltqy9tAow4N93ev98ld4T_3io8p",
            "https://drive.google.com/uc?export=view&id=1q92Co5aGkgTK3aWV_h_QNgZNK3XB3zZ7",
            "https://drive.google.com/uc?export=view&id=1pzQEHSnX4UaU543uDn-albwKRNp5Uwfr",
            "https://drive.google.com/uc?export=view&id=1Q4_qbgr7h4A55HxwzACh-D6730AYv5Pu",
            "https://drive.google.com/uc?export=view&id=1maaqax6SVcFzV38sOos9Oz8s0tWm7f0K",
            "https://drive.google.com/uc?export=view&id=1wMh5Hh4gunx0xdqHBOj9AEfW-73aK8iH",
            "https://drive.google.com/uc?export=view&id=1A0tuugPLACbz-r1H_W73MGtJDL7BZ4MT",
            "https://drive.google.com/uc?export=view&id=1ONfOaYDBvA66Kn_dfnQuLe1sQ83jU5m7",
            "https://drive.google.com/uc?export=view&id=1IuMibK2lmWi659veJ_A11ujhUgoffMH2",
            "https://drive.google.com/uc?export=view&id=1EBr8EOFvADMYkYafQ39xO2dlGLhXDU6Z",
            "https://drive.google.com/uc?export=view&id=1vm04DZQYBqK2H82Vk3zFHzptwrbtIrKi",
            "https://drive.google.com/uc?export=view&id=11AnDic8Vv6FObPdGpIwYFz5n99ZC-mxS",
            "https://drive.google.com/uc?export=view&id=1N3w1XVQ1Tx22wi6yFFMMn6Rlxc1BIi6m",
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
                "Kesan": "Abangnya baik",
                "Pesan":"manngats bang"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "kakaknya keren",  
                "Pesan":"sukses terus kak"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "Kakaknya suka ketawaa",  
                "Pesan":"semangat kakak, ceria selau yapss kak"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "kakaknya cantik",  
                "Pesan":"mangatss kuliahnya kakak cantik "
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@esteriars",
                "Kesan": "kakaknya kiyowooo",  
                "Pesan":"cemangat coolyeahnyaaa kakak kiyowoooo macam eonni korea"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "kakaknya imuut deeh",  
                "Pesan":"Sukses terus kakaak imuut"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "kakaknya cantik",  
                "Pesan":"Semangat terus kakak cantik"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "Kakakya cantiik bangett, vibesnya tenang",  
                "Pesan": "semangat ngaspraknya kak, sukses teruss"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "Bang Tobias kereeen dan baik",  
                "Pesan":"Semangat dan sukses terus bang"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "kakaknya keren sekalii",  
                "Pesan":"Semangat terus kakak cantik"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "Abangnya kereen",  
                "Pesan":"Semangat bang"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "Abangnya asik dan kereen",  
                "Pesan": "Sukses terus bang"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                 "Kesan": "kakaknya keren sekalii",  
                "Pesan":"Semangat terus kakak cantik"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "Abangnya kereen",  
                "Pesan":"Semangat bang"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "kakak Izza kereen puoool",  
                "Pesan":"Semangat terus kak Izza cantik"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "Kakaknya maniis banget",  
                "Pesan":"semnagat dan selalu jaga kesehatan ya kak"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "Abangnya kereen",  
                "Pesan":"Semangat teruss bang"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "Kakaknya imuut dan kiyowoooo sekali",  
                "Pesan":"Semangat terus kakak kiyowoo"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1o88WNksnkPt2lfnir7hnrZSZ6rAeakz0",
            "https://drive.google.com/uc?export=view&id=14Wgzb9OEYcpqF9-ODKDpfy6BCLzJiQOW",
            "https://drive.google.com/uc?export=view&id=1PyKgCDgsAWUklfeWTZE5nOEm2kwzE-eR",
            "https://drive.google.com/uc?export=view&id=11yV5dSe6Ri3P1JEHxlaegp_JvHVBDnmn",
            "https://drive.google.com/uc?export=view&id=1f71-R2pQ0PxcWj8vXrle_H2ov4pcQ76p",
            "https://drive.google.com/uc?export=view&id=1GJIUxnTV6l8jvsaSodS_3MT5eC-p1TVH",
            "https://drive.google.com/uc?export=view&id=1jJIoMizvwmAHmL72oc8DjIfnAUCERY52",
            "https://drive.google.com/uc?export=view&id=1iIJPLQIacHM_xLkjMm7c3c3lCDur88zQ",
            "https://drive.google.com/uc?export=view&id=1HKJtCL8j2-T3xXUeXMS1fP-Pa1nuS37I",
            "https://drive.google.com/uc?export=view&id=11uF-1QYuYKm9TJLeOK909oH8IEkJl1N7",
            "https://drive.google.com/uc?export=view&id=1kBgm16KWmKuO2as88PAjVF0OMO2DjvTf",
            "https://drive.google.com/uc?export=view&id=1Y73u3l562zF6Kt7OafBfoHL51V3Jmltn",
            "https://drive.google.com/uc?export=view&id=1DW6RYKvaFxRGzuz8SD-p-EvEeKlAup3n",
            "https://drive.google.com/uc?export=view&id=1A9Z0V9tEy01JO1FXs_4_027g8vngghyX",
            "https://drive.google.com/uc?export=view&id=1uNQKKfIw4OIsNx6xWtOTSMea1ieS_OVs",
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
                "Pesan": "semangat dan sehat selalu bang"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "kakaknya pasti jago masaak",  
                "Pesan": "kapan-kapan penegn nyicipin masakan kakaknyaa"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "abangnya baiiik",  
                "Pesan": "semangat olahrganya bang"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "Abangnya pasti jago ADS",  
                "Pesan": "semangat ngaspraknya bang"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "kakaknya kalem syekali",  
                "Pesan": "semangat kakak manisss"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "abangnya suka bantu codingan eror",  
                "Pesan": "semangat ngaspraknyaaa bang"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "kakaknya cantiik dan manis",  
                "Pesan": "sehat selalu kaka vantik"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "kak Dinda baiiik hati sekali",  
                "Pesan": "sehat dan sukses selalu kak"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "Kakaknya keren poool, apalagi kalo lagi nutorin matdas langsung ngertii",  
                "Pesan": "sukses teruss kak Etaaa Kiyowooo"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "Kak nitaaa ceriaaa dan ramaah sekaliiii",  
                "Pesan": "semangat dan suskses terus kedepannya kak Nitaaaa, selalu ceria ya kak"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "hobi kakaknya out of the box",  
                "Pesan": "semangat membangkitkan bilangan kakak"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "Abangnya kaleem",  
                "Pesan": "sukses pokoknya bang"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "abangnya kereen",  
                "Pesan": "semangat terus bang"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "hobi kakaknya sangaat kewreeen",  
                "Pesan": "semoga dapet A teruss kakakkk rajiiiin, semoga rajinnya nular ke aku hehehe"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "Abangnya keren",  
                "Pesan": "semangat ngegamee nya baang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1jf331iaMVchi20iI-rxY-5nMo1eKEbvS",
            "https://drive.google.com/uc?export=view&id=1fRGOmIZuqsClUIdtSokBq_uWAu8_R4RF",
            "https://drive.google.com/uc?export=view&id=119PmcyS0DALeYTJohEgeqLjTLrr9pFS_",
            "https://drive.google.com/uc?export=view&id=1Tk20B4KyFAFmnWNCjscPkCquYedee_RJ",
            "https://drive.google.com/uc?export=view&id=1VlC4CAGr0WEZMQONM8kR0MfTOZBKTAJs",
            "https://drive.google.com/uc?export=view&id=13m2gtaS4-w0bZEjvXywSQ2ulCUivz26E",
            "https://drive.google.com/uc?export=view&id=1PUU6-LnHFgW2tAePoE1W2qWI_6Id2Jt2",
            "https://drive.google.com/uc?export=view&id=12NAws67YFcGL6vxqfSdZXyFmQYQrBlZc",
            "https://drive.google.com/uc?export=view&id=1k2kZWRd5NLWv3Qnome407SRsAR8xGMoG",
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
                "Kesan": "Abangnya keren parahh",  
                "Pesan":"semangat baang, jangan kasih kendor"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "kakaknya manis deeh",  
                "Pesan":"semangat yaa kakak maniez"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "kakaknya imuut banget",  
                "Pesan":"mangats coolyeah nya kak"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "Abangnya asik",  
                "Pesan":"Semangat baang"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "Abangnya keren, asik banget diajak ngobrol",  
                "Pesan":"Bang tolongiiiin ADS saya yaa bang heheehe"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "Abangnya asik",  
                "Pesan":"semangat terus bang"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
               "Kesan": "Kakaknya baik sekalii",  
                "Pesan":"semangat terus kakak baiiik"
            },
            {
                "Nama": "Nabilah Andika Fitriati",
                "NIM": "121450139",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kedaton",
                "Hobi": "Bikin JJ",
                "Sosmed": "@nabilahanftr",
                "Kesan": "Kakaknya baik suka senyum",  
                "Pesan":"sehat selalu kakak"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "Kakaknya baik suka senyum",  
                "Pesan":"sehat selalu kakak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EzjNqivIEpKq7wWxI2zZxzgJa_Z6CfHJ",
            "https://drive.google.com/uc?export=view&id=1Nqgncne0vZ5QG4ZeCPmB2gRrubMwoQul",
            "https://drive.google.com/uc?export=view&id=10ZbJqK0SgH7V3HopvIqx7MZ4n-XlgFGv",
            "https://drive.google.com/uc?export=view&id=1pU741X3KReVqbuF7-KPTFll5P4GIBIKO",
            "https://drive.google.com/uc?export=view&id=1auD44wZS7yF9fSDfGbvovtdTL8H46VwL",
            "https://drive.google.com/uc?export=view&id=1eYA-_xMrEXNtCtZSWiL5h-_IzOsLgARP",
            "https://drive.google.com/uc?export=view&id=1Vh8VeAgC1kXoBRPCed3FCozDB1brwDRd",
            "https://drive.google.com/uc?export=view&id=1lvuIw1R9BTo-zuyNaKXVnFyhwoU8aESA",
            "https://drive.google.com/uc?export=view&id=1R1BtEIXNAh5I3HeqVGjaQ1uAHEdI9FRd",
            "https://drive.google.com/uc?export=view&id=1rlO-VCQGpR1-i4BX4h9SSoXwpTX2QaMV",
            "https://drive.google.com/uc?export=view&id=16QKzBGEAB5291QfYUazwb_zTpAsEPnMy",
            "https://drive.google.com/uc?export=view&id=1FRaUDkn3out8vjf4HxJAEBte3hGHG-hh",
            "https://drive.google.com/uc?export=view&id=1srhFptlXjbP6NPDhn4nvDGqVK_Ti55M1",
            "https://drive.google.com/uc?export=view&id=1FDY7N_VWvmi07bLZQd4-qQt5QfJ4Zmw0",
            "https://drive.google.com/uc?export=view&id=1l4v7n-Mxju7KHnefLoyfb76-uyz8OYJq",
            "https://drive.google.com/uc?export=view&id=1F3Ao4Q0bsrwBGeeORGHfNjE6-IIsQoWq",
            "https://drive.google.com/uc?export=view&id=1ZZ1bNg2rz0Y8l_rvDzAEyyGxtaI2KzsV",
            "https://drive.google.com/uc?export=view&id=1bS4MMpvaO7S0mcEyiSfAhtIbOXWLn_ve",
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
                "Kesan": "Abangnya keren, tapi aku suka gak ciren kalo abangnya lagi lepas topi",  
                "Pesan":"semangat bang"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "Kakaknya baik dan manis, relate banget sama namanya, kakaknya sangat Elok",  
                "Pesan":"sehat selallu kakak manis"
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "Kakaknya cantiik sekali",  
                "Pesan":"semnagat ngontennya kakak"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "Kakaknya cantik bangeeet",  
                "Pesan":"semangat kakak cantik"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "Kak juju vibes nya penyabar banget",  
                "Pesan":"stay strong kak Juju, sukses terus kak"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "Kak Ciaa vibes nya ceriaa banget, sama kayak outfitnya",  
                "Pesan":"semangat kuliahnya kak ciaaa yang sangaad ceriaa"
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "Kakaknya vibes keibuan sekali, adem kak",  
                "Pesan":"Sukses terus kak, always happy ya kak"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "Kakaknya baik dan cantik",  
                "Pesan":"Sehat selalu kakak cantik"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "Waah ternyata kita satu kabupaten bang",  
                "Pesan":"Semoga hobi nya cepet ketemu ya bang"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "Kakaknya baik",  
                "Pesan":"Semangat ya  kak"
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@gymnn.as",
                "Kesan": "Abangnya asiik diajak ngobrol",  
                "Pesan":"semangat baca komik nya baang heheehe"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "Kakaknya kereeen dan cantiiik",  
                "Pesan":"Semangat ya kakak cantik"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "kakaknya kiyowoooo",  
                "Pesan":"Semangat terus kaak, sukses selalu"
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": "Abangnya baik",  
                "Pesan":"Semangat kuliahnya bang"
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "Bang Abit pastii ngdoning sam gaming nya keren banget ",  
                "Pesan":"Sukses terus bang Abit"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "Abangnya kereen dan baik banget",  
                "Pesan":"Semangat ngasprak nya bang Akmal"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "Abangnya baik, ramah, dan suka ngelucu",  
                "Pesan":"semangat dan sukses terus bang"
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "Kak Khusnun rajiiiin banget, pasti rumahnya kinclong",  
                "Pesan":"Semangat dan sehat selaluu kaak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()