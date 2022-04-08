import strawberry
from typing import List

from company import types, models


@strawberry.type
class Query:
    company: types.Company = strawberry.django.field()
    employee: types.Employee = strawberry.django.field()
    project: types.Project = strawberry.django.field()
    companies: List[types.Company] = strawberry.django.field()
    employees: List[types.Employee] = strawberry.django.field()
    projects: List[types.Project] = strawberry.django.field()


@strawberry.type
class Mutation:

    @strawberry.mutation
    def add_company(self, name: str) -> types.Company:
        return types.Company(name=name, employees=[])


schema = strawberry.Schema(query=Query, mutation=Mutation)
