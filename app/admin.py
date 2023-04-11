from django.contrib import admin

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

class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id','area','asunto','registro', 'created_at','updated_at')
    search_fields =  ('area__nombre','asunto__categoria','registro')
    list_filter = ('registro','created_at','asunto',)
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