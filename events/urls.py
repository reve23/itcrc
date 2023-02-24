from django.urls import path
from .views import *
urlpatterns = [
    path('v1/',getRoutes),
    path('v1/events',all_events),
]