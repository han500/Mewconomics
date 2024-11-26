from django.db import models

# Create your models here.
class Comment(models.Model):
    unit = models.CharField(max_length=3)
    content = models.TextField()
    author = models.CharField(max_length=25)
    date = models.DateField()