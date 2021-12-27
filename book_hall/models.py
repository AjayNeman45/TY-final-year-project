from django.db import models
from members.models import Member
# Create your models here.
class BookHall(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    event_Name = models.CharField(max_length=200)
    date = models.DateField()
    start_Time = models.TimeField()
    end_Time = models.TimeField()

    def __str__(self):
        return "Hall is booked by the member {} {} for the event {} ".format(self.member.first_name, self.member.first_name, self.member.event_Name )
