from django.contrib import admin
from .models import (Issue,Location,Patient,Staff,Visit,Receipt,Prescription)


# Register your models here.
admin.site.register(Issue)
admin.site.register(Location)
admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Visit)
admin.site.register(Receipt)
admin.site.register(Prescription)




