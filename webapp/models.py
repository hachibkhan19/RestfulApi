from django.db import models


# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstName
