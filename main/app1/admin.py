from django.contrib import admin
from app1.models import Department, Employee, Project

# Register your models here.
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Department)