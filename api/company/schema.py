import strawberry
from typing import List

from company import types


@strawberry.type
class Query:
    companies: List[types.Company] = strawberry.django.field()
    employees: List[types.Employee] = strawberry.django.field()
    projects: List[types.Project] = strawberry.django.field()


schema = strawberry.Schema(query=Query)
