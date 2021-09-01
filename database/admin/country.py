from django.contrib import admin
from database.models import *


class CityInline(admin.StackedInline):
    model = City
    extra = 0


@admin.register(FanClubCountry)
class FanClubCountryAdmin(admin.ModelAdmin):
    inlines = [CityInline]
