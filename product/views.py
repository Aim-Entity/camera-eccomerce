from django.shortcuts import render


def product(request):
    context = {

    }
    return render(request, "product/product.html", context)


def product_list(request):
    context = {

    }
    return render(request, "product/list.html", context)
