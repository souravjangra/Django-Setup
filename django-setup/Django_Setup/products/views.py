from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)