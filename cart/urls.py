from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from .import views



urlpatterns = [
    path('',views.cart, name = 'cart'),
  
    path('add_cart/<int:product_id>/',views.add_cart ,name='add_cart')
]
