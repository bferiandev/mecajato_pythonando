from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Carro
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.shortcuts import redirect
import re
import json


def clientes(request):
    if request.method == 'GET':
        clientes_list = Cliente.objects.all()
        return render(request, 'clientes.html', {'clientes': clientes_list})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carro = request.POST.getlist('carro')
        placa = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente.exists():
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carro, placa, ano)})
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carro, placa, ano)})

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        cliente.save()
        
        for carro, placa, ano in zip(carro, placa, ano):
            car = Carro(carro=carro, placa=placa, ano=ano, cliente=cliente)
            car.save()
        
        return render(request, 'clientes.html')
       

def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')

    cliente = Cliente.objects.filter(id=id_cliente)
    carros = Carro.objects.filter(cliente=cliente[0])
    
    clientes_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    carros_json = json.loads(serializers.serialize('json', carros))
    
    carros_json = [{'fields': carro['fields'], 'id': carro['pk']} for carro in carros_json]
   
    data = {'cliente': clientes_json, 'carros': carros_json}

    return JsonResponse(data)


@csrf_exempt
def update_carro(request, id):    
    nome_carro = request.POST.get('carro')
    placa = request.POST.get('placa') 
    ano = request.POST.get('ano')

    carro = Carro.objects.get(id=id)
    list_carros = Carro.objects.filter(placa=placa).exclude(id=id)
    
    if list_carros.exists():
        return HttpResponse('Placa existente')
    
    carro.carro = nome_carro
    carro.placa = placa
    carro.ano = ano
    carro.save()
    
    return HttpResponse('Dados alterados com sucesso')


def excluir_carro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()
        return redirect(reverse_lazy('clientes_app:clientes')+f'aba=att_cliente&id_cliente={id}')
    except:
        #TODO: MENSAGEM DE ERRO
        return redirect(reverse_lazy('clientes_app:clientes')+f'aba=att_cliente&id_cliente={id}')







#TODO: remover carros
