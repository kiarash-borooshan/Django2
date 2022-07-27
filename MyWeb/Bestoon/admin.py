from django.contrib import admin
from .models import Expense, Income
# Register your models here.

# admin.site.register(Expense)
# admin.site.register(Income)


@admin.register(Expense)
class Expense_Admin(admin.ModelAdmin):
    list_display = ("Choose", "Amount")


@admin.register(Income)
class Income_Admin(admin.ModelAdmin):
    list_display = ("Amount", "User")