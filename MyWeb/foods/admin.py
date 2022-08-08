from django.contrib import admin
from .models import food
# Register your models here.

@admin.register(food)
class food_admin(admin.ModelAdmin):
    list_display = ("Name", "Description", "Price")