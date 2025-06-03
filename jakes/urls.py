
from django.urls import path
from .views import (register_view,logout_view,login_view,product,
product_create,product_detail,product_delete,product_edit)

urlpatterns = [
    path('', product,name='product'),
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('product/create/',product_create,name='product_create'),
    path('product/<int:pk>/',product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
]