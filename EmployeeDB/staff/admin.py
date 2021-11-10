from .models import Employee
from django.contrib import admin
admin.site.site_url = "/home"
# Register your models here.
admin.site.register(Employee)
