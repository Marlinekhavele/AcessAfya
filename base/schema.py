import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import (Receipt,Prescription,Issue,Location,Patient,Staff,Visit)



class ReceiptType(DjangoObjectType):
    class Meta:
        model = Receipt
        fields = ("id", "name", "created_at","updated_at")

class PrescriptionType(DjangoObjectType):
    class Meta:
        model = Prescription
        fields = ("id", "name", "created_at","updated_at")

class IssueType(DjangoObjectType):
    class Meta:
        model = Issue
        fields = ("id", "name", "receipt","prescription","created_at","updated_at")

class Query(graphene.ObjectType):
    receipt = graphene.List(ReceiptType)
    prescription = graphene.List(PrescriptionType)
    issue = graphene.List(IssueType)


    def resolve_receipt(root,info):
        return Receipt.objects.all()
    
    def resolve_prescription(root,info):
        return Prescription.objects.all()


    def resolve_issue(root,info):
        return Issue.objects.all()

schema = graphene.Schema(query=Query)





