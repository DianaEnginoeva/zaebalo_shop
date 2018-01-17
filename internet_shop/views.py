from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404

def cart_list(request):
    products = Product.objects.filter(cost=True).order_by('name')
    return render(request, 'internet_shop/cart_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'internet_shop/product_detail.html', {'product': product})
