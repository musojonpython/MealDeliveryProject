from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import(
		SearchFilter,
		OrderingFilter,
	)
from rest_framework.generics import ListAPIView, RetrieveAPIView

from foods.models import (
	Foods,
	Salads,
	Drinks 
	)
from .serializers import (
	FoodListSerializer,
    SaladListSerializer,
    DrinkListSerializer
	)

class FoodListAPIView(ListAPIView):
	queryset  = Foods.objects.all()
	serializer_class = FoodListSerializer
	'''
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'index.html'
	
	def get(self, request):
		queryset_food  = Foods.objects.all()
		queryset_salad = Salads.objects.all()
		queryset_drink = Drinks.objects.all()
		contex = {
		'foods':  queryset_food,
		'salads': queryset_salad,
		'drinks': queryset_drink
		}
		return Response(contex)
	'''
class FoodSellListAPIView(ListAPIView):

	queryset         = Foods.objects.all()
	serializer_class = FoodListSerializer

class SaladSellListAPIView(ListAPIView):
	queryset         = Salads.objects.all()
	serializer_class = SaladListSerializer

class DrinkSellListAPIView(ListAPIView):
	queryset         = Drinks.objects.all()
	serializer_class = DrinkListSerializer