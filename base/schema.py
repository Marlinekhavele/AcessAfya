import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import (Issue,Location,Patient,Staff,Visit)

class IssueType(DjangoObjectType):
    class Meta:
        model = Issue
        fields = ("id", "name", "created_at","updated_at")

class Query(graphene.ObjectType):
    all_issue = graphene.List(IssueType)

schema = graphene.Schema(query=Query)





