# Create your views here.
from rest_framework import viewsets
from deployment import models, serializers

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

class VersionViewSet(viewsets.ModelViewSet):
    queryset = models.Version.objects.all()
    serializer_class = serializers.VersionSerializer

class VersionFileViewSet(viewsets.ModelViewSet):
    queryset = models.VersionFile.objects.all()
    serializer_class = serializers.VersionFileSerializer

class ConfigFileViewSet(viewsets.ModelViewSet):
    queryset = models.ConfigFile.objects.all()
    serializer_class = serializers.ConfigFileSerializer

class ConfigFileParamViewSet(viewsets.ModelViewSet):
    queryset = models.ConfigFileParam.objects.all()
    serializer_class = serializers.ConfigFileParamSerializer

class DeploymentApplicationViewSet(viewsets.ModelViewSet):
    queryset = models.DeploymentApplication.objects.all()
    serializer_class = serializers.DeploymentApplicationSerializer

class DeploymentApplicationParamViewSet(viewsets.ModelViewSet):
    queryset = models.DeploymentApplicationParam.objects.all()
    serializer_class = serializers.DeploymentApplicationParamSerializer