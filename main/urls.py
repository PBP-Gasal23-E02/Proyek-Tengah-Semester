from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_awal, name='show_awal'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('maen/', show_main, name='show_main'),
    path("api/books/", get_books, name="get_books"),
    path("add-product-ajax/", add_product_ajax, name="add_product_ajax"),
    path("get-user/", get_user, name="get_user")
]