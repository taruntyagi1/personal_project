from django.shortcuts import render,get_object_or_404
from .models import Products
from Category.models import category

# Create your views here.



def store(request,Category_slug=None):
    Category = None
    products = None
    if Category_slug!=None:
        Category = get_object_or_404(category,slug = Category_slug)
        products = Products.objects.filter(category = Category, is_available = True)

    else:

        products = Products.objects.all().filter(is_available = True)
    context = {
        'product' : products
    }
    return render(request, 'store.html',context)



def product_detail(request,Category_slug,products_slug):
    try:
        single_product = Products.objects.get(category__slug = Category_slug, slug = products_slug)

    except Exception as e:
        raise e

    context = {
        'single_product' : single_product
    }

    return render(request, 'store.html',context)


