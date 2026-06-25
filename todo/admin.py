from .models import tooo
from django.contrib import admin



admin.site.register(tooo)
class admintoo(admin.ModelAdmin):
    list_display = ['srno','title','date','user']