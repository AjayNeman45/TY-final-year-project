from django.db import models

# Create your models here.

class SocietyInformation(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=1000)
    number_of_Flats = models.IntegerField()
    number_of_Residents = models.IntegerField()
    number_of_Tenants = models.IntegerField()
    number_of_Wings = models.IntegerField()
    total_Area = models.IntegerField(null=True, blank=True)
    registration_Date = models.DateField( null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.name
