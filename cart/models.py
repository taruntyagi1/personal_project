from django.db import models
from products.models import Products

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length = 100 , blank = True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Cart"


    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    


    class Meta:
        verbose_name_plural = "Cart Item"

    

