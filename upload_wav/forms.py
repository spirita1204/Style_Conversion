from django import forms
from .models import UserSong
import os
from django.core.exceptions import ValidationError  #還要改

class UserSongForm(forms.ModelForm):
    class Meta: #覆寫modelform 記得加
        model = UserSong
        fields = ('audio_file','give_image')
    
    def clean_audio_file(self):
        file = self.cleaned_data.get('audio_file',False)
        if file:                                          #再研究
            #if file.size > 4*1024*1024:
                #raise ValidationError("Audio file too large ( > 4mb )")
            #if not file.content-type in ["audio/mpeg","audio/..."]:
                #raise ValidationError("Content-Type is not mpeg")
            #if not os.path.splitext(file.name)[1] in [".mp3",".wav/..."]:
                #raise ValidationError("Doesn't have proper extension")
             # Here we need to now to read the file and see if it's actually 
             # a valid audio file. I don't know what the best library is to 
             # to do this
            #if not some_lib.is_audio(file.content):
                #raise ValidationError("Not a valid audio file")
            return file
        else:
            raise ValidationError("Couldn't read uploaded file")
 