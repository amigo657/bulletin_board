from django.contrib import admin
from category.models import Work


class AdminWork(admin.ModelAdmin):
    list_display = ("work_class", "salary")
    
admin.site.register(Work, AdminWork)
