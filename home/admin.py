from django.contrib import admin
from .models import CaseRequest

@admin.register(CaseRequest)
class CaseRequestAdmin(admin.ModelAdmin):
    list_display = ('req_id', 'lawyer', 'name', 'email', 'phone', 'approval', 'cust_approval')
    list_filter = ('approval', 'cust_approval')
    search_fields = ('name', 'email', 'lawyer')
