from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_slug')
    prepopulated_fields = {'category_slug': ('category_name', )}
    list_display_links = ('category_name', )


@admin.register(CountryOfOrigin)
class CountryOfOriginAdmin(admin.ModelAdmin):
    list_display = ('id', 'countryoforigin_name', 'countryoforigin_slug')
    prepopulated_fields = {'countryoforigin_slug': ('countryoforigin_name', )}
    list_display_links = ('countryoforigin_name', )


@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_name')
    list_display_links = ('unit_name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_description', 'product_price', 'product_quantity',
                    'product_units', 'product_image', 'is_available', 'product_countriesoforigin')
    prepopulated_fields = {'product_slug': ('product_name', )}
    list_editable = ('product_price', 'product_quantity', 'is_available')
