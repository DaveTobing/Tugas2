from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, new_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('create-task/', new_task, name='new_task'), #sesuaikan dengan nama fungsi yang dibuat
]
    
    