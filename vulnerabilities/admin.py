from django.contrib import admin
from vulnerabilities.models import Vulnerability

class Vulnerabilities(admin.ModelAdmin):
    list_display = ('id','vulnerability_title','vulnerability_severity',
    'vulnerability_cvss','vulnerability_publication_date','vulnerability_fixed')
    list_display_links = ('id', 'vulnerability_title')
    search_fields = ('vulnerability_title',)
    list_per_page = 50
    ordering =('vulnerability_title',)

admin.site.register(Vulnerability, Vulnerabilities)