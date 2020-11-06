from django.contrib import admin
from .models import Staffs
from .models import Products


# Register your models here.

admin.site.register(Staffs)
admin.site.register(Products)