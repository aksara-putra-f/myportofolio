# Identitas Diri
**Nama  :** Aksara Putra Fachruddin

**NPM   :** 2506597284

**Kelas :** PBP B


# Progress Mingguan
- **Sabtu, 5 September 2026 (11:53 - 21:00 WIB)**
    - Membuat struktur konten untuk web portofolio bagian 'Project' pada file index.html
    - Membuat struktur konten untuk web portofolio bagian 'Education' pada file index.html
    - Membuat struktur konten untuk web portofolio bagian 'Experience' pada file index.html
    - Membuat struktur konten untuk web portofolio bagian 'Project' pada file index.html

- **Minggu, 6 September 2026 (09:00 - 13:39 WIB)**
    - Membuat aturan styling untuk web portofolio bagian "Projects"

- **Minggu, 6 September 2026 (15:39 - 17:48 WIB)**
    - Membuat aturan styling untuk web portofolio bagian "Skills"

- **Minggu, 6 Septermber 2026 (19:51 - 22:21 WIB)**
    - Membuat aturan styling untuk web portofolio bagian "Experiences"

- **Senin, 7 September 2026 (10:49 - 15:14 WIB)**
    - Mengatur posisi dan menambahkan outline pada card-card di section Skills dan Projects
    - Membuat aturan styling untuk section education pada web portofolio
    - Melakukan merge pada setiap fitur ke main untuk melakukan uji hasil web app untuk tampilan desktop

- **Senin, 7 September 2026 (15:38 - 18:10 WIB)**
    - Membuat aturan styling pada section Education, Skill, Experience, dan Project untuk tampilan mobile


# Log Penggunaan AI
**Tanggal:** Sabtu, 5 September 2026

**Tools:** Gemini

**Masalah:** Kotak-kotak (card-card) pada section "Projects" melebihi ukuran container ketika jumlah kotak melebihi ukuran container secara   
             horizontal. Alih-alih card yang sudah melebihi kapasitas container untuk secara otomatis turun ke baris berikutnya, card tersebut "memaksa" untuk masuk di samping card yang sudah ada, menyebabkan lebar card-card lainnya memendek dan card melewati batas dari container.

**Strategi Prompting:** Saya menyatakan apa yang sedang saya kerjakaan saat itu dan menyebutkan titik pada web portofolio saya yang menjadi 
                        masalah. Saya juga menjabarkan masalah apa yang saya hadapi. Selain itu, saya juga menyertakan file css dan html serta _screenshot_ berupa bagian web portofolio yang menjadi topik permasalahan, dalam hal ini section Projects. Saya juga meminta AI untuk memberikan konsep dibalik solusi yang diberikan AI tersebut.

**Keputusan dalam Menerima Jawaban AI:** AI memberikan atribut CSS yang harus saya tambahkan, yaitu 'flex-wrap' dengan nilai 'wrap'. AI juga 
                                         memberikan perbaikan kode pada bagian spesifik, tetapi saya tidak menggunakan kode tersebut karena kode yang diberikan hanya untuk mensejajarkan konten di dalam card secara horizontal 

**Link Percakapan**: https://gemini.google.com/share/d/1PDQbuouRDju6DJrF3KG9j1pXzkjHqfhK?usp=sharing

---

**Tanggal:** Sabtu, 5 September 2026

**Tools:** Gemini

**Masalah:** Pada web portofolio, terdapat section 'Projects' yang menampilkan semua projek yang pernah saya kerjakan. Setiap projek ditampilkan 
             dalam 'card', setiap card berisi gambar/logo, deskripsi projek, dan link untuk melihat projek. Permasalahan yang saya hadapi, bagaimana semua konten dalam card dapat sejajar secara vertikal dan kotak link menempel pada sisi bawah card. Sebelumnya, posisi kotak link mengikuti panjang paragraf dari deskripsi projek. Hal tersebut membuat posisi tiap kotak link bisa terlihat tidak sejajar antara satu card dengan card lainnya.

