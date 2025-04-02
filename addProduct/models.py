from django.db import models
class Product(models.Model):
    ProductName = models.CharField(unique=True ,max_length=150)
    Image = models.ImageField(upload_to= "ProductImage/")
    Category = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=9 , decimal_places=1)
    Stock = models.IntegerField()
    Brand = models.CharField(max_length=50)
    
