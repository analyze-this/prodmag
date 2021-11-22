from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer, FeedbackSerializer
from main_app.models import Product, Category
from rest_framework.response import Response
from rest_framework.decorators import api_view

from main_app.models import FeedbackModel


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


@api_view(['GET', 'POST'])
def categories_view(request):
	if request.method == 'POST':
		serializer = CategorySerializer(data=request.data)
		print("POST - ", serializer)
		if serializer.is_valid():
			print('vd')
			serializer.save()
			return Response(serializer.data)
		else:
			print(serializer.data)
			return Response(serializer.errors)
	else:
		data = Category.objects.all()
		print('data - ', data)
		serializer = CategorySerializer(data, many=True)
		return Response(serializer.data)


@api_view(['GET', 'POST'])
def feedback_view(request):
	if request.method == 'POST':
		serializer = FeedbackSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)
	else:
		feeds = FeedbackModel.objects.all()
		serializer = FeedbackSerializer(feeds, many=True)
		return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def feedbackupdate_view(request, pk):
	if request.method == 'PUT':
		feed = FeedbackModel.objects.get(pk=pk)
		serializer = FeedbackSerializer(feed, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)

	else:
		feeds = FeedbackModel.objects.all()
		serializer = FeedbackSerializer(feeds, many=True)
		return Response(serializer.data)


