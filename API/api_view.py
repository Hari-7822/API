from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets, generics, renderers, response
from .models import user, Snippet
from API.permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, userSerializer, GroupSerializers, NewSerializer

from ajax.models import Demo

class UserView(viewsets.ModelViewSet):
    queryset= user.objects.all().order_by('date_joined')
    serializer_class= UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupView(viewsets.ModelViewSet):
    queryset=Group.objects.all().order_by('name')
    serializer_class=GroupSerializers
    permission_classes=[permissions.IsAuthenticated]

class NewView(viewsets.ModelViewSet):
    queryset = Demo.objects.all().order_by('id')
    serializer_class=NewSerializer
    permission_classes = [permissions.IsAuthenticated]


# class UserList(generics.ListAPIView):
#     queryset=user.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class UserDetail(generics.RetrieveAPIView):
#     queryset=user.objects.all()
#     serializer_class = userSerializer
#     # permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class SnippetHighlight(generics.GenericAPIView):
    queryset=Snippet.objects.all()
    renderer_classes= [renderers.StaticHTMLRenderer]

    def get(self, req, *args, **kwargs):
        snip = self.get_object()
        return response.Response(snip.highlighted)