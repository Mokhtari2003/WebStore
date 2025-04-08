from django.shortcuts import render
from addProduct.models import Product

def ProductList(request):
    Products = list(Product.objects.values(
            'ProductName' ,
            'Category' ,
            'Price' ,
            'Stock' ,
            'Brand' ,
            'Image' ,).order_by("Brand" ,"Category" ,"Price"))
    
    for x in Products:
        if len(x['Image']) < 1000 :
            m = x['Image']
            x["Image"] = {
                "value" : m ,
                "url" : f"../media/{m}"
            }
        else :
            m = x['Image']
            x["Image"] = {
                "value" : x['ProductName'] ,
                "url" : f"{m}"
            }
    context = { 'products' : Products }
    return render(request , "ProductList/index.htm" ,context)


def rid(request ,data):
    selected_dataCATEGORY = list(Product.objects.values("Category"))
    selected_dataCATEGORY_remake = []
    for item in selected_dataCATEGORY :
        m = item["Category"]
        selected_dataCATEGORY_remake.append(m)
    selected_dataCATEGORY_remake = list(set(selected_dataCATEGORY_remake))
    selected_dataBRAND = list(Product.objects.values("Brand"))
    selected_dataBRAND_remake =[]
    for item in selected_dataBRAND :
        m = item['Brand']
        selected_dataBRAND_remake.append(m)
    selected_dataBRAND = list(set(selected_dataBRAND_remake))
    if data in selected_dataCATEGORY_remake:
        main_d = Product.objects.filter(Category = data).values(
            'ProductName' ,
            'Category' ,
            'Price' ,
            'Stock' ,
            'Brand' ,
            'Image' ,
        )
        for x in main_d:
            if len(x['Image']) < 1000 :
              m = x['Image']
              x["Image"] = {
                  "value" : m ,
                  "url" : f"../media/{m}"
              }
            else :
                m = x['Image']
                x["Image"] = {
                    "value" : x['ProductName'] ,
                    "url" : f"{m}"
                }
        
        print(main_d)
        context = { "products" : main_d }
        return render(request , "ProductList/index.htm" , context)
    elif data in selected_dataBRAND_remake:
        main_d = Product.objects.filter(Brand = data).values(
            'ProductName' ,
            'Category' ,
            'Price' ,
            'Stock' ,
            'Brand' ,
            'Image' ,
        )
        for x in main_d:
            if len(x['Image']) < 1000 :
              m = x['Image']
              x["Image"] = {
                  "value" : m ,
                  "url" : f"../media/{m}"
              }
            else :
                m = x['Image']
                x["Image"] = {
                    "value" : x['ProductName'] ,
                    "url" : f"{m}"
                }
        print(main_d)
        context = { "products" : main_d }
        return render(request , "ProductList/index.htm" , context)
    
    # data

