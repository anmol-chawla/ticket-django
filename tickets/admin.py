from django.contrib import admin
from .models import Sales

# Register your models here.


class SalesAdmin(admin.ModelAdmin):
    list_display = ['name', 'reg_no', 'mobile_no', 'college',
                    'event_name', 'amount', 'pch_name', 'time']


admin.site.register(Sales, SalesAdmin)
