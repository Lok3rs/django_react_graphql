import strawberry
from strawberry_django_plus import gql
from strawberry_django_plus.optimizer import DjangoOptimizerExtension
from typing import List, Optional

from strawberry_django_plus.relay import GlobalID

from company import types, models


@gql.django.input(models.Company)
class CompanyInput:
    name: gql.auto


@gql.django.partial(models.Company)
class CompanyInputPartial(gql.NodeInput):
    name: gql.auto


@gql.django.input(models.Employee)
class EmployeeInput:
    first_name: gql.auto
    last_name: gql.auto
    company: gql.auto


@gql.django.partial(models.Employee)
class EmployeeInputPartial(gql.NodeInput):
    first_name: gql.auto
    last_name: gql.auto
    company: gql.auto


@gql.type
class Query:
    companies: List[types.Company] = gql.django.field()
    employees: List[types.Employee] = gql.django.field()
    projects: List[types.Project] = gql.django.field()


@gql.type
class Mutation:
    # !IMPORTANT : ID FIELD NEEDS TO BE ALWAYS ENCODED TO BASE64
    # For example Company:1 == Q29tcGFueTox

    """
    mutation {
      createCompany(input: {name: "First Company"}) {
        ... on Company {
          name
        }
      }
    }
    """
    create_company: types.Company = gql.django.create_mutation(CompanyInput)

    """
    mutation {
      updateCompany(input: {id: "Q29tcGFueTox", name: "First Name Changed"}) {
        ... on Company {
          name
        }
      }
    }
   """
    update_company: types.Company = gql.django.update_mutation(CompanyInputPartial)
    delete_company: types.Company = gql.django.delete_mutation(gql.NodeInput)
    """
    mutation {
      createEmployee(input: {firstName: "Dawid", lastName: "Adamski", company: {id: "Q29tcGFueTox"}}) {
        ... on Employee {
          firstName
        }
      }
    }
    """
    create_employee: types.Employee = gql.django.create_mutation(EmployeeInput)
    update_employee: types.Employee = gql.django.update_mutation(EmployeeInputPartial)
    delete_employee: types.Employee = gql.django.delete_mutation(gql.NodeInput)


schema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[DjangoOptimizerExtension])
