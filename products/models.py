from django.db import models
from django.urls import reverse
from Category.models import category

# Create your models here.

class Products(models.Model):
    product_name = models.CharField(max_length=100 , unique=True)
    slug = models.SlugField(max_length=100, unique =True)
    description = models.TextField()
    price = models.CharField(max_length = 100)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='photos/product')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"

    def get_url(self):
        return reverse('product_detail',args = [self.category_slug, self.slug])




    def __str__(self):
        return self.product_name
