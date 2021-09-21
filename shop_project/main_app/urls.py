from django.urls import path
from .views import *


app_name = 'main_app'
urlpatterns = [
    path('', MainWithCategory.as_view(), name='supermain'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='productdetail'),
    path('<int:category_id>/', MainWithCategory2.as_view(), name='supermain1'),
    path('main/', main_view, name='main'),
    path('view/', ClassView.as_view(), name='view'),
    path('templateview/', TemplateClassView.as_view(), name='templateview'),
    path('listview/', ClassListView.as_view(), name='listview'),
    path('detailview/<int:pk>/', MyDetailView.as_view(), name='detailview'),
    path('create_product/', create_product_view, name='create_product'),
]