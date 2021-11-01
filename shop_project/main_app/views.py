from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View, TemplateView

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
                return render(request, template_name='main.html', context={'products': products, 'form': form,
                                                                           'message': 'Укажите цену в числовом формате'})
        if request.GET.get('category_name'):
            category_name_id = int(request.GET['category_name'])
            complex_request.append(Q(product_categories=category_name_id))
            products = products.filter(product_categories=category_name_id)
        print(complex_request)
    return render(request, template_name='main.html', context={'products': products, 'form': form})


@login_required
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


class ClassView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, template_name='view.html', context={'message': 'Hello', 'products': products})

    def post(self, request):
        return redirect('main_app:main')


class TemplateClassView(TemplateView):
    template_name = 'templateview.html'
    extra_context = {'message': 'Hello again!'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['key'] = 'New page'
        print(**kwargs)
        print(self.request.__dict__)
        return context


class ClassListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'listview.html'


class MyDetailView(DetailView):
    model = Product
    template_name = 'detailview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("context befor: ", context)
        context['category'] = Category.objects.all()
        print('context after: ', context)
        return context


class MainWithCategory(ListView):
    model = Product
    template_name = 'supermain1.html'
    # paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_list = Category.objects.all()
        context['categories'] = categories_list
        return context


class MainWithCategory2(ListView):
    model = Product
    template_name = 'supermain1.html'
    paginate_by = 3

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        qs = super().get_queryset()
        category = get_object_or_404(Category, pk=category_id)
        products = qs.filter(product_categories=category)
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_list = Category.objects.all()
        context['categories'] = categories_list
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_list = Category.objects.all()
        context['categories'] = categories_list
        return context
