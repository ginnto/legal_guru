from django.contrib import admin
from .models import *

class AdvocateRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'officename', 'place', 'state', 'district', 'contactno')
    search_fields = ('user__username', 'specialization', 'officename')

admin.site.register(AdvocateRegistration, AdvocateRegistrationAdmin)
