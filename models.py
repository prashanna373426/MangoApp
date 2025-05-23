from django.db import models

class Grower(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.EmailField()

    def __str__(self):
        return self.name

class PlantPart(models.Model):
    part_name = models.CharField(max_length=50)

    def __str__(self):
        return self.part_name

class SurveillanceRecord(models.Model):
    grower = models.ForeignKey(Grower, on_delete=models.CASCADE)
    date = models.DateField()
    plant_count = models.IntegerField()
    plant_parts = models.ManyToManyField(PlantPart)
    notes = models.TextField()

    def __str__(self):
        return f"{self.grower.name} - {self.date}"
