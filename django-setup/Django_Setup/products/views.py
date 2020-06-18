from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)