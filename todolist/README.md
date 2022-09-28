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
``` html
    
- action untuk menentukan aksi yang akan dilakukan saat data dikirim dengan mengisi dengan sebuah url 
- method metode pengiriman data bisa GET atau POST dimana POST akan mengirimkan data langsung ke action untuk ditampung, tanpa menampilkan pada URL sedangkan method   GET akan menampilkan data/nilai pada URL, kemudian akan ditampung oleh action

Dan didalam sebuah form perlu sebuah Field yang merupakan sebuah ruas yang dapat diisi dengan data.
Contoh field:
    
``` 
<input type="text" name="info" />
```html
    
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

