from django.urls import path
from publication.views import *

urlpatterns = [
    path('', your_publication, name='your_publication'),
    path('publication/', new_publication, name='new_publication'),
]