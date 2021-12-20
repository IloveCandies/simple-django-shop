from django.contrib import admin

from ecommerce.models import *
# Register your models here.

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display=('product','quantity','cost','total')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('total',)

@admin.register(Order)
class CartAdmin(admin.ModelAdmin):
    list_display=('id','first_name','email','created','paid')

@admin.register(OrderItem)
class CartAdmin(admin.ModelAdmin):
    list_display=('id','order','product','price','quantity')
    
