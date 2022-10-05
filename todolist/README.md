## Tugas 4 dan Tugas 5

# Link heroku
- https://tugas3-pbp.herokuapp.com/todolist

# 1 Apa kegunaan {% csrf_token %} pada elemen "<form>" ? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>

kegunaan csrf_token adalah sejenis token yang mencegah penyerangan CSRF sehingga token ini harus unik agar penyerang susah untuk menebak . Jika sebuah form tidak ada token tersebut maka akan terdapat serangan CSRF yang membuat penyerang tidak dapat membuat permintaan yang valid ke server.


# 2 Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa dengan menggunakan tag <form> yang terdapat pada HTML.Tag ini memiliki beberapa atribut yang harus diberikan,Contoh:

``` 
<form action="prosess.php" method="GET">
<!-- form field di sini -->
</form>
```
    
- action -> menentukan aksi yang akan dilakukan saat data dikirim dengan mengisi dengan sebuah url 
- method -> pengiriman data dengan menggunakan GET atau POST dimana POST akan mengirimkan data langsung ke action untuk ditampung, tanpa menampilkan pada URL sedangkan method GET akan menampilkan data/nilai pada URL, kemudian akan ditampung oleh action

Dan didalam sebuah form perlu sebuah Field yang merupakan sebuah ruas yang dapat diisi dengan data.
Contoh field:
    
``` 
<input type="text" name="info" />
```
    
Field memiliki beberapa atribut yang harus diberikan:
- type merupakan type dari field.
- name merupakan nama dari field yang akan menjadi kunci dan variabel di dalam program.

# 3 Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

user akan melakukan HTTP Request ke http://host/path pada broswer dan server akan menerima HTTP request tersebut dan menyesuaikan dengan user pada kasus user akan mengisi sebuah form  maka server akan membuat sebuah halaman HTML berjenis form pada browser yang dimana user akan menginput data- data yang diperlukan pada halaman browwser tersebut dan setelah user sudah siap mengisi data - data tersebut maka server akan menyimpan input dari user dan akan disimpan pada server dan kemudian data - data tersebut akan ditampilkan pada halaman broswer sesuai dengan path yang dihasilkan di views.py

# 4 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama melakukan perintah python manage.py startapp todolist yang berguna untuk membuat sebuah django-app dan folder bernama todolist dan kemudian tambahkan todolist pada INSTALLED_APPS di file settings.py di folder project_django. Kemudian membuat sebuah function di file models.py di folder todolist untuk menyimpan semua data-data ke server django.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.TextField()
    description =  models.TextField()

Kedua membuat file html pada folder templates yaitu login.html untuk melakukan login pada user, register.html merupakan sebuah form yang memerlukan user untuk mengisi username dan password untuk membuat akun baru, todolist.html untuk menampilkan data" user sesuai dengan akunnya, create-task.html sebuah form yang memerlukan input dari user untuk menyimpan data" yang ingin ditampilkan pada file todolist.html

Ketiga membuat beberapa function pada file views.py di dalam folder todolist: 

- show_todolist -> untuk menampilkan task dari user 
- register -> membuat akun baru untuk user jika tidak mempunyai akun
- login_user ->  melakukan login dengan mengisi username dan password dari akun user
- logout_user -> untuk mengeluarkan akun user 
- new_task -> meminta user untuk mengisi deskripsi dan judul dari tugas-tugas yang ingin ditambahkan 



## Tugas 5

# 1 Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

- Internal CSS adalah kode CSS yang dibuat di dalam tag <style> pada file HTML yang dituliskan di bagian (header) file HTML. 
        Kekurangan -> Tidak efisien apabila ingin menggunakan css yang sama dalam secara terus menurus di file HTML
        Kelebihan ->  Class dan ID bisa digunakan oleh internal stylesheet 

- Inline CSS adalah kode CSS yang dibuat langsung pada elemen HTML. Dimana Setiap elemen HTML memiliki atribut style.
        Kekurangan -> kode CSS hanya dapat diterapkan pada satu elemen pada file HTML 
        Kelebihan -> Berguna untuk memperbaiki code dengan cepat


