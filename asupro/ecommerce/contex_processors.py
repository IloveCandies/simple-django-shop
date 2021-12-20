from django.db import models
from django.urls import reverse
import os
from  .cart import Cart 
def cart(request):
    return{'cart': Cart(request)}
