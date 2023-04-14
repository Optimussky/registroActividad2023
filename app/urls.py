from django.contrib import admin
from django.urls import path

admin.site.site_header = 'Registro de Actividades'                    # default: "Django Administration"
admin.site.index_title = 'Módulos'                 # default: "Site administration"
admin.site.site_title = 'Sistema de Registro de Actividades' # default: "Django site admin"


urlpatterns = [
    path('admin/', admin.site.urls),
]
