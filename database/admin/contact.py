from django.contrib import admin
from database.models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact',
                    'line1',
                    'line2',
                    'line3']
