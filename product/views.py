from django.shortcuts import render


def product_list(request):
    context = {

    }
    return render(request, "product/list.html", context)
