from rest_framework import serializers
from database.models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'city', 'lat', 'lon']


class CountrySerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True)

    class Meta:
        model = FanClubCountry
        fields = ['id', 'country', 'cities']
