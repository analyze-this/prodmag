from django.urls import path
from .views import *


app_name = 'main_app'
urlpatterns = [
    path('main/', main_view, name='main'),
    path('create_product/', create_product_view, name='create_product'),
]