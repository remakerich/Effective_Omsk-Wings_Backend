from django.contrib import admin
from database.models import *
from django.utils.html import mark_safe


class TrophyInline(admin.StackedInline):
    model = Trophy
    extra = 0


def image(obj):
    return mark_safe('<img src="/media/%s" width="200" />' % obj.image)


def image_preview(obj):
    return mark_safe('<img src="/media/%s" width="400"/>' % obj.image)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    inlines = [TrophyInline]
    list_display = ['season',
                    'description',
                    'result',
                    image]

    readonly_fields = [image_preview]
