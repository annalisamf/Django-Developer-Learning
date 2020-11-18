from django.contrib import admin

from .models import Pet


@admin.register(Pet)  # register the class to tell which model it is associated with
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
