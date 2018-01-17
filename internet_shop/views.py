from django.shortcuts import render

def cart_list(request):
    return render(request, 'internet_shop/cart_list.html', {})
