from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.


from edrink.models import Avatar
from edrink.models.room import Room


class Participant(models.Model):
    name = models.CharField(max_length=4096, default=False)
    avatar = models.ForeignKey(Avatar, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default=None)
    assigned_in_room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, default=-1)

    class Meta:
        db_table = 'edrink_participant'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=4096, default=False)
    avatar = models.ForeignKey(Avatar, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'edrink_euser'
