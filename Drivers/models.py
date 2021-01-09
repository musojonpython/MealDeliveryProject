from django.db import models
from users.models import Users

# Create your models here.

class Drivers(models.Model):
	first_name  = models.CharField(max_length=150)
	last_name   = models.CharField(max_length=150)
	login		= models.CharField(max_length=100)
	password    = models.CharField(max_length=100)
	telephone   = models.CharField(max_length=50)

	def __str__(self):
		return self.first_name + self.last_name
		

