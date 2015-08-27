from rest_framework import viewsets
from ServerAdministrator.models import Host, SshUser
from ServerAdministrator.serializers import HostSerializer, SshUserSerializer

__author__ = 'dracks'



class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class SshUserViewSet(viewsets.ModelViewSet):
    queryset = SshUser.objects.all()
    serializer_class = SshUserSerializer