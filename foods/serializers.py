from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField
	)
from foods.models import (
	Foods,
	Salads,
	Drinks
	)

class FoodListSerializer(ModelSerializer):
	class Meta:
		model = Foods
		fields = [
		'title',
		'cost',
		'content',
		'images',
		 ]

class SaladListSerializer(ModelSerializer):
	class Meta:
		model = Salads
		fields = [
		'title',
		'cost',
		'content',
		'images',
		]

class DrinkListSerializer(ModelSerializer):
	class Meta:
		model = Drinks
		fields = [
		'title',
		'cost',
		'content',
		'images',
		]
