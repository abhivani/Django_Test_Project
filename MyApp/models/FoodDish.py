from django.db import models
from .Category import Category

class FoodDish(models.Model):
    name = models.CharField(max_length=20)
    descrtption = models.CharField(max_length=20, default='')
    price = models.IntegerField(default=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='uploads/products/', default='')

    def __str__(self):
        return self.name


    @staticmethod
    def get_all_food_dish():
        return FoodDish.objects.all()