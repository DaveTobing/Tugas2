# Link heroku


# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>

kegunaan csrf_token adalah sejenis token yang mencegah penyerangan CSRF sehingga token ini harus unik agar penyerang susah untuk menebak . Jika sebuah form tidak ada token tersebut maka akan terdapat serangan CSRF yang membuat penyerang tidak dapat membuat permintaan yang valid ke server.


# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.


# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

user akan melakukan HTTP Request ke http://host/path pada broswer dan server akan menerima HTTP request tersebut dan menyesuaikan dengan user pada kasus user akan mengisi sebuah form  maka server akan membuat sebuah halaman HTML berjenis form pada browser yang dimana user akan menginput data- data yang diperlukan pada halaman browwser tersebut dan setelah user sudah siap mengisi data - data tersebut maka server akan menyimpan input dari user dan akan disimpan pada server dan kemudian data - data tersebut akan ditampilkan pada halaman broswer sesuai dengan path yang dihasilkan di views.py

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

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

