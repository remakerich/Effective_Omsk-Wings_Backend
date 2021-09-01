from database.serializers import *
from rest_framework import generics, mixins


def media_albums(page_reference_filter):
    class MediaAlbumsList(generics.GenericAPIView,
                          mixins.ListModelMixin):
        serializer_class = MediaAlbumSerializer
        queryset = MediaAlbum.objects.filter(
            page_reference=page_reference_filter)

        def get(self, request):
            return self.list(request)

    return MediaAlbumsList
