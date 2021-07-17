from django.contrib import admin

from forexapp.models import *

class AdminCustome(admin.ModelAdmin):
    list_display=['user','phone']
admin.site.register(Customer,AdminCustome)
