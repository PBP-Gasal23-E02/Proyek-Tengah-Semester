from django.urls import path
from publication.views import *

app_name = 'publication'

urlpatterns = [
    path('your-publication/', show_main, name='show_main'),
    path('publication/', new_publication, name='new_publication'),
]