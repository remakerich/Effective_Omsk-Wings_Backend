from database.serializers import *
from rest_framework import generics, mixins


class SeasonsList(generics.GenericAPIView,
                  mixins.ListModelMixin):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()

    def get(self, request):
        return self.list(request)
