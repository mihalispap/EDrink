from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from edrink.models import User, Room

admin.site.register(User, UserAdmin)
admin.site.register(Room)
