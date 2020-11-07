from django.db import models

# python3 manage.py makemigrations <app>
# python3 manage.py sqlmigrate <app> XXXX
# python3 manage.py migrate

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=4096, default=False)
    capacity = models.IntegerField()
    link_to_join = models.CharField(max_length=4096, default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'edrink_room'
