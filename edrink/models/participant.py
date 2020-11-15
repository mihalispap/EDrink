from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models

# Create your models here.


from edrink.models.room import Room


class Participant(models.Model):
    name = models.CharField(max_length=4096, default=False)
    avatar = models.ImageField(upload_to='media')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    assigned_in_room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'edrink_participant'

