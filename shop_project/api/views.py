from django.shortcuts import render
from api.serializers import ProductSerializer
from main_app.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def product_view(request):
	if request.method == "POST":
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			Product.objects.create(**serializer.validated_data)
			return Response(serializer.data, status=201)
		else:
			return Response(serializer.errors)
	else:
		queryset = Product.objects.all()
		serializer = ProductSerializer(queryset, many=True)
		return Response(serializer.data)

