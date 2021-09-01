from django.contrib import admin
from database.models import *
from django.utils.html import mark_safe


def logo(obj):
    return mark_safe('<img src="/media/%s" width="70" />' % obj.logo)


def logo_preview(obj):
    return mark_safe('<img src="/media/%s" width="200"/>' % obj.logo)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'type',
                    'url',
                    logo]
    fields = ['type',
              'name',
              'url',
              'description',
              'logo',
              logo_preview]

    readonly_fields = [logo_preview]

    search_fields = ['name',
                     'type']

    list_filter = ['type']
