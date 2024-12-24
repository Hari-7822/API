from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets, generics
from .models import user
from API.permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, userSerializer, GroupSerializers


class UserView(viewsets.ModelViewSet):
    queryset= user.objects.all().order_by('date_joined')
    serializer_class= UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupView(viewsets.ModelViewSet):
    queryset=Group.objects.all().order_by('name')
    serializer_class=GroupSerializers
    permission_classes=[permissions.IsAuthenticated]

class UserList(generics.ListAPIView):
    queryset=user.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveAPIView):
    queryset=user.objects.all()
    serializer_class = userSerializer
    # permission_classes = [permissions.IsAuthenticated]