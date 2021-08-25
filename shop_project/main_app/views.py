from django.shortcuts import render
from .models import *


def main_view(request):
    products = Product.objects.all()
    if 'price' in request.GET:
        price = request.GET.get('price')
        products = Product.objects.filter(product_price=price)
        if not products:
            products = Product.objects.all()
    return render(request, template_name='main.html', context={'products': products})
