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
            "https://drive.google.com/uc?export=view&id=1NvXGxe-2OSUxFs_BbnOd7WrwDrTZrXqv",
            "https://drive.google.com/uc?export=view&id=1NsclPB9SREGm93gYcB6eA4czwVahhH7Y", # Ini Benerin ya wulan
            "https://drive.google.com/uc?export=view&id=1NkzsV4G7Ql5gnPZwmnT3Mb7fYwOejrJ7",
            "https://drive.google.com/uc?export=view&id=1NsV2p1i7nhJoqZQD8JaadNzhB80Xkrzt",
            "https://drive.google.com/uc?export=view&id=1dLTAugWvRdrYGVR8eUPjiRwxqznfpCVd",
            "https://drive.google.com/uc?export=view&id=1NoY6sQLphWt0llpOAI-GiZ67eLrkfSnl",
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
                "Kesan": "Abang nya keren amatt, mengayomi sekalii😎👌🔥👏",  
                "Pesan":"Suksess terus bangg, semangat mengemban tugasnya"
            },
            {
                "Nama": "Pandra Insani Putra Azwar",
                "NIM": "121450137",
                "Umur": "21",
                "Asal":"Lampung Utara",
                "Alamat": "Sukarame",
                "Hobi": "Main gitar",
                "Sosmed": "@pndrinsani27",
                "Kesan": "Abangnya baik, asikk, tau banyak drakor ( ◡̀_◡́)ᕤ ",  
                "Pesan":"Abang hebat, terus maju dan jangan pernah ragu sama diri sendiri!"
            },
            {
                "Nama": "Meliza Wulandari",
                "NIM": "121450065",
                "Umur": "20",
                "Asal":"Pagaralam",
                "Alamat": "Kotabaru",
                "Hobi": "Nonton Drakor",
                "Sosmed": "@wulandarimeliza",
                "Kesan": "Kakaknya seru, suasananya juga enak banget ˚ʚ💗ɞ˚ ",  
                "Pesan":"Semangat terus kak, sukses buat semua yang kakak kerjain!"
            },
            {
                "Nama": " Putri Maulida Chairani",
                "NIM": "121450050",
                "Umur": "21",
                "Asal":"Payakumbuh, Sumbar",
                "Alamat": "Nangka 4",
                "Hobi": "Dengerin pandra main gitar",
                "Sosmed": "@ptrimaulidas_",
                "Kesan": "Kakaknya humble, enak diajak ngobrol💕",  
                "Pesan":"Semangat terus ya kak, yakin deh kakak bakal sukses!"
            },
            {
                "Nama": "Hartiti Fadilah",
                "NIM": "121450031",
                "Umur": "21",
                "Asal":"Palembang",
                "Alamat": "Pemda",
                "Hobi": "Nyanyi",
                "Sosmed": "@hrtfdlh",
                "Kesan": "Kakak nya baikk, ramah kalii Kakak ini, asikヾ( ˃ᴗ˂ )◞ • *✰",  
                "Pesan":"Sukses terus kaa, semangat kuliahnyaa !!!"# 1
            },
            {
                "Nama": "Nadilla Andhara Putri",
                "NIM": "121450003",
                "Umur": "21",
                "Asal":"Metro",
                "Alamat": "Kotabaru",
                "Hobi": "Membaca",
                "Sosmed": "@nadilaandr26",
                "Kesan": "Kakak ini baik, asik, dan seruu💐🌺",  
                "Pesan":"Selalu semangat kak, sukses terus di langkah ke depan!!"# 1
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RDyRjyzvKbY2ohIng7WoTehlqqOtCt78",
            "https://drive.google.com/uc?export=view&id=1RR4QNOx_1BxIc0XWNUiPvKMO4gu7UBlz",
            "https://drive.google.com/uc?export=view&id=1RFjWvnPvuurdrvx-uMOLnoP-uKfsaBpk",
            "https://drive.google.com/uc?export=view&id=1RNyqmzpuvXJs9tAous5t4WsRq5XCb6vd",
            "https://drive.google.com/uc?export=view&id=1RWRXdMqHLFqFK6mzN6ImvNp1T7QpYri0",
            "https://drive.google.com/uc?export=view&id=1QqLoc1bS0kKHm9YXhD4JfxCwyER9q3st",
            "https://drive.google.com/uc?export=view&id=1R3D6hefxerkIrQM0FYKvSFpfF1KxQvv1",
            "https://drive.google.com/uc?export=view&id=1RE4fj0WY8PYjg7qPTeEcqjUd07yxbyZQ",
            "https://drive.google.com/uc?export=view&id=1eruVX0LRe3yW2A9O2xsJ4_GgqN7C-bJ2",
            "https://drive.google.com/uc?export=view&id=1RF0xWBv2-hwAi3Z8oc75VXiEas-qPM7T",
            "https://drive.google.com/uc?export=view&id=1QpeYzhzCWD2AeAHdL9rvyvdXsaf1b4sC",
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
                "Kesan": "Kakak asik banget, bikin suasana jadi nyaman ⸜(˃.˂)⸝♡",  
                "Pesan":"Keep going, kak! Kaka pasti bisa mencapai semua target di kuliah dan pekerjaan."
            },
            {
                "Nama": "Annisa Cahyani Surya",
                "NIM": "121450114",
                "Umur": "21",
                "Asal":"Tanggerang Selatan",
                "Alamat": "Way Huwi",
                "Hobi": "Membaca, Nonton",
                "Sosmed": "@annisacahyanisurya",
                "Kesan": "Kakaknya asyik, obrolan jadi seru(੭˃ᴗ˂)੭",  
                "Pesan":"Sukses nunggu di depan, terus semangat kaka!"
            },
            {
                "Nama": "Wulan Sabina",
                "NIM": "121450150 ",
                "Umur": "21",
                "Asal":"Medan",
                "Alamat": "Raden Saleh",
                "Hobi": "Nonton drakor",
                "Sosmed": "@wlnsbn0",
                "Kesan": "Kakaknya inspiratif, bikin ngobrol jadi makin menyenangkan❤️❤️",  
                "Pesan":"Tetap optimis kak, setiap usaha pasti ada hasilnya!"
            },
            {
                "Nama": "Anisa Dini Amalia",
                "NIM": "121450081",
                "Umur": "21",
                "Asal":"Tanggerang",
                "Alamat": "Jati Agung",
                "Hobi": "Nonton Dracin",
                "Sosmed": "@anisadini10",
                "Kesan": "Kakak bikin suasana jadi lebih chill🌻",  
                "Pesan":"Semoga hari kaka selalu cerah!"
            },
            {
                "Nama": "Renisha Putri Giani",
                "NIM": "122450079",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Denger lagu",
                "Sosmed": "@fleurnsh",
                "Kesan": "Kakak keren, obrolannya ringan dan seru💕",  
                "Pesan":"Keep going, kak! Kamu pasti bisa!"
            },
            {
                "Nama": "Feryadi Yulius",
                "NIM": "122450087",
                "Umur": "20",
                "Asal":"Batu Raja, Sumsel",
                "Alamat": "Way Kandis",
                "Hobi": "Baca buku",
                "Sosmed": "@fer_yulius",
                "Kesan": "Abangnya humble, obrolan jadi enak😎👌🔥",  
                "Pesan":"Semangat kuliahnya bangg, sukses teruss"
            },
            {
                "Nama": "Mirzan Yusuf Rabbani",
                "NIM": "122450118",
                "Umur": "20",
                "Asal":"Jakarta",
                "Alamat": "Korpri",
                "Hobi": "Main kucing",
                "Sosmed": "@myrrinn",
                "Kesan": "Abangnya cool skalii bro👏",  
                "Pesan":"Semoga kuliah dan semua pekerjaannya lancar, bang!"
            },
            {
                "Nama": "Dhea Amelia Putri",
                "NIM": "122450004",
                "Umur": "20",
                "Asal":"Sukabumi, Jabar",
                "Alamat": "Natar",
                "Hobi": "Suka Ikut Tes SKD",
                "Sosmed": "@dhea_wedding",
                "Kesan": "Kakaknya lucu, asyik, seru ngobrol sama kakaknya🫶🏻",  
                "Pesan":"Terus jalani kuliah dan pekerjaan dengan semangat, kak! Hasil yang baik pasti menunggu!"
            },
            {
                "Nama": "Muhammad Fahrul Aditya",
                "NIM": "121450156",
                "Umur": "22",
                "Asal":"Surakarta, Jateng",
                "Alamat": "Pahoman",
                "Hobi": "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "Sosmed": "@fhrul.pdf",
                "Kesan": "Abangnya keren, baik, dan ramahh👍",  
                "Pesan":"Semangat bang kuliah nyaa"
            },
            {
                "Nama": "Jeremia Susanto",
                "NIM": "122450022",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Marah-marah",
                "Sosmed": "@jeremia_s_",
                "Kesan": "Abangnya asik, pembawaannya seru skalii(^▽^)👍",  
                "Pesan":"Semoga segala usahanya membuahkan hasil yang diinginkan, semangat bangg"
            },
            {
                "Nama": "Berliana Enda Putri",
                "NIM": "122450065",
                "Umur": "21",
                "Asal":"Sumatera Barat",
                "Alamat": "Way Huwi",
                "Hobi": "Main game",
                "Sosmed": "@berlyyanda",
                "Kesan": "Kakak nya cakep, baik, dan seru💗",  
                "Pesan":"Semangat kaka cantikk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1N_kn4kOGfYs0w0ALceJbSIJ9DrPQzItP",
            "https://drive.google.com/uc?export=view&id=1NZErL1Fj6VdiBQG_ylw9l3uK50Vpwu0V",
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
                "Kesan": "Kakaknya baik dan humble🌞💖",  
                "Pesan":  "Semangat kak kuliahnyaa, lancar segala urusannyaa"
            },
            {
                "Nama": "Rian Bintang Wijaya",
                "NIM": "122450094",
                "Umur": "20",
                "Asal":"Palembang",
                "Alamat": "Kota Baru",
                "Hobi": "Dengerin Kak Luthfi nyanyi",
                "Sosmed": "@bintangtwinkle",
                "Kesan": "Abangnya baik dan sangat mengayomi👍⭐",  
                "Pesan": "Semangat dan sukses terus bangg!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen Internal":
    def Departemen_Internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PbD8aY8XGJxfZ2wX92-3SLdiOJJ5yrgu",
            "https://drive.google.com/uc?export=view&id=1PJ4P7DVAN6WQFiW6LakOJwcjKfAf0Pz-",
            "https://drive.google.com/uc?export=view&id=1Pc5uBax3UJGJ4Lt4byfC_IRdXmnS5oVb",
            "https://drive.google.com/uc?export=view&id=1Pd5g1KyT-O19chRxBo-U3CNssANZ3iv1",
            "https://drive.google.com/uc?export=view&id=1P6WFuI80Ros0Dr0kPh-19nBNwz3cjiZH",
            "https://drive.google.com/uc?export=view&id=1PcwlfTJKCH7OYqQT5RIZrXCVCXj01HRn",
            "https://drive.google.com/uc?export=view&id=1Ph5w83IljikUVnYAmaO3LfuFg5Gp9ytk",
            "https://drive.google.com/uc?export=view&id=1P8ZfFIKIZa42f3WWw3vTX1q6ocIXUTOX",
            "https://drive.google.com/uc?export=view&id=1PUEUdAo1ujY34V9AmiQN_h34YM6CE22V",
            "https://drive.google.com/uc?export=view&id=1P6xMadS-qxqC3DWKYk7JElm_26bCwAoC",
            "https://drive.google.com/uc?export=view&id=1PKaZaVkMcCZvSSe9ls111RJB93lE2LEX",
            "https://drive.google.com/uc?export=view&id=1PYgRbZ0tMHmlHOk8f25qjZHAD_UofeF5",
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
                "Kesan": "Abangnya baik, seru, asik diajak ngobrol😎👌🔥",  
                "Pesan":"Semangat terus bangg, semoga suksek untuk kedepannyaa, segala urusannya dipermudahh"
            },
            {
                "Nama": "Catherine Firdhasari Maulina Sinaga",
                "NIM": "121450072",
                "Umur": "20",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Baca Novel",
                "Sosmed": "@cathrine.sinagaa",
                "Kesan": "Kakaknya sangat positive vibes🌸💖",  
                "Pesan": "Semangat kuliahnya kakaa, semoga apa yang kakak kerjakan membawa kearah yang baik"
            },
            {
                "Nama": "M. Akbar Resdika",
                "NIM": "121450066",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan dalam, untung",
                "Hobi": "Ngoding Dari gpt",
                "Sosmed": "@akbar_resdika",
                "Kesan": "Abangnya baik dan asik👍",  
                "Pesan": "Semangat kuliahnya bangg!!"
            },
            {
                "Nama": "Rani Puspita Sari",
                "NIM": "122450030",
                "Umur": "20",
                "Asal": "Metro",
                "Alamat": "Rajabasa",
                "Hobi": "Denger Musik",
                "Sosmed": "@ranipuny2",
                "Kesan": "Kakaknya baik dan cantik🌷",  
                "Pesan": "Semangat kuliahnya ka, sukses selalu"
            },
            {
                "Nama": "Rendra Eka Prayoga",
                "NIM": "122450112",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "jl. Lapas Raya",
                "Hobi": "Bikin Lagu",
                "Sosmed": "@rendra.epr",
                "Kesan": "Abangnya komunikatif dan sangat menginspirasi👍👏",  
                "Pesan": "Semangat kuliahnya bang, lancar jayaa"
            },
            {
                "Nama": "Salwa Farhanatussaidah",
                "NIM": "122450055",
                "Umur": "20",
                "Asal": "Pessawaran",
                "Alamat": "Airan",
                "Hobi": "Nonton",
                "Sosmed": "@slwafhn_694",
                "Kesan": "Kakaknya baik dan sangat mengayomi💗",  
                "Pesan":"Semangat kuliahnya kakakk, sehat selalu yaa"
            },
            {
                "Nama": "Renta Siahaan",
                "NIM": "122450077",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Gerbang Barat",
                "Hobi": "mancing Keributan",
                "Sosmed": "@renta.shn",
                "Kesan": "Kakak orang yang penuh energi positif dan asik diajak ngobrol(๑>◡<๑)",  
                "Pesan": "Semangat terus kuliahnya kakk, sehat-sehat, semoga tiap hari dapat bergembiraa "
            },
            {
                "Nama": "Ari Sigit",
                "NIM": "121450069",
                "Umur": "23",
                "Asal": "Lampung Barat",
                "Alamat": "Labuhan Ratu",
                "Hobi": "Futsal",
                "Sosmed": "@ari_sigit12",
                "Kesan": "Abangnya baik dan sangat mengayomi👍😊",  
                "Pesan": "Semangat kuliahnya bangg,, sukses lancar jaya"
            },
            {
                "Nama": "Meira Listyaningrum",
                "NIM": "122450011",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Airan",
                "Hobi": "Membaca",
                "Sosmed": "@meiralsty_",
                "Kesan": "Kakanya lucu nan cantikㅤ♡ ",  
                "Pesan": "Selalu semangat ya kakk, semoga segala urusannya dimudahkann"
            },
            {
                "Nama": "Azizah Kusumah Putri",
                "NIM": "122450068",
                "Umur": "21",
                "Asal": "Lampung Selatan",
                "Alamat": "Natar",
                "Hobi": "Berkebun",
                "Sosmed": "azizahksmh15",
                "Kesan": "Kakak baik hati💐",  
                "Pesan": "Semangat kuliahnya kakk, sukses selalu yaa"
            },
            {
                "Nama": "Rendi Alexander Hutagalung",
                "NIM": "122450057",
                "Umur": "20",
                "Asal": "Tanggerang",
                "Alamat": "Belwis",
                "Hobi": "Nyanyi",
                "Sosmed": "@rexanderr",
                "Kesan": "Abangnya baik, tidak pemarah, dan tidak sombong👍👏",  
                "Pesan": "Semangat kuliahnya bang, sehat selalu, sukses terus!"
            },
            {
                "Nama": "Josua Panggabean",
                "NIM": "122450061",
                "Umur": "21",
                "Asal": "Sumatera Utara",
                "Alamat": "Griya Kost",
                "Hobi": "Nonton Film",
                "Sosmed": "@josuapanggabean16_",
                "Kesan": "Abangnya baik dan sangat baik👍",  
                "Pesan": "Semanagat ya bang kuliahnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Internal()

elif menu == "Departemen PSDA":
    def Departemen_PSDA():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1X5kFKiBNXnZDShPmE89oryTw9xE1rn5t",
            "https://drive.google.com/uc?export=view&id=1XWMd5O_--n8bf_798ax4W7FM4S-kfop1",
            "https://drive.google.com/uc?export=view&id=1XOlax2jXj_LZLzDKjCbsfTZvIO6IyJUA",
            "https://drive.google.com/uc?export=view&id=1XKzr4g1cADB8iTwcpGGxDQ6fdC2kjuMI",
            "https://drive.google.com/uc?export=view&id=1XPEUtiBAy2XOiI0DsUqC01-zslCACU0K",
            "https://drive.google.com/uc?export=view&id=1XRa4IeP1kL1AU7pt4v9lDZpQRNuQRLhq",
            "https://drive.google.com/uc?export=view&id=1XSaNH5LmvwI_JPaFITw06VzGETyWVdtB",
            "https://drive.google.com/uc?export=view&id=1XL39a_geBqrRD5jQ4wUibIZkkr9eF23c",
            "https://drive.google.com/uc?export=view&id=1XOXJrz_g_5HynC1tOLXOzxilpBapLD-g",
            "https://drive.google.com/uc?export=view&id=1XgDoddXzQWIINfkM58MRRpokBLcfK0Ya",
            "https://drive.google.com/uc?export=view&id=1XdBDkqI2DBpmLxwGf2h_bWuvsG0ZsH-i",
            "https://drive.google.com/uc?export=view&id=1XXug68vZwY8nbDYjZc-X2TwaOZeKp2j_",
            "https://drive.google.com/uc?export=view&id=1XbeadW9DEXNHgb6ruKMWX40-Pz9NV34J",
            "https://drive.google.com/uc?export=view&id=1XZmdRnj9BRwjW1sbK_3ocd0JYcQ4rvxo",
            "https://drive.google.com/uc?export=view&id=1XfPpCmwt_pmwQZwWJYjEZEZQNt9FjdYP",
            "https://drive.google.com/uc?export=view&id=1XeDBOxlb1RwK1q80ax24max4CNpL6Exu",
            "https://drive.google.com/uc?export=view&id=1XYdj-0y4THP8U4lzP7xspN71TszIUwlT",
            "https://drive.google.com/uc?export=view&id=1X_vA5Bc_5wYicpu726D_amtKeY9F2eCk",
            "https://drive.google.com/uc?export=view&id=1XIRQ8_icvYzQCawqtX92x1V5rfp4WnD6",
            "https://drive.google.com/uc?export=view&id=1XF49Vk4bk3EZ0y5wZdLMS0bwJ6H9yd4H",
            "https://drive.google.com/uc?export=view&id=1ajK9y5pPU96ZZUs40y9OeRnA60FTgPjH",
            "https://drive.google.com/uc?export=view&id=1XEC3Q4vZV1CZDXujNJqF4UuRZNq93dXH",
            "https://drive.google.com/uc?export=view&id=1XCFWfY6StyhRA0R-tjenIAlREqDBkxrN",
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
                "Kesan": "Abangnya bijak dan sangat berpengalaman, memberikan banyak masukan berharga😎👌🔥",  
                "Pesan": "Semangat ya bang kuliahnyaa, semoga segala yang dikerjakan lancar jaya"
            },
            {
                "Nama": "Elisabeth Claudia",
                "NIM": "122450123",
                "Umur": "18",
                "Asal": "Pekanbaru",
                "Alamat": "Sukarame",
                "Hobi": "Memancing Keributan",
                "Sosmed": "@celisabethh_",
                "Kesan": "Kakak cantik, cutipie, seru, dan asik🌞💖",  
                "Pesan": "Semangat kak kuliahnyaa, sehat selalu, tetap ceriaa"
            },
            {
                "Nama": "Nisrina Nur Afifah",
                "NIM": "122450052",
                "Umur": "19",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nyender dibahu Allya",
                "Sosmed": "@afifahhnsrn",
                "Kesan": "Kakaknya cantik dan baik dan ramah juga(*ᴗˬᴗ)ꕤ*.ﾟ",  
                "Pesan": "Semangat kak, semoga segala usahanya membuahkan hasil sesuai dengan yang diinginkan"
            },
            {
                "Nama": "Allya Nurul Islami Pasha",
                "NIM": "122450033",
                "Umur": "20",
                "Asal": "Sumatera barat",
                "Alamat": "Kemiling",
                "Hobi": "Makan ayam kalasan warboy",
                "Sosmed": "@allyaislami_",
                "Kesan": "Kakak tegas tapi tetap sangat mendukung dan baik ε(´•᎑•`)っ 💕",  
                "Pesan": "Semangat kuliahnya kakk, sehat selalu ya kakk!!"
            },
            {
                "Nama": "Farahanum Afifah Ardiansyah",
                "NIM": "122450056",
                "Umur": "20",
                "Asal": "Padang",
                "Alamat": "Sukarame",
                "Hobi": "Gangguin Allya",
                "Sosmed": "@farahanumafifahh",
                "Kesan": "Kakaknya ramah dan baikk🌸",  
                "Pesan": "Semangat kuliahnya kakk, suksess"
            },
            {
                "Nama": "M. Deriansyah Okutra",
                "NIM": "122450101",
                "Umur": "19",
                "Asal": "Kayuagung",
                "Alamat": "Pagaralam, Kedaton",
                "Hobi": "Push rank tapi menang",
                "Sosmed": "@dransyh_",
                "Kesan": "Abangnya baik dan asik👍👏",  
                "Pesan":"Semangat bang kuliahnyaa, sukses lancar jayaa"
            },
            {
                "Nama": "Eksanty F. Sugma Islamiaty",
                "NIM": "122450001",
                "Umur": "20",
                "Asal": "Kebon Jeruk, Jakarta Barat",
                "Alamat": "Pulau Damar",
                "Hobi": "Berkebun",
                "Sosmed": "@eksantyfebriana",
                "Kesan": "Kakaknya cakep, pasti jop(jajaran orang pintar)😎⭐",  
                "Pesan": "Semangat kuliahnya kakk, semoga segala urusannya dipermudah"
            },
            {
                "Nama": "Oktavia Nurwinda Puspitasari",
                "NIM": "122450041",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Way Huwi",
                "Hobi": "Ngeliatin Tingkah Orang",
                "Sosmed": "@_oktavianrwnda_",
                "Kesan": "Kakanya baik dan kalemm🪻",  
                "Pesan": "semangat kaka kuliahnyaaa, semoga segala yang dikerjakan bermanfaat untuk kedepannya"
            },
            {
                "Nama": "Ferdy Kevin Naibaho",
                "NIM": "122450107",
                "Umur": "20",
                "Asal": "Medan",
                "Alamat": "jl. Pangeran Senopati Raya",
                "Hobi": "Futsal",
                "Sosmed": "@ferdy_kevin",
                "Kesan": "Abangnya seperti pendiam, tapi abangnya baik👍😊",  
                "Pesan": "Semangat ya bang kuliahnya, sukses!"
            },
            {
                "Nama": "Deyvan Loxefal",
                "NIM": "121450148",
                "Umur": "21",
                "Asal": "Duri, Riau",
                "Alamat": "Kobam",
                "Hobi": "Balap Keong",
                "Sosmed": "@depanloo",
                "Kesan": "Abangnya lucu, asik, seru diajak ngobrol👏😎👌",  
                "Pesan":"Semangat bang kuliahnyaa!!"
            },
            {
                "Nama": "Ibnu Farhan Al-Ghifari",
                "NIM": "121450121",
                "Umur": "21",
                "Asal": "Kerinci, Jambi",
                "Alamat": "Kobam",
                "Hobi": "Menonton, Bermain Game",
                "Sosmed": "@al_ghifari032",
                "Kesan": "Abangnya baik dan juga ramah👍",  
                "Pesan": "Semangat kuliahnya banggg!!"
            },
            {
                "Nama": "Johannes Krisjon Silitonga",
                "NIM": "122450043",
                "Umur": "19",
                "Asal": "Tanggerang",
                "Alamat": "jl. Lapas",
                "Hobi": "Memuji Tuhan",
                "Sosmed": "@johanneskrisjnnn",
                "Kesan": "Abangnya baik dan asik diajak ngobrol😎🔥",  
                "Pesan":"Semangat kuliahnya bangg, semoga segala urusannya dipermudahh"
            },
            {
                "Nama": "Kemas Veriandra Ramadhan",
                "NIM": "122450016",
                "Umur": "19",
                "Asal": "Bekasi",
                "Alamat": "Kojo golf asri",
                "Hobi": "ngeprint(Hello dunia)",
                "Sosmed": "@kemasverii",
                "Kesan": "Abangnya kerenn, pasti jop jugaa👍👌",  
                "Pesan": "Semangat kuliahnya bangg, sehat selalu, dan sukses lancar jayaa"
            },
            {
                "Nama": "Leonard Andreas Napitupulu",
                "NIM": "121450153",
                "Umur": "21",
                "Asal": "Medan",
                "Alamat": "Kobam",
                "Hobi": "Belajar",
                "Sosmed": "@lnrd.__",
                "Kesan": "Abangnya baik, ramah jugaa👍",  
                "Pesan": "Semangat bang kuliahnyaa, sehat-sehat laa"
            },
            {
                "Nama": "Presilia",
                "NIM": "122450081",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Kota Baru",
                "Hobi": "Tidur",
                "Sosmed": "@preciliamg",
                "Kesan": "Kakak yang ini cantik kalii🌷",  
                "Pesan": "Semangat terus kaka cantikkkk"
            },
            {
                "Nama": "Rafa Aqilla Jungjunan",
                "NIM": "122450142",
                "Umur": "20",
                "Asal": "Pekanbaru",
                "Alamat": "Belwis",
                "Hobi": "Baca webtoon",
                "Sosmed": "@rafaaqilla",
                "Kesan": "Kakaknya baik dan ramahhh🌞",  
                "Pesan": "Semangat kakk, sukses perkuliahannyaa!!"
            },
            {
                "Nama": "Sahid Maulana",
                "NIM": "122450109",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "jl. Airan Raya",
                "Hobi": "Nonton Jagat riview",
                "Sosmed": "@sahid_maul19",
                "Kesan": "Abangnya baik dan peduli👍",  
                "Pesan":"Semangat kuliahnya bangg, sehat-sehat, dan sukses selalu"
            },
            {
                "Nama": "Vanessa Olivia Rose",
                "NIM": "121450108",
                "Umur": "20",
                "Asal": "Jakarta",
                "Alamat": "Perum Korpri",
                "Hobi": "Belajar",
                "Sosmed": "@roselivnes__",
                "Kesan": "Kakak ini keren kaliiദ്ദി(˵ •̀ ᴗ - ˵ ) ✧",  
                "Pesan":"Semangat kaka kuliahnyaa, segala urusannya dimudahkann"
            },
            {
                "Nama": "M. Farhan Athaulloh",
                "NIM": "121450117",
                "Umur": "21",
                "Asal": "Lampung",
                "Alamat": "Kotabaru",
                "Hobi": "Menolong",
                "Sosmed": "@mfarhan.ath",
                "Kesan": "Abangnya baik, keren, dan asik😎👌🔥",  
                "Pesan": "Semangat kuliahnya ya bangg, sukses selaluu"
            },
            {
                "Nama": "Gede Moena",
                "NIM": "1214500014",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Belajar dan main game",
                "Sosmed": "@gedemoenaa",
                "Kesan": "Abangnya baik dan ramah jugaa👍",  
                "Pesan": "Semangat bang, semangat kuliah, dan semangat menjalani hidup"
            },
            {
                "Nama": "Jaclin Alcavella",
                "NIM": "122450015",
                "Umur": "19",
                "Asal": "Sumatera Selatan",
                "Alamat": "Korpri",
                "Hobi": "Berenang",
                "Sosmed": "@jaclinalcv_",
                "Kesan": "Kakak cantik dan baik hati💖",  
                "Pesan": "Semangat kak kuliahnyaa, semoga hari-harinya menyenangkann"
            },
            {
                "Nama": "Rafly Prabu Darmawan",
                "NIM": "122450140",
                "Umur": "20",
                "Asal": "Bangka Belitung",
                "Alamat": "Sukarame",
                "Hobi": "Main game",
                "Sosmed": "@raflyy_pd",
                "Kesan": "Abangnya baik dan ramah👍",  
                "Pesan": "Semangat bang kuliahnya!!!!"
            },
            {
                "Nama": "Syalaisha Andini Putriansyah",
                "NIM": "122450111",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Sukarame",
                "Hobi": "Membaca",
                "Sosmed": "@syalaisha.i__",
                "Kesan": "Kakaknya baik, ramah jugaa🌸",  
                "Pesan":"Semangat kuliahnya kakk, semoga impiannya dapat tercapai"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_PSDA()

elif menu == "Departemen Eksternal":
    def Departemen_Eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1NKJLpNHrjGn_yLjwOslLns-ViOwgguSI",
            "https://drive.google.com/uc?export=view&id=1NLPv4Qw2O0ACU4XwrF3DtbNtzPym98gM",
            "https://drive.google.com/uc?export=view&id=1NTFwWiZ47RIltVDLyM3WLU4FAtIgTSHu",
            "https://drive.google.com/uc?export=view&id=1NGTyf8cnxYx-t_4lt8bwkZQ0ShuXhVoB",
            "https://drive.google.com/uc?export=view&id=1NSkXcxtOBbU-8ygDhvGUD2BIZOeXK_ng",
            "https://drive.google.com/uc?export=view&id=1N3zr0AnYyxeT9sdauoIhX95VGRd1WOgC",
            "https://drive.google.com/uc?export=view&id=1RyHv42srzhlAs08QAs64u5d4rSRTu3YU",
            "https://drive.google.com/uc?export=view&id=1MkSlE_dGab0RKlQw2UoMGfRO9QSpIQbg",
            "https://drive.google.com/uc?export=view&id=1NFLmkzwwbCNij9dMShHzI3qLoFTnGeyr",
            "https://drive.google.com/uc?export=view&id=1N8ArvVNodDyHQ89_cyXtnJO0KLpiztGn",
            "https://drive.google.com/uc?export=view&id=16NSpN8ca2TOkYxQ5IX8JTxygobEFg-U5",
            "https://drive.google.com/uc?export=view&id=1MuywFv9YUiGFU2fFbQxskE0ZMe8UMVEz",
            "https://drive.google.com/uc?export=view&id=1MsMkEPHaOq66vyEmbyZ1UJTuWWxritS0",
            "https://drive.google.com/uc?export=view&id=1N2OjhhuHWfZKaCRpE27QFjr8m8Unbav9",
            "https://drive.google.com/uc?export=view&id=1MrNlXwX9k1A3SPGrAeLEy9wu2cjvnvDt",
            "https://drive.google.com/uc?export=view&id=1Mr717166zMODTRTQR5jFP98cyK8ENn2z",
            "https://drive.google.com/uc?export=view&id=1N2ig8rHgnlN2th7shNPTg86RQDLqDy64",
            "https://drive.google.com/uc?export=view&id=1Mzx7FKdlOSBgcezolpgkvmmbIZgsUUyp",
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
                "Kesan": "Abang nya baik dan menginspirasi😎👌🔥",  
                "Pesan": "Semangat kuliahnya bangg, sukses selaluu"
            },
            {
                "Nama": "Ramadhita Atifa Hendri",
                "NIM": "121450131",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar Lampung",
                "Hobi": "Jalan-jalan",
                "Sosmed": "@ramadhitatifa",
                "Kesan": "Kakaknya baik dan sangat mengayomi💞",  
                "Pesan": "Semangat kuliahnya kakk, semoga segala usaha kakak tidak sia-sia"
            },
            {
                "Nama": "Nazwa Nabilla",
                "NIM": "121450022",
                "Umur": "21",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Main Golf",
                "Sosmed": "@nazwanbilla",
                "Kesan": "Kakaknya baik dan ramah🥰",  
                "Pesan":"Semangat kuliahnya kakakk!!"
            },
            {
                "Nama": "Dea Mutia Risani",
                "NIM": "122450099",
                "Umur": "20",
                "Asal": "Sumatera Barat",
                "Alamat": "Korpri",
                "Hobi": "Berkebun",
                "Sosmed": "@dea.tiarsn",
                "Kesan": "Kakaknya asik diajak ngobrol❤️",  
                "Pesan":"Semangat kuliahnya kakk, sehat selalu!"
            },
            {
                "Nama": "Esteria Rohanauli Sidauruk",
                "NIM": "122450025",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Main golf",
                "Sosmed": "@esterias",
                "Kesan": "Kakaknya baik, ramah jugaa >.<",  
                "Pesan":"Semangat terus kakk!"
            },
            {
                "Nama": "Natasya Ega Lina Marbun",
                "NIM": "122450024",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Korpri",
                "Hobi": "Surving",
                "Sosmed": "@nateee__15",
                "Kesan": "Kakaknya baik, lucu, ramahh✿˖˚ ༘𐙚",  
                "Pesan": "Semangat terus kuliahnya kakakk, semoga bisa lulus tepat waktu"
            },
            {
                "Nama": "Novelia Adinda",
                "NIM": "122450104",
                "Umur": "21",
                "Asal": "Jakarta Timur",
                "Alamat": "Belwis",
                "Hobi": "Tidur",
                "Sosmed": "@nvliaadinda",
                "Kesan": "Kakaknya baik dan cantikkk🌺",  
                "Pesan":"Semangat kuliahnya kaa, sukses selaluu"
            },
            {
                "Nama": "Ratu Keisha Jasmine Deanova",
                "NIM": "122450106",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Way Kandis",
                "Hobi": "Sepak Takraw",
                "Sosmed": "@jasminedea",
                "Kesan": "Kakaknya baik, ramah, cantik, dan sangat mengayomi⸜(˃.˂)⸝♡",  
                "Pesan": "Semangat kuliahnya kakk, sehat selaluu"
            },
            {
                "Nama": "Tobias David Manogari",
                "NIM": "122450091",
                "Umur": "20",
                "Asal": "Jakarta Selatan",
                "Alamat": "Pemda",
                "Hobi": "Jogging",
                "Sosmed": "@tobiassiagian",
                "Kesan": "Abangnya keren dan baik jugaaദ്ദി(˵ •̀ ᴗ - ˵ ) ✧",  
                "Pesan": "Semangat terus bangg, lancar-lancar kuliahnyaa"
            },
            {
                "Nama": "Yohana Manik",
                "NIM": "122450126",
                "Umur": "19",
                "Asal": "Jakarta Selatan",
                "Alamat": "Belwis",
                "Hobi": "Bulu Tangkis",
                "Sosmed": "@yo_hanamnk",
                "Kesan": "Kakaknya baikk🤗",  
                "Pesan": "Semangat terus kaa!"
            },
            {
                "Nama": "Rizki Adrian Bennovry",
                "NIM": "121450073",
                "Umur": "21",
                "Asal": "Bekasi",
                "Alamat": "TVRI",
                "Hobi": "Bikin Portofolio",
                "Sosmed": "@rzkdrnnn",
                "Kesan": "Abangnya baik dan ramahh👍",  
                "Pesan": "Selalu semangat bangg!"
            },
            {
                "Nama": "Arafi Ramadhan Maulana",
                "NIM": "122450122",
                "Umur": "20",
                "Asal": "Bandung",
                "Alamat": "Way Huwi",
                "Hobi": "Bertani",
                "Sosmed": "@arafiramadhanmaulana",
                "Kesan": "Abangnya ramah dan sangat mengayomi👍",  
                "Pesan": "Semangat terus bangg, sukses lancar jaya"
            },
            {
                "Nama": "Asa Do'a Uyi",
                "NIM": "122450005",
                "Umur": "20",
                "Asal": "Muara Enim",
                "Alamat": "Korpri",
                "Hobi": "Tepuk Semangat",
                "Sosmed": "@u'_yippy",
                "Kesan": "Kakaknyaa baik skaliii, ramah skalii🧸❤️",  
                "Pesan": "Semangat terus kakaa, sehat-sehatt!"
            },
            {
                "Nama": "Irvan Alfaritzi",
                "NIM": "122450093",
                "Umur": "21",
                "Asal": "Sumatera Barat",
                "Alamat": "Sukarame",
                "Hobi": "Nonton Youtube",
                "Sosmed": "@alvaritziirvan",
                "Kesan": "Abangnya baikk dan asik jugaa👍",  
                "Pesan":"Semangat bang kuliahnyaa, semoga semua urusannya dipermudahh"
            },
            {
                "Nama": "Izza Lutfia",
                "NIM": "122450090",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "T. betung utara",
                "Hobi": "Main Rubik",
                "Sosmed": "@izzalutfiaa",
                "Kesan": "Kakaknya asik, baik, dan ramahh♡︎♡︎♡︎",  
                "Pesan": "Semangat kuliahnya kakakkk, semoga bisa lulus sesuai target"
            },
            {
                "Nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "NIM": "122450034",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Rajabasa",
                "Hobi": "Ngaji",
                "Sosmed": "@alyaavanevi",
                "Kesan": "Kakaknya lucu, asik, namanya baguss🌻",  
                "Pesan": "Semangat kuliahnya kakk, sehat selalu, sukses selaluu"
            },
            {
                "Nama": "Raid Muhammad Naufal",
                "NIM": "122450027",
                "Umur": "20",
                "Asal": "Lampung Tengah",
                "Alamat": "Sukarame",
                "Hobi": "Nemenin Tobias Lari",
                "Sosmed": "@rayths__",
                "Kesan": "Abangnya sepertinya pendiamm, abangnya baik jugaa🤗👍",  
                "Pesan":"Semangat terus bang menjalani kuliahnyaa, sehat selaluu, semoga segala urusannya dipermudah"
            },
            {
                "Nama": "Tria Yunanni",
                "NIM": "122450062",
                "Umur": "20",
                "Asal": "Way Kanan",
                "Alamat": "Sukarame",
                "Hobi": "Baca Buku",
                "Sosmed": "@tria_y062",
                "Kesan": "Kakaknya baikk, asik, dan ramahh💛",  
                "Pesan": "Semangat terus kak kuliahnyaa"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_Eksternal()

elif menu == "Departemen MIKFES":
    def Departemen_MIKFES():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1XlKgnFkaBKwjOrBqqKwNKIAu3RNwox1O",
            "https://drive.google.com/uc?export=view&id=1Xt1LE5kam1fdAUqHxeVcJTEnvMz8v0et",
            "https://drive.google.com/uc?export=view&id=1YEWIGg_jJk7IJoDfL59vL60hH4JnUa6W",
            "https://drive.google.com/uc?export=view&id=1YMhWAcMnHDvlO00N00zZZvV0fGwnmbAi",
            "https://drive.google.com/uc?export=view&id=1XgkXAoGMSoYNHiAYX77SvUiDVBz-RNFM",
            "https://drive.google.com/uc?export=view&id=1Y8-KBeFYixgBPw6qsuluS361lLoVlweZ",
            "https://drive.google.com/uc?export=view&id=1Y3lcv_peWv23BRLxGoaXZ4dj4Y5mbpUE",
            "https://drive.google.com/uc?export=view&id=1XrrMVW4vlzMwFjRaFeEAAzoVqSOum_H9",
            "https://drive.google.com/uc?export=view&id=1XkqanVfkLRoXBAn_WvcoN9CZTYMD03br",
            "https://drive.google.com/uc?export=view&id=1YIYgDP016ittwp5mC9ZA9sVlb4flYyPk",
            "https://drive.google.com/uc?export=view&id=1Y3MiCXdAHlComGxYNNFeGR57qdZIkc-Q",
            "https://drive.google.com/uc?export=view&id=1Xj69zTc73MeMME3YfNC3ECBAjExtS6QM",
            "https://drive.google.com/uc?export=view&id=1XjqLBZQiysZDaovDfNkvmQVe9dL-SsDH",
            "https://drive.google.com/uc?export=view&id=1XpC_OfFuX2qqcYMxBudKh5Juh3NFw0yo",
            "https://drive.google.com/uc?export=view&id=1YMqCd-nqxWlgDgfXLViXMB0UZrNUtbHx",
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
                "Kesan": "Abangnya baik, ramah, sangat mengayomi dan menginspirasii😎👌🔥",  
                "Pesan": "Semangat bang kuliahnyaa, semoga segala urusannya dipermudah, sehat selaluu"
            },
            {
                "Nama": "Annisa Novantika",
                "NIM": "121450005",
                "Umur": "21",
                "Asal": "Lampung Utara",
                "Alamat": "Jl. Pulau sabesi",
                "Hobi": "Memasak",
                "Sosmed": "@anovavona",
                "Kesan": "Kakaknya baik dan ramahh",  
                "Pesan": "Semangat kuliahnya kakakkk, semoga bisa kulus tepat waktuu💗"
            },
            {
                "Nama": "Ahmad Sahidin Akbar",
                "NIM": "122450044",
                "Umur": "20",
                "Asal": "Tulang Bawang",
                "Alamat": "Sukarame",
                "Hobi": "Olahraga",
                "Sosmed": "@sahid22__",
                "Kesan": "Abangnya baikk👏",  
                "Pesan": "Semangat terus banggg!!"
            },
            {
                "Nama": "Muhammad Regi Abdi Putra Amanta",
                "NIM": "122450031",
                "Umur": "25",
                "Asal": "Palembang",
                "Alamat": "Jl. Permadi",
                "Hobi": "Ngasprak ADS",
                "Sosmed": "@mregiiii_",
                "Kesan": "Abang ramahh dan asikk🤓👍",  
                "Pesan": "Semangat terus bang kuliahnyaa, sehat selaluu"
            },
            {
                "Nama": "Syalaisha Andina Putriansyah",
                "NIM": "122450121",
                "Umur": "21",
                "Asal": "Tanggerang",
                "Alamat": "Gg. Yudistira",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@dkselsd_31",
                "Kesan": "Kakaknya baik dan ramahh(ෆ˙ᵕ˙ෆ)♡",  
                "Pesan": "Semangat kaka kuliahnyaa, semoga apa yang diusahakan membuahkan hasil yang diharapkan"
            },
            {
                "Nama": "Anwar Muslim",
                "NIM": "122450117",
                "Umur": "21",
                "Asal": "Bukit Tinggi",
                "Alamat": "Korpri",
                "Hobi": "ML (Machine Learning)",
                "Sosmed": "@here.am.ai",
                "Kesan": "Abangnya ramahh👏🤗",  
                "Pesan": "Semangat kuliahnya bangg, sehat selaluu"
            },
            {
                "Nama": "Deva Anjani Khayyuninafsyah",
                "NIM": "122450014",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Kemiling",
                "Hobi": "Resume webinar",
                "Sosmed": "@anjaniidev",
                "Kesan": "Kakaknya lucuu, baik, asik jugaa",  
                "Pesan": "Semangat kuliahnya kakakk, sehat selalu, semoga bisa lulus sesuai target🌼"
            },
            {
                "Nama": "Dinda Nababan",
                "NIM": "122450120",
                "Umur": "20",
                "Asal": "medan",
                "Alamat": "Jl. lapas",
                "Hobi": "Membaca Journal bu Mika",
                "Sosmed": "@dindanababan",
                "Kesan": "Kakaknya baikk, pasti kakaknya pintar skalii🌹",  
                "Pesan": "Semangat kuliahnya kakk, sehat selaluu"
            },
            {
                "Nama": "Marleta Cornelia Leander",
                "NIM": "122450092",
                "Umur": "20",
                "Asal": "Depok",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Review Journal bu Mika",
                "Sosmed": "@marletacornelia",
                "Kesan": "Kakaknya sangat baikk, sangat ramahh, asik diajak ngobrol, dan mau sharing pengalamann🌷˚ʚ💗ɞ˚ 🌷",  
                "Pesan": "Semangat kuliahnya kakaaa, sehat selalu, tetap ceriaa"
            },
            {
                "Nama": "Rut Junita Sari Siburian",
                "NIM": "122450103",
                "Umur": "20",
                "Asal":"Kep. Riau",
                "Alamat": "Gg. Nangka 3",
                "Hobi": "Menghitung akurasi",
                "Sosmed": "@junitaa_0406",
                "Kesan": "Kakak ini sangat baikk, i love you kakk🫶💖💗🥰💞",  
                "Pesan": "Semangat terus kuliahnya ka nitaa, semoga kakak sukses selaluu"
            },
            {
                "Nama": "Syadza Puspadari Azhar",
                "NIM": "122450072",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Belwis",
                "Hobi": "Membangkitkan bilangan",
                "Sosmed": "@puspadrr",
                "Kesan": "Kakaknya baik dan ramahh🌞",  
                "Pesan": "Semangat kaka kuliahnyaa, sehat selalu yaa"
            },
            {
                "Nama": "Aditya Rahman",
                "NIM": "122450113",
                "Umur": "20",
                "Asal":"Metro",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@rahm.adityaa",
                "Kesan": "Abangnya baikk, ramah, keliatan skali orang pintar🤓👍",  
                "Pesan": "Semangat bang kuliahnyaa, semoga segala yang dikerjakan berguna kedepannya"
            },
            {
                "Nama": "Eggi satria",
                "NIM": "122450032",
                "Umur": "20",
                "Asal":"Sukabumi",
                "Alamat": "Korpri",
                "Hobi": "Ngoding wisata",
                "Sosmed": "@_egistr",
                "Kesan": "Abangnya ramah dan baik jugaa😊",  
                "Pesan": "Semangat kuliahnya bangg, sehat selaluu!!"
            },
            {
                "Nama": "Febiya Jomy Pratiwi",
                "NIM": "122450074",
                "Umur": "20",
                "Asal":"Tulang Bawang",
                "Alamat": "Jl. Kelengkeng Raya",
                "Hobi": "Review Journal",
                "Sosmed": "@pratiwifebiya",
                "Kesan": "Kakaknya baik dan ramah, saat diajak ngobrol juga seru🌷",  
                "Pesan": "Semangat kuliahnya kaka! semoga bisa lulus tepat waktu"
            },
            {
                "Nama": "Happy Syahrul Ramadhan",
                "NIM": "122450013",
                "Umur": "20",
                "Asal": "Lampung Timur",
                "Alamat": "Karang Anyar",
                "Hobi": "Main game",
                "Sosmed": "@sudo.syahrulramadhannn",
                "Kesan": "Abangnya ramahh, nama abangnya baguss🤗",  
                "Pesan": "Semangat kuliahnya bangg, happy selalu yakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MIKFES()

elif menu == "Departemen SSD":
    def Departemen_SSD():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15VSTCB-0AhDyOUNhN2KVUvd8vhbKlR9D",
            "https://drive.google.com/uc?export=view&id=1hI2iG6n7G0LsWBDvHSP7ub3x76p4tAhZ",
            "https://drive.google.com/uc?export=view&id=1h2H64aBBw8DKcN-hvgWRtAcS0h1Hk3DI",
            "https://drive.google.com/uc?export=view&id=1hPG7RPmr1FLsY6lb02Nw1wjhUy9mw_FN",
            "https://drive.google.com/uc?export=view&id=1hLgEoZFTvFzF15CC24cTahbYuh4GCnok",
            "https://drive.google.com/uc?export=view&id=1hXchMs3YHJTRqD6SO7xrjqzS8rxHYxBt",
            "https://drive.google.com/uc?export=view&id=1hNl2uwv_a2YtG4DHqzYX1301PDsNl-Eq",
            "https://drive.google.com/uc?export=view&id=15YEWJslsb7ygH5cq7pT92XzIiYWRyQjs",
            "https://drive.google.com/uc?export=view&id=15ZAV5P_K7YTyMmY6ukfE1qeTpZFVbTXE",
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
                "Kesan": "Abang ini sangat asik diajak ngobroll, abangnya punya banyak fun fact😎👌🔥",  
                "Pesan":"Semangat bang kuliahnyaa, sukses selaluu!!"
            },
            {
                "Nama": "Adisty Syawaida Ariyanto",
                "NIM": "121450136",
                "Umur": "23",
                "Asal":"Metro",
                "Alamat": "Sukarame",
                "Hobi": "Nonton film",
                "Sosmed": "@adistysa_",
                "Kesan": "Kakaknya ramah dan mengayomi𓆩♡𓆪",  
                "Pesan":"Semangat kaka kuliahnyaa, semoga bisa lulus tepat waktu yaa"
            },
            {
                "Nama": "Nabila Azhari",
                "NIM": "121450029",
                "Umur": "21",
                "Asal":"Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Ngitung duit",
                "Sosmed": "@zhjung_",
                "Kesan": "Kakaknya asik diajak ngobrol, sangat menginspirasi˚‧｡⋆🌻⋆｡‧˚",  
                "Pesan":"Semangat kuliahnya kakk, semoga selalu berbahagiaa"
            },
            {
                "Nama": "Ahmad Rizqi",
                "NIM": "12245138",
                "Umur": "20",
                "Asal":"Bukit Tinggi",
                "Alamat": "Airan",
                "Hobi": "Badminton",
                "Sosmed": "@ahmad.riz45",
                "Kesan": "Abangnya ramahh👏",  
                "Pesan":"Semangat kuliahnya bangg!"
            },
            {
                "Nama": "Danang Hilal Kurniawan",
                "NIM": "122450085",
                "Umur": "21",
                "Asal":"Bandar Lampung",
                "Alamat": "Airan",
                "Hobi": "Touring",
                "Sosmed": "@dananghk",
                "Kesan": "Abangnya ramah, seru, asik diajak ngobrol(^▽^)👍",  
                "Pesan":"Semangat kuliahnya bangg, semoga bisa lulus sesuai target"
            },
            {
                "Nama": "Farrel Julio Akbar",
                "NIM": "122450010",
                "Umur": "20",
                "Asal":"Bogor",
                "Alamat": "Lapas",
                "Hobi": "Olahraga",
                "Sosmed": "@farrel__julio",
                "Kesan": "Abang ini baik dan sangat mengayomi🤓👍",  
                "Pesan":"Semangat kuliahnya bangg, semoga segala urusannya dimudahkann"
            },
            {
                "Nama": "Tessa Kania Sagala",
                "NIM": "122450040",
                "Umur": "20",
                "Asal":"Simalungun Utara",
                "Alamat": "Pemda",
                "Hobi": "Menulis",
                "Sosmed": "@tessakhanias",
                "Kesan": "Kakaknya baik hati dan sangat ramahh🌹",  
                "Pesan":"Semangat kuliahnya kaka, semoga segala harapan kaka dan plan kaka dapat tercapai"
            },
            {
                "Nama": "Dhafin Razaqa Luthfi",
                "NIM": "122450133",
                "Umur": "20",
                "Asal":"Bandar Lampung",
                "Alamat": "Jl. Nangka Sari",
                "Hobi": "Olahraga",
                "Sosmed": "@dhafinrzqa13",
                "Kesan": "Abangnya ramah dan baik 👍",  
                "Pesan":"Semangat kuliahnya bang, sehat selalu!!"
            },
            {
                "Nama": "Elia Meylani Simanjuntak",
                "NIM": "12245026",
                "Umur": "20",
                "Asal":"Bekasi",
                "Alamat": "Korpri",
                "Hobi": "Nyanyi dan main alat musik",
                "Sosmed": "@meylanielia",
                "Kesan": "Ihh kaka ini sangat lucuu, baik, ramah, asik diajak ngobrol, ceria sekalii (๑>◡<๑)",  
                "Pesan":"Semangat kuliahnya kakakk, semoga segala urusannya dimudahkan, tetap ceria ya kakk"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_SSD()

elif menu == "Departemen MEDKRAF":
    def Departemen_MEDKRAF():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15pCgS9NI6rBtcLnbjYPebJ0xX5D8BjB1",
            "https://drive.google.com/uc?export=view&id=15yxVHXjxtA_sznpubOOsi4b25UDxFp5j",
            "https://drive.google.com/uc?export=view&id=15pK05_p-dPZfYH72lUQsC-MkIdPA8ku0",
            "https://drive.google.com/uc?export=view&id=15j7_hTd_wa2e5Hnjz4FA_LKLhYNBZUEl",
            "https://drive.google.com/uc?export=view&id=16A-Z7FyW2SPAMU3YxwP0Hk9gehcHoqFd",
            "https://drive.google.com/uc?export=view&id=15nJZQnFIHQsJgp0kMwoszXoC4Jnnr3SP",
            "https://drive.google.com/uc?export=view&id=15uZoc_Cga2qV43BBYdW2vj14qkctidtx",
            "https://drive.google.com/uc?export=view&id=15jYXB48XPMf8glagjazCmlYni9cCvKBJ",
            "https://drive.google.com/uc?export=view&id=15qCMTr7-vQ_p1pc8hVkPF4j9nYsSnnMQ",
            "https://drive.google.com/uc?export=view&id=161SZ-yds7o2n6RY7zfXf0pNTGuYBEHKg",
            "https://drive.google.com/uc?export=view&id=15ePNx8SWArfvsUU6nKsoYgq3HgKHGa02",
            "https://drive.google.com/uc?export=view&id=15yrGq8c78vpWC-nAFpYbXoHZuWg_QQPH",
            "https://drive.google.com/uc?export=view&id=15rwQ6PyelGmSgEYVlyH6P56SXSfB-rx1",
            "https://drive.google.com/uc?export=view&id=1675dhe5IQoQyk8A-D17at3lvQKmoAugn",
            "https://drive.google.com/uc?export=view&id=15mVKz7lm45wmRohgpD_-25K1ihIq6Btx",
            "https://drive.google.com/uc?export=view&id=16JKrE5NRkw82QPnbfr55ortFSGgabAAx",
            "https://drive.google.com/uc?export=view&id=15m3JaTPhIJMxOB04YPc3-m19wJBrZShN",
            "https://drive.google.com/uc?export=view&id=15odPEUWSEkJ3OVt-0REKX4qoXEfd9p5J",
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
                "Kesan": "Abangnya mengayomi sekalii😎👌🔥",  
                "Pesan": "Semangat kuliahnya bang, semoga bisa lulus tepat waktuu"
            },
            {
                "Nama": "Elok Fiola",
                "NIM": "122450051",
                "Umur": "19",
                "Asal": "Bandar Lampung",
                "Alamat": "Bandar lampung",
                "Hobi": "Ngedit",
                "Sosmed": "@elokfiola",
                "Kesan": "Kakaknya cantik dan baik hatii🌷🫧💭",  
                "Pesan": "Semangat terus kuliahnya kakk, sehat selalu yaa"
            },
            {
                "Nama": "Arsyiah Azahra",
                "NIM": "121450035",
                "Umur": "21",
                "Asal": "Bandar Lampung",
                "Alamat": "Tanjung Senang",
                "Hobi": "Ngonten",
                "Sosmed": "@arsyiah._",
                "Kesan": "Kakak ini baik dan ramahh🌻",  
                "Pesan": "Semangat kak kuliahnyaa, suksek selalu yaa"
            },
            {
                "Nama": "Cintya Bella",
                "NIM": "122450066",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Teluk Betung",
                "Hobi": "Ngegym",
                "Sosmed": "@cintyabella28",
                "Kesan": "Kakaknya ramahh❤︎",  
                "Pesan": "Semangat kuliahnya kaa, sehat selaluu"
            },
            {
                "Nama": "Najla Juwairia",
                "NIM": "122450037",
                "Umur": "198",
                "Asal": "Sumatera Utara",
                "Alamat": "Airan",
                "Hobi": "Nulis, baca, fangirling",
                "Sosmed": "@nanana.minjoo",
                "Kesan": "Kakak inii lucu, baik, ramah, dan asikk (˶ᵔ ᵕ ᵔ˶)",  
                "Pesan": "Semangat kakak kuliahnyaa, sehat selalu kakaa, semoga hari-harinya menyenangkan"
            },
            {
                "Nama": "Patricia Leondrea Diajeng Putri",
                "NIM": "122450050",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Jatimulyo",
                "Hobi": "Shopping",
                "Sosmed": "@patriciadiajeng",
                "Kesan": "Kaka cantik nan baik hatii🌺",  
                "Pesan": "Semangat kaka kuliahnyaa, sukses selaluu, tetap bersemanagt dan ceriaa"
            },
            {
                "Nama": "Rahma Neliyana",
                "NIM": "122450036",
                "Umur": "20",
                "Asal": "Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Membaca merk mobil",
                "Sosmed": "@rahmaneliyana",
                "Kesan": "Kakanya ramahh, asik diajak ngobrol, baik lagii >.<💐",  
                "Pesan": "Semangat kuliahnya ya kakk, sehat selalu, tetap optimis dalam menjalani hari-harinyaa"
            },
            {
                "Nama": "Try Yani Rizki Nur Rohmah",
                "NIM": "122450020",
                "Umur": "20",
                "Asal": "Lampung Barat",
                "Alamat": "Korpri",
                "Hobi": "Ngoding",
                "Sosmed": "@tryyaniciciqola",
                "Kesan": "Kakaknya sangat ramahh❤️❤️",  
                "Pesan": "Semangat kuliahnya kakak, semoga segala usahanya membuahkan hasil yang diinginkan"
            },
            {
                "Nama": "Muhammad Kaisar Firdaus",
                "NIM": "121450135",
                "Umur": "20",
                "Asal": "Pesawaran",
                "Alamat": "Way kandis",
                "Hobi": "Masih nyari",
                "Sosmed": "dino_rapet",
                "Kesan": "Abangnya keren, baik jugaa👍",  
                "Pesan": "Semangat bang dalam menjalani perkuliahannyaa!!"
            },
            {
                "Nama": "Dwi Ratna Anggraeni",
                "NIM": "122450008",
                "Umur": "20",
                "Asal": "Jambi",
                "Alamat": "Pemda",
                "Hobi": "Nonton",
                "Sosmed": "@dwiratnn_",
                "Kesan": "Kakaknya baik dan sangat ramah<(˶ᵔᵕᵔ˶)>",  
                "Pesan": "Semangat terus ya kak! sukses selaluu"
            },
            {
                "Nama": "Gymnastiar Al Khoarizmy",
                "NIM": "122450096",
                "Umur": "20",
                "Asal": "Serang",
                "Alamat": "Lap. Golf",
                "Hobi": "Baca komik",
                "Sosmed": "@gymnn.as",
                "Kesan": "Abangnya keren, kece, dan asikദ്ദി(˵ •̀ ᴗ - ˵ ) ✧",  
                "Pesan": "Semangat kuliahnya bang, semoga segala urusannya dipermudah"
            },
            {
                "Nama": "Nasywa Nur Afifah",
                "NIM": "122450125",
                "Umur": "20",
                "Asal": "Bekasi",
                "Alamat": "Jl. Durian 1",
                "Hobi": "Suka dengerin musik JJ",
                "Sosmed": "@nsywannaf",
                "Kesan": "Kakaknya sangat mengayomi ๋࣭⭑ֶֶֶָָָ֢֢֢𖹭",  
                "Pesan": "Semangat kuliahnya kakkkk"
            },
            {
                "Nama": "Priska Silvia Ferantiana",
                "NIM": "122450053",
                "Umur": "20",
                "Asal": "Palembang",
                "Alamat": "Jl. Nangka 2",
                "Hobi": "Nonton yang bikin nangis",
                "Sosmed": "@prskslv",
                "Kesan": "Kakak ini baik dan sangat ramahh𓍢ִ໋🌷͙֒",  
                "Pesan": "Semangat kak kuliahnyaa, semoga kaka berbahagia setiap hari"
            },
            {
                "Nama": "Muhammad Arsal Ranjana Utama",
                "NIM": "121450111",
                "Umur": "21",
                "Asal": "Depok",
                "Alamat": "Jl. Nangka 3",
                "Hobi": "Main game",
                "Sosmed": "@arsal.utama",
                "Kesan": "Abangnya ramah dan baik👍",  
                "Pesan": "Semangat bang kuliahnyaa, semoga bisa lulus tepat waktu yaa"
            },
            {
                "Nama": "Abit Ahmad Oktarian",
                "NIM": "122450042",
                "Umur": "19",
                "Asal": "Rajabasa",
                "Alamat": "Jl. Padat Karya",
                "Hobi": "Ngoding dan gaming",
                "Sosmed": "@abitahmad",
                "Kesan": "Abangnya keren, dan ramah, dan menginspirasi✧₊⁺",  
                "Pesan": "Semangat kuliahnya bangg, sehat selaluu"
            },
            {
                "Nama": "Akmal Faiz Abdillah",
                "NIM": "122450114",
                "Umur": "20",
                "Asal": "Bandar Lampung",
                "Alamat": "Sukarame",
                "Hobi": "Main hp",
                "Sosmed": "@_akmal.faiz",
                "Kesan": "Abangnya baik, ramah, dan asik diajak ngobrol😊",  
                "Pesan": "Semangat kuliahnya bangg, kalo cape istirahat jangan nyerahh"
            },
            {
                "Nama": "Hermawan Manurung",
                "NIM": "122450069",
                "Umur": "20",
                "Asal": "Bogor",
                "Alamat": "Jl. deket tol",
                "Hobi": "Baca novel Tere Liye",
                "Sosmed": "@hermawan.mnrng",
                "Kesan": "Abangnya kece, seru, asik, keren dah pokoknya ദ്ദി(˵ •̀ ᴗ - ˵ )✧",  
                "Pesan": "Semangat kuliahnya bangg, sukses lancar jayaa, bahagia teruss!!"
            },
            {
                "Nama": "Khusnun Nisa",
                "NIM": "122450078",
                "Umur": "20",
                "Asal": "Lampung Selatan",
                "Alamat": "Belwis",
                "Hobi": "Ngepel",
                "Sosmed": "@khusnun_nisa335",
                "Kesan": "Kakak ini baik sekali, ramah jugaa, senang diajak ngobrol🌟",  
                "Pesan": "Semangat kuliahnya kaka, sehat selalu yaa, semoga semua urusannya dimudahkan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    Departemen_MEDKRAF()