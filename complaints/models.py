from django.db import models
from members.models import Member
# Create your models here.

class Complaint(models.Model):
    member =  models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    status = models.CharField(max_length=20, choices=[("active","Active"),("pending","Pending"),("resolved","Resolved")], default="pending")
    created_At = models.DateTimeField()

    def __str__(self):
        return self.title