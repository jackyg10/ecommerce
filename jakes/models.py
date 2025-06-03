from django.db import models
from django.contrib.auth.models import User
# Create your models here ..a
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to="product/")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

'''
class cart(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    quantity=models.PositiveIntegerField(default=1)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username}.s cast"                                                                                                                                                                                                                                                                                                                                         
        '''