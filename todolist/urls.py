from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    path('create-task/', new_task, name='new_task'), 
    path('json/', get_json, name = 'get_json'),
    path('add/', add_task_ajax, name = 'add_task_ajax')
]
    
    