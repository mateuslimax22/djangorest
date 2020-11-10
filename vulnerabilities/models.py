from django.db import models

class Vulnerability(models.Model):
    
    """Database Model"""
    FIXED = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    vulnerability_title = models.CharField(max_length=200)
    vulnerability_severity = models.CharField(max_length=50)
    vulnerability_cvss = models.FloatField()
    vulnerability_publication_date= models.DateField()
    vulnerability_fixed = models.CharField(max_length=1, choices=FIXED, blank=False, default='N')
    
    

    def __str__(self):
        return self.vulnerability_title
