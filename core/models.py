from django.db import models

# Create your models here.
class AccidentReport(models.Model):
    report= models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime= models.DateTimeField(auto_now_add=True)
    urgency =models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ("medium", 'Medium'),
        ('high', 'High'),  
    ], default='low')
    def __str__(self):
        return f"Accident Report: {self.report} at ({self.latitude}, {self.longitude}) on {self.datetime} with urgency {self.urgency}"
    