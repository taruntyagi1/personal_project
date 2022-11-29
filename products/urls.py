from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from .import views



urlpatterns = [
    path('',views.store , name = 'store'),
    path('<slug:Category_slug>/',views.store ,name='product_category'),
    path('<slug:Category_slug>/<slug:products_slug>/',views.product_detail ,name = "product_detail")
]
