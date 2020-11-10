from django.db import models
from vulnerabilities.models import Vulnerability

class Host(models.Model):

    """Database Model"""
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, related_name='vulne')
    asset_hostname = models.CharField(max_length=50)
    asset_ip_adress = models.CharField(max_length=20)
    host = models.ManyToManyField(Vulnerability,related_name="host_list", blank=True)
    
    def __str__(self):
        return self.asset_hostname