from django.forms import ModelForm
from .models import Product


class PruductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'ProductName' ,
            'Category' ,
            'Price' ,
            'Stock' ,
            'Brand' ,
            'Image' ,
        ]
    