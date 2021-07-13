import uuid
from django.db import models

class Power(models.Model):  # table
   #  id int autoincrement unique
    name = models.CharField(max_length=32, unique=True)  # column
    description = models.CharField(max_length=512)  # column
#    id = models.UUIDField(editable=False, default=uuid.uuid4)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Enemy(models.Model):
    name = models.CharField(max_length=32, unique=True)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name

class Superhero(models.Model):
    name = models.CharField(max_length=32, unique=True)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)

    def __str__(self):
        return self.name


