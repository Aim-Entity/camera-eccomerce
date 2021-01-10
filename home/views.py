from django.shortcuts import render, redirect
from product.models import *
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


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
    if request.method == "POST":
        contact = ContactForm(request.POST)

        if contact.is_valid():
            contact.save()

            name = contact.cleaned_data.get("fullname")
            message = contact.cleaned_data.get("message")
            email = contact.cleaned_data.get("email")
            send_mail(
                f"Contact Form: {name}",
                f"Message: \n{message}\nEmail: \n{email}",
                settings.EMAIL_HOST_USER,
                ["bilaluddin474@gmail.com"],
                fail_silently=False
            )  # Email sent to web owner or staff

            return redirect("home")

    else:
        contact = ContactForm()

    context = {
        "contact": contact
    }

    return render(request, "home/contact.html", context)
