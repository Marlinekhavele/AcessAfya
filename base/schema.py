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
        fields = ("id", "name", "created_at","updated_at")

class LocationType(DjangoObjectType):
    class Meta:
        model = Location
        fields = ("id","name","description","created_at","updated_at")

class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        fields = ("id","first_name","last_name","age","phone_number","id_number","next_kin","satisfaction","created_at","updated_at")

class StaffType(DjangoObjectType):
    class Meta:
        model = Staff
        fields = ("id", "email", "first_name","last_name","date_joined","is_active","is_staff","avatar")



class VisitType(DjangoObjectType):
    class Meta:
        model = Visit
        fields = ("id", "receipt","prescription","patient", "location","staff","issues","nps","cost","created_at","updated_at")


class Query(graphene.ObjectType):
    receipt = graphene.List(ReceiptType)
    prescription = graphene.List(PrescriptionType)
    issue = graphene.List(IssueType)
    location = graphene.List(LocationType)
    patient = graphene.List(PatientType)
    staff = graphene.List(StaffType)
    visit = graphene.List(VisitType)

    def resolve_receipt(root,info):
        return Receipt.objects.all()
    
    def resolve_prescription(root,info):
        return Prescription.objects.all()


    def resolve_issue(root,info):
        return Issue.objects.all()

    def resolve_location(self, info, **kwargs):
        return Location.objects.all()

    def resolve_patient(self, info, **kwargs):
        return Patient.objects.all()

    def resolve_staff(self, info, **kwargs):
        return Staff.objects.all()

    def resolve_visit(self, info, **kwargs):
        return Visit.objects.all()

schema = graphene.Schema(query=Query)





