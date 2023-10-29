from django.urls import path
from publication.views import *

app_name = 'publication'

urlpatterns = [
    path('your-publication/', show_main, name='show_main'),
    path('publication/', new_publication, name='new_publication'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]