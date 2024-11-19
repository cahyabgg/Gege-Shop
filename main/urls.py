from django.urls import path
from main.views import (
    show_main,create_product,show_json,
    show_json_by_id,show_xml,show_xml_by_id,
    register,user_login,logout_user,
    edit_product,delete_product,welcome,
    add_product_ajax,create_product_flutter
    )

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path("json/",show_json, name= "show_json"),
    path("xml/",show_xml, name= "show_xml"),
    path("json/<int:id>/",show_json_by_id,name="show_json_by_id"),
    path("xml/<int:id>/",show_xml_by_id,name="show_xml_by_id"),
    path("login/",user_login,name= "login"),
    path("register/",register,name="register"),
    path("logout/",logout_user,name="logout"),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete-product/<int:id>', delete_product, name='delete_product'),
    path("welcome/",welcome, name="welcome"),
    path('create-product-ajax', add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_book_flutter'),
]