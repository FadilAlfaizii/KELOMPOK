import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set up the page title and layout
st.set_page_config(page_title="Evaluasi Peran Program Magang", layout="wide")

# Title and Introduction
st.title("Evaluasi Peran Program Magang dalam Mempersiapkan Mahasiswa untuk Dunia Kerja")
st.header("INSTITUT TEKNOLOGI SUMATERA")

# Abstrak Section
st.subheader("Abstrak")
st.markdown("""
Artikel ini bertujuan untuk mengevaluasi peran program magang dalam mempersiapkan mahasiswa memasuki dunia kerja melalui kolaborasi antara perguruan tinggi dan industri. Hasil penelitian menunjukkan bahwa program magang secara signifikan mendukung pengembangan keterampilan teknis serta soft skill, seperti kemampuan komunikasi, adaptasi, kerja tim, dan manajemen tugas, yang sangat dibutuhkan di lingkungan kerja saat ini. Kemitraan antara perguruan tinggi dan industri dalam merancang kurikulum yang sesuai dengan kebutuhan industri terbukti efektif meningkatkan kesiapan mahasiswa menghadapi perubahan dan tuntutan dunia kerja. Selain itu, program magang menawarkan keuntungan bagi perusahaan dalam proses rekrutmen awal serta kesempatan untuk menilai potensi calon tenaga kerja. Secara keseluruhan, program magang berperan penting dalam mendukung perguruan tinggi untuk menghasilkan lulusan yang kompeten, siap kerja, dan berdaya saing di tingkat global.""")

# Keywords
st.markdown("**Kata Kunci:** Program magang, keterampilan teknis, soft skill, kolaborasi perguruan tinggi dan industri, kesiapan kerja.")

