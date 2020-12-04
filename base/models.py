from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from decimal import Decimal

# Create your models here.
class Receipt(models.Model):
    """receipt model"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name

class Prescription(models.Model):
    """ prescription model"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name


class Issue(models.Model):
    """issue model"""
    name = models.CharField(max_length=100)
    receipt = models.ForeignKey(Receipt,on_delete=models.CASCADE,related_name="receipt")
    prescription = models.ForeignKey(Prescription,on_delete=models.CASCADE,related_name="prescription")
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

class Patient(models.Model):
    """ Patient Model"""
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)  
    phone_number = models.IntegerField() 
    id_number = models.IntegerField() 
    next_kin = models.TextField()       
    satisfaction = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.first_name


class Staff(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name


class Visit(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="patient")
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name="location")
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,related_name="staff")
    issues = models.ManyToManyField('Issue')
    nps = models.IntegerField()
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal("0.00"))
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    def ___str___(self):
        return "{} visit at {}".format(self.patient.name, self.location.name)















    




    



    
