from .models import Snippet
from .serializers import Modelserializer

from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset=Snippet.objects.all()
    serializer_class=Modelserializer

    def get(self, req, *args, **kwargs):
        return self.list(req, *args, **kwargs)
    
    def post(self, req, *args, **kwargs):
        return self.create(req, *args, **kwargs)
    
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset= Snippet.objects.all()
    serializer_class=Modelserializer

    def get(self, req, *args, **kwargs):
        return self.retrieve(req, *args, **kwargs)
    
    def put(self, req, *args, **kwargs):
        return self.update(req, *args, **kwargs)
    
    def delete(self, req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs)