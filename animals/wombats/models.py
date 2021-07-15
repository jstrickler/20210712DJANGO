from django.db import models

# Create your models here.

class Wombat(models.Model):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=16)
    shootable = models.BooleanField(default=False)
    age = models.PositiveSmallIntegerField()
    speed = models.FloatField(default=0.0)
    attitude = models.CharField(max_length=32, null=False)
    location = models.CharField(max_length=64)
    sex = models.CharField(
        max_length=1,
        choices=[('m', 'male'), ('f', 'female')],
        null=False,
    )

    def __str__(self):
        return f"{self.name} ({self.location})"
