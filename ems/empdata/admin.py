from django.contrib import admin
from empdata import models
# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display=('firstName','lastName','employeeID','city')

admin.site.register(models.employee, employeeAdmin)