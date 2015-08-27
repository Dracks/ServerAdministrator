from django.db import models
from ServerAdministrator.models import SshUser

TYPES_CONFIGURATION = (
    (0,'Generate'),
    (1, 'Edit')
)

TYPES_PARAM = (
    (0, 'String'),
    (1, 'Int'),
    (2, 'Host'),
    (3, 'Path')
)

# Create your models here.
class Application(models.Model):
    name = models.CharField(max_length=50)

class Version(models.Model):
    application = models.ForeignKey(Application)
    version = models.IntegerField()
    is_downgrade = models.BooleanField()
    publish = models.DateTimeField()

class VersionFile(models.Model):
    version = models.ForeignKey(Version)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    hash = models.CharField(max_length=50)
    content = models.TextField()

class ConfigFile(VersionFile):
    type = models.IntegerField(choices=TYPES_CONFIGURATION)
    template = models.TextField()

class ConfigFileParam(models.Model):
    file = models.ForeignKey(ConfigFile)
    name = models.CharField(max_length=50)
    type = models.IntegerField(choices=TYPES_PARAM)

class DeploymentApplication (models.Model):
    user = models.ForeignKey(SshUser)
    current_version = models.ForeignKey(Version)
    path = models.CharField(max_length=500)

class DeploymentApplicationParam (models.Model):
    application = models.ForeignKey(DeploymentApplication)
    param = models.ForeignKey(ConfigFileParam)
    value = models.CharField(max_length=200)