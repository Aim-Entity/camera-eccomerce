from django.shortcuts import render


def checkout(request):
    context = {

    }
    return render(request, "cart/checkout.html", context)


def cart(request):
    context = {

    }
    return render(request, "cart/cart.html", context)
