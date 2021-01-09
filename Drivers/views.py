from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserlistSerializer
from users.models import Users
from rest_framework.generics import  ListAPIView

# Create your views here.

class UsersListAPIView(ListAPIView):
	queryset 		 = Users.objects.all()
	serializer_class = UserlistSerializer

