from django.db import models


class Pet(models.Model):  # inherit from model
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()  # no restricted length
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)  # null means unknown, blank might be 0
    vaccinations = models.ManyToManyField('Vaccine', blank=True)  # a pet can have many vaccines


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self): # override how the name of the vaccine is displayed - change str representation
        return self.name
