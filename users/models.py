from django.db import models
from foods.models import Foods

class Users(models.Model):
	first_name = models.CharField(max_length = 150)
	last_name  = models.CharField(max_length = 150)
	telephone  = models.CharField(max_length = 20)
	adress     = models.CharField(max_length = 100)
	comment    = models.TextField()

	def __str__(self):
		return str(self.first_name)

class FoodsType(models.Model):
	foodstypename = models.CharField(max_length = 150)

	def __str__(self):
		return str(self.foodstypename)

class UsersFoods(models.Model):
	foodstype = models.ForeignKey(FoodsType, on_delete=models.CASCADE, default=1)
	foodsid   = models.ForeignKey(Foods, on_delete=models.CASCADE, default=1)
	usersid   = models.PositiveIntegerField(default=1)
	count      = models.PositiveIntegerField(default=1)
	
	def __str__(self):
		return str(self.users_id)
