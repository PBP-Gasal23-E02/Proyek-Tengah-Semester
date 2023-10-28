from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_awal, name='show_awal'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('main/', show_main, name='show_main'),
    path("api/books/", get_books, name="get_books"),
    path('logout/', logout_user, name='logout'),
]