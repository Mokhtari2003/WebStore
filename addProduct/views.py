from django.shortcuts import render
from .forms import PruductForm
def addproduct(request):
    ProductForm_V = PruductForm()
    return render(request ,"addProduct/index.htm" , {'Pform' : ProductForm_V})
