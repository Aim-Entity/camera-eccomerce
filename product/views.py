from django.shortcuts import render
from product.models import *
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from product.filters import ProductFilter


class ProductDetailView(DetailView):
    template_name = "product/product.html"
    model = Product
    context_object_name = "product"


def product_list(request):
    products = Product.objects.all()
    filtered_products = ProductFilter(
        request.GET,
        queryset=Product.objects.all()
    )

    paginated_filtered_products = Paginator(filtered_products.qs, 9)
    page_number = request.GET.get("page")
    product_page_obj = paginated_filtered_products.get_page(page_number)

    context = {
        "products": products,
        "filtered_products": filtered_products,
        "product_page_obj": product_page_obj
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
