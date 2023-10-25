from django.urls import path
from YourBook.views import show_main

app_name = 'YourBook'

urlpatterns = [
    path('', show_main, name='show_main'),
]