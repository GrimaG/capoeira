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
        self.joao.nome = "jao"
        
    def testCreating(self):
        self.assertEquals(self.joao.nome, "jao")
