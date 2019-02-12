from rest_framework import generics
from portal.models import Staff,Visitor, VisitRequests
from .serializers import StaffSerializer

class PortalRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = StaffSerializer

    def get_queryset(self):
        return Staff.objects.all()


class PortalCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = StaffSerializer

    def get_queryset(self):
        return Staff.objects,all()