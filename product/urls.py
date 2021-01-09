from django.urls import path
from . import views

urlpatterns = [
    path("product-list/", views.product_list, name="product-list"),
    path("product-camera/", views.product_camera, name="product-camera"),
    path("product-drone/", views.product_drone, name="product-drone"),
    path("product-recorder/", views.product_recorder, name="product-recorder"),
    path("product-lighting/", views.product_lighting, name="product-lighting"),

    path("product/<str:slug>", views.ProductDetailView.as_view(),
         name="product-detail"),
]
