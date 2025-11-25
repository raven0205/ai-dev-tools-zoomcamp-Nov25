from django.contrib import admin

# Register your models here.
from .models import Todo

# to view and edit TODOs in Django Admin
admin.site.register(Todo)
