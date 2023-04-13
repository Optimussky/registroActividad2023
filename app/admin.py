from import_export import resources
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Areas, Asunto, Registro, Agenda_telefonica


class AreasAdmin(admin.ModelAdmin):
    list_display = ['id','nombre', 'created_at',]
    search_fields =  ('nombre',)
    ordering = ['nombre']
    list_display_links = ('nombre',)
    #actions = [make_published]

admin.site.register(Areas,AreasAdmin)

class AsuntoAdmin(admin.ModelAdmin):
    list_display = ['id','categoria','created_at' ]
    search_fields =  ('categoria',)
    ordering = ['categoria']
    list_display_links = ('categoria',)
    #actions = [make_published]

admin.site.register(Asunto,AsuntoAdmin)

class RegistroResources(resources.ModelResource):

    #fields = ('area__nombre','asunto__categoria','registro', 'created_at','updated_at')

    class Meta:
        model = Registro

class RegistroAdmin(admin.ModelAdmin):
    resource_class = RegistroResources
    readonly_fields = ('created_at','updated_at')
    list_display = ('id','area','asunto','registro', 'created_at','updated_at')
    search_fields =  ('area__nombre','asunto__categoria','registro')
    #list_filter = ('registro','created_at','asunto',)
    list_filter = ('created_at','asunto__categoria')
    list_display_links = ('area',)
    
    
    
    ordering = ['-created_at']
    #actions = [make_published]

admin.site.register(Registro,RegistroAdmin)

class Agenda_telefonicaAdmin(admin.ModelAdmin):
    list_display = ('id','area_persona','numero','created_at')
    search_fields = ('area_persona','numero')
    list_filter = ('area_persona','numero')
    list_display_links = ('area_persona',)

    ordering = ['area_persona']

admin.site.register(Agenda_telefonica,Agenda_telefonicaAdmin)