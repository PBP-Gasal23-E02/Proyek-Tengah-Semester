<<<<<<< HEAD
from django.urls import path
from main.views import *
=======
from django.urls import include, path
from main.views import show_main
>>>>>>> df978eff73c00fa7e4fccc0276cc1cb9452a89ca

app_name = 'main'

urlpatterns = [
    path('', show_awal, name='show_awal'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('main/', show_main, name='show_main'),
]