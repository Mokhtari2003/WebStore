from django.forms import ModelForm
from .models import Product
import django.forms

class PruductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'ProductName' ,
            'Image' , 
            'Category' ,
            'Price' ,
            'Stock' ,
            'Brand' ,
        ]
    