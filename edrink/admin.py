from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from edrink.models import Settings
from edrink.models.participant import Participant
from edrink.models.room import Room

admin.site.register(Room)
admin.site.register(Settings)
admin.site.register(Participant)
# admin.site.register(EDrinkUser, UserAdmin)
