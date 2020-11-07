from django.contrib import admin

# Register your models here.
from edrink.models import Avatar, Settings
from edrink.models.participant import Participant
from edrink.models.room import Room

admin.site.register(Avatar)
admin.site.register(Room)
admin.site.register(Settings)
admin.site.register(Participant)
