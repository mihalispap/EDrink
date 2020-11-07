from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.
from edrink.models import Avatar
from edrink.models.room import Room


class Participant(models.Model):
    name = models.CharField(max_length=4096, default=False)
    avatar = models.ForeignKey(Avatar, on_delete=models.DO_NOTHING)
    assigned_in_room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'edrink_participant'
