from django.contrib import admin
from database.models import *


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'text']

    fields = ['title',
              'text',
              'icon']
