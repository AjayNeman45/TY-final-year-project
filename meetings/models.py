from django.db import models

# Create your models here.

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    date_And_Time = models.DateTimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.title