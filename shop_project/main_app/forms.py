from django import forms
from .models import *


class FilterForm(forms.Form):
    category_name = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория товара',  required=False, widget=forms.Select())
    product_name = forms.CharField(label='Наименование товара', required=False)
    gl = forms.CharField(widget=forms.Select(choices=[('greater', '>'), ('less', '<')]),
                         label='', required=False)
    product_price = forms.DecimalField(label='Цена товара', required=False)


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_categories', 'product_countriesoforigin', 'product_quantity',
                  'product_units', 'product_price', 'product_description', 'product_image', 'is_available']
        widgets = {'product_name': forms.TextInput(attrs={'id': 'product_input', 'placeholder': 'Введите название товара'})}





