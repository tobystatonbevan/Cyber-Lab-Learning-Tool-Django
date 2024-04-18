from django.contrib import admin
from pages.models import Vulnerability

class VulnerabilityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vulnerability, VulnerabilityAdmin)