from django.contrib import admin
from .models import Grower, PlantPart, SurveillanceRecord

# Register your models here.
admin.site.register(Grower)
admin.site.register(PlantPart)
admin.site.register(SurveillanceRecord)