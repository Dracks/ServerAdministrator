import os, hashlib
from django.db import models
from django.db.models import Max
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
    is_draft = models.BooleanField(default=True)
    is_downgrade = models.BooleanField(default=False)

    @staticmethod
    def get_next_version(application):
        max_version = Version.objects.filter(application=application).aggregate(Max('version'))['version__max']
        if max_version is None:
            return 1
        return max_version+1

    @staticmethod
    def create_from_zip(application, zip_file):
        self = Version(application=application, version=Version.get_next_version(application))
        self.save()
        for name in zip_file.namelist():
            file_name = os.path.basename(name)
            file_path = os.path.dirname(name)
            contents = zip_file.read(name)
            md5 = hashlib.md5(contents).hexdigest()
            VersionFile(version=self, name=file_name, path=file_path, hash=md5, content=contents).save()

class VersionFile(models.Model):
    version = models.ForeignKey(Version)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    hash = models.CharField(max_length=50)
    content = models.TextField()

class ChangeFile(models.Model):
    application = models.ForeignKey(Application)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    delete = models.BooleanField(default=False)
    rename = models.CharField(max_length=100, null=True)

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