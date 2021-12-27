from django.db import models

from members.models import Member

# Create your models here.

class Income(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE);
    member_Bank_Name = models.CharField(max_length=200)
    society_Bank_Name = models.CharField(max_length=200)
    check_Number = models.CharField(max_length=100)
    amount = models.IntegerField()
    createdAt = models.DateTimeField()

    def __str__(self):
        return self.member.first_name + " " + self.member.last_name


class Expense(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    amount = models.IntegerField()
    createdAt = models.DateTimeField()

    def __str__(self):
        return self.title

class Charges(models.Model):
    charges_Type = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        return self.charges_Type