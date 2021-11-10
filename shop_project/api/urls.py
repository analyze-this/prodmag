from django.urls import path
from api.views import product_view


urlpatterns = [
	path('', product_view)
]