from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

# Create your views here.
@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body = data['body']
    )
    serializer = Noteserializer(note, many=False)
    return Response(serializer.data) 

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = Noteserializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
    notes = Note.objects.get(id=pk)
    serializer = Noteserializer(notes, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = Noteserializer(instance=note, data=data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted successfully!!')