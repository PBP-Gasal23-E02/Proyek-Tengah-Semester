from django.urls import path
from bookmark.views import *

urlpatterns = [
    path('bookmark/bookmarked_book/', all_bookmarked, name='all_bookmarked'),
    path('bookmark/add/<int:buku_id>/', add_bookmark, name='add_bookmark'),
    path('bookmark/remove/<int:buku_id>/', remove_bookmark, name='remove_bookmark'),
]