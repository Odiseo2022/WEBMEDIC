from django.contrib import admin
from AppWebmedic.models import Especialidad_medica
from AppWebmedic.models import Datos_profesional
from AppWebmedic.models import Sedes

# Register your models here.
admin.site.register(Especialidad_medica)
admin.site.register(Datos_profesional)
admin.site.register(Sedes)