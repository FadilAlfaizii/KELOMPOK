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
            "https://drive.google.com/uc?export=view&id=1dpRKDmh741PWz_S-qkh6ypeLjaQhxidJ",
            "https://drive.google.com/uc?export=view&id=1drPX_amXyvNjbbM71z3VoFEIFhHGb2UU",
            "https://drive.google.com/uc?export=view&id=1dn8MsQcHtd5NQGMqcOJY8u4O9L3vTc6v",
            "https://drive.google.com/uc?export=view&id=1dmrtyjuDwClq22bM-bHDFh8uZRGKJ6qA",
            "https://drive.google.com/uc?export=view&id=1e0ocCj6KemuXLzbi7xlLkMGgdwq32lDj",
            "https://drive.google.com/uc?export=view&id=1e-PuWjxrekEzIXS-7vuFFxMYpXYf4kQ2",
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
                "Nama": "Pandra Insani Putra Azwar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "Abangnya kalem",
                "Pesan":"stay positif bang"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagar Alam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "Kakaknya ramah",  
                "Pesan":"semoga lulus tepat waktu kak!!!"
            },
            {
                "Nama": "Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin Pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "kakaknya keren",  
                "Pesan":"keren terus ya kak"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "kakaknya baik",  
                "Pesan":"baik terus ya kak"
            },
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "Kakak ini ngomongnya halus",  
                "Pesan":"stay with tutur katanya ya kakk!!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1eCHBkZntuvGp1GCjfIgZn_Eh4v0pxmYQ",
            "https://drive.google.com/uc?export=view&id=1eSJSCRcoBQtDYDPE6FL3XCHnVcmdbyVV",
            "https://drive.google.com/uc?export=view&id=1eK2E1Mq98IsGHoUgBdOe6xenzbJulde9",
            "https://drive.google.com/uc?export=view&id=1eexKQ_6CjBUE_BeGamHG5AAx0Hh2NVPq",
            "https://drive.google.com/uc?export=view&id=1efKT8M8k564fuDJ4KotwgdlecbrGPKuj",
            "https://drive.google.com/uc?export=view&id=1eV_RzBs6IKwJM78OfPFocPpvVjiPEAJI",               
            "https://drive.google.com/uc?export=view&id=1eGs0PWgNit7nuS5N_br67Inh3Skryif4",
            "https://drive.google.com/uc?export=view&id=1eUH5QbSmT7uc6rE6wv1EBmB1iVj2sufx",
            "https://drive.google.com/uc?export=view&id=16wt54R668NwuFlXu1hb5U5fwejBOfDv1",
            "https://drive.google.com/uc?export=view&id=1eOmor-sEgwF9ULHYiM_qKs9ilJ_cWSqD",
            "https://drive.google.com/uc?export=view&id=1eVqlbU9kv9nMMx43TJf0_mjjH3cKyX0Y",
            
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
                "Kesan": "gokil abangnya",  
                "Pesan":"alwaysss semangat bangg"
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tangerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "Kakaknya lucu banget",  
                "Pesan":"smoga bisa capai yang ingin dicapai !!!"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "Kakak ini ngomongnya onpoint",  
                "Pesan":"efektif terus ya kakk !!!"
            },
            {
                "Nama": "Anisa Dini Amalia",
                "NIM": "121450081",
                "Umur": "20",
                "Asal":"Tangerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "Kakaknya kasih teladan yang positif",  
                "Pesan":"makasih kak udah sharing-sharing !!!"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "kakak ini auranya baik",  
                "Pesan":"keep up the good work kak !!!"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "asik bener kakaknya",  
                "Pesan":"thankyou kak !!!"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "abangnya suka dngerin the weeknd",  
                "Pesan":"tetap keren bangg"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka ikut tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "Kakak ini keliatannya pinter",  
                "Pesan":"insight dari kakak bakal aku inget terus"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "122450156",
                "Umur": "22",
                "Asal":"Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin musik, nonton film, dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "abangnya cool",  
                "Pesan":"stay cool n be awasome bang"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "abangnya suka ngelawak",  
                "Pesan":"rukun-rukun sama vany bang"
            },
            {
                "Nama": "Berliana Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumbar",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "Kakaknya berwibawa",  
                "Pesan":"stay in a good way kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1n9IByThr4JcspEMHedGrdjWJsNg7ZTgJ",
            "https://drive.google.com/uc?export=view&id=1msMpAr27QfWFPypOnOXZf8fEH33IFGUu",
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
                "Kesan": "kakaknya inspiratif",  
                "Pesan":  "terimakasih sudah menjadi senator kami kak"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "abangnya gila sticker",  
                "Pesan": "terimakasih ilmunya bang, stickernya bagi-bagi"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16kDJDh9Gfm3nsa5LaarPpm2zriLs4M_n",
            "https://drive.google.com/uc?export=view&id=16iS108VIS2HDMvsTy0D6oSOAQ34gAeQ8",
            "https://drive.google.com/uc?export=view&id=16DCswo0clgg4QjMt-ZhwANsGWI4LRobM",
            "https://drive.google.com/uc?export=view&id=166YBk7oxonpI7HZPK2L-jNlnUD_TlcNQ",
            "https://drive.google.com/uc?export=view&id=16nYEcc2-hI0-601QK_TLz4bTr6I18t6G",
            "https://drive.google.com/uc?export=view&id=16sWY4L7Z7Ycda3P2d-UNoEaZFlL6-kl9",
            "https://drive.google.com/uc?export=view&id=16IsK61Nc1bus6LOPUXCd6_CNRpbT55vY",
            "https://drive.google.com/uc?export=view&id=16X4twNlwSEzd2AbrB5uedeLERGNc_7Zl",
            "https://drive.google.com/uc?export=view&id=16jObRuNTZx5ptapbPYU0N12glllGXRD4",
            "https://drive.google.com/uc?export=view&id=16cmpTc5mJUxoiEM7vxlR8o-5WeoDMGGH",
            "https://drive.google.com/uc?export=view&id=16axyFgvyFJOd4ZeA1u-NlG_npA1_bhLn",
            "https://drive.google.com/uc?export=view&id=16RLFmgt_57RZ4td66_q7OwY3JhSnQhwE",
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
                "Kesan":"abangnya confident",  
                "Pesan":"be yourself terus kak"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "kakaknya profesional",  
                "Pesan": "terimakasih atas sesi wawancaranya kak"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "kakaknya pandai ngejelasin sesuatu",  
                "Pesan": "thankyou for the wwc nya kak"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "emang keliatan kya suka denger musik",  
                "Pesan": "stay ramah yaa kak"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "abangnya skena",  
                "Pesan": "keren terus bang rend"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "kakaknya mirip ma temen aku",  
                "Pesan":"keep up ur good energy kak"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "vibe kakaknya positif",  
                "Pesan": "stay with that energy kak"
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "emang keliatan kya jago main bola abangnya",  
                "Pesan": "semangat terus dengan hobinya bang"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "looks like a smart women",  
                "Pesan": "terimmakasih kak udah luangin waktu buat wwc"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "kakaknya humble",  
                "Pesan": "humble terus ya ka"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "kakaknya keliatan rajin ",  
                "Pesan": "smoga lulus cumlaude kak"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "kakaknya looks disiplin",  
                "Pesan": "keep up dengan apa yang ingin diraih kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1o_rO-x1MTxQoeV-C3vVVhn3UVHroHhBp",
            "https://drive.google.com/uc?export=view&id=1oY2FhQaN_NVPC32ASzTtoHuTqHXWWyy_",
            "https://drive.google.com/uc?export=view&id=1nicQZkp7Ql7joIMaddcLjkx_qaqAdIEM",
            "https://drive.google.com/uc?export=view&id=1nlif97uyB_qGkwJ15IXY7NOeuTfr2rk4",
            "https://drive.google.com/uc?export=view&id=1nMRXHs8No8zZ8PsE3p87igopE8alPQSH",
            "https://drive.google.com/uc?export=view&id=1nXp97H0OEEjT6g-NitssrFid7x28oKcp",
            "https://drive.google.com/uc?export=view&id=1nfatkEEEq_4UoeWtWvX2VvnU6LO6cvGF",
            "https://drive.google.com/uc?export=view&id=1n_XDMn6Ex8JruDTk9-ALlMY3sR-3qXFI",
            "https://drive.google.com/uc?export=view&id=1nIC7yiiFO2UySr5JvkjOtAq3uYR68Wt8",
            "https://drive.google.com/uc?export=view&id=1o4xX1MUHsbFNpIWNCYIpl8hz5KeLYG8I",
            "https://drive.google.com/uc?export=view&id=1od2ps8TSH7-WxGVbeFrFJztFizfS8nka",
            "https://drive.google.com/uc?export=view&id=1nyvk1kykaElBiqOJYHF03BeDI2kz78ig",
            "https://drive.google.com/uc?export=view&id=1oAeQLqdpiLVa-U_obOgY7KcQCVxFc5Jc",
            "https://drive.google.com/uc?export=view&id=1odCNRlWLJcBjqOz504e34RLG9DGeu1C7",
            "https://drive.google.com/uc?export=view&id=1nySxYhDSSJn36dq-cpwO0HinK8geCQOe",
            "https://drive.google.com/uc?export=view&id=1nlsOkPgujk11LOZEteStbGVLZi4kmvPl",
            "https://drive.google.com/uc?export=view&id=1o8KwOiA9PdMdcSpPx8gjMEuxRFQUBcZJ",
            "https://drive.google.com/uc?export=view&id=1o8cBwHNRUFYDclIRUpYb-24l20VB8jlH",
            "https://drive.google.com/uc?export=view&id=1oWE84FA09vo3nvWc1OfSMRWav5wPBacH",
            "https://drive.google.com/uc?export=view&id=1oUjFxtxvK737fXmzQIC1oqXe_OrDHRaB",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1oKA8l7Fey30DbAGLLPk-5SD_2RHVlMBK",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1oUSFRrDXYLnzFr4mYmHyV0Z3NhphtGYN",
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
                "Kesan": "bang econ tegas orangnya",  
                "Pesan": "semangat teruss bang econn, makasih atas ilmunya"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "kakaknya ceria",  
                "Pesan": "langgeng sama bang jo ya kak"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "kakaknya mirip urang awak",  
                "Pesan": "terimakasih atas kesabarannya kak"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "kak alya profesional bet",  
                "Pesan": "goodluck kak al"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "kakaknya mirip chindo",  
                "Pesan": "saran kakak ngebantu,  makasih banyak kak"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "abang ini santai namun onpoint",  
                "Pesan":"be awasome terus bang derr"
            },
            {
                "Nama": "Eksanty F. Sugma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "@eksantyfebriana",
                "Kesan": "muka kakaknya familiar",  
                "Pesan": "moga bisa banyak belajar dari kakak kedepannya"
            },
            {
                "Nama": "Oktavia Nurwinda Puspitasari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "kakaknya cermat",  
                "Pesan": "thanks for the knowledge kak"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "abangnya kalem abis",  
                "Pesan": "stay cool terus bang fer"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "terasa kali riaunya",  
                "Pesan":"moga apa yg diusahakan mencapai hasil yang memuaskan bang"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "abangnya rapi",  
                "Pesan": "profesional but still humble keren bang"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "post up nya bagus",  
                "Pesan":"gokil terus bang jo"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "kayanya jago main ml",  
                "Pesan": "ayo basket lagi bang kemaas"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "hobinya teladan bener bang",  
                "Pesan": "semangat belajarnya bang leo"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "cantik kakaknya",  
                "Pesan": "kakak memberikan insight yang sangat berharga"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "wih anak pekanbaru juga ni",  
                "Pesan": "tetep jadi kakak yang humble dan asik ya!"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "jago main gitar sepertinya",  
                "Pesan":"kapan-kapan ngejam bareng bang"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "gaul bet",  
                "Pesan":"semangat basketnya kak moga winner chicken dinner"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "abang ini pandai ngomong",  
                "Pesan": "sukses terus bang ateng"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "abangnya asik kalau cerita pengalaman",  
                "Pesan": "kelas terus bang ged"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "",  
                "Pesan": ""
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "abangnya mririp temen sd ku",  
                "Pesan": "gg terus bang"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "kakaknya ramah lembut",  
                "Pesan":"semoga sukses kakak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1x6IfqcEau0siOxcSPbkYGgOg9_7OWzFR",
            "https://drive.google.com/uc?export=view&id=1wzAliOjqprSd8DM4Jvb8f5D8eJFpjm7l",
            "https://drive.google.com/uc?export=view&id=1wmrV89czHsRtbyLqt_qn2zD2BIOvmFNY",
            "https://drive.google.com/uc?export=view&id=1wqqgjViY5rbKF87RQv4SiVm8VC2OmS5x",
            "https://drive.google.com/uc?export=view&id=1wkKEA1EOAYEfeNLELu0onpQGa-vmWvMV",
            "https://drive.google.com/uc?export=view&id=1wwneN1jZsxaFNOtXopSo3q-dCnXcxGC-",
            "https://drive.google.com/uc?export=view&id=151kwyaiGCQgOFxMvCGnG2AIBkhOGyZfG",
            "https://drive.google.com/uc?export=view&id=1wevk5hnWrdSqSmlyo4dKFPDSCxiyswxu",
            "https://drive.google.com/uc?export=view&id=1wiS4PA-jlK13i3MR7Gp836Y_-_yv83TU",
            "https://drive.google.com/uc?export=view&id=1wtlcVaiCnDM0Cuown_55Qo_MJ202JsLA",
            "https://drive.google.com/uc?export=view&id=1zlEGzMVaON1XTKImuW5-A-lVP8pJeFCM",
            "https://drive.google.com/uc?export=view&id=1wSB9ROBXs6iTnDocTWhogotxXQZpJn89",
            "https://drive.google.com/uc?export=view&id=1x8Wi-_khgfxPHb9POkcSJfZWh5i7UQ-l",
            "https://drive.google.com/uc?export=view&id=1wTC5eSfuMS2P7hlyTwKe5KoRGxwrANzt",
            "https://drive.google.com/uc?export=view&id=1xDG9z4qqvDYHkxfG0TuaxJYSMZKF00eg",
            "https://drive.google.com/uc?export=view&id=1xDF6e71SDPLAYz1D7xWhUCoug5ZzMxoD",
            "https://drive.google.com/uc?export=view&id=1xAVco9Cl5CiQxSg4u-RJ5qP_KPkHUPyq",
            "https://drive.google.com/uc?export=view&id=1wOIGp_F9JqHfWzCnP5MkVmOmDLEuBiUQ",
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
                "Kesan": "seru abangnya",  
                "Pesan": "stay seru bangg"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "kakaknya keliatan kaya bisa dipercaya",  
                "Pesan": "semoga ipk kakak semester ini 4 ya kak"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "kakaknya menghibur",  
                "Pesan":"kebantu sama ilmu yang kakak berikan"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "vibe dari kakaknya ceria",  
                "Pesan":"ceria terus kakk"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@esteriars",
                "Kesan": "ramah bet kakaknya baik",  
                "Pesan":"terimakasih atas keramahannya kak"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "kakak orangnya sabar keliatannya",  
                "Pesan": "murah hati selalu kakak!"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "cakep kakaknya",  
                "Pesan":"makasih udah ngebimbing saat wwc kak"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "keren hobinya",  
                "Pesan": "banyak insight baru yang aku dapat dari kakak, terimakasih kak"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "abang ni tegas orangnya",  
                "Pesan": "jangan potong rambut bang tob"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "fun kakaknya",  
                "Pesan": "makasih atas dukungannya kak"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "abang ini kulbet",  
                "Pesan": "banyak ilmu baru yang aku pelajarin setelah wwc dgn abang, makasih bang"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "hobinya unik",  
                "Pesan": "optimis selalu bang!"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "keren nama kakaknya",  
                "Pesan": "pengen bisa sekeren kakak"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "abang ini jeli orangnya",  
                "Pesan":"terimakasih atas tipsnya bang"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "keliatan seperti orang yang kreatif",  
                "Pesan": "terimakasih atas sikap positifnya kak"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "subhanallah hobinya",  
                "Pesan": "konsisten dengan hobinya kak, terimakasih udah sharing pengalaman kakak saat wwc"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "abangnya baik dan humoris",  
                "Pesan":"gas produktif terus bang"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "kakaknya keliatan kaya orang yang rajin",  
                "Pesan": "thanks kak sharing session saat wwcnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=153-GrEyZ2z29l4luqK1K3VuM9mUaEhB9",
            "https://drive.google.com/uc?export=view&id=1-OFI7kj3EfVzWH_IIU2i8KlATy7t41Ov",
            "https://drive.google.com/uc?export=view&id=1-YbB36IaX2HM4_ouEIYKdy8aMB4lQ-gB",
            "https://drive.google.com/uc?export=view&id=1-in6FhTNAYG6IyT0UTKofK5poyH8LdTb",
            "https://drive.google.com/uc?export=view&id=15E8tYQZ63mYSvv6-BKyyYdsY9vpRJy8_",
            "https://drive.google.com/uc?export=view&id=1-Bfz6YFwVHuyxYftxXIn2eRdqYF-5X74",
            "https://drive.google.com/uc?export=view&id=1qfQoIaU4KlbbzFVz-t-n_t4WzLb42GYs",
            "https://drive.google.com/uc?export=view&id=1-V9LjWFlksm8gSAY9kBk76lAGqFZH1rN",
            "https://drive.google.com/uc?export=view&id=1-cNAp92dJ3Bo2trDr8OwQKOtjS1ocSXI",
            "https://drive.google.com/uc?export=view&id=1-9XMsZNRrYyQ5sNrSZTHb7q9PFp4MJgj",
            "https://drive.google.com/uc?export=view&id=1zu2ccL0bUhJcTZEP0LdhDQtXV3rMGQBv",
            "https://drive.google.com/uc?export=view&id=1-AaQs4GkibG6sI1dS8_BL4E7RhyRywba",
            "https://drive.google.com/uc?export=view&id=1-DBzhnwZmkR39jT5vkLwOyn-z0V7v4h8",
            "https://drive.google.com/uc?export=view&id=1-VdAk_NZJj4EWfAWbGmpc6t-dDS69ro6",
            "https://drive.google.com/uc?export=view&id=1--tWNsm6i01LxSqzLMD0XP-MR4iluVX8",
            
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
                "Kesan": "pintar abnagnya",  
                "Pesan": "stay pintar bang rafi"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "pemahaman kakaknya bagus",  
                "Pesan": "semangat  terus  kak, semoga berkah kuliahnya"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "abangnya berwibawa",  
                "Pesan": "abang memberikan insight yang bermanfaat saat wwc"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "abang asprak ads",  
                "Pesan": "bang tolong ads saya bang"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "kakaknya mirip kak andini",  
                "Pesan": "gasin terus kak"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "abangnya berdedikasi",  
                "Pesan": "ajarin ml bang"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "pemikiran kakaknya kritis dan strategis",  
                "Pesan": "ajarin ngeresume webinar kak"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "kakaknya lucu, fun dan membangun",  
                "Pesan": "semangat baca journal bu Mikanya kak"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "mirip razka kakaknya",  
                "Pesan": "semangat kak review journal bu Mikanya"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "kakaknya ceria, pj tugas kelompok saya",  
                "Pesan": "makasih kak nit"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "kakaknya semangat dan berpikiran terbuka",  
                "Pesan": "goodluck ngebangkitin bilangannya kak"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "gapaham sama hobi abangnya",  
                "Pesan": "semangat bang menjalani hobinya"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "kakaknya gigih dan sopan",  
                "Pesan": "semangat ngoding wisatanya bang"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "kakaknya smart n kind",  
                "Pesan": "semangat kak review journalnya"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "abangnya ga kya orang yang suka main game",  
                "Pesan": "semoga win terus ngegamenya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15ixa5Z71zGfFMrhqlHKKC13EEmjMS5GQ",
            "https://drive.google.com/uc?export=view&id=15pwG7EE8wObq2vKy7GcI0zFKLp9qdVsa",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=15kR9wh6m0Y1I---He10gmgTElBrTeqIK",
            "https://drive.google.com/uc?export=view&id=15bLxFoxKkBmzGOvR4U8KSSFh-WvF7f1p",
            "https://drive.google.com/uc?export=view&id=15nORbPF_GJ2nC1ls98SKwE80RPCkyNSG",
            "https://drive.google.com/uc?export=view&id=15cFZ899h4t3zB6ua6BHtLq-kW68ACmpr",
            "https://drive.google.com/uc?export=view&id=15tNOuwoZ65706Re2Kcu9Z12mAhLt-czI",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
        ]
        data_list = [
            {
                "Nama": "Andrian Agustinus Lumban Gaol",
                "NIM": "121450090",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Belwis",
                "Hobi": "Nyari hobi",
                "Sosmed": "@andrianlgaol",
                "Kesan": "banyak bet funfactnya",  
                "Pesan":"inspiratif terus bang"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "baik kakaknya ramah",  
                "Pesan":"jangan cape jadi orang baik ya kak"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "ga nyangka sama umurnya",  
                "Pesan":"makasih udah sharing ilmu bermanfaat saat wwc kak"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "keren abangnya",  
                "Pesan":"semoga sukses bang ahmad"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "abang ini keliatan aktif orangnya",  
                "Pesan":"turunin harga sticker bangg wkwk, terimakasih atas ilmu yang abg berikan"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "abang capo",  
                "Pesan":"semoga nice terus bang"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "kakaknya baik banget",  
                "Pesan":"terimakasih atas kebaikannya kak"
            },
            {
                "Nama": "Nabilah Andika Fitriati",
                "NIM": "121450139",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kedaton",
                "Hobi": "Bikin JJ",
                "Sosmed": "@nabilahanftr",
                "Kesan": "kakaknya ramah dan ceria orangnya",  
                "Pesan":"thanks for your kindness kak"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "kakaknya humble dan bersemangat orangnya",  
                "Pesan":"be humble terus kak n keep ur spirit up"
            }            
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17RbFN6NgI-9igRcQFrKzR26EaG4esXNc",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=17YtIeVdx8qqe0mPEd53hRMSJt5uovr6p",
            "https://drive.google.com/uc?export=view&id=17GdLS9v_aKIpK3l2vA0Pecq_JcCZpInD",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=17TUxaKDmJXKT2Ip_N5Y4HVvgq6W5Hoip",
            "https://drive.google.com/uc?export=view&id=1tBo0l5pxH4N8o3rNk-Iupet4c12OATy_",
            "https://drive.google.com/uc?export=view&id=17ejCwSPPNgTprxdqcOE234Tq5Z0eAqNL",
            "https://drive.google.com/uc?export=view&id=176EDctjv70TXgf729ZxdvnESd_1Q2wkm",
            "https://drive.google.com/uc?export=view&id=17avoCVz8x0WfyuaMBj2k2NdgSQG2gUwB",
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
                "Kesan": "abang keren, gokil abis",  
                "Pesan": "makasih atas ilmu-ilmu barunya bang, sangat bermanfaat"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "kakaknya inspiratif",  
                "Pesan": "ajarin ngedit kak"
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "cermat dan profesional",  
                "Pesan": "insight baru yang kakak berikan helpful bener"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "terampil kakaknya",  
                "Pesan": "sehat selalu kakak"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "keliatan kaya orang yang suka belajar kakaknya",  
                "Pesan": "senang bisa ngobrol sama kakak"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "baik kakaknya ramah, confident dan positif",  
                "Pesan": "semangat terus kak cia!"
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "mantep juga hobi kakak ini",  
                "Pesan": "ayo adu skill sama adek saya kak hobinya juga sama"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "cerdas kakaknya",  
                "Pesan": "ajarin ngoding kak"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "bisa gitu hobinya",  
                "Pesan": "makasih udah sharing ilmu dan menghibur saat wwc bang"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": ";Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "keliatan tenang orangnya kakak ini ",  
                "Pesan": "makasih kak udah antusias saat menanggapi pertanyaan saat wwc"
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@gymnn.as",
                "Kesan": "humoris betul",  
                "Pesan": "minta rekom komik bang"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "fun, seru, asik kakaknya",  
                "Pesan": "salut ama kakak"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "kakaknya supportif",  
                "Pesan": "ada-ada saja hobi kakaknya, keren"
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": "abang ini keliatan jago main game",  
                "Pesan": "makasih bg udah ngeshare knowledgenya saat wwc "
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "pro coding",  
                "Pesan": "ajarin ngoding bang abit"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "baik abangnya humble",  
                "Pesan": "stay humble bang akmal"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "energetic orangnya",  
                "Pesan": "stay semangat bang mawan"
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "lucu kakaknya",  
                "Pesan": "ajarin r kak khusnun"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()