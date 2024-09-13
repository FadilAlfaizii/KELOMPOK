import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    # palu
    "Buku Kating/064_Muhammad Hanif Dzaky Arifin.py",
    title="064 - Muhammad Hanif Dzaky Arifin",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    # bulu
    "Buku Kating/035_Fabiolla Charissa Putri.py",
    title="035 - Fabiolla Charissa Putri",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    #padil
    "Buku Kating/115_Muhammad Fadil Alfaizi.py",
    title="115 - Muhammad Fadil Alfaizi",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    #dzikra
    "Buku Kating/124_Muhammad Dzikra.py",
    title="124 - Muhammad Dzikra",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    #zai
     "Buku Kating/111_Zailani Satria.py",
    title="111 - Zailani Satria",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    #razka
    "Buku Kating/046_Gusti Putu Ferazka.py",
    title="046 - Gusti Putu Ferazka",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    #vany
    "Buku Kating/022_Vany Salsabila Putri.py",
    title="022 - Vany Salsabila Putri",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    #hafsa
    "Buku Kating/079_Hafsa Fazila Arradhi.py",
    title="079 - Hafsa Fazila Arradhi",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    #ilmi
    "Buku Kating/053_Khazanatil Ilmi.py",
    title="053 - Khazanatil Ilmi",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    #fai
    "Buku Kating/044_Fairuz Ary Syifa.py",
    title="044 - Fairuz Ary Syifa",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    #daniar
    "Buku Kating/061_Erma Daniar Safitri.py",
    title="061 - Erma Daniar Safitri",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    #wulan
<<<<<<< HEAD
    "Buku Kating/061_Erma Daniar Safitri.py",
    title="061 - Erma Daniar Safitri",
=======
   "Buku Kating/027_Wulan Lumbantoruan.py",
    title="027 - Wulan Lumbantoruan",
>>>>>>> 4f2b8945bff18523827d0fbedbe2dcb84b6138ef
    icon=":material/person:",
)


#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6, Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

