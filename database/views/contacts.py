from database.serializers import *
from rest_framework import generics, mixins


class ContactsList(generics.GenericAPIView,
                   mixins.ListModelMixin):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get(self, request):
        return self.list(request)
