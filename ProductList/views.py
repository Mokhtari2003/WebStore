from django.shortcuts import render
from addProduct.models import Product

def ProductList(request):
    Products = list(Product.objects.values(
            'ProductName' ,
            'Category' ,
            'Price' ,
            'Stock' ,
            'Brand' ,
            'Image' ,))
    
    for x in Products:
        print(f"image : {x["Image"]}")
        m = x['Image']
        x["Image"] = {
            "value" : m ,
            "url" : f"../media/{m}"
        }
        print("Image : ",x['Image'])
    print(Products)
    context = { 'products' : Products }
    return render(request , "ProductList/index.htm" ,context)

