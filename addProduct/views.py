from django.shortcuts import render
from .forms import PruductForm
def addproduct(request):
    if request.method == 'POST':
        ProductForm_V = PruductForm(request.POST ,request.FILES)
        print(request.POST ,ProductForm_V.is_valid())
        if ProductForm_V.is_valid():
            ProductForm_V.save()
            print("sucsessfully added")
        else:
            print(ProductForm_V.errors)
    return render(request ,"addProduct/index.htm" , {'Pform' : PruductForm()})
