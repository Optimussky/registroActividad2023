from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Agenda
#from . import models
# Register your models here.

class AgendaResources(resources.ModelResource):

    fields = ('id','area_persona','numero',)

    class Meta:
        model = Agenda



class AgendaAdmin(ImportExportModelAdmin,admin.ModelAdmin):

	resource_class = AgendaResources
	readonly_fields = ('created_at','updated_at')
	list_display=('id','area_persona','numero','created_at')
	search_fields=('area_persona',)
	list_filter=('area_persona',)
	list_display_links=('area_persona',)

	ordering=['area_persona']


admin.site.register(Agenda,AgendaAdmin)