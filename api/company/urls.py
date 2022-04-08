from django.urls import include, path
from strawberry.django.views import AsyncGraphQLView
from company import schema

urlpatterns = [
    path('graphql', AsyncGraphQLView.as_view(schema=schema))
]
