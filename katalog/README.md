## LINK APLIKASI HEROKU
https://tugas-pbp2.herokuapp.com/katalog/

## Bagan yang berisi request client ke web aplikasi berbasis Django
<img src="D:\Dave\UI\sem 3\PBP\Blank diagram.png">

# PENJELASAN BAGAN :
Pertama user akan membuka browser favorite mereka dan mengetik URL ke webiste yang mereka ingin buka.Ketika user tekan enter maka browser akan melakukan HTTP Request kepada server yang menyimpan data - data pada website tersebut.Permintaan akan masuk ke dalam server Django.Ketika aplikasi dijalankan maka aplikasi akan melihat URL route yang sudah diketikkan oleh user.Pada tugas ini user mengetik https://tugas-pbp2.herokuapp.com/katalog/ maka akan route dari url tersebut adalah /katalog

Django akan mengakses file urls.py dan mencari pola URL yang sama atau yang cocok pada urlpatterns. Ketika telah menemukan pola yang cocok, maka dilanjutkan untuk mengambil views untuk meminta halaman yang dimaksud. Ketika suatu pola URL yang diminta tidak ditemukan, maka Django akan memanggil error-handling yakni untuk menangani halaman error yang diantaranya ada handler400, handler403. handler404, dan handler500.

views.py merupakan sebuah fungsi pada python yang menerima web request atau web response, ini bisa berupa HTTP reqeust, html template atau berubah ke halaman lain pada website 

data-data pada website disimpan pada models.py sehingga model mengelola semua data agar dapt ditampilkan pada views.py

Halaman yang muncul pada browser user merupakan file html yang disimpan pada sebuah template

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment adalah sebuah alat untuk menjaga ruang terpisah untuk sebuah proyek dengan pustaka dan dependensi di satu tempat. Environment ini spesifik ke proyek tertentu dan tidak berinterfer dengan dependensi proyek lainnya.Dalam membuat aplikasi web kita tidak harus menggunakan virtual environment

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Pertama, membuat fungsi bernama show_katalog pada "views.py" di folder catalog dengan request sebagai parameter. Lalu, memindahkan isi dari CatalogItem ke variabel bernama data_barang_Katalog. Kemudian membuat sebuah dictionary bernama context yang akan diteruskan ke file html, sehingga data pada dictionary dapat digunakan pada file html kemudian fungsi tersebut akan return  request, file html: "katalog.html", dan variabel dictionary tadi sebagai parameternya.

Kedua, mengisi file bernama "urls.py" pada folder katalog yang berisi sebuah variabel yang akan menyimpan semua pemetaan URL Route katalog app ke fungsi bersesuaian yang ada di "views.py". Variabel tersebut bernama urlpatterns dengan tipe data list.

Ketiga, Untuk menampilkan daftar katalog ke webiste, maka perlu melakukan iterasi terhadap variabel list_katalog yang telah di render ke dalam HTML.Dengan cara memanggil nama variabel/atribut spesifik dari objek tersebut  dengan menulis "{{ <key> }}" pada file html-nya.

Keempat, buat aplikasi baru pada heroku. kemudian tambahkan "HEROKU_API_KEY" dan "HEROKU_API_NAME" pada secrets di repository django project tersebut yang ada pada github dan tinggal re-deploy file dpl.yml