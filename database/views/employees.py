from database.serializers import *
from rest_framework import generics, mixins


class ManagersList(generics.GenericAPIView,
                   mixins.ListModelMixin):
    serializer_class = ManagerSerializer
    queryset = Employee.objects.filter(department='Руководство').order_by('order')

    def get(self, request):
        return self.list(request)


class CoachesList(generics.GenericAPIView,
                  mixins.ListModelMixin):
    serializer_class = CoachSerializer
    queryset = Employee.objects.filter(department='Тренерский штаб').order_by('order')

    def get(self, request):
        return self.list(request)


class StaffList(generics.GenericAPIView,
                mixins.ListModelMixin):
    serializer_class = StaffSerializer
    queryset = Employee.objects.filter(department='Персонал').order_by('order')

    def get(self, request):
        return self.list(request)
