from database.serializers import *
from rest_framework import generics, mixins


class PlayersList(generics.GenericAPIView,
                  mixins.ListModelMixin):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    def get(self, request):
        return self.list(request)
