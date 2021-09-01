from database.serializers import *
from rest_framework import generics, mixins


class RulesList(generics.GenericAPIView,
                mixins.ListModelMixin):
    serializer_class = RuleSerializer
    queryset = Rule.objects.all()

    def get(self, request):
        return self.list(request)
