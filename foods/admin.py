from django.contrib import admin

from .models import (
	Foods, 
	Salads,
	Drinks
	)
# Register your models here.

class FoodModelAdmin(admin.ModelAdmin):
	list_display = ["title", "cost", "content", "id"]
	list_filter  = ["title"]
	search_fields = ["title", "content"]

	class Meta:
		model = Foods

class SaladModelAdmin(admin.ModelAdmin):
	list_display = ["title", "cost", "id"]
	list_filter  = ["title"]
	search_fields = ["title", "content"]

	class Meta:
		model = Salads

class DrinkModelAdmin(admin.ModelAdmin):
	list_display = ["title", "cost", "id"]
	list_filter  = ["title"]
	search_fields = ["title", "content"]

	class Meta:
		model = Drinks


admin.site.register(Foods, FoodModelAdmin)
admin.site.register(Drinks, DrinkModelAdmin)
admin.site.register(Salads, SaladModelAdmin)
