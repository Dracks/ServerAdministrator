from rest_framework import serializers
from deployment import models
from ServerAdministrator.models import SshUser

__author__ = 'dracks'

class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Application
        fields = ('id', 'name')

class VersionSerializer(serializers.HyperlinkedModelSerializer):
    application = serializers.PrimaryKeyRelatedField(queryset=models.Application.objects.all())

    class Meta:
        model = models.Version
        fields = ('id', 'application', 'is_downgrade', 'publish')

class VersionFileSerializer(serializers.HyperlinkedModelSerializer):
    version = serializers.PrimaryKeyRelatedField(queryset=models.Version.objects.all())

    class Meta:
        model = models.VersionFile
        fields = ('id', 'version', 'name', 'path', 'hash', 'content')

class ConfigFileSerializer(VersionFileSerializer):

    class Meta:
        model = models.ConfigFile
        fields = ('id', 'version', 'name', 'path', 'hash', 'content', 'type', 'template')


class ConfigFileParamSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.PrimaryKeyRelatedField(queryset=models.ConfigFile.objects.all())

    class Meta:
        model = models.ConfigFileParam
        fields = ('id', 'file', 'name', 'type')

class DeploymentApplicationSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=SshUser.objects.all())
    current_version = serializers.PrimaryKeyRelatedField(queryset=models.Version.objects.all())

    class Meta:
        model = models.DeploymentApplication
        fields = ('id', 'user', 'current_version', 'path')

class DeploymentApplicationParamSerializer(serializers.HyperlinkedModelSerializer):
    application = serializers.PrimaryKeyRelatedField(queryset=models.DeploymentApplication.objects.all())
    param = serializers.PrimaryKeyRelatedField(queryset=models.ConfigFileParam.objects.all())

    class Meta:
        model = models.DeploymentApplicationParam
        fields = ('id', 'application', 'param', 'value')
