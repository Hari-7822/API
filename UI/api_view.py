from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets
from .models import user

from .serializers import UserSerializer, GroupSerializers


class UserView(viewsets.ModelViewSet):
    queryset= user.objects.all().order_by('date_joined')
    serializer_class= UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupView(viewsets.ModelViewSet):
    queryset=Group.objects.all().order_by('name')
    serializer_class=GroupSerializers
    permission_classes=[permissions.IsAuthenticated]