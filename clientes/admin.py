from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento


class EmpregadoAdmin(admin.ModelAdmin):
    #fields = ('nome', 'endereco') #Não esquecer de não ocultar itens obrigatórios
    list_display = ('id', 'nome', 'endereco', 'email')
    list_filter = ('departamentos', ) #Criar uma coluna de filtragem
    search_fields = ('id', 'nome', 'email', 'departamentos__nome') #Campo de busca


#Classes Registradas no Admin do Django
admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(Departamento)
admin.site.register(CPF)
