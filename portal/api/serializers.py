from portal.models import Visitor, Staff,VisitRequests
from rest_framework import serializers


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = [
            'pk',
            'staff_name',
            'staff_email',
        ]
        # read_only_fields = ['pk']
