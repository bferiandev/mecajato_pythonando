from django.shortcuts import render
from django.views.generic import TemplateView

class ClientesView(TemplateView):
    template_name = 'clientes.html'
    