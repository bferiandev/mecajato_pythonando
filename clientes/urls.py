from django.urls import path
from .views import ClientesView


app_name='clientes'
urlpatterns = [
    path('clientes/', ClientesView.as_view(), name="clientes"),
]
