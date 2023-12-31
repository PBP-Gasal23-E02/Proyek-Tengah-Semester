from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_awal, name='show_awal'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('main/', show_main, name='show_main'),
    path("api/books/", get_books, name="get_books"),
    path("add-product-ajax/", add_product_ajax, name="add_product_ajax"),
    path("get-user/", get_user, name="get_user"),
    path("get-buku/", get_buku, name="get_buku"),
     path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]