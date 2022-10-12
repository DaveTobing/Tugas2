from audioop import add
import datetime
from hashlib import new
import json
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from todolist.forms import create_form
from todolist.models import Task
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    if request.user.is_authenticated:
        data = Task.objects.filter(user = request.user)
        last_login_info = request.COOKIES.get('last_login', 'not found')
        if (last_login_info == 'not found'):
            return redirect('todolist:login')
        context = {
            'list': data,
            'user_name': request.user.username,
            'last_login': request.COOKIES.get('last_login', 'not found'),
        }
        return render(request, "todolist.html", context)

    else:
        return redirect('todolist:login')


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/todolist/login/')
def new_task(request):
    if request.user.is_authenticated:
        my_form = create_form()
        if request.method == 'POST':
            my_form = create_form(request.POST)
            if my_form.is_valid():
                title = my_form.cleaned_data['title']
                description = my_form.cleaned_data['description']
                newtask = Task.objects.create( title=title, description=description, user=request.user, date= datetime.date.today())
                return redirect('todolist:show_todolist')

        context = {'form': my_form}
        return render(request, 'create-task.html', context)    
    else:
        return redirect('todolist:login')


def get_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url='/todolist/login/')
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

        # context = {
        #     'form': form,
        # }
        # return render(request, 'create-task.html', context)
    else:
        return redirect('todolist:login')