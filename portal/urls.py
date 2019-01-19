from . import views
from django.urls import path

app_name='portal'

urlpatterns = [
    path('',views.formpage, name='formpage'),
    path('approval/<int:staff_id>/<slug:token>/', views.approval),
    path('staff_requests/<int:staff_id>/',views.requests),
    path('all_requests/',views.all_requests, name='all_requests'),
]