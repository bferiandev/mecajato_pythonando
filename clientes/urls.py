from django.urls import path
from . import views


app_name='clientes_app'

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/atualiza_cliente/', views.att_cliente, name='atualiza_clientes'),  
]
