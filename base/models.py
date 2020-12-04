from django.db import models
from datetime import datetime


# Create your models here.
class Location(models.Model):
    """Location Model"""
    name = models.CharField(max_length=100)
    def ___str___(self):
        return self.name

class Prescription(models.Model):
    """ prescription Model"""
    name = models.CharField(max_length=100)

    def ___str___(self):
        return self.name

class Customer(models.Model):
    """ Customer Model"""
    name = models.CharField(max_length=100)        
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name="location")
    prescription = models.ForeignKey(Prescription,on_delete=models.CASCADE,related_name="prescription")
    # receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,related_name="receipt")
    # order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order")
    satisfaction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name

class Receipt(models.Model):
    """ receipt Model"""
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name="location")
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="customer")
    prescription = models.ForeignKey(Prescription,on_delete=models.CASCADE,related_name="prescription")
    def ___str___(self):
        return self.name

class Order(models.Model):
    """Order Model"""
    name = models.CharField(max_length=100)
    prescription = models.ForeignKey(Prescription,on_delete=models.CASCADE,related_name="prescription")
    customer = models .ForeignKey(Customer,on_delete=models.CASCADE,related_name="customer")
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name="location")
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,related_name="receipt")
    def ___str___(self):
        return self.name


class Staff(models.Model):
    """ Staff Model"""
    name = models.CharField(max_length=100)

    def ___str___(self):
        return self.name

class KeyIssues(models.Model):
    """ Key Issues Model"""
    name = models.CharField(max_length=100)
    customer = models .ForeignKey(Customer,on_delete=models.CASCADE,related_name="customer")
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name="location")
    def ___str___(self):
        return self.name






    






    




    



    
