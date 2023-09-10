from django.contrib import admin

# Register your models here.

from .models import State, City

admin.site.register(State)

admin.site.register(City)



