from django.shortcuts import render
from rest_framework.views import APIView
from Drivers.models import Drivers
from users.models import Users
from rest_framework.generics import  (
	CreateAPIView, 
	ListAPIView,
	UpdateAPIView,
	DestroyAPIView,
	RetrieveAPIView,
	)
from foods.models import (
	Foods,
	Salads, 
	Drinks,
	)
from .serializers import (
	SaladsCreateSerializer,
	SaladsDetailSerializer,

	FoodsCreateSerializer, 
	FoodsDetailSerializer,
	
	DrinksCreateSerializer,
	DrinksDetailSerializer,
	
	DriversCreateSerializer,
	DriversDetailSerializer,
	
	UsersListSerializer,
	UsersDetailSerializer,
	)

class DriverCreateAPIView(CreateAPIView):
	queryset 		 = Drivers.objects.all()
	serializer_class = DriversCreateSerializer

class DriverUpdateAPIView(UpdateAPIView):
	queryset		 = Drivers.objects.all()
	serializer_class = DriversDetailSerializer
	lookup_field     = 'id'

class DriverDeleteAPIView(DestroyAPIView):
	queryset		 = Drivers.objects.all()
	serializer_class = DriversDetailSerializer
	lookup_field     = 'id'

class DriverDetailAPIView(RetrieveAPIView):
	queryset		 = Drivers.objects.all()
	serializer_class = DriversDetailSerializer
	lookup_field     = 'id'

class DriverListAPIView(ListAPIView):
	queryset		 = Drivers.objects.all()
	serializer_class = DriversCreateSerializer

class FoodsCreateAPIView(CreateAPIView):
	queryset  		 = Foods.objects.all()
	serializer_class = FoodsCreateSerializer

class FoodsListAPIView(ListAPIView):
	queryset		 = Foods.objects.all()
	serializer_class = FoodsCreateSerializer

class FoodsUpdateAPIView(UpdateAPIView):
	queryset		 = Foods.objects.all()
	serializer_class = FoodsDetailSerializer
	lookup_field     = 'id'

class FoodsDeleteAPIView(DestroyAPIView):
	queryset		 = Foods.objects.all()
	serializer_class = FoodsDetailSerializer
	lookup_field     = 'id'

class FoodsDetailAPIView(RetrieveAPIView):
	queryset		 = Foods.objects.all()
	serializer_class = FoodsDetailSerializer
	lookup_field     = 'id'

class SaladsCreateAPIView(CreateAPIView):
	queryset  		 = Salads.objects.all()
	serializer_class = SaladsCreateSerializer

class SaladsListAPIView(ListAPIView):
	queryset 		 = Salads.objects.all()
	serializer_class = SaladsCreateSerializer

class SaladsUpdateAPIView(UpdateAPIView):
	queryset		 = Salads.objects.all()
	serializer_class = SaladsDetailSerializer
	lookup_field	 = 'id'

class SaladsDeleteAPIView(DestroyAPIView):
	queryset		 = Salads.objects.all()
	serializer_class = SaladsDetailSerializer
	lookup_field     = 'id'

class SaladsDetailAPIView(RetrieveAPIView):
	queryset		 = Salads.objects.all()
	serializer_class = SaladsDetailSerializer
	lookup_field	 = 'id'

class DrinksCreateAPIView(CreateAPIView):
	queryset		 = Drinks.objects.all()
	serializer_class = DrinksCreateSerializer

class DrinksListAPIView(ListAPIView):
	queryset		 = Drinks.objects.all()
	serializer_class = DrinksCreateSerializer

class DrinksUpdateAPIView(UpdateAPIView):
	queryset		 = Drinks.objects.all()
	serializer_class = DrinksDetailSerializer
	lookup_field     = 'id'

class DrinksDeleteAPIView(DestroyAPIView):
	queryset		 = Drinks.objects.all()
	serializer_class = DrinksDetailSerializer
	lookup_field     = 'id'

class DrinksDetailAPIView(RetrieveAPIView):
	queryset		 = Drinks.objects.all()
	serializer_class = DrinksDetailSerializer
	lookup_field     = 'id'

class UsersListAPIView(ListAPIView):
	queryset 		 = Users.objects.all()
	serializer_class = UsersListSerializer;

class UsersDeleteAPIView(DestroyAPIView):
	queryset		 = Users.objects.all()
	serializer_class = UsersDetailSerializer
	lookup_field     = 'id'

class UsersDetailAPIView(RetrieveAPIView):
	queryset		 = Users.objects.all()
	serializer_class = UsersDetailSerializer
	lookup_field     = 'id'
