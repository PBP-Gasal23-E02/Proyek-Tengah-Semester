from django.urls import path
from Publication.views import new_publication

app_name = 'main'

urlpatterns = [
    path('publication', new_publication, name='new_publication'),
]