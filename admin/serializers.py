from rest_framework.serializers import ModelSerializer
from foods.models import(
	Foods,
	Salads,
	Drinks
	)
from Drivers.models import Drivers
from users.models import Users 

class DriversCreateSerializer(ModelSerializer):
	class Meta:
		model = Drivers
		fields = [
		'id',
		'first_name',
		'last_name',
		'login',
		'password',
		'telephone',
		]

class DriversDetailSerializer(ModelSerializer):
	class Meta:
		model = Drivers
		fields = [
		'first_name',
		'last_name',
		'login',
		'password',
		'telephone',
		]

class FoodsCreateSerializer(ModelSerializer):
	class Meta:
		model = Foods
		fields = [
		'id',
		'title',
		'cost',
		'content',
		'images',
		]

class FoodsDetailSerializer(ModelSerializer):
	class Meta:
		model = Foods
		fields = [
			'title',
			'cost',
			'content',
			'images',
		]

class SaladsCreateSerializer(ModelSerializer):
	class Meta:
		model = Salads
		fields = [
		'id',
		'title',
		'cost',
		'content',
		'images',
		]

class SaladsDetailSerializer(ModelSerializer):
	class Meta:
		model = Salads
		fields = [
			'title',
			'cost',
			'content',
			'images',
		]

class DrinksCreateSerializer(ModelSerializer):
	class Meta:
		model = Drinks
		fields = [
			'id',
			'title',
			'cost',
			'content',
			'images',
			]

class DrinksDetailSerializer(ModelSerializer):
	class Meta:
		model = Drinks
		fields = [
			'title',
			'cost',
			'content',
			'images',
		]
		
class UsersListSerializer(ModelSerializer):
	class Meta:
		model = Users
		fields = [
			'id',
			'first_name',
			'last_name',
			'adress',
			'telephone',
		]
class UsersDetailSerializer(ModelSerializer):
	class Meta:
		model = Users
		fields = [
			'first_name',
			'last_name',
			'adress',
			'telephone',
		]

