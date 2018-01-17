from django.shortcuts import render
from .models import Product

def cart_list(request):
    products = Product.objects.filter(cost=True).order_by('name')
    return render(request, 'internet_shop/cart_list.html', {'products': products})