**Strategi Prompting:** Saya menyatakan apa yang sedang saya kerjakaan saat itu dan menyebutkan titik pada web portofolio saya yang menjadi 
                        masalah. Saya juga menjabarkan masalah apa yang saya hadapi. Selain itu, saya juga menyertakan file css dan html serta _screenshot_ berupa bagian web portofolio yang menjadi topik permasalahan, dalam hal ini section Projects. Saya juga meminta AI untuk memberikan konsep dibalik solusi yang diberikan AI tersebut.

**Keputusan dalam Menerima Jawaban AI:** AI mengatakan bahwa saya harus memperbaiki dua bagian spesifik pada file style.css saya, yaitu ".
                                         project-card" dan ".project-link". Namun, AI juga memberikan perbaikan kode untuk bagian-bagian diluar dari yang telah disebutkan sebelumnya. Dalam hal ini saya hanya berfokus pada ".project-card" dan ".project-link". 

**Link Percakapan**: https://gemini.google.com/share/d/1jAgRam8eJsaplcRsNyPfcF7OnN5vCxIQ?usp=sharing


# Refleksi Mandiri
### Tugas 1
1. Dalam tugas 1, saya menggunakan element html section. Dalam proses pengerjaannya, saya menjadi lebih mudah untuk melihat pembagian struktur konten pada halaman index.html di text editor saya, dalam hal ini VS Code. Saya dapat dengan jelas menentukan bagian dari index.html yang mengatur bagian 'About Me', 'Projek', 'Education', dan section-section lainnya. Selain itu, elemen html section juga dapat diberikan atribut id dan class yang membuat saya lebih mudah lagi dalam melihat pembagian konten pada file index.html saya. 

2. Tantangan saya hadapi adalah pengaturan ukuran dan posisi. Saya menemukan ada banyak atribut yang bisa digunakan untuk mengatur posisi suatu elemen html pada suatu container (div, section, dan lain-lain). Sejauh ini, yang saya gunakan adalah justify-content, justify-self, align-content, dan align-self. Namun, saya masih belum bisa membedakan atribut-atribut pengatur posisi yang ada pada css. Tantangan selanjutnya adalah menentukan satuan (px, %, dan lain-lain) dalam mengatur ukuran, terutama untuk mengatur width dan height. Saya masih belum menemukan kapan sebaiknya menggunakan salah satu dari satuan-satuan tersebut. Yang terakhir adalah atribut display untuk mengatur bagaimana elemen-elemen pada container disusun. Sejauh ini, yang saya gunakan adalah flex, block, dan grid. 
Tantangan-tantangan tersebut juga menjadi hal yang menjadi fokus utama saya ketika mengatur tampilan dari desktop ke mobile. Pengaturan seperti apa yang harus saya lakukan didasarkan pada seperti apa elemen-elemen pada suatu container ingin saya tampilkan jika berpindah dari tampilan desktop ke mobile. Selanjutnya, saya menentukan nilai display apa yang perlu saya gunakan, apakah tetap sama seperti sebelumnya atau harus diubah. Selanjutnya adalah permasalahan pengaturan ukuran (width dan height) dan posisi (padding, margin, justify-content, align-items, dan lain-lain)

3. Batasan yang saya rasakan adalah efisiensi dalam memperbarui, menambahkan, atau menghapus konten pada salah satu section. Untuk melakukannya, saya harus melihat kembali file html saya. Jika file html sudah cukup panjang dan rumit, proses manajemen konten (menambah, mengubah, menghapus) bisa sulit karena saya harus mencari bagian yang mengatur konten tersebut. Dalam web portofolio saya, saya ingin menampilkan konten-konten yang relevan sehingga fokus keahlian saya bisa lebih tersampaikan. Misalnya, saya ingin menampilkan projek-projek yang relevan dan benar-benar menunjukkan keterlibatan saya, skill-skill yang relevan, dan experience yang relevan. Jika saya ingin mengubah isi dari konten-konten tersebut, saya harus menelurusi file html saya yang bisa saja file tersebut sudah cukup panjang dan kompleks sehingga akan sulit untuk menemukan bagian yang saya cari. Dengan web dinamis, harapannya web portofolio saya bisa secara dinamis mengatur konten-konten yang sesuai untuk ditampilkan dengan sedikit campur tangan saya.