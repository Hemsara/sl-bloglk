from django.db import models

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length=50)
    body = models.CharField(max_length=250)
    image = models.CharField(max_length=2550)

    def __str__(self):
        return self.title

