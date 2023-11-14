from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Software(models.Model):
    plc = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    crc_md5_user_software = models.CharField(max_length=256)
    crc_md5_runtime = models.CharField(max_length=256)
    #date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.creator.username + ' ' + self.crc_md5_user_software

