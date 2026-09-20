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

- **Senin, 7 September 2026 (21:12 WIB)**
    - Mengatur text alignment bio pada section 'About Me' menjadi justify
    - Mengatur gambar foto diri untuk berada di tengah layar pada tampilan mobile

- **Sabtu, 12 September - Minggu, 13 September 2026**
    - Membuat model data untuk Experience, Skill, Project, dan Education
    - Membuat template untuk section Experience, Skill, Project, dan Education
    - Membuat path pada urls.py untuk mendapatkan view template section Experience, Skill, Project, dan Education ketika mendapatkan request

- **Minggu, 13 September 2026**
    - Membuat aturan styling pada style.css untuk template page section Experience, Skill, Project, dan Education

- **Senin, 14 September 2026**
    - Mengubah tampilan pada index.html menjadi hanya menampilkan ringkasan/highlight dari fitur-fitur informasi pada section Education, Experience, Skill, dan Project.
    - Membuat unit test

- **Minggu, 20 September 2026**
    - Membuat form untuk menambahkan data baru dan menambahkan fitur search data untuk setiap page section (Education, Skill, Project, dan Experience)

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

---

**Tanggal:** 12 September 2026

**Tool:** Claude

**Masalah:** Bagaimana menampilkan atribut data pada model yang menggunakan field "ImageField" atau "FileField" pada template.

**Strategi Prompting:** Saya menyatakan apa masalah yang saya hadapi, yaitu bagaimana menggunakan data model yang menggunakan atribut "ImageField" atau "FileField" untuk bisa ditampilkan ke user. Saya juga meminta AI untuk menjelaskan bagian-bagian kode yang diberikannya. Saya juga melakukan percakapan beruntun untuk menanyakan bagian yang belum saya pahami.

**Keputusan dalam Menerima Jawaban AI:** Menerima sebagian besar kode yang diberikan AI. Ada bagian yang tidak saya implementasikan, yaitu pada bagian "urls.py". Baik implementasi saya maupun AI sama-sama harus menambahkan "urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)", tetapi AI memberikana conditional, yaitu ketika Setting.DEBUG, sedangkan saya tidak memberikan conditional.

**Link Percakapan:** https://claude.ai/share/31f61328-176a-46ec-b7bd-dc3cc9369f49

---

**Tanggal:** 14 September 2026

**Tool:** Claude

**Masalah:** Mendeteksi letak kesalahan pada unit test dan meminta penjelasan dari AI terkait bagaimana membuat unit test untuk data model dengan field ImageField dan JSONField

**Strategi Prompting:** Saya memberitahu AI tentang apa yang ingin saya ketahui, bagaimana membuat unit test untuk data model dengan field ImageField dan JSONField. Lalu, untuk proses debugging unit test, saya melakukannya pada prompt terpisah dari sebelumnya. Saya mengirimkan kode views.py, models.py, template, dan test.py serta pesan error terminal kepada AI, lalu saya meminta bantuan AI untuk mendeteksi kesalaha yang belum dapat saya lihat.

**Keputusan dalam Menerima Jawaban AI:** AI mengatakan bahwa ternyata ada hal dari file lain yang pada akhirnya membuat test menjadi gagal, jadi kesalahan tidak hanya terletak pada test.py. Meskipun begitu, saya tidak membaca seluruh respons AI. Saya berhenti pada pertengahan hasil respons AI dan memutuskan untuk mencoba membaca pesan error yang ada di terminal untuk melihat letak error tersebut muncul.

**Link percakapan:** https://claude.ai/share/31f61328-176a-46ec-b7bd-dc3cc9369f49

# Refleksi Mandiri
### Tugas 1
1. Dalam tugas 1, saya menggunakan element html section. Dalam proses pengerjaannya, saya menjadi lebih mudah untuk melihat pembagian struktur konten pada halaman index.html di text editor saya, dalam hal ini VS Code. Saya dapat dengan jelas menentukan bagian dari index.html yang mengatur bagian 'About Me', 'Projek', 'Education', dan section-section lainnya. Selain itu, elemen html section juga dapat diberikan atribut id dan class yang membuat saya lebih mudah lagi dalam melihat pembagian konten pada file index.html saya. 

