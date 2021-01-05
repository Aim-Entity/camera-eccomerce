from django.shortcuts import render
from product.models import *


def index(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {"get_cart_total": 0, 'get_cart_items': 0, "shipping": False}
        cartItems = order["get_cart_items"]

    products = Product.objects.all()
    p1 = Product.objects.all().filter(offer=True)[0]
    p2 = Product.objects.all().filter(offer=True)[1]
    p3 = Product.objects.all().filter(offer=True)[2]
    p4 = Product.objects.all().filter(offer=True)[3]
    p5 = Product.objects.all().filter(offer=True)[4]
    p6 = Product.objects.all().filter(offer=True)[5]
    context = {
        'products': products,
        "cartItems": cartItems,
        "p1": p1,
        "p2": p2,
        "p3": p3,
        "p4": p4,
        "p5": p5,
        "p6": p6,
    }
    return render(request, "home/index.html", context)


def contact(request):
    context = {

    }
    return render(request, "home/contact.html", context)
