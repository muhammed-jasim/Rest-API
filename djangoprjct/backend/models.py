from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f'Post :{self.title}'
    
class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_date = models.DateField()
    evnt_description = models.TextField()