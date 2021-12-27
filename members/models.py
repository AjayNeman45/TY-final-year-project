from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Member(AbstractUser):
    profile_Photo = models.ImageField(null=True, blank=True, upload_to="Media/")
    email = models.EmailField(_('email address'), unique=True, null=True, blank=True)
    phone_Number = models.CharField(max_length=255, null=True, blank=True)
    wing = models.CharField(max_length=5, choices=[('a','A'),('b','B'),('c','C'),('d','D')], null=True, blank=True)
    floor_Number = models.CharField(max_length=10, choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7')], null=True, blank=True)
    flat_Number = models.CharField(max_length=10, null=True, blank=True, unique=True)
    flat_Type = models.CharField(max_length=10, choices=[('1rk','1RK'),('1bhk','1BHK')],null=True, blank=True)
    area = models.IntegerField(null=True, blank=True)
    member_Type = models.CharField(max_length=256, choices=[('resident', 'Resident'), ('tenant', 'Tenant')])

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

class CommiteeMember(models.Model):
    member = models.OneToOneField(Member,  unique=True, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, unique=True, choices=[("head","Head"),("subhead","Subhead"),("secretary","Secretary"),("treasurer","Treasurer")])
    from_Date = models.DateField()

    def __str__(self):
        return self.member.first_name + " " + self.member.last_name + " for position {}".format(self.position)
