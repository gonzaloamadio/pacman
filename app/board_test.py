import unittest

from app.board import Board


class BoardTests(unittest.TestCase):
    def test_valid(self):
        t = Board(5, 5, []).is_valid_move(3, 3)
        self.assertEqual(t, True)

    def test_invalid_s(self):
        t = Board(5, 5, []).is_valid_move(-1, 3)
        self.assertEqual(t, False)

    def test_invalid_n(self):
        t = Board(5, 5, []).is_valid_move(5, 1)
        self.assertEqual(t, False)

    def test_invalid_e(self):
        t = Board(5, 5, []).is_valid_move(1, 5)
        self.assertEqual(t, False)

    def test_invalid_w(self):
        t = Board(5, 5, []).is_valid_move(1, -1)
        self.assertEqual(t, False)

    def test_height(self):
        self.assertEqual(Board(5, 5, []).height(), 5)

    def test_width(self):
        self.assertEqual(Board(5, 5, []).width(), 5)

    def test_move_in_a_wall(self):
        t = Board(5, 5, [(1, 3)]).is_valid_move(1, 3)
        self.assertEqual(t, False)

    def test_move_near_a_wall(self):
        t = Board(5, 5, [(1, 3)]).is_valid_move(1, 2)
        self.assertEqual(t, True)
