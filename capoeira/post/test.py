from django.test import TestCase
import unittest
from capoeira.models import *

class EnderecoCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")

    def testCreating(self):
        self.assertEquals(self.ifes.bairro, "manguinhos")

class EnderecoUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.ifes.bairro = "jacaraipe"
    def testCreating(self):
        self.assertEquals(self.ifes.bairro, "jacaraipe")

#####################################################################################################################

class GrupoCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)

    def testCreating(self):
        self.assertEquals(self.beatles.nome, "mutantes")

class GrupoUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.beatles.nome = "x-man"
    def testCreating(self):
        self.assertEquals(self.beatles.nome, "x-man")

#####################################################################################################################

class PessoaCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)


    def testCreating(self):
        self.assertEquals(self.joao.nome, "Joao")


class PessoaUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.joao.nome = "jao"
    def testCreating(self):
        self.assertEquals(self.joao.nome, "jao")

#####################################################################################################################


class AlunoCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)

    def testCreating(self):
        self.assertEquals(self.platini.mae, "Eva")

class AlunoUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.platini.nome = "platini"
    def testCreating(self):
        self.assertEquals(self.platini.nome, "platini")

#####################################################################################################################


class ProfessorCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo = Professor.objects.create(registro="992345",nome="Paulo",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)

    def testCreating(self):
        self.assertEquals(self.paulo.registro, "992345")

class ProfessorUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo = Professor.objects.create(registro="992345",nome="Paulo",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo.nome = "Paulo Sergio"
    def testCreating(self):
        self.assertEquals(self.paulo.nome, "Paulo Sergio")

#####################################################################################################################


class TurmaCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo = Professor.objects.create(registro="992345",nome="Paulo",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.turma1 = Turma.objects.create(nome="turma1",turno="matutino",horario="2016-01-01",dia_semana="Segunda",aluno=self.platini,professor=self.paulo)

    def testCreating(self):
        self.assertEquals(self.paulo.registro, "992345")

class TurmaUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo = Professor.objects.create(registro="992345",nome="Paulo",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.turma1 = Turma.objects.create(nome="turma1",turno="matutino",horario="2016-01-01",dia_semana="Segunda",aluno=self.platini,professor=self.paulo)
        self.turma1.nome = "turma2"
    def testCreating(self):
        self.assertEquals(self.turma1.nome, "turma2")

#####################################################################################################################


class ExameCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo = Professor.objects.create(registro="992345",nome="Paulo",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.turma1 = Turma.objects.create(nome="turma1",turno="matutino",horario="2016-01-01",dia_semana="Segunda",aluno=self.platini,professor=self.paulo)
        self.exame1 = Exame.objects.create(data="2016-01-01",endereco=self.ifes,mestre_examinador="Paulo",turma=self.turma1)

    def testCreating(self):
        self.assertEquals(self.exame1.data, "2016-01-01")

class ExameUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.ifes = Endereco.objects.create(logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",endereco = self.ifes)
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo = Professor.objects.create(registro="992345",nome="Paulo",rg="123",data_nascimento="1991-03-03",endereco = self.ifes,telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.turma1 = Turma.objects.create(nome="turma1",turno="matutino",horario="2016-01-01",dia_semana="Segunda",aluno=self.platini,professor=self.paulo)
        self.exame1 = Exame.objects.create(data="2016-01-01",endereco=self.ifes,mestre_examinador="Paulo",turma=self.turma1)
        self.exame1.data = "2016-02-01"

    def testCreating(self):
        self.assertEquals(self.exame1.data, "2016-02-01")

#########################################################################################################################

class CordaCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.corda1 = Corda.objects.create(cor="azul")

    def testCreating(self):
        self.assertEquals(self.corda1.cor, "azul")

class CordaUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.corda1 = Corda.objects.create(cor="azul")
        self.corda1.cor = "preto"

    def testCreating(self):
        self.assertEquals(self.corda1.cor, "preto")