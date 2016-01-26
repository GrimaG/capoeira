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

#singleto+decorator
def singleton(class_):
  class class_w(class_):
    _instance = None
    def __new__(class_, *args, **kwargs):
      if class_w._instance is None:
          class_w._instance = super(class_w,
                                    class_).__new__(class_,
                                                    *args,
                                                    **kwargs)
          class_w._instance._sealed = False
      return class_w._instance
    def __init__(self, *args, **kwargs):
      if self._sealed:
        return
      super(class_w, self).__init__(*args, **kwargs)
      self._sealed = True
  class_w.__name__ = class_.__name__
  return class_w
#fabrica
@singleton
class factory(models.Model):

    def retornar_objeto(self, objeto):
        if objeto== "aluno":
            return Aluno
        if objeto== "professor":
            return  Professor
        if objeto == "grupo":
            return Grupo
        if objeto == "turma":
            return Turma
        if objeto == "exame":
            return  Exame
