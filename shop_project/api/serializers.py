from rest_framework import serializers

from main_app.models import Product, UnitOfMeasure, Category, CountryOfOrigin


class UnitOfMeasureSerializer(serializers.ModelSerializer):
	class Meta:
		model = UnitOfMeasure
		fields = ['unit_name']


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['category_name']


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

