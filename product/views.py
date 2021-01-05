from django.shortcuts import render
from .models import *


def product(request):
    context = {

    }
    return render(request, "product/product.html", context)


def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "product/list.html", context)
