from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Employee(models.Model):
    EmpCode = models.CharField(max_length=150)
    EmpName = models.EmailField(blank=True)
    Dept = models.CharField(max_length=50)
    Age = models.IntegerField(blank=True, null=True)
    Experience = models.TextField()

    def __str__(self):
        return self.EmpName
