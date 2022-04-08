from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=120)


class Employee(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE, related_name='employees')


class Project(models.Model):
    type = models.CharField(choices=[
        ('int', 'Internal'),
        ('ext', 'External')
    ], max_length=10)
    duration_hours = models.FloatField()
    employees = models.ManyToManyField(to=Employee, related_name='projects')
