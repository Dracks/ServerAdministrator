from rest_framework import serializers
from ServerAdministrator.models import Host, SshUser

__author__ = 'dracks'

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('id', 'name', 'ip')

class SshUserSerializer(serializers.HyperlinkedModelSerializer):
    host = serializers.PrimaryKeyRelatedField(queryset=Host.objects.all())
    public_key = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user = SshUser.objects.create(**validated_data)
        user.generate_keys()
        return user


    class Meta:
        model = SshUser
        fields = ('id', 'name', 'host', 'user', 'public_key')