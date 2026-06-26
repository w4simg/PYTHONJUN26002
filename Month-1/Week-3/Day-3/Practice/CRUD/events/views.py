from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Event

# Create your views here.
@api_view(['GET'])
def welcome(request):
    return Response("Welcome to events apis...")

@api_view(['POST'])
def addEvent(request):
    
    ser = EventSerializer(data = request.data)
    
    if (ser.is_valid()):
        ser.save()
        
        return Response(ser.data)
    
    return Response(ser.errors)

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serData = EventSerializer(events,many=True)
    return Response(serData.data)

@api_view(['PUT', 'PATCH'])
def updateEvent(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)
    
    ser = EventSerializer(event, data=request.data, partial=True)
    if ser.is_valid():
        ser.save()
        return Response(ser.data)
    return Response(ser.errors)

@api_view(['DELETE'])
def deleteEvent(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)
    
    event.delete()
    return Response({"message": "Event deleted successfully"})

