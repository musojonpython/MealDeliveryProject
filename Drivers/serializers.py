from rest_framework.serializers import ModelSerializer
from users.models import Users

class UserlistSerializer(ModelSerializer):
	class Meta:
		model = Users
		fields = [
			"first_name",
			"last_name",
			"telephone",
			"adress",
			
		]