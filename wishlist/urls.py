
from wishlist.views import show_main, add_wishlist, show_xml, show_json, show_json_by_id, show_xml_by_id, remove_wishlist, add_wishlist_ajax, get_wishlist_json, logout_user, create_wishlist_flutter
from django.urls import path

app_name = 'wishlist'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-wishlist', add_wishlist, name='add_wishlist'),
    path('xml/', show_xml, name='show_xml'), 
    path('logout/', logout_user, name='logout'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('remove-wishlist/<int:item_id>', remove_wishlist, name='remove_wishlist'), 
    path('create-wishlist-ajax/', add_wishlist_ajax, name='add_wishlist_ajax'),
    path('get-wishlist/', get_wishlist_json, name='get_wishlist_json'),
    path('create-flutter/', create_wishlist_flutter, name='create_wishlist_flutter'),
]