from django.shortcuts import render

from django.http.response import HttpResponse
from django.http.response import JsonResponse
from rest_framework.response import Response    
from .models import Note
from .serializers import NoteSerializer
from rest_framework import viewsets,permissions
# Create your views here.
def home(req):
    if req.method =='GET':
        return JsonResponse({"message":"Nothings"})



# class MyViewSet(viewsets.ViewSet,viewsets.ModelViewSet):
#     queryset=Note.objects.all()
#     serializer=NoteSerializer
#     permission_classes=[permissions.AllowAny]
#     def list_one(self,req,pk):
#         queryset=Note.objects.filter(id=pk)
#         serializer=NoteSerializer(queryset,many=True)
#         permission_classes=[permissions.AllowAny]
#         return Response(serializer.data)



class NoteViewSet(viewsets.ModelViewSet):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer
    permission_classes=[permissions.AllowAny]

note_list=NoteViewSet.as_view({
    'get':'list',
    'post':'create',
})

note_detail=NoteViewSet.as_view({

    'delete':'destroy',
})