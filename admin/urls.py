from django.conf.urls import url
from .views import (
	DriverCreateAPIView,
	DriverUpdateAPIView,
	DriverDeleteAPIView,
	DriverDetailAPIView,
	DriverListAPIView,
    
    FoodsCreateAPIView,
    FoodsListAPIView,
    FoodsUpdateAPIView,
    FoodsDetailAPIView,
    FoodsDeleteAPIView,
    
    SaladsCreateAPIView,
    SaladsListAPIView,
    SaladsUpdateAPIView,
    SaladsDeleteAPIView,
    SaladsDetailAPIView,
    
    DrinksCreateAPIView,
    DrinksListAPIView,
    DrinksUpdateAPIView,
    DrinksDeleteAPIView,
    DrinksDetailAPIView,
    
    UsersListAPIView,
    UsersDeleteAPIView,
    UsersDetailAPIView,
	)

urlpatterns = [
 url(r'^drivercreate/$', DriverCreateAPIView.as_view()),
 url(r'^driverlist/$', DriverListAPIView.as_view()),
 url(r'^(?P<id>\d+)/driverdetail/$', DriverDetailAPIView.as_view()),
 url(r'^(?P<id>\d+)/driverupdate/$', DriverUpdateAPIView.as_view()),
 url(r'^(?P<id>\d+)/driverdelete/$', DriverDeleteAPIView.as_view()),
 
 url(r'^foodscreate/$',  FoodsCreateAPIView.as_view()),
 url(r'^foodslist/$',  FoodsListAPIView.as_view()),
 url(r'^(?P<id>\d+)/foodsupdate/$',  FoodsUpdateAPIView.as_view()),
 url(r'^(?P<id>\d+)/foodsdetail/$',  FoodsDetailAPIView.as_view()),
 url(r'^(?P<id>\d+)/foodsdelete/$',  FoodsDeleteAPIView.as_view()),
 
 url(r'^saladscreate/$', SaladsCreateAPIView.as_view()),
 url(r'^saladslist/$', SaladsListAPIView.as_view()),
 url(r'^(?P<id>\d+)/saladsupdate/$', SaladsUpdateAPIView.as_view()),
 url(r'^(?P<id>\d+)/saladsdelete/$', SaladsDeleteAPIView.as_view()),
 url(r'^(?P<id>\d+)/saladsdetail/$', SaladsDetailAPIView.as_view()),
 
 url(r'^drinkslist/$',   DrinksListAPIView.as_view()),
 url(r'^drinkscreate/$', DrinksCreateAPIView.as_view()),
 url(r'^(?P<id>\d+)/drinksupdate/$', DrinksUpdateAPIView.as_view()),
 url(r'^(?P<id>\d+)/drinksdetail/$', DrinksDetailAPIView.as_view()),
 url(r'^(?P<id>\d+)/drinksdelete/$', DrinksDeleteAPIView.as_view()),
 
 url(r'^userslist/$',    UsersListAPIView.as_view()),
 url(r'^(?P<id>\d+)/usersdelete/$',  UsersDeleteAPIView.as_view()),
 url(r'^(?P<id>\d+)/usersdetail/$',  UsersDetailAPIView.as_view()),
 ]