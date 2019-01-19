from django.contrib import admin
from .models import Staff, Visitor, VisitRequests

admin.site.register(Staff)
admin.site.register(Visitor)
admin.site.register(VisitRequests)