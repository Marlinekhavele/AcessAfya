from django.contrib import admin
from .models import Customer, Receipt, Prescription, Order,Location,Staff,KeyIssues


# Register your models here.
admin.site.register(Customer)
admin.site.register(Receipt)
admin.site.register(Prescription)
admin.site.register(Order)
admin.site.register(Location)
admin.site.register(Staff)
admin.site.register(KeyIssues)


