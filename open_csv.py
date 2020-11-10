import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vulnerabilitymanager.settings')

import django
django.setup()

import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from vulnerabilities.models import Vulnerability
from hosts.models import Host
from datetime import datetime


def add_data():

    """Load data"""
    data = pd.read_csv (r'asset_vulnerability.csv')
    interation = 0

    """Get Values"""
    for _ in range(data.shape[0]):
        asset_hostname = data.loc[interation,'ASSET - HOSTNAME']
        asset_ip_adress = data.loc[interation,'ASSET - IP_ADDRESS']
        vulnerability_title = data.loc[interation,'VULNERABILITY - TITLE']
        vulnerability_severity = data.loc[interation,'VULNERABILITY - SEVERITY']
        vulnerability_cvss = data.loc[interation,'VULNERABILITY - CVSS']
        vulnerability_publication_date = data.loc[interation,'VULNERABILITY - PUBLICATION_DATE']
        vulnerability_fixed = 'N'
        
        """Assigning Values to Vulnerability"""
        if(str(vulnerability_publication_date) == 'nan'):
            vulnerability = Vulnerability(vulnerability_title = str(vulnerability_title),vulnerability_severity= str(vulnerability_severity),vulnerability_cvss=vulnerability_cvss,
            vulnerability_publication_date = datetime.today().strftime('%Y-%m-%d') ,vulnerability_fixed=str(vulnerability_fixed))
            
        else:
            vulnerability = Vulnerability(vulnerability_title = str(vulnerability_title),vulnerability_severity= str(vulnerability_severity),vulnerability_cvss=vulnerability_cvss,
            vulnerability_publication_date = vulnerability_publication_date,vulnerability_fixed=str(vulnerability_fixed))
            
        """ADD Values to database"""
        try:
            Compare = Vulnerability.objects.filter(vulnerability_title = str(vulnerability_title)).get(vulnerability_title = str(vulnerability_title))
            if(str(Compare) == str(vulnerability_title)):
                hosts = Host(asset_hostname = asset_hostname, asset_ip_adress = asset_ip_adress, vulnerability_id = Vulnerability.objects.latest('pk').pk)
                hosts.save()

                pk_host = Host.objects.latest('pk').pk
                lasthost = Host.objects.filter(pk=pk_host).get(pk=pk_host)
                lasthost.host.add(Vulnerability.objects.latest('pk').pk)
        
        except ObjectDoesNotExist:
                vulnerability.save()
                hosts = Host(asset_hostname = asset_hostname, asset_ip_adress = asset_ip_adress, vulnerability_id = Vulnerability.objects.latest('pk').pk)
                hosts.save()

                pk_host = Host.objects.latest('pk').pk
                lasthost = Host.objects.filter(pk=pk_host).get(pk=pk_host)
                lasthost.host.add(vulnerability)

        interation+= 1
        
    print("Successfully added !!!!")

add_data()