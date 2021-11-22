from rest_framework import serializers

from main_app.models import Product, UnitOfMeasure, Category, CountryOfOrigin
from slugify import slugify

from main_app.models import FeedbackModel


class UnitOfMeasureSerializer(serializers.ModelSerializer):
	class Meta:
		model = UnitOfMeasure
		fields = ['unit_name']


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'

	def create(self, validated_data):
		category_name = validated_data.get('category_name', 'default slug')
		validated_data['category_slug'] = slugify(category_name)
		# print(category_name)
		# category_slug = slugify(category_name)
		return Category.objects.create(**validated_data)

	def update(self, instance, validated_data):
		pass


class CountryOfOriginSerializer(serializers.Serializer):
	countryoforigin_name = serializers.CharField()
	countryoforigin_code = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
	# product_units = serializers.StringRelatedField()
	product_units = serializers.StringRelatedField(source='product_units.new_str')
	product_categories = CategorySerializer(many=True)

	class Meta:
		model = Product
		exclude = ['product_slug', 'is_available']
		# depth = 1


class FeedbackSerializer(serializers.ModelSerializer):
	class Meta:
		model = FeedbackModel
		fields = '__all__'

	def create(self, validated_data):
		return FeedbackModel.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.product_name = validated_data.get(validated_data['product_name'], instance.product_name)
		instance.title = validated_data.get(validated_data['title'], instance.title)
		instance.content = validated_data.get(validated_data['content'], instance.content)
		instance.save()
		return instance

