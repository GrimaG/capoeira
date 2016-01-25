from django.db import models
from django.utils import timezone
from django.http import HttpResponse
# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Corda(models.Model):
    cor = models.CharField(max_length=100   )
    def __str__(self):
        return self.cor


class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    sequencia_corda = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100, default='')
    numero = models.IntegerField( default=0)
    bairro = models.CharField(max_length=100, default='')
    cidade = models.CharField(max_length=100, default='')
    complemento = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=50)
    profissao = models.CharField(max_length=50)
    grau_escolar = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=100, default='')
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=100, default='')
    cidade = models.CharField(max_length=100, default='')
    complemento = models.CharField(max_length=100, default='')
    cor_corda = models.ForeignKey(Corda)

    def __str__(self):
        return self.nome

class Professor(Pessoa):
    registro = models.CharField(max_length=100)

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    turno = models.CharField(max_length=100)
    horario = models.DateField(default=0)
    dia_semana = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, default=None)
    professor = models.ForeignKey(Professor, default=None)

class Aluno(Pessoa):
    turma = models.ForeignKey(Turma, default=None)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Exame(models.Model):
    data = models.DateField() #Considerando que data e hora estao contidos no mesmo campo
    logradouro = models.CharField(max_length=100, default='')
    numero = models.IntegerField(default=0)
    bairro = models.CharField(max_length=100, default='')
    cidade = models.CharField(max_length=100, default='')
    complemento = models.CharField(max_length=100, default='')
    mestre_examinador =  models.ForeignKey(Professor)
    turma = models.ForeignKey(Turma)

#Composite menu navegacao
class Menu(models.Model):
    item = ''
    def __init__(self, item):
        item = item

    def get_item():
        return self.item

class Part(Menu):
    def __init__(self, arg):
        super(self.__class__, self).__init__(arg)

class Assembly(Menu):
    list=""
    def __init__(self):
        list=""
    def add(self,item):
        self.list+=item
    def monta_menu(self):
        return HttpResponse(list)

class criar_menu(models.Model):
    menu = Assembly()
    def __init__(self):
        submenu_grupo = Part("<a class='{% navactive request 'servers help_server' %}' href='{% url list_group %}'>Grupos</a>")
        menu.add(submenu_grupo.item)
