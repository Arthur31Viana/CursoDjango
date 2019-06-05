from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class CPF(models.Model):
    numero = models.CharField(max_length=15)
    # Data de expedição do cpf
    data_exp = models.DateTimeField(auto_now=False) #auto_now=False significa que ele não pode pegar a data atual pq o cpf foi emitido antes

    def __str__(self):
        return self.numero

class Empregado(models.Model):
    #Campo de letras
    nome = models.CharField(max_length=70, blank=False, null=False) #Length = Quant. de caracteres, blank = Pode ficar em branco, null = Não obrigatório
    endereco = models.CharField(max_length=200, blank=False, null=False)
    #Campo de digitos decimais
    salario = models.DecimalField(max_digits=10, decimal_places=2) #digits = Quant. de digitos, places = Casas após a virgula
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, on_delete=0, null=True, blank=True) #Campo opcional
    departamentos = models.ManyToManyField(Departamento, blank=True) #Muitos para Muitos
    foto = models.ImageField(upload_to='cliente_fotos')

    #Retorna o objeto criado no admin do Django
    def __str__(self):
        return self.nome


class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    
    #Criar chave primaria de um para muitos
    empregado = models.ForeignKey(Empregado, on_delete=0)
    
    def __str__(self):
        return self.descricao + ' - ' + self.numero
