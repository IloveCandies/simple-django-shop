"""asupro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from maincontent.views import *
from ecommerce.views import *
from mailoperations.views import *


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    
    ##maincontent.views
    path('index/',main_page),
    path('contacts/',contacts_page),
    path('company/',company_page),
    path('requisites/',requisites_page),
    path('licensions/',licensions_page),
    path('partners/',partners_page),
    path('search/<q>/',search_results, name = 'search'),
    path('search/',search_page,name='empty_search' ),
    path('product/<product_slug>/',product, name = 'product'),
    path('catalog/<q>/',catalog_products, name = 'catalog'),
    
    ##ecommerce.views
    path('cart/',cart_detail),
    path('add/<product_slug>/',cart_add, name = 'add'),
    path('increase/<product_slug>/',cart_add, name = 'increase'),
    path('remove/<product_slug>/',cart_remove, name = 'remove'),
    path('decrease/<product_slug>/',decrease_item, name = 'decrease'),

    #mail
    path('subscribe/<followermail>/',subscribe, name = 'subscribe')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)