from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

from .models import Snippet
from .serializers import Modelserializer
from API.permissions import IsOwnerOrReadOnly
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.reverse import reverse


class SnippetList(APIView):
    # permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get(self, req, format=None):
        snip = Snippet.objects.all()
        ser = Modelserializer(snip, many=True)
        return Response(ser.data)

    def post(self, req, format=None):
        ser = Modelserializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, stauts=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snip = self.get_object(pk)
        ser = Modelserializer(snip)
        return Response(ser.data)

    def put(self, req, pk, format=None):
        snip = self.get_object(pk)
        ser = Modelserializer(snip, data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, req, pk, format=None):
        snip=self.get_object(pk)
        snip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def snippet_list(req, format=None):
    if req.method == 'GET':
        data= Snippet.objects.all()
        ser= Modelserializer(data, many=True)
        return Response(ser.data)
    
    elif req.method == 'POST':
        ser = Modelserializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(req, pk, format=None):
        try:
             snip = Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)
        
        if req.method == "GET":
            ser = Modelserializer(snip)
            return Response(ser.data)
        
        elif req.method == "PUT":
            data = JSONParser().parse(req)
            ser = Modelserializer(snip, data=data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif req.method == "DELETE":
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        


@api_view(["GET"])
def api_root(req, format=None):
    return Response({
        'users': reverse('user-list', request=req, format=format),
        'snippet': reverse('snippet-list', request=req, format=format)
    })