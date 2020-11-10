from rest_framework import viewsets, filters, generics
from vulnerabilities.models import Vulnerability
from hosts.models import Host
from django.db.models import F,Count, Q, Subquery,OuterRef
from vulnerabilities.serializer import VulnerabilitySerializer, VulnerabilityListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class VulnerabilitiesViewSet(viewsets.ModelViewSet):
    serializer_class = VulnerabilitySerializer

    """Authentication"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    """Filters"""
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter ]
    search_fields = ['host_list__asset_hostname','vulnerability_severity', 'vulnerability_fixed']
    filterset_fields = ['vulnerability_severity','host_list__asset_hostname']
    
    def get_queryset(self):

        """Count affected hosts"""
        query_count=Vulnerability.objects.prefetch_related('vulne').filter(Q(vulnerability_fixed= 'N')).values('id').filter(id=OuterRef('id')).order_by()
        sum_id = query_count.annotate(count_id=Count('id')).values('count_id')
        queryset = Vulnerability.objects.prefetch_related('vulne').annotate(num_host = Subquery(sum_id))
        query_update = Vulnerability.objects.prefetch_related('vulne').filter(vulnerability_fixed = "Y").annotate(host_id = F('host_list__id'))
        
        for x in query_update:  #Update the vulnerability values
            if(x.host_id != None):
                last_vulne = Vulnerability.objects.filter(pk = x.id).update(vulnerability_severity="Low",vulnerability_fixed='Y')
                
        return queryset

class VulnerabilityList(generics.ListAPIView):
    serializer_class= VulnerabilityListSerializer

    """Authentication"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        """Count affected hosts"""
        query_count=Vulnerability.objects.prefetch_related('vulne').filter(Q(vulnerability_fixed= 'N')).values('id').filter(id=OuterRef('id')).order_by()
        sum_id = query_count.annotate(count_id=Count('id')).values('count_id')
        queryset = Vulnerability.objects.prefetch_related('vulne').filter(id=self.kwargs['pk']).annotate(num_host = Subquery(sum_id))
        return queryset
