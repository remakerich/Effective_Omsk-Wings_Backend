from database.serializers import *
from rest_framework import generics, mixins


def sponsors_and_social_media(type_filter):
    class SponsorsAndSocialMediaList(generics.GenericAPIView,
                                     mixins.ListModelMixin):
        serializer_class = SponsorSerializer
        queryset = Sponsor.objects.filter(type=type_filter)

        def get(self, request):
            return self.list(request)

    return SponsorsAndSocialMediaList
