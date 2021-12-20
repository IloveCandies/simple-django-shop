from django.db import models
from django.urls import reverse
from django.db.models import F
import os
from tinymce.models import HTMLField
from maincontent.models import Product 
# Create your models here.


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    cost = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)
    total = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)
    
    def save(self, *args, **kwargs):
        self.cost = self.product.cost
        self.total = self.quantity * self.cost
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(self.product)

class PromoCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30,)
    title = models.CharField(max_length=30,)
    total = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)
    
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100,)
    products = models.ManyToManyField(CartItem)
    promocodes = models.ManyToManyField(PromoCode)
    total = models.DecimalField(max_digits=9, decimal_places=2,default = 0.00)

    def get_products(self):
        return "\n".join([str(p.product) for p in self.products.all()])

    def __unicode__(self):
        return str(self.id)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
 
    class Meta:
        ordering = ('-created',)
 
    def __str__(self):
        return 'Order {}'.format(self.id)
 
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
 
 
class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
 
    def __str__(self):
        return '{}'.format(self.id)
 
    def get_cost(self):
        return self.price * self.quantity