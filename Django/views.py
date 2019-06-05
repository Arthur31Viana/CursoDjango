from django.http import HttpResponse  #Enviando resposta ao usuário
from django.shortcuts import render #Renderizando arquivos em HTML

'''
def home(request):
    sexo = 'f'
    nome = 'Nathalia'
    return render(request, 'index.html', {'sexo': sexo, 'nome': nome}) #Jogando variável para o templatesdef home(request):
'''

def home(request):
    sexo = 'f'
    nome = 'Nathalia'
    lista = [
        {'nome': 'Arthur', 'sexo':'m'},
        {'nome': 'Nathalia', 'sexo':'f'},
        {'nome': 'Joaquina', 'sexo':'f'},
        {'nome': 'joão', 'sexo':'m'},
    ]
    data = {'lista': lista, 'sexo': sexo, 'nome': nome}
    return render(request, 'index.html', data) #Jogando variável para o templates
