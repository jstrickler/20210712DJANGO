from django.db import models
import uuid
# Create your models here.

class Director(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                          editable=False, help_text="Unique ID of this director")
    name = models.CharField(max_length=64, unique=True, help_text="Name of director")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "director"

class Movie(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                          editable=False, help_text="Unique ID of this movie")
    title = models.CharField(max_length=256, help_text="Title of movie")
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    run_time = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "movie"











