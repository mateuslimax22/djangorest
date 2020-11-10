from rest_framework import serializers
from vulnerabilities.models import Vulnerability
from hosts.serializer import HostSerializer


class VulnerabilitySerializer(serializers.ModelSerializer):

    """Serializers"""
    num_host = serializers.IntegerField(read_only=True)
    host_list = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='asset_hostname'
     )
     
    class Meta:
        model = Vulnerability
        fields = ['host_list','vulnerability_title', 'vulnerability_severity', 'vulnerability_cvss',
        'vulnerability_publication_date', 'vulnerability_fixed','num_host']
        read_only_fields = ['host_list','vulnerability_title', 'vulnerability_severity', 'vulnerability_cvss',
        'vulnerability_publication_date','num_host']


class VulnerabilityListSerializer(serializers.ModelSerializer):
    
    """Serializers"""
    num_host = serializers.IntegerField(read_only=True)
    host_list = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='asset_hostname'
     )
     
    class Meta:
        model = Vulnerability
        fields = ['host_list','vulnerability_title', 'vulnerability_severity', 'vulnerability_cvss',
        'vulnerability_publication_date', 'vulnerability_fixed','num_host']
