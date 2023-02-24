from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Event,Segment
from .serializers import EventSerializer,SegmentSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    data = [
        {
        'Endpoint':'/api/',
        'Methods': 'GET',
        'Details':'Gets all routes'
        },
    ]
    return Response(data)

@api_view(['GET'])
def all_events(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events,many=True)
        return Response(serializer.data)
