from __future__ import unicode_literals
from django.conf import settings
from django.utils import timezone
from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1500)
    serves = models.IntegerField()
    prep_time = models.TimeField((u"Conversation Time"), blank=True)
    cook_time = models.TimeField((u"Conversation Time"), blank=True)
    ingredients = models.CharField(max_length=1500)
    instructions = models.CharField(max_length=1500)
    suits = models.CharField(max_length=1500)
    mealType = (
        ('Breakfast'),
        ('Lunch'),
        ('Dinner'),
        ('Starter'),
        ('Dessert'),
        )
    calories = models.DecimalField(max_digits=5, decimal_places=2, default="")
    fat = models.DecimalField(max_digits=5, decimal_places=2, default="")
    saturates = models.DecimalField(max_digits=5, decimal_places=2, default="")
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default="")
    sugars = models.DecimalField(max_digits=5, decimal_places=2, default="")
    fibre = models.DecimalField(max_digits=5, decimal_places=2, default="")
    protein = models.DecimalField(max_digits=5, decimal_places=2, default="")
    salt = models.DecimalField(max_digits=5, decimal_places=2, default="")
    created_date = models.DateField((u"Conversation Date"), blank=True)
    published_date  = models.DateField((u"Conversation Date"), blank=True)
    warnings =(
        ('May Contain Nuts'),
        ('May Contain Pork/ Meat'),
        )
