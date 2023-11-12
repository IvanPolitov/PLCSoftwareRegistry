from django.db import models
from django.contrib.auth.models import User

class Software(models.Model):
    plc = models.CharField(max_length=256)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    crc_md5_user_software = models.CharField(max_length=256)
    crc_md5_runtime = models.CharField(max_length=256)

    def __str__(self):
        return self.creator.username + ' ' + self.crc_md5_user_software

