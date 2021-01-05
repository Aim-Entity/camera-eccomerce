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


def product_camera(request):
    products = Product.objects.all().filter(product_type="cameras")
    context = {
        "products": products,
    }
    return render(request, "product/camera.html", context)


def product_drone(request):
    products = Product.objects.all().filter(product_type="drones")
    context = {
        "products": products,
    }
    return render(request, "product/drone.html", context)


def product_recorder(request):
    products = Product.objects.all().filter(product_type="recorders")
    context = {
        "products": products,
    }
    return render(request, "product/recorder.html", context)


def product_lighting(request):
    products = Product.objects.all().filter(product_type="lighting")
    context = {
        "products": products,
    }
    return render(request, "product/lighting.html", context)
