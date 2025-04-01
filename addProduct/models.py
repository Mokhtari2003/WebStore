from django.db import models
class Product(models.Model):
    ProductID = models.GenericIPAddressField(unique=True)
    ProductName = models.CharField(unique=True ,max_length=150)
    Category = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=9 , decimal_places=2)
    Stock = models.IntegerField()
    Brand = models.CharField(max_length=50)
    Image = models.ImageField()
    
