from django.contrib import admin

from .models import Users , FoodsType, UsersFoods
# Register your models here.

class UsersModelAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name", "telephone"]
	list_filter  = ["first_name"]
	search_fields = ["first_name", "last_name"]

	class Meta:
		model = Users

class UserFoodModelAdmin(admin.ModelAdmin):
	list_display = ["foodsid",  "count"]

	class Meta:
		model = UsersFoods

class FoodstypeModelAdmin(admin.ModelAdmin):
	list_display = ["foodstypename"]

	class Meta:
		model = FoodsType

admin.site.register(UsersFoods, UserFoodModelAdmin)
admin.site.register(FoodsType, FoodstypeModelAdmin)
admin.site.register(Users, UsersModelAdmin)
