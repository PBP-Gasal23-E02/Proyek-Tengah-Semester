from django.urls import path
from YourBook.views import *
app_name = 'YourBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('logout/', logout_user, name='logout'),
    path('get-product/<str:filter>', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
    path('get_jumlah_item/', get_jumlah_item, name='get_jumlah_item'),
    path('get-product-flutter/', get_product_json_flutter, name='get_product_json_flutter'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
     path('delete-flutter/', delete_item_flutter, name='delete_product_flutter'),
]