from django.db import models

# Create your models here.
class Image(models.model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.URLField()

    def __str__(self):
        return self.title
