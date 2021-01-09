from django.contrib import admin
from .models import Drivers

# Register your models here.

class DriversModelAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name", "telephone"]
	search_filed = ["first_name", "last_name"]

	class Meta:
		model = Drivers

admin.site.register(Drivers, DriversModelAdmin)
