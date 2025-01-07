from django.contrib import admin
from .models import *


class specadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields ={'slug':('name',)}
admin.site.register(specializations,specadmin)


class AdvocateRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'officename', 'place', 'state', 'district', 'contactno')
    search_fields = ('user__username', 'specialization', 'officename')

admin.site.register(AdvocateRegistration, AdvocateRegistrationAdmin)
