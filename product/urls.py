from django.urls import path
from . import views

urlpatterns = [
    path("product-list/", views.product_list, name="product-list"),
    path("product/", views.product, name="product"),
]
