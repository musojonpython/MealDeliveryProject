from django.conf.urls import url
from .views import UserCreateAPIView , UserFoodAPIView

urlpatterns = [
    url(r'^create/$', UserCreateAPIView.as_view(), name='create'),
    url(r'^userfood/$', UserFoodAPIView.as_view(), name='userfood')
]