# Teori Dasar Section
st.subheader("Teori Dasar")
st.markdown("""
Perguruan tinggi sebagai salah satu wadah dalam memberikan pendidikan dan melatih kemampuan mahasiswa di bidang akademis maupun profesional memiliki tujuan untuk meluluskan mahasiswa yang memiliki keterampilan siap guna di tengah-tengah masyarakat maupun dunia kerja dituntut untuk dapat menyiapkan rangkaian program perkuliahan yang mendukung hal tersebut sehingga mahasiswa mempunyai daya saing serta mampu menghadapi berbagai tantangan secara global (Rinandiyana, 2021). mengungkapkan bahwasanya dalam proses untuk mendukung kemampuan mahasiswa dan persiapannya menghadapi dunia kerja secara nyata, maka perguruan tinggi dituntut untuk dapat memberikan fasilitas serta dukungan agar mahasiswa mampu mempraktikkan keahlian yang dimiliki melalui pelaksanaan magang kerja secara langsung di Dunia kerja maupun industri (Du/Di). Selain itu, pelaksanaan magang kerja yang difasilitasi oleh perguruan tinggi sekaligus sebagai upaya untuk menciptakan lulusan yang berkualitas dan siap guna. Dengan demikian perguruan tinggi dianggap telah mencapai tujuannya sebagai wadah untuk mempersiapkan lulusan yang memiliki kemampuan akademis dan profesional di bidang-bidang tertentu yang tentunya dapat diaplikasikan di tengah-tengah masyarakat. Dengan pelaksanaan program magang juga dapat meningkatkan kemampuan dan kompetensi mahasiswa.
Magang sebagai jembatan antara teori dan praktik memainkan peran penting dalam membantu mahasiswa menerapkan ilmu yang mereka miliki dan pelajari ke dalam situasi dunia kerja nyata. Melalui magang, mahasiswa tidak hanya memperoleh keterampilan teknis, tetapi juga soft skill seperti kemampuan berkomunikasi, kolaborasi, adaptasi, dan problem-solving yang sangat dihargai di dunia kerja (Arisandi, 2022).
Tagala berpendapat bahwasanya kompetensi memiliki definisi sebagai salah satu bawaan individu yang berhubungan dengan tingkat dan kemampuan kerja dengan pekerjaannya (Lutfia & Rahadi, 2020). Dengan demikian potensi mahasiswa sebagai peserta magang akan ditingkatkan melalui pelatihan secara langsung dan pengalaman yang ia peroleh. Dalam upaya peningkatan pengetahuan dan nilai tambah mahasiswa sebelum akhirnya turun pada dunia kerja, melalui program magang mahasiswa diharapkan memperoleh pengalaman dan persiapan untuk menghadapi dunia kerja yang sangat kompetitif serta menuntut pekerja yang handal dan memiliki pengetahuan sebagai bekal yang diperlukan dalam dunia kerja (Rinandiyana, 2021). 
Program magang pada kenyataannya juga efektif untuk meningkatkan kemampuan berkomunikasi dengan baik, kemampuan menyesuaikan diri, kemampuan manajerial kerja secara berkelompok, kemampuan dalam berinteraksi, dan meningkatkan ketelitian dalam bekerja sebagai bagian dari kemampuan soft skill yang harus dimiliki mahasiswa (Lutfia & Rahadi, 2020). Tidak hanya bermanfaat terhadap proses pencapaian tujuan perguruan tinggi yang juga sebagai wadah bagi mahasiswa untuk berkembang dan manfaatnya bagi mahasiswa itu sendiri, program magang ini juga memberikan keuntungan tersendiri bagi industri dan perusahaan yang terlibat sebagai wadah lain untuk mahasiswa praktik kerja langsung dan memperoleh pengalaman dunia kerja. Sebagaimana telah menjadi tanggung jawab sosial maupun menyesuaikan dengan undang-undang bahwa pendidikan merupakan tanggung jawab berbagai pihak, baik orang tua, sekolah, pemerintah, dan masyarakat. Maka, perusahaan dituntut untuk membuka diri sebagai wadah yang membantu perguruan tinggi dalam menciptakan lulusan yang memiliki pengetahuan, keterampilan, dan siap guna agar terserap secara cepat di dunia kerja.
Dalam mendukung penciptaan lulusan yang kompeten, keterlibatan industri dalam program magang bukan hanya sebagai bentuk tanggung jawab sosial perusahaan, tetapi juga memberikan peluang bagi industri untuk mendapatkan tenaga kerja potensial dengan kompetensi yang telah terbentuk. Melalui keterlibatan ini, perusahaan dapat membantu mahasiswa mendapatkan wawasan mengenai dinamika dunia kerja serta tuntutan dan standar kerja yang harus dipenuhi di industri yang sebenarnya. Sinergi ini menciptakan keuntungan dua arah; mahasiswa memperoleh pengalaman langsung yang berharga, sementara perusahaan memiliki akses untuk melihat potensi dan kinerja para mahasiswa yang mungkin menjadi bagian dari tenaga kerja di masa mendatang (Syarifudin & Widiastuti, 2020).
Selain itu, kolaborasi perguruan tinggi dan perusahaan dalam pelaksanaan program magang menciptakan peluang pengembangan kurikulum berbasis kebutuhan industri. (Menurut Wahyuni,2021). kurikulum yang disesuaikan dengan kompetensi yang dibutuhkan di industri dapat membantu mahasiswa lebih siap menghadapi tantangan yang relevan dengan bidang kerja yang mereka tekuni. Perusahaan yang terlibat juga mendapatkan manfaat berupa akses terhadap calon-calon tenaga kerja yang lebih siap beradaptasi dengan sistem kerja, teknologi, dan budaya perusahaan yang berkembang secara dinamis.
Pada tingkat individu, program magang telah terbukti meningkatkan keterampilan soft skill seperti komunikasi, kerja sama tim, dan kemampuan adaptasi—kemampuan yang sangat dibutuhkan di dunia kerja modern. Sebagaimana disampaikan oleh Arifin dan (Santoso, 2020). soft skill merupakan aspek esensial yang melengkapi keterampilan teknis mahasiswa, menjadikannya siap untuk berkolaborasi dan berkontribusi dalam lingkungan kerja yang beragam. Dengan demikian, program magang tidak hanya mempersiapkan mahasiswa dalam aspek teknis tetapi juga dalam kemampuan interpersonal yang penting untuk keberhasilan di tempat kerja (Rukmana, 2021).
Dalam jangka panjang, kolaborasi yang baik antara perguruan tinggi dan industri berpotensi meningkatkan daya saing SDM Indonesia di tingkat global. Dengan adanya program magang yang relevan dan terarah, mahasiswa dapat mengembangkan potensi dan keahlian yang diperlukan untuk menjadi profesional yang adaptif dan inovatif, sesuai dengan tuntutan zaman dan kebutuhan industri yang terus berubah (Rinandiyana, 2021).

""")

