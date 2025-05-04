from django.contrib import admin
from .models import City, Feature, Place, Category
# Register your models here.
admin.site.register(City)
admin.site.register(Feature)
admin.site.register(Place)
admin.site.register(Category)