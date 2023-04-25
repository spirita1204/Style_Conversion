from django.db import models

# Create your models here.
class UserSong(models.Model):
    audio_file = models.FileField()
    give_image = models.ImageField(upload_to='give_image/')
    def delete(self,*args,**kwargs): #delete in database
        self.audio_file.delete()
        self.give_image.delete()
        super().delete(*args,**kwargs)