# Metode Penelitian Section
st.subheader("Metode Penelitian")
st.markdown("""
Metode penelitian yang digunakan dalam penelitian ini merupakan pendekatan kuantitatif. Pendekatan kuantitatif yang digunakan adalah kuantitatif deskriptif dengan teknik pengumpulan data menyebarkan angket atau kuesioner melalui link google form yang berisikan daftar pertanyaan dan skala rating terhadap tingkat kesulitan magang tiap divisi kaderisasi, dengan skala rating, data mentah yang didapatkan berbentuk angka, selanjutnya ditafsirkan dalam pemahaman kualitatif. Dalam penelitian ini yang menjadi populasi adalah peserta magang kaderisasi HMSD Adyatama.
""")

# Hasil dan Pembahasan Section
st.subheader("Hasil dan Pembahasan")
st.markdown("""
Penelitian ini bertujuan untuk menganalisis peran program magang dalam mempersiapkan mahasiswa menghadapi dunia kerja melalui kemitraan antara perguruan tinggi dan industri. Hasil analisis menunjukkan beberapa temuan utama terkait pelaksanaan program magang, yaitu:
Peningkatan Keterampilan Teknis dan Soft Skill
Program magang berkontribusi signifikan dalam mengembangkan keterampilan teknis mahasiswa sesuai bidang keahlian mereka. Dengan pengalaman langsung di lingkungan industri, mahasiswa dapat menerapkan teori yang dipelajari dalam praktik nyata. Temuan penelitian juga mengungkapkan bahwa magang meningkatkan keterampilan soft skill, seperti kemampuan komunikasi, kerja tim, adaptasi, dan pengelolaan tugas, yang sangat diperlukan di dunia kerja saat ini (Lutfia & Rahadi, 2020; Arifin & Santoso, 2020).
Penguatan Kompetensi melalui Kurikulum yang Sesuai dengan Industri
Kolaborasi antara perguruan tinggi dan industri dalam menyusun kurikulum berbasis kebutuhan industri membantu mahasiswa menjadi lebih siap menghadapi tantangan di bidang pekerjaan mereka. Kurikulum ini meningkatkan daya saing mahasiswa, sehingga mereka tidak hanya memiliki keahlian teknis tetapi juga mampu beradaptasi dengan teknologi dan sistem kerja modern yang diterapkan di perusahaan-perusahaan (Wahyuni et al., 2021).
Peluang Rekrutmen dan Pemetaan Kompetensi oleh Industri
Penelitian ini menunjukkan bahwa perusahaan mendapat manfaat dari program magang melalui akses langsung terhadap calon tenaga kerja potensial. Melalui program ini, industri dapat mengevaluasi kinerja mahasiswa dan mengidentifikasi talenta yang layak direkrut. Ini memberikan keuntungan bagi kedua belah pihak; mahasiswa mendapatkan pengalaman praktik langsung, sedangkan perusahaan memperoleh informasi tentang kompetensi calon pekerja (Syarifudin & Widiastuti, 2020).
Mendukung Pencapaian Tujuan Perguruan Tinggi
Program magang mendukung tujuan perguruan tinggi untuk menghasilkan lulusan yang kompeten, berpengetahuan, dan siap kerja. Data yang diperoleh menunjukkan bahwa melalui kolaborasi aktif dengan industri, perguruan tinggi telah mencapai sebagian besar tujuan ini, memungkinkan mahasiswa memperoleh pengalaman langsung dan meningkatkan keterampilan mereka baik dalam aspek akademis maupun profesional (Rinandiyana et al., 2021).
""")

# Visualization Section
st.subheader("Visualisasi Data Penelitian")
st.markdown("Berikut ini adalah beberapa visualisasi data terkait hasil penelitian program magang.")

# Example: Displaying a chart using data from your notebook (replace with actual data)
# Example Bar Chart: Dummy Data
data = {
    'Division': ['Data Science', 'Marketing', 'Engineering', 'HR'],
    'Difficulty': [3.5, 4.2, 2.8, 3.0]
}
df = pd.DataFrame(data)
fig, ax = plt.subplots()
df.plot(kind='bar', x='Division', y='Difficulty', color='skyblue', ax=ax)
ax.set_title("Tingkat Kesulitan Magang Tiap Divisi")
ax.set_ylabel("Rating Kesulitan")
st.pyplot(fig)

# Add more visualizations if available, such as from the notebook file
# Example: st.image("path/to/your/image.png")

