from django.contrib import admin

# Register your models here.
from upload_wav.models import UserSong 

class datashow3(admin.ModelAdmin):
    list_display = ('audio_file','give_image')

admin.site.register(UserSong,datashow3)