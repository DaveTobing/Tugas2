## TUGAS PBP 3

#links
html : https://tugas3-pbp.herokuapp.com/mywatchlist/html/
json : https://tugas3-pbp.herokuapp.com/mywatchlist/json/
xml : https://tugas3-pbp.herokuapp.com/mywatchlist/xml/


# Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON = JavaScript Object Notation atau yang lebih dikenal dengan JSON adalah merupakan sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna. Biasanya, file JSON berisikan teks.

XML = XML adalah bahasa markup yang dirancang untuk menyimpan data. XML popular digunakan untuk transfer data.  XML dapat menentukan elemen markup dan menghasilkan bahasa markup yang disesuaikan. Unit dasar dalam XML dikenal sebagai elemen.

HTML = HTML (HyperText Markup Language) adalah bahasa yang menggunakan tanda-tanda tertentu (tag) untuk menyatakan kode-kode yang harus ditafsirkan oleh browser agar halaman tersebut dapat ditampilkan secara benar.

Perbedaanya adalah:
1) cara menyimpan elemen,  JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien.

2) JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. Sedangkan XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan.

3) Nama dari file JSON akan diakhiri dengan ekstensi .json, file XML akan diakhiri dengan ekstensi .xml. dan file HTML akan diakhir dengan .html

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
sebuah proses dalam transfer data-data yang ingin ditampilkan pada sebuah web
caranya:
1) browser request halaman html dan server akan mengembalikan sebuah file HTML
2) browser request style sheet dan server akan mengembalikan sebuah file css
3) browser request JPG image dan server akan mengemablikan sebuah file JPG
4) browser request Javascript code dan server akan mengembalikan sebuah file JS 
5) browser request data dan server akan mengembalikan sebuah data dalam bentuk XML/JSON

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama melakukan perintah python manage.py startapp mywatchlist yang berguna untuk membuat sebuah django-app dan folder bernama mywatchlist dan kemudian tambahkan mywatchlist pada INSTALLED_APPS di file settings.py di folder project_django. Kemudian membuat sebuah function di file models.py di folder mywatchlist untuk menyimpan semua data-data ke server django.

class MyWatchList(models.Model):
    watched = models.CharField(max_length=50)
    title = models.TextField()
    rating = models.IntegerField()
    release_date =  models.TextField()
    review =  models.TextField()

Kedua membuat file json bernama initial_mywatchlist_data.json di folder fixtures yang terdapat pada folder mywatchlist dan mengisikan 10 jenis data" yang mempunyai atribut watched,title,rating,release_date,review

Ketiga membuat 4 function pada file views.py di dalam folder mywatchlist yang berguna untuk mengembalikan data-data dalam bentuk JSON,XML dan html

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_html(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
    'list_movie': data_watchlist,
    }
    return render(request, "mywatchlist.html", context)


def show_start(request):
    context = {
    'nama': 'Dave Matthew Peter Lumban Tobing',
    'NPM' : '2106700870'
    }
    return render(request, "start.html", context)

Dan kemudian untuk melihat isi dari json.xml dan html maka lakukan "python manage.py runserver" pada cmd dan buka http://localhost:8000/start/ pada browser jika ingin lihat mywatchlist dalam bentuk html maka http://localhost:8000/mywatchlist/html jika ingin lihat dalam bentuk json maka http://localhost:8000/mywatchlist/json dan jika ingin dalam bentuk xml maka http://localhost:8000/mywatchlist/xml

# Mengakses tiga URL di poin 6 menggunakan Postman, menangkap screenshot, dan menambahkannya ke dalam README.md
-- html--
![Screenshot 2022-09-20 215915](https://user-images.githubusercontent.com/112268258/191300021-17e0a85a-ad65-423d-ae86-4207cc84311c.png)

-- json --
![Screenshot 2022-09-20 215934](https://user-images.githubusercontent.com/112268258/191300167-ef3eff9c-78c1-4fad-8ce6-4270635fc9d6.png)

-- xml --
![Screenshot 2022-09-20 215953](https://user-images.githubusercontent.com/112268258/191300224-37bfabe0-b3b8-42d7-b775-03b77b95b059.png)