# Pembahasan Section
st.subheader("Pembahasan")
st.markdown("""
Penelitian ini menemukan bahwa program magang memiliki peran signifikan dalam mempersiapkan mahasiswa menghadapi dunia kerja dengan memberikan pengalaman langsung di lingkungan industri. Magang tidak hanya menjadi sarana bagi mahasiswa untuk mengaplikasikan teori yang dipelajari di kampus, tetapi juga membantu dalam mengembangkan keterampilan teknis dan soft skill yang esensial untuk dunia kerja.
Pertama, peningkatan keterampilan teknis yang didapatkan melalui program magang memberi mahasiswa kesempatan untuk memahami proses kerja yang sesungguhnya, yang tidak dapat dicapai hanya melalui pembelajaran di kelas. Dalam praktik industri, mahasiswa mampu mengasah keterampilan teknis spesifik sesuai bidang studi mereka. Hal ini memperkaya pemahaman mereka tentang bagaimana teori diterapkan dalam konteks yang lebih kompleks dan dinamis. Selain itu, mahasiswa juga mengalami peningkatan dalam soft skill, seperti komunikasi, kemampuan berkolaborasi, adaptabilitas, dan pengelolaan tugas. Soft skill ini penting karena dunia kerja mengharuskan individu untuk tidak hanya menguasai teknis pekerjaan, tetapi juga berinteraksi efektif dengan tim dan beradaptasi dalam berbagai situasi kerja.
Penelitian ini juga menunjukkan bahwa kesesuaian kurikulum dengan kebutuhan industri menjadi salah satu faktor penting dalam mempersiapkan lulusan yang lebih siap kerja. Kerjasama antara perguruan tinggi dan industri memungkinkan kurikulum disusun berdasarkan keahlian dan teknologi yang relevan, sehingga mahasiswa mampu mengembangkan kompetensi yang selaras dengan tuntutan pekerjaan modern. Dengan begitu, lulusan yang dihasilkan tidak hanya menguasai teori, tetapi juga telah terlatih untuk beradaptasi dengan perubahan teknologi dan metode kerja yang berkembang di industri saat ini.
Program magang juga memberikan keuntungan bagi industri dalam hal rekrutmen. Penelitian ini menemukan bahwa perusahaan dapat memanfaatkan magang sebagai cara untuk mengidentifikasi calon tenaga kerja potensial. Melalui program magang, perusahaan dapat mengevaluasi kinerja mahasiswa, sehingga mereka memiliki kesempatan untuk merekrut individu yang sudah terbukti kompeten dan cocok dengan kebutuhan perusahaan. Di sisi lain, mahasiswa mendapat kesempatan berharga untuk menunjukkan keterampilan mereka di lingkungan kerja nyata, yang sering kali meningkatkan peluang mereka untuk direkrut setelah lulus.
Dari perspektif perguruan tinggi, program magang mendukung tujuan akademis dalam menghasilkan lulusan yang tidak hanya berkompeten secara teknis tetapi juga siap menghadapi berbagai tantangan di dunia kerja. Kolaborasi dengan industri memungkinkan mahasiswa untuk memperoleh wawasan yang lebih mendalam serta keterampilan yang tidak dapat diperoleh di ruang kelas saja. Dengan demikian, program magang mendukung perguruan tinggi dalam melahirkan lulusan yang memiliki keseimbangan antara pengetahuan akademis dan keterampilan praktis. 
Penelitian ini memperlihatkan pentingnya sinergi antara perguruan tinggi dan industri dalam membentuk program magang yang lebih optimal. Dengan pengembangan kurikulum yang berfokus pada kebutuhan industri dan keterlibatan aktif dari perusahaan dalam memberikan bimbingan, program magang dapat terus ditingkatkan sebagai jalur yang efektif untuk mempersiapkan mahasiswa menjadi lulusan yang kompeten, siap kerja, dan memiliki daya saing tinggi di pasar tenaga kerja.

""")

# Kesimpulan Section
st.subheader("Kesimpulan")
st.markdown("""
Berdasarkan penelitian yang telah dilakukan, dapat disimpulkan bahwa program magang memiliki peranan penting dalam mempersiapkan mahasiswa memasuki dunia kerja. Tingkat kesulitan yang dihadapi peserta magang bervariasi tergantung pada divisi yang dipilih. Beberapa faktor yang menyebabkan kesulitan meliputi kurangnya pengalaman peserta magang, kompleksitas tugas, dan rentang waktu yang diberikan. Selain itu, komunikasi dan interaksi antar tim juga berperan penting. Dengan program magang yang terstruktur dan sistematis, peserta kaderisasi menjadi lebih siap menghadapi dunia kerja.
""")
