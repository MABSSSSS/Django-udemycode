from django.contrib import admin
from PayRollApp.models import Employee ,OnSiteEmployees,State,City
# Register your models here.
admin.site.register(Employee)
admin.site.register(OnSiteEmployees)
admin.site.register(State)
admin.site.register(City)
