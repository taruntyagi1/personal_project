from django.db import models

# Create your models here.

class category(models.Model):
    category_name = models.CharField(max_length= 200 , unique = True,)
    slug = models.SlugField(max_length=100, unique = True)
    Image = models.ImageField(upload_to='photos/Category', null = False , blank= False)
    description = models.TextField(null = True, blank= True)

    class Meta:
        # verbose_name = "category"
        verbose_name_plural = "category"



    def __str__(self):
        return self.category_name
