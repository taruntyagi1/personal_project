from django.contrib import admin
from .models import Products

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price','stock','is_available','category','created_date']



admin.site.register(Products,ProductAdmin)
