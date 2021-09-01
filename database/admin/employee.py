from django.contrib import admin
from database.models import *
from django.utils.html import mark_safe


class AchievementInline(admin.StackedInline):
    model = Achievement
    extra = 0


def photo(obj):
    return mark_safe('<img src="/media/%s" width="70" />' % obj.photo)


def photo_preview(obj):
    return mark_safe('<img src="/media/%s" width="200"/>' % obj.photo)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    inlines = [AchievementInline]
    list_display = ['full_name',
                    'position',
                    'department',
                    'birthday',
                    photo,
                    'order']

    readonly_fields = [photo_preview]

    search_fields = ['birthday',
                     'department',
                     'first_name',
                     'last_name',
                     'middle_name',
                     'position']
    list_filter = ['department']
