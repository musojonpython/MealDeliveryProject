from rest_framework.generics import  CreateAPIView
from users.models import Users , UsersFoods
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import UsersCreateSerializer, UserFoodCreateSerializer
from rest_framework.views import APIView


class UserCreateAPIView(CreateAPIView):
	queryset         = Users.objects.all()
	serializer_class = UsersCreateSerializer

'''
	renderer_classes = [TemplateHTMLRenderer]
	template_name    = 'reservation.html'
	def get(self, request):
		queryset_user    = Users.objects.all()
		contex      = {'users' : queryset_user}	 
		return Response(contex)
'''

class UserFoodAPIView(CreateAPIView):
	queryset 		 = UsersFoods.objects.all()
	serializer_class = UserFoodCreateSerializer
