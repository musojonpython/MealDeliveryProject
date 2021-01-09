
from django.db import models
# Create your models here.

class Foods(models.Model):
	title 	= models.CharField(max_length=200)
	cost  	= models.CharField(max_length=100)
	content = models.TextField()
	images  = models.ImageField(null=True, blank=True, 
		width_field="width_field", 
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field  = models.IntegerField(default=0)

	def __str__(self):
		return self.title	

class Salads(models.Model):
	title 	= models.CharField(max_length=200)
	cost  	= models.CharField(max_length=100)
	content = models.TextField()
	images  = models.ImageField(null=True, blank=True, 
		width_field="width_field", 
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field  = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title	

class Drinks(models.Model):
	title 	= models.CharField(max_length=200)
	cost  	= models.CharField(max_length=100)
	content = models.TextField()
	images  = models.ImageField(null=True, blank=True, 
		width_field="width_field", 
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field  = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title	

