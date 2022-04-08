import strawberry
from strawberry.django import auto
from typing import List
from company import models


@strawberry.django.type(models.Company)
class Company:
    name: str
    employees: List['Employee']


@strawberry.django.type(models.Employee)
class Employee:
    first_name: str
    last_name: str
    company: Company
    projects: List['Project']


@strawberry.django.type(models.Project)
class Project:
    duration_hours: float
    employees: List[Employee]
