from django.db import models

from django.db import models
from django.contrib.auth.models import User

PRODUCT_TYPE = (
    ('cameras', 'cameras'),
    ('drones', 'drones'),
    ('recorders', 'recorders'),
    ('lighting', 'lighting'),
    ('other', 'other'),
)


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    offer = models.BooleanField(default=False, null=True, blank=False)
    slug = models.SlugField(default="Change-me", max_length=300)
    product_type = models.CharField(choices=PRODUCT_TYPE,
                                    null=True, blank=True, default=PRODUCT_TYPE[-1], max_length=100)

    detail_one = models.CharField(
        max_length=2000, null=True, blank=False, default="Erat nam at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales neque. d donec ultrices tincidunt arcu non sodales neque. tincidunt arcu non sodales neque.")
    title_one = models.CharField(
        max_length=200, null=True, blank=False, default="The Best Quality Photos")
    detail_two = models.CharField(
        max_length=2000, null=True, blank=False, default="Erat nam at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales.")
    title_two = models.CharField(
        max_length=200, null=True, blank=False, default="Long Lasting Battery")
    detail_three = models.CharField(
        max_length=2000, null=True, blank=False, default="Erat nam at lectus urna duis convallis convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales.")

    weight = models.IntegerField(null=True, blank=True, default=175)
    spec_type = models.CharField(
        max_length=120, null=True, blank=True, default="Compact")

    height = models.IntegerField(null=True, blank=True, default=100)
    width = models.IntegerField(null=True, blank=True, default=100)
    depth = models.IntegerField(null=True, blank=True, default=100)
    pixels = models.FloatField(null=True, blank=True)
    aspect_ratio = models.CharField(
        max_length=40, null=True, blank=True, default="3:2")
    colour_filter = models.CharField(
        max_length=120, null=True, blank=True, default="Standard")

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = 0
        for item in orderitems:
            total += item.get_total

        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = 0
        for item in orderitems:
            total += item.quantity

        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)

    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)

    quantity = models.IntegerField(default=0, null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)

    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, blank=True)

    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
