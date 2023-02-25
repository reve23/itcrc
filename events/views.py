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
        'Endpoint':'/api/v1',
        'Methods': 'GET',
        'Details':'Gets all routes'
        },
        {
        'Endpoint':'http://127.0.0.1:8000/api/v1/events',
        'Methods': 'GET',
        'Details':'Gets all the events'
        },
        {
        'Endpoint':'http://127.0.0.1:8000/api/v1/events/3',
        'Methods': 'GET',
        'Details':'Gets one event'
        },
        {
        'Endpoint':'http://127.0.0.1:8000/api/v1/segments',
        'Methods': 'GET',
        'Details':'Gets all the segments'
        },
        {
        'Endpoint':'http://127.0.0.1:8000/api/v1/segments/3',
        'Methods': 'GET',
        'Details':'Gets one segment'
        },
    ]
    return Response(data)

@api_view(['GET'])
def all_events(request):
    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_one_event(request,pk):
    if request.method == 'GET':
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event,many=False)
        return Response(serializer.data)
    
@api_view(['GET'])
def get_all_segments(request):
        if request.method == 'GET':
            segments = Segment.objects.all()
            serializer = SegmentSerializer(segments,many=True)
            return Response(serializer.data)
        
@api_view(['GET'])
def get_one_segment(request,pk):
    if request.method == 'GET':
        segment = Segment.objects.get(pk=pk)
        serializer = SegmentSerializer(segment,many=False)
        return Response(serializer.data)