from django.db import models

# Create your models here.

class Wombat(models.Model):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=16)
    shootable = models.BooleanField(default=False)
    age = models.PositiveSmallIntegerField()
    speed = models.FloatField(default=0.0)
    location = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} ({self.location})"
