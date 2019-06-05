from django.shortcuts import render
from django.http import HttpResponse  #Enviando resposta ao usuário


'''
Toda function based views tem por obrigação dar uma request
toda request tem que dar um response
'''

#Criando Views
def clientes(request):
    return HttpResponse('Maria, José, João')

def cliente_detalhe(request, id):
    return HttpResponse(id)

def cliente_por_nome(request, nome):
    return HttpResponse('Olá %s' % nome)