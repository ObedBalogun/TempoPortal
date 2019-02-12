from .views import PortalRudView
from django.conf.urls import url

urlpatterns = [
    url(r'(?P<pk>\d+)/$',PortalRudView.as_view()),
]
