from django.db import models

from django.contrib.auth.models import AbstractUser


# TODO: add background music link here
class Room(models.Model):
    name = models.CharField(max_length=4096, default=False)
    capacity = models.IntegerField()
    link_to_join = models.CharField(max_length=4096, default=False)


# TODO: migrate this to settings and remove entity all together
class Settings(models.Model):
    reassign_every = models.IntegerField()


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media', null=True)
    assigned_in_room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, null=True)
