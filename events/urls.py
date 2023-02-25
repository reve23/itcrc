from django.urls import path
from .views import *
urlpatterns = [
    path('v1/',getRoutes),
    path('v1/events',all_events),
    path('v1/segments',get_all_segments),
    path('v1/events/<int:pk>',get_one_event),
    path('v1/segments/<int:pk>',get_one_segment),
]