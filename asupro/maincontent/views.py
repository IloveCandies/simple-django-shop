from django.shortcuts import render
from decimal import Decimal
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

from maincontent.models import *
from ecommerce.cart import Cart
def main_page(request):
    cart = Cart(request)
    context = {'cart':cart}
    return render(request,'index-centred.html',context)

def company_page(request):
    cart = Cart(request)
    context = {'cart':cart}
    return render(request,'company.html',context)

def partners_page(request):
    cart = Cart(request)
    context = {'cart':cart}
    return render(request,'partners.html',context)

def requisites_page(request):
    cart = Cart(request)
    context = {'cart':cart}
    return render(request,'requisites.html',context)

def licensions_page(request):
    cart = Cart(request)
    context = {'cart':cart}
    return render(request,'documents.html',context)

def contacts_page(request):
    cart = Cart(request)  
    context = {'cart':cart}
    return render(request,'contacts.html',context)

def catalog_products(request,q):
    cart = Cart(request)
    if(q == "all"):   
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
        'categories':categories,
        'products':products,
        'cart':cart}
        return render(request,'catalog.html',context)
    else:
        categories = Category.objects.all()
        query_category = Category.objects.get(slug=q)
        products = Product.objects.filter(category=query_category)
        context = {
        'query_category':query_category,
        'categories':categories,
        'products':products,
        'cart':cart}
        return render(request,'catalog.html',context)
   
def product(request, product_slug):
    cart = Cart(request)
    product = Product.objects.get(slug = product_slug) 
    context = {
        'product':product,
        'cart':cart
    }
    return render(request,'product.html',context)

def search_results(request,q):
    cart = Cart(request)
    query_category = Category.objects.get(slug=q)
    categories = Category.objects.filter(Q(slug=q)|Q(name = q))
    products = Product.objects.filter(Q(category=query_category)|Q(title = q)|Q(text =q))
    maincontent = MainPageContent.objects.filter(content = q)
    parterscontent = PartnersPageContent.objects.filter(Q(link = q))
    requisitescontent = RequsitesPageContent.objects.filter(Q(first_column = q)| Q(second_column =q))
    context = {
        'categories':categories,
        'products':products,
        'maincontent':maincontent,
        'parterscontent':parterscontent,
        'requisitescontent':requisitescontent,
        'cart':cart,
        }
    return render(request,'results.html',context)

def search_page(request):
    cart = Cart(request)
    return render(request,'results.html', {'cart': cart})
