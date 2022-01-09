from django.db import models
from members.models import Member
# Create your models here.

STATUS_CHOICES = [
    ("pending", "PENDING"),
    ("approved", "APPROVED"),
    ("declined", "DECLINED"),
]
class BookHall(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    event_Name = models.CharField(max_length=200)
    date = models.DateField()
    start_Time = models.TimeField()
    end_Time = models.TimeField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="pending")


    def __str__(self):
        return "Hall is booked by the member {} {} for the event {} ".format(self.member.first_name, self.member.last_name, self.event_Name )
