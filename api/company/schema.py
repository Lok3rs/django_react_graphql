import strawberry
from typing import List

import strawberry_django

from company import types


@strawberry.type
class Query:
    companies: List[types.Company] = strawberry_django.field()
    employees: List[types.Employee] = strawberry_django.field()
    projects: List[types.Project] = strawberry_django.field()
