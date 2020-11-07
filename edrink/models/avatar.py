from django.core.files.storage import FileSystemStorage
from django.db import models


# python3 manage.py makemigrations <app>
# python3 manage.py sqlmigrate <app> XXXX
# python3 manage.py migrate

# Create your models here.
class Avatar(models.Model):
    name = models.CharField(max_length=4096, default=False)
    pic = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'edrink_avatar'
