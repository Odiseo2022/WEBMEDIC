from unicodedata import name
from django.urls import path
from AppWebmedic.views import principal, solicitud, institucional,inicio, especialidad, formulario_consulta





urlpatterns = [
    path('inicio/', inicio,),
    path('principal/', principal,),
    path('solicitud/', solicitud),
    path('institucional/', institucional),
    path('especialidad/', especialidad),
    path('formulario/', formulario_consulta),
]