from django.db import models
class Product(models.Model):
    ProductID = models.IPAddressField(unique=True)
    ProductName = models.CharField(unique=True)
    Category = models.CharField()
    Price = models.DecimalField()
    Stock = models.IntegerField()
    Brand = models.CharField()
    Image = models.ImageField()
