from django.urls import path
from bookmark.views import *

app_name = 'bookmark'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add_bookmark', add_bookmark, name='add_bookmark'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('get-bookmark/', get_bookmark_json, name='get_bookmark_json'),
    path('create-bookmark-ajax/', add_bookmark_ajax, name='add_bookmark_ajax'),
    path('remove-bookmark/<int:item_id>', remove_bookmark, name='remove_bookmark'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]