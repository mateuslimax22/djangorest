from rest_framework import serializers
from hosts.models import Host
from vulnerabilities.models import Vulnerability

class HostSerializer(serializers.ModelSerializer):

    """Serializers"""
    num_vulnerability = serializers.CharField(read_only=True)
    vulnerability_title = serializers.CharField(read_only=True)
    vulnerability_severity = serializers.CharField(read_only=True)
    vulnerability_fixed = serializers.CharField(read_only=True)     
    
    class Meta:
        model = Host
        fields = ['asset_hostname','asset_ip_adress','vulnerability_severity','vulnerability_title','vulnerability_fixed','num_vulnerability']
        read_only_fields = fields

    
class HostListSerializer(serializers.ModelSerializer):

    """Serializers"""
    num_vulnerability = serializers.CharField(read_only=True)
    vulnerability_title = serializers.CharField(read_only=True)
    vulnerability_severity = serializers.CharField(read_only=True)
    vulnerability_fixed = serializers.CharField(read_only=True)
    class Meta:
        model = Host
        fields = ['asset_hostname','asset_ip_adress','vulnerability_title','vulnerability_severity','vulnerability_fixed','num_vulnerability' ]
        
