from django.contrib import admin
from hosts.models import Host

class Hosts(admin.ModelAdmin):
    list_display = ('id','asset_hostname', 'asset_ip_adress')
    list_display_links = ('id', 'asset_hostname')
    search_fields = ('asset_hostname',)
    list_per_page = 50
    ordering = ('asset_hostname',)

admin.site.register(Host, Hosts)