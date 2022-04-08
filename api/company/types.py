from strawberry_django_plus import gql
from typing import List
from company import models


@gql.django.type(models.Company)
class Company:
    id: gql.auto
    name: str
    employees: List['Employee']


@gql.django.type(models.Employee)
class Employee:
    id: gql.auto
    first_name: str
    last_name: str
    company: Company
    projects: List['Project']


@gql.django.type(models.Project)
class Project:
    id: gql.auto
    duration_hours: float
    employees: List[Employee]
