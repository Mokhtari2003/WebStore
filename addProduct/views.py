from django.shortcuts import render
from .forms import PruductForm
from . import image_to_base64
def addproduct(request):
    if request.method == 'POST':
        requestPOSTandIMG = request.POST.copy()
        requestPOSTandIMG['Image'] = image_to_base64.imgToBase64(request.FILES['Image'])
        ProductForm_V = PruductForm(requestPOSTandIMG)
        
        if ProductForm_V.is_valid():
            ProductForm_V.save()
            print("sucsessfully added")
        else:
            print(ProductForm_V.errors)
    return render(request ,"addProduct/index.htm" , {'Pform' : PruductForm()})
