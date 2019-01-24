import unittest

from resources.resource_loader import load_input
from util.exception import InputFormatException


class ResourceLoaderTests(unittest.TestCase):
    def test_load_input_good(self):
        i = load_input('test_resources/input_good.txt')
        self.assertEqual(i.board_dimension, (5, 5))
        self.assertEqual(i.initial_position, (1, 2))
        self.assertEqual(
            i.movements,
            ['N', 'N', 'E', 'S', 'E', 'E', 'S', 'W', 'N', 'W', 'W'])
        self.assertEqual(i.walls, {(1, 0), (2, 3), (2, 2)})

    def test_load_input_no_wall(self):
        i = load_input('test_resources/input_good_no_wall.txt')
        self.assertEqual(i.board_dimension, (5, 5))
        self.assertEqual(i.initial_position, (1, 2))
        self.assertEqual(
            i.movements,
            ['N', 'N', 'E', 'S', 'E', 'E', 'S', 'W', 'N', 'W', 'W'])
        self.assertEqual(i.walls, set())

    def test_load_input_coord_error(self):
        with self.assertRaises(InputFormatException) as e:
            load_input('test_resources/input_coord_error.txt')
        self.assertEqual(
            str(e.exception), "invalid literal for int() with base 10: 'Z'")

    def test_load_input_moves_error(self):
        with self.assertRaises(InputFormatException) as e:
            load_input('test_resources/input_moves_error.txt')
        self.assertEqual(
            str(e.exception),
            "wrong move format in: ['1', '2', '3', 'S', 'E', 'E']")

    def test_load_input_missing_size(self):
        with self.assertRaises(InputFormatException) as e:
            load_input('test_resources/input_missing_size.txt')
        self.assertEqual(
            str(e.exception),
            "invalid literal for int() with base 10: 'NNESEESWNWW'")
