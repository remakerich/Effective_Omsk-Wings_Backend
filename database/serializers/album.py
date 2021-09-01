from rest_framework import serializers
from database.models import *


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'


class MediaAlbumSerializer(serializers.ModelSerializer):
    media_files = MediaFileSerializer(many=True)

    class Meta:
        model = MediaAlbum
        fields = ['id',
                  'name',
                  'page_reference',
                  'event_date',
                  'date_created',
                  'media_files']
