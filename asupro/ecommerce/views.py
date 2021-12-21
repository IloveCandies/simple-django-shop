from django.shortcuts import render
from decimal import Decimal
from django.http import HttpResponseRedirect, HttpResponse
from .cart import Cart
from maincontent.models import Product, Category,Brand
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST


def cart_add(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    cart.add(product=product, quantity=1,update_quantity = False)
    return HttpResponseRedirect('/catalog/all')
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_slug)
    cart.remove(product)
    return HttpResponseRedirect('/cart')
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})

def increase_item(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    cart.add(product=product, quantity=1,update_quantity = False)
    return HttpResponseRedirect('/cart/')

def decrease_item(request,product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    cart.decrease(product=product, quantity=1,update_quantity = False)

    return HttpResponseRedirect('/cart/')


