from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models.FoodDish import FoodDish
from .models.Category import Category
from .models.Customer import  Customer


class AdminFoodDish(admin.ModelAdmin):
    list_display = ['name','descrtption','price','category']

class CustomerList(admin.ModelAdmin):
    list_display = ['name','email','number']




admin.site.register(FoodDish,AdminFoodDish)
admin.site.register(Category)
admin.site.register(Customer,CustomerList)