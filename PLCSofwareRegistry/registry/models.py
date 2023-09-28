from django.db import models

class Software(models.Model):
    plc = models.CharField(max_length=256)
    creator = models.CharField(max_length=256)
    crc_md5_user_software = models.CharField(max_length=256)
    crc_md5_runtime = models.CharField(max_length=256)

    def __str__(self):
        return self.creator + ' ' + self.crc_md5_user_software

