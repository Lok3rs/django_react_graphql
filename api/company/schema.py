import strawberry
from strawberry_django_plus import gql
from strawberry_django_plus.optimizer import DjangoOptimizerExtension
from typing import List

from company import types, models


@gql.django.input(models.Company)
class CompanyInput:
    name: gql.auto


@gql.django.partial(models.Company)
class CompanyInputPartial(gql.NodeInput):
    name: gql.auto


@gql.type
class Query:
    companies: List[types.Company] = gql.django.field()
    employees: List[types.Employee] = gql.django.field()
    projects: List[types.Project] = gql.django.field()


@gql.type
class Mutation:
    create_company: types.Company = gql.django.create_mutation(CompanyInput)
    update_company: types.Company = gql.django.update_mutation(CompanyInputPartial)
    delete_company: types.Company = gql.django.delete_mutation(gql.NodeInput)


schema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[DjangoOptimizerExtension])
