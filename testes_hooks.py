"""
Unittests - Antes e apos hooks

hooks - execucao dos testes

setup() - executado antes de cada metodo de teste. eh util para criarmos instancias de objetos e outros dados

tearDown() - executado depois de cada metodo de teste. eh util para excluir dados ou fechas conexoes com BD

"""

import unittest


class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configuracao
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar apos o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste
        # tearDown() vai rodar apos o teste
        pass

    def tearDown(self):
        # Configuracao do tearDown()
        pass

