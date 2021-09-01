from database.serializers import *
from rest_framework import generics, mixins


class CountryList(generics.GenericAPIView,
                  mixins.ListModelMixin):
    serializer_class = CountrySerializer
    queryset = FanClubCountry.objects.all()

    def get(self, request):
        return self.list(request)
