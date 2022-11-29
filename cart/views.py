from django.shortcuts import render,redirect,HttpResponse
from products.models import Products
from cart.models import (
    Cart,
    CartItem
)

# Create your views here.
def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product  = Products.objects.get(id = product_id)
    try:
        cart = Cart.objects.get(cart_id = cart_id(request))

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = cart_id(request)
        )

    try:
        cart_item = CartItem.objects.get(product = product, cart = cart)

        cart_item.quantity += 1
        cart_item.save()

    except:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()


    
    return redirect('cart')
     
    

        



def cart(request, total = 0 , quantity = 0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id = cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active = True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

    except Exception as e:
            pass

    context = {
        'total' : total,
        'quantity' : quantity,
        'cart_items' : cart_items,
    }

   

    return render(request, 'cart.html',context)


