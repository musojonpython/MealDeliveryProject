from django.conf.urls import url
from .views import UsersListAPIView

urlpatterns = [
url(r'^$', UsersListAPIView.as_view()),
]
