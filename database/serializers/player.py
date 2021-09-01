from rest_framework import serializers
from database.models import *


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id',
                  'full_name',
                  'position',
                  'birthday',
                  'birthday_short',
                  'birthday_long',
                  'age',
                  'number',
                  'photo']
