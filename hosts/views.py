from rest_framework import viewsets, filters, generics
from hosts.models import Host
from django.db.models import F, Count, Q, OuterRef, Subquery
from hosts.serializer import HostSerializer, HostListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class HostsViewSet(viewsets.ModelViewSet):
    serializer_class = HostSerializer

    """Authentication"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    """Filters"""
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter ]
    search_fields = ['vulnerability_title','asset_hostname']
    ordering_fields = ['asset_hostname','asset_ip_adress','num_vulnerability']
    filterset_fields = ['host__vulnerability_title']
    
    def get_queryset(self):

        """Count affected hosts"""
        query_count = Host.objects.select_related('vulnerability').filter(Q(host__vulnerability_fixed= 'N')).values('id').filter(id=OuterRef('id')).order_by()
        sum_id = query_count.annotate(count_id=Count('id')).values('count_id')
        queryset = Host.objects.select_related('vulnerability').annotate(vulnerability_fixed= F('host__vulnerability_fixed')).annotate(num_vulnerability = Subquery(sum_id)).annotate(
        vulnerability_severity = F('host__vulnerability_severity')).annotate(vulnerability_title = F('host__vulnerability_title'))
        return queryset

class HostList(generics.ListAPIView):
    serializer_class= HostListSerializer

    """Authentication"""
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        """Count affected hosts"""
        query_count = Host.objects.select_related('vulnerability').filter(Q(host__vulnerability_fixed= 'N')).values('id').filter(id=OuterRef('id')).order_by()
        sum_id= query_count.annotate(count_id=Count('id')).values('count_id')
        queryset = Host.objects.filter(id=self.kwargs['pk']).annotate(num_vulnerability = Subquery(sum_id)).annotate(vulnerability_title = F('host__vulnerability_title')).annotate(
        vulnerability_severity = F('host__vulnerability_severity')).annotate(vulnerability_fixed= F('host__vulnerability_fixed'))

        return queryset
    
    


