import unittest

from unittest_atividades import comer, dormir, engracada


class AtividadesTestes(unittest.TestCase):

    def test_comer_bem(self):
        """Testando o retorno com comida saudavel"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_bobagem(self):
        """Testando o retorno com bobagens"""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza porque a gente so vive uma vez'
        )

    def test_dormir_pouco(self):
        """Testando o retorno com dormir pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado so dormi 4 horas'
        )

    def test_dormir_muito(self):
        """Testando o retorno com dormir muito"""
        self.assertEqual(
            dormir(10),
            'Dormi demais!'
        )

    def test_engracada(self):
        """Testando o retorno de se eh engracada"""
        # self.assertEquals(engracada('Pedrinho'), False)
        self.assertFalse(engracada('Pedrinho'))
        self.assertTrue(engracada('Jim Carrey'), 'Ele deveria ser engracado')


if __name__ == '__main__':
    unittest.main()


