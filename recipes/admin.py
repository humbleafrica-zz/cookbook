from django.contrib import admin
from .models import Cuisine, Meal, Utensil, Recipe, Source

# Register your models here.
admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Utensil)
admin.site.register(Recipe)
admin.site.register(Source)