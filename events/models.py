from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    venue = models.CharField(max_length=100)
    start_Date_Time = models.DateTimeField()
    end_Date_Time = models.DateTimeField()

    def __str__(self):
        return self.title;