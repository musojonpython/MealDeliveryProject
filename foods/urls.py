from django.conf.urls import url
from .views import FoodListAPIView, FoodSellListAPIView
	
urlpatterns = [
    url(r'^$', FoodListAPIView.as_view(), name='list'),
    url(r'^sellfood/$', FoodSellListAPIView.as_view(), name='sellfoods'),
    #url(r'^check/$', FoodcheckAPIView.as_view(), name='check')
    ]
    