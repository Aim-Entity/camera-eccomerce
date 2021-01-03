from django.shortcuts import render


def index(request):
    context = {

    }
    return render(request, "home/index.html", {})


def contact(request):
    context = {

    }
    return render(request, "home/contact.html", context)
