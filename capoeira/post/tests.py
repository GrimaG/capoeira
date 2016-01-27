from django.test import TestCase
import unittest
from capoeira.models.post import *

# Create your tests here.
class GrupoCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutantes",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")

    def testCreating(self):
        self.assertEquals(self.beatles.nome, "mutantes")

class GrupoUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="thor",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.beatles.nome = "x-man"
        
    def testCreating(self):
        self.assertEquals(self.beatles.nome, "x-man")
        
#####################################################################################################################

class PessoaCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.joao = Pessoa.objects.create(nome="Joao",rg="123",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)

    def testCreating(self):
        self.assertEquals(self.joao.nome, "Joao")

class PessoaUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.joao = Pessoa.objects.create(nome="Joao Henrique",rg="123456",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.joao.nome = "jao"
            
    def testCreating(self):
        self.assertEquals(self.joao.nome, "jao")

#####################################################################################################################

class AlunoCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="muta",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao Lucas",rg="1234567",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)

    def testCreating(self):
        self.assertEquals(self.platini.mae, "Eva")

class AlunoUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="muta",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao Lucas",rg="1234567",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.platini.nome = "platini"
        
    def testCreating(self):
        self.assertEquals(self.platini.nome, "platini")
        
#####################################################################################################################


class ProfessorCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutante",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.paulo = Professor.objects.create(registro="992345",nome="Paulo",rg="1234",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)

    def testCreating(self):
        self.assertEquals(self.paulo.registro, "992345")

class ProfessorUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="mutante",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.paulo = Professor.objects.create(registro="992345",nome="Paulo",rg="1234",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo.nome = "Paulo Sergio"
        
    def testCreating(self):
        self.assertEquals(self.paulo.nome, "Paulo Sergio")

#####################################################################################################################

class TurmaCreateTestCase(unittest.TestCase):
    def setUp(self):
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="kapoeira",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao Lucas",rg="123456789",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo = Professor.objects.create(registro="992347",nome="Paulo Henrique",rg="1234532",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.turma1 = Turma.objects.create(nome="turma1",turno="matutino",horario="2016-01-01",dia_semana="Segunda",aluno=self.platini,professor=self.paulo)

    def testCreating(self):
        self.assertEquals(self.turma1.nome, "turma1")

class TurmaUpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.beatles = Grupo.objects.create(sequencia_corda="azul", nome="kapo",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada")
        self.platini = Aluno.objects.create(mae = "Eva", pai="Adao",nome="Joao Henrique",rg="12345432",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="estudante",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.paulo = Professor.objects.create(registro="992355",nome="Paulo Lucas",rg="1238762",data_nascimento="1991-03-03",logradouro="ES-010", numero="1",bairro="manguinhos",cidade="Serra",complemento="nada",telefone="1234-5678",profissao="professor",grau_escolar="superior",cor_corda="azul",grupo = self.beatles)
        self.turma1 = Turma.objects.create(nome="turma3",turno="matutino",horario="2016-01-01",dia_semana="Segunda",aluno=self.platini,professor=self.paulo)
        self.turma1.nome = "turma2"
        
    def testCreating(self):
        self.assertEquals(self.turma1.nome, "turma2")