2. Tantangan saya hadapi adalah pengaturan ukuran dan posisi. Saya menemukan ada banyak atribut yang bisa digunakan untuk mengatur posisi suatu elemen html pada suatu container (div, section, dan lain-lain). Sejauh ini, yang saya gunakan adalah justify-content, justify-self, align-content, dan align-self. Namun, saya masih belum bisa membedakan atribut-atribut pengatur posisi yang ada pada css. Tantangan selanjutnya adalah menentukan satuan (px, %, dan lain-lain) dalam mengatur ukuran, terutama untuk mengatur width dan height. Saya masih belum menemukan kapan sebaiknya menggunakan salah satu dari satuan-satuan tersebut. Yang terakhir adalah atribut display untuk mengatur bagaimana elemen-elemen pada container disusun. Sejauh ini, yang saya gunakan adalah flex, block, dan grid. 
Tantangan-tantangan tersebut juga menjadi hal yang menjadi fokus utama saya ketika mengatur tampilan dari desktop ke mobile. Pengaturan seperti apa yang harus saya lakukan didasarkan pada seperti apa elemen-elemen pada suatu container ingin saya tampilkan jika berpindah dari tampilan desktop ke mobile. Selanjutnya, saya menentukan nilai display apa yang perlu saya gunakan, apakah tetap sama seperti sebelumnya atau harus diubah. Selanjutnya adalah permasalahan pengaturan ukuran (width dan height) dan posisi (padding, margin, justify-content, align-items, dan lain-lain)

3. Batasan yang saya rasakan adalah efisiensi dalam memperbarui, menambahkan, atau menghapus konten pada salah satu section. Untuk melakukannya, saya harus melihat kembali file html saya. Jika file html sudah cukup panjang dan rumit, proses manajemen konten (menambah, mengubah, menghapus) bisa sulit karena saya harus mencari bagian yang mengatur konten tersebut. Dalam web portofolio saya, saya ingin menampilkan konten-konten yang relevan sehingga fokus keahlian saya bisa lebih tersampaikan. Misalnya, saya ingin menampilkan projek-projek yang relevan dan benar-benar menunjukkan keterlibatan saya, skill-skill yang relevan, dan experience yang relevan. Jika saya ingin mengubah isi dari konten-konten tersebut, saya harus menelurusi file html saya yang bisa saja file tersebut sudah cukup panjang dan kompleks sehingga akan sulit untuk menemukan bagian yang saya cari. Dengan web dinamis, harapannya web portofolio saya bisa secara dinamis mengatur konten-konten yang sesuai untuk ditampilkan dengan sedikit campur tangan saya.


### Tugas 2
1. Ketika user membuka halaman portofolio, user, melalui browser, akan mengirimkan request yang akan diterima oleh urls.py. Berdasarkan pada path yang ditunjukkan oleh URL request, urls.py akan memanggil function dari views.py yang sesuai. Function pada views.py yang dipanggil akan mengambil template, misalnya file html, yang di-render oleh function tersebut. Function tersebut juga dapat memberikan context dalam bentuk pasangan-pasangan key-value dengan value dapat di-set secara hardcoded atau diambil dari model class data yang telah diatur di Models.py. Template, beserta data yang dimasukkan ke template, akan dikirimkan dari views.py ke urls.py, lalu dikirimkan ke user melalui broswer.

2. Mengelola data secara langsung pada template akan membuat pemeliharaan dan pengembangan aplikasi akan berjalan tidak efisien. Setiap kali ada penambahan, penghapusan, atau pembaruan data, file template harus dilakukan perubahan. Konsekuensi jika menggunakan pendekatan tersebut:
- File template dapat menjadi sangat panjang
- Redudansi kode (misalkan ada bagian yang berperan sebagai card dari item. Jika menggunakan pendekatan ini, bagian kode tersebut harus dibuat sebanyak data yang ada)
- Kesulitan dalam menavigasi file template
Pada model, kita membuat rancangan atribut-atribut data untuk suatu class model data. Data-data dari objek yang terbentuk dari suatu class model dapat digunakan oleh template menggunakan Django Template Tag setelah data-data tersebut dikirim oleh views.py melalui context. Pengelolaan data yang sebelumnya dilakukan langsung di template dapat dilakukan melalui Shell atau page admin yang telah disediakan Django.

3. makemigrations berfungsi untuk menyiapkan perubahan pada model untuk dimigrasi ke database Django lokal, sedangkan migration berfungsi untuk mengaplikasikan perubahan pada model ke database Django lokal. Dengan kata lain, makemigrations hanya untuk menyiapkan perubahan pada model, tetapi hasil perubahannya belum terlihat. Agar perubahannya terlihat, langkah selanjutnya adalah migrate. Kita harus melakukan makemigrations dan migrate ketika kita melakukan perubahan pada model kita di models.py, seperti menambahkan atribut data baru, menghapus atribut data yang sudah ada, dan mengubah tipe field pada suatu atribut data model. 