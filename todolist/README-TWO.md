# Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Synchronous programming: poses jalannya program secara sequential , dimana terdapat antrian saat melakukan ekseskusi program. 

- Asynchronous programming: proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian

# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
 Event-Driven Programming - > sebuah tindakan yang dapat dibuat oleh user seperti klik mouse atau penekanan tombol. Setelah user melakukan tindakan tersebut maka program akan melakukan tugas lain seperti dalam sebuah HTML form jika tombol submit ditekan maka data - data yang telah diinput oleh user akan disimpan dalam sebuah server.

 # Jelaskan penerapan asynchronous programming pada AJAX.
 AJAX menerapkan metode asynchronous programming yang digunakan untuk melakukan permintaan data dan menangani tanggapan baik response dalam bentuk JSON atau XML dari sebuah API

 # Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- menambahakn function get_json untuk menampilkan data" pada website dalam bentuk json pada views.json
    ``` 
    def get_json(request):
        data = Task.objects.filter(user = request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

- menambahkan function add_task_ajax untuk menambahkan data - data pada modal secara Asynchronous pada views.json
        ```
        def add_task_ajax(request):
            if request.user.is_authenticated:
                form = create_form(request.POST)
                data = {}
            
                if request.method == 'POST' and form.is_valid():
                    title = form.cleaned_data['title']
                    description = form.cleaned_data['description']
                    new_task = Task.objects.create(title=title, description=description, user=request.user, date=datetime.date.today())
                    data['title'] = title
                    data['description'] = description
                    data['user'] = request.user
                    data['date'] = datetime.date.today()
                    return JsonResponse(data);

                context = {
                    'form': form,
                }
                return render(request, 'create-task.html', context)
            else:
                return redirect('todolist:login')
        ```

- menambahkan path json/ dan add/ pada file urls.py

- menambahkan link bootstrap CSS dan JS pada file HTMl agar bisa menggunakan AJAX dan tools bootstrap

- menambahkan function form_reset untuk reset isi dari form

- menambahkan function card_reset untuk menampilkan data data pada file json 

- menambahkan function add_task untuk menyimpan data data yang telah diinput