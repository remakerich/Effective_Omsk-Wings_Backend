from django.contrib import admin
from database.models import *
from django.utils.html import mark_safe


def photo(obj):
    return mark_safe('<img src="/media/%s" width="70" />' % obj.photo)


def photo_preview(obj):
    return mark_safe('<img src="/media/%s" width="200"/>' % obj.photo)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['full_name',
                    'position',
                    'birthday',
                    'number',
                    photo]

    readonly_fields = [photo_preview]

    search_fields = ['birthday',
                     'first_name',
                     'last_name',
                     'position']

    list_filter = ['position']
