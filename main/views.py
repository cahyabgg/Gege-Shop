from django.shortcuts import render,redirect
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

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
        book.user = request.user #Gajadi pake cookies
        book.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")