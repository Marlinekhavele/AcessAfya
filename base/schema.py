import graphene
from graphene_django import DjangoObjectType
from .models import (Issue,Location,Prescription,Patient,Staff,Visit)

class IssueType(DjangoObjectType):
    class Meta:
        model = Issue
        fields = ("id", "name", "created_at","updated_at")




