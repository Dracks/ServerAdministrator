from django.db import models
from paramiko import RSAKey
import cStringIO
import base64

__author__ = 'dracks'

class Host(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=16)

    def __unicode__(self):
        return self.name

class SshUser(models.Model):
    name = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    host = models.ForeignKey(Host)
    key = models.TextField()
    public_key = models.TextField()

    def generate_keys(self):
        key_object = RSAKey.generate(bits=1024, progress_func=None)
        key_string = cStringIO.StringIO()
        key_object.write_private_key(key_string)
        self.key = base64.b64encode(key_string.getvalue())
        key_string.close()
        self.public_key = key_object.get_base64()
        self.save()


