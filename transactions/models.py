from email.policy import default
from secrets import choice
from urllib import request
from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from members.models import Member

# Create your models here.

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


def getTotalCharges():
    charges = Charges.objects.all()
    sum = 0;
    for i in charges:
        sum += i.amount
    return sum

class Income(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE);
    member_Bank_Name = models.CharField(max_length=200)
    society_Bank_Name = models.CharField(max_length=200, default="SBI Bank")
    check_Number = models.CharField(max_length=100)
    createdAt = models.DateTimeField()
    amount= models.IntegerField()
    totalCharges = models.CharField(max_length=100, blank=True, verbose_name="Total Charges", default=getTotalCharges())


    def __str__(self):
        return self.member.first_name + " " + self.member.last_name

