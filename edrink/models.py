from django.db import models

from django.contrib.auth.models import AbstractUser


# TODO: add background music link here
class Room(models.Model):
    name = models.CharField(max_length=4096)
    capacity = models.IntegerField()
    link_to_join = models.CharField(max_length=4096)

    def __str__(self):
        return self.name + " with capacity: " + str(self.capacity)


# TODO: migrate this to settings and remove entity all together
class Settings(models.Model):
    reassign_every = models.IntegerField()


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media', null=True)
    assigned_in_room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, null=True)
