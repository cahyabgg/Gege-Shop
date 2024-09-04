from django.shortcuts import render,redirect
from main.models import Product
from main.forms import ProductForm

# Create your views here.

def show_main(request):
    product = Product.objects.all()

    context = {
        "name" : "Cahya Bagus Gautama Gozales",
        "npm" : "2306275380",
        "class" : "PBP C",
        "products" : product 
    }

    return render(request,"main.html",context)

def create_product(request):

 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
    book = form.save(commit=False)
    book.user = request.user
    book.save()
    return redirect('main:show_main')

 context = {'form': form}
 return render(request, "create_product.html", context)
