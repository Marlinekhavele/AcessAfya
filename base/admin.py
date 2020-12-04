from django.contrib import admin
from .models import (Issue,Location,Patient,Staff,Visit)


# Register your models here.
admin.site.register(Issue)
admin.site.register(Location)
admin.site.register(Patient)
admin.site.register(Staff)
admin.site.register(Visit)


