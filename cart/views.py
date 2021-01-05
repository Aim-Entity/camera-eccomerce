from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from product.models import *
from django.http import JsonResponse
import json
import datetime


def checkout(request):
    context = {

    }
    return render(request, "cart/checkout.html", context)


def cart(request):
    context = {

    }
    return render(request, "cart/cart.html", context)
