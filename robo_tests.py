import unittest

from robo import Robo


class RoboTests(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print('Executando setUp()')

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), f'OI, EU SOU MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria estar com 49%')

    def tearDown(self):
        print('Executando tearDown()')



if __name__ == '__main__':
    unittest.main()
