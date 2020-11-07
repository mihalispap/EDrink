from django.contrib import admin

# Register your models here.
from edrink.models import Avatar, Participant, Settings
from edrink.models.room import Room

admin.site.register(Avatar)
admin.site.register(Participant)
admin.site.register(Room)
admin.site.register(Settings)
