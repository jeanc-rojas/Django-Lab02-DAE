from django.urls import path
from . import views

app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),

    # URLs Tarea 1: Operaciones
    path('operaciones/', views.formulario_operacion, name='formulario_operacion'),
    path('calcular_operacion/', views.calcular_operacion, name='calcular_operacion'),
    
    # URLs Tarea 2: Cilindro
    path('cilindro/', views.formulario_cilindro, name='formulario_cilindro'),
    path('calcular_cilindro/', views.calcular_cilindro, name='calcular_cilindro'),
]
