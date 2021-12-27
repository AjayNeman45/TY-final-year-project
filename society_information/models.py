from django.db import models

# Create your models here.

class SocietyInformation(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=1000)
    number_of_Flats = models.IntegerField()
    number_of_Residents = models.IntegerField()
    number_of_Tenants = models.IntegerField()
    number_of_Wings = models.IntegerField()

    def __str__(self):
        return self.name
