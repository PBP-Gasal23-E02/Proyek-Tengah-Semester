from django.urls import path
from YourBook.views import *
app_name = 'YourBook'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('tambah_stok/<int:id>/', tambah_stok, name='tambah_stok'),
    path('kurangi_stok/<int:id>/', kurangi_stok, name='kurangi_stok'),
    path('hapus_item/<int:id>/', hapus_item, name='hapus_item'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
]