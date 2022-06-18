from django.shortcuts import render

# Create your views here.
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import NoteSerializer
from api.models import Note
@api_view(['GET'])
def getNotes(request):
    notes=Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    note=Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def createNote(request):
    data= request.data

    note = Note.objects.create(
        body=data['body']
    )

    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)




@api_view(['PUT'])
def updateNote(request,pk):
    data= request.data

    note = Note.objects.get(id=pk)
    
    serializer = NoteSerializer(note, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    
    return Response('DELETED')