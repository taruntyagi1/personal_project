from django.contrib import admin
from django.shortcuts import HttpResponse,render
from products.models import Products


def home(request):
    products  = Products.objects.all().filter(is_available = True)
    context = {
        'products' : products
    }
    return render(request, 'homepage.html',context)