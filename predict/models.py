from __future__ import unicode_literals
from django.db import models

# Create your models here.

class message(models.Model):
    username = models.CharField(max_length=1000)
    transfer_audio = models.FileField(upload_to='output_audio/',default="")  
  