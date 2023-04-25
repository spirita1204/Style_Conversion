from django.contrib import admin

# Register your models here.
from predict.models import message 

class datashow2(admin.ModelAdmin):
    list_display = ('username','transfer_audio')

admin.site.register(message,datashow2)