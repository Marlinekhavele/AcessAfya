from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from decimal import Decimal




# Create your models here.
class Issue(models.Model):
    """issue model"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    def ___str___(self):
        return self.name


class Location(models.Model):
    """Location Model"""
    name = models.CharField(max_length=100)
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name

class Prescription(models.Model):
    """ prescription Model"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)



    def ___str___(self):
        return self.name

class Patient(models.Model):
    """ Patient Model"""
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)  
    phone_number = models.IntegerField() 
    id_number = models.IntegerField() 
    next_kin = models.IntegerField()       
    satisfaction = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name

class Receipt(models.Model):
    """ receipt Model"""
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name="location")
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="customer")
    prescription = models.ForeignKey(Prescription,on_delete=models.CASCADE,related_name="prescription")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name



class Staff(models.Model):
    """ Staff Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    def ___str___(self):
        return self.name

class Visit(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="patient")
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name="location")
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name="staff")
    Issue= models.ManyToManyField()
    nps = models.IntegerField()
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


    def ___str___(self):
        return self.nps















    




    



    
