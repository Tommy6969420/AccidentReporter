from django.db import models

# Create your models here.
class Accident(models.Model):
    report= models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    date= models.DateField(auto_now_add=True)
    