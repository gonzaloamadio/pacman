import unittest

from app.the_pacman import ThePacman


class ThePacmanTests(unittest.TestCase):
    def test_go_s(self):
        p = ThePacman(0, 0).move('S')
        self.assertEqual(p.coord(), (0, -1))

    def test_go_n(self):
        p = ThePacman(0, 0).move('N')
        self.assertEqual(p.coord(), (0, 1))

    def test_go_e(self):
        p = ThePacman(0, 0).move('E')
        self.assertEqual(p.coord(), (1, 0))

    def test_go_w(self):
        p = ThePacman(0, 0).move('W')
        self.assertEqual(p.coord(), (-1, 0))
