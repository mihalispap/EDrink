from django.core.files.storage import FileSystemStorage
from django.db import models


# python3 manage.py makemigrations <app>
# python3 manage.py sqlmigrate <app> XXXX
# python3 manage.py migrate

# Create your models here.
class Settings(models.Model):
    reassign_every = models.IntegerField()

    class Meta:
        db_table = 'edrink_settings'
