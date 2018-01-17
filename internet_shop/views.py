from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
from django.shortcuts import redirect

def cart_list(request):
    products = Product.objects.filter(name='Продукт').order_by('name')
    return render(request, 'internet_shop/cart_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'internet_shop/product_detail.html', {'product': product})

def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'internet_shop/product_edit.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            product.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'internet_shop/product_edit.html', {'form': form})