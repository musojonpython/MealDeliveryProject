from rest_framework.serializers import ModelSerializer
from users.models import Users , UsersFoods


class UsersCreateSerializer(ModelSerializer):
	class Meta:
		model = Users
		fields = [
		'first_name',
		'last_name',
		'telephone',
		'adress',
		 ]

class UserFoodCreateSerializer(ModelSerializer):
	class Meta:
		model = UsersFoods
		fields = [
		'foodsid',
		'usersid',
		'count',
		'foodstype',
		]
		