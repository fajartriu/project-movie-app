from django.db import models

# Create your models here.
class Genres(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genres)
    language = models.CharField(max_length=50)
    mpaaRatingTypto = models.CharField(max_length=50)
    mpaaRatingLabel = models.CharField(max_length=255)
    userRating = models.IntegerField()

    def __str__(self):
        return self.name
    