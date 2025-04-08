from django.db import models
class Product(models.Model):
    ProductName = models.CharField(unique=True ,max_length=150)
    Image = models.TextField(max_length=100000)
    Category = models.CharField(max_length=50)
    Price = models.IntegerField(max_length=15)
    Stock = models.IntegerField()
    Brand = models.CharField(max_length=50)
    