- Eksternal CSS adalah kode CSS yang ditulis secara terpisah pada sebuah file CSS. Untuk menghubungkan file eksternal CSS dengan file HTML maka file css akan diletakkan pada bagian <head> pada file HTML.
        Kekurangan -> Halaman HTML tidak ditampilkan secara sempurna apabila file CSS tidak dipanggil atau belum selesai.
        Kelebihan -> File CSS yang sama dapat digunakan pada banyak file HTML, Struktur dari code HTML menjadi rapi


# 2 Jelaskan tag HTML5 yang kamu ketahui.

    ``` 
    - <a> -> mendefenisikan sebuah hyperlink yang dimana link tersebut dapat merujuk ke halaman lain
    - <b> -> membuat text menjadi bold
    - <body> -> mendefenisikan isi dari suatu HTML yang akan ditampilkan pada browsernya.
    - <br> -> membuat sebuah line break.
    - <button> -> membuat sebuah button yang dapat di click
    - <div>	->  mengelompokkan elemen atau tag agar menjadi satu group
    - <form> ->	membuat sebuah form pada HTML yang dapat di-input oleh user
    - <header> -> memberikan informasi tentang dokumen
    - <h1> to <h6> -> headings pada html
    - <input> -> mendefenisikan input untuk user
    - <link> ->	mendefenisikan hubungan file html dengan file eksternal 
    - <ol> -> mendefenisikan sebuah  ordered list.
    - <p> -> membuat sebuah paragraph
    - <style> -> menambahkan design pada html seperti font,warna atau ukuran font dll
    - <table> -> membuat sebuah table 
    - <td> -> mendefenisikan cell pada sebuah table
    - <textarea> -> sebuah tempat untuk user dapat meng-input sebuah text
    - <th> -> header  dari sebuah table.
    - <title> -> judul dokumen HTML.
    - <tr> -> mendefenisikan row dari sebuah table
    - <u> -> mendefenisikan text mempunyai garis bawah
    - <ul> -> mendefenisikan sebuah unordered list.
    ```


# 3 Jelaskan tipe-tipe CSS selector yang kamu ketahui.
    - tag -> selektor untuk memilih elemen html berdasarkan nama tag
    - class -> selektor untuk memilih elemen html berdasarkan nama class
    - universal -> selektor untuk memilih semua elemen pada html dengan menggunakan "*"


# 4 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    Pertama menambahkan link bootstrap pada bagian head di tiap file html dan kemudian menambahkan 
    
    ``` 
    class="p-3 mb-2 bg-dark text-white" class="alert alert-success" role="alert" 
    ```
    
    pada bagian body di tiap file html agar websitenya responsive dan mempunyai background hitam dengan text berwarna putih

    kemudian pada file login.html , register.html dan create-task.html menambahkan

    ``` 
    class="container text-center" class="table table-dark table-striped"  <div class="col col-lg-6">  <div class="row justify-content-md-center">
    ```

    - container text-center -> didalam container tiap text akan di align ke tengah pada website
    - table table-dark table-striped -> design dari table 
    - col col-lg-6 - >Kelas kolom menunjukkan jumlah kolom yang ingin Anda gunakan dari kemungkinan 12 per baris. untuk kasus ini akan mempunyai 2 column dengan lebar yang sama
    - row justify-content-md-center -> isi dari container akan dibuat ke tengah pada file html

    
    pada file todolist.html terdapat beberapa class:

    ``` 
    class="row row-cols-1 row-cols-md-3 g-4" class="col w-50" class="card text-center" class="card text-bg-secondary mb-3" class="card text-center"  class="card-footer" class="row align-item-start" class="card-body"  class="card-header"
    ```

    - class=row row-cols-1 row-cols-md-3 g-4 -> membuat cards dalam 1 column dengan membagi cards tersebbut menjadi 3 cards yang sama
    - col w-50 -> membuat sebauh column dengan width 50
    - card text-center -> text pada card akan di tengah
    - card text-bg-secondary mb-3 -> background colour dari card
    - card-footer -> footer dari sebuah card
    - row align-item-start
    - card-body  -> body dari sebuah card
    - card-header -> header dari sebuah card