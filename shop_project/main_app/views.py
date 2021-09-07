from decimal import Decimal

from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from slugify import slugify


def main_view(request):
    products = Product.objects.all()
    form = FilterForm()
    if 'product_name' in request.GET:
        complex_request = []
        if request.GET.get('product_name'):
            complex_request.append(Q(product_name=request.GET['product_name']))
            products = products.filter(product_name=(request.GET['product_name']))
        if request.GET.get('product_price'):
            try:
                price = Decimal(request.GET['product_price'])
                if price >= 0:
                    if request.GET['gl'] == 'greater':
                        complex_request.append(Q(product_price__gt=price))
                        products = products.filter(product_price__gt=price)
                    else:
                        complex_request.append(Q(product_price__lt=price))
                        products = products.filter(product_price__gt=price)
                else:
                    return render(request, template_name='main.html', context={'products': products, 'form': form,
                                                                               'message': 'Цена должна быть числом выше 0'})
            except ValueError:
                return render(request, template_name='main.html', context={'products': products, 'form': form, 'message': 'Укажите цену в числовом формате'})
        if request.GET.get('category_name'):
            category_name_id = int(request.GET['category_name'])
            complex_request.append(Q(product_categories=category_name_id))
            products = products.filter(product_categories=category_name_id)
        print(complex_request)
    return render(request, template_name='main.html', context={'products': products, 'form': form})


def create_product_view(request):
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            form.cleaned_data['product_slug'] = slugify(form.cleaned_data['product_name'])
            form.save()
            return redirect('main')
    else:
        form = CreateProductForm()
        return render(request, template_name='create_product.html', context={'form': form})


