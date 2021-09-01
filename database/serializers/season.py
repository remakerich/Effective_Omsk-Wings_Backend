from rest_framework import serializers
from database.models import *


class TrophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Trophy
        fields = ['event',
                  'place']


class SeasonSerializer(serializers.ModelSerializer):
    trophies = TrophySerializer(many=True)

    class Meta:
        model = Season
        fields = ['id',
                  'season',
                  'description',
                  'result',
                  'image',
                  'trophies']
