from django.db import models


# Create your models here.
class GestationalTable(models.Model):
    MedicalStatus = [
        ("True", "True"),
        ("False", "False"),
        ("Others", "Others"),
    ]

    GenderStatus = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("None Binary", "None Binary"),
        ("Other", "Other"),
    ]

    age = models.IntegerField()
    medical_history = models.CharField(max_length=20, choices=MedicalStatus, default='True')
    documents = models.TextField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=20, choices=MedicalStatus, default='True')
    volunteer_health = models.BooleanField(default=True)
    height = models.FloatField(default=0.0)
    unit_of_height = models.CharField(max_length=100, blank=True, null=True)
    weight = models.FloatField(default=0.0)
    unit_of_weight = models.CharField(max_length=100, blank=True, null=True)
    temperature = models.FloatField(default=0.0)
    unit_of_temperature = models.CharField(max_length=100, blank=True, null=True)
    blood_pressure = models.FloatField(max_length=100, blank=True, null=True)
    unit_of_blood_pressure = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "gestation"


class GestationalImages(models.Model):
    image = models.FileField(upload_to='images/')
    gestation = models.ForeignKey("GestationalTable", on_delete=models.CASCADE, related_name="gestation")

    class Meta:
        db_table = "gestation_images"
