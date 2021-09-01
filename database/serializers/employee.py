from rest_framework import serializers
from database.models import *


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ['employee_id', 'years', 'achievement']


class ManagerSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True)

    class Meta:
        model = Employee
        fields = ['id',
                  'order',
                  'full_name',
                  'position',
                  'department',
                  'birthday',
                  'birthday_short',
                  'birthday_long',
                  'age',
                  'about',
                  'photo',
                  'achievements']


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id',
                  'order',
                  'full_name',
                  'position',
                  'department',
                  'birthday',
                  'birthday_short',
                  'birthday_long',
                  'age',
                  'about_short',
                  'about_dropdown',
                  'photo']


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id',
                  'order',
                  'full_name',
                  'position',
                  'department',
                  'birthday',
                  'birthday_short',
                  'birthday_long',
                  'age',
                  'about',
                  'photo']
