import unittest

import util
from app.board import Board
from app.game_orchestrator import GameOrchestrator
from resources.resource_loader import Input
from util.exception import PositionException


class GameOrchestratorTests(unittest.TestCase):
    def test_invalid_position_not_in(self):
        i = Input(
            board_dimension=(5, 5),
            initial_position=(0, 5),
            movements=[],
            walls=set())
        with self.assertRaises(PositionException):
            GameOrchestrator(i)

    def test_invalid_position_wall(self):
        i = Input(
            board_dimension=(5, 5),
            initial_position=(1, 1),
            movements=[],
            walls={(1, 1)})
        with self.assertRaises(PositionException) as e:
            GameOrchestrator(i)
        self.assertEqual(
            str(e.exception),
            "The pacman can not be placed at the location: (1, 1)")

    def test_game_without_bumping_in_a_wall(self):
        i = Input(
            board_dimension=(5, 5),
            initial_position=(1, 1),
            movements=['E', 'E', 'N'],
            walls={(1, 2)})
        x, y, c = GameOrchestrator(i).play()
        self.assertEqual((x, y, c), (3, 2, 3))

    def test_game_with_coming_back_on_previous_steps(self):
        i = Input(
            board_dimension=(5, 5),
            initial_position=(1, 1),
            movements=['E', 'W', 'E', 'W', 'W'],
            walls={(1, 2)})
        x, y, c = GameOrchestrator(i).play()
        self.assertEqual((x, y, c), (0, 1, 2))

    def test_game_with_bumping_on_wall(self):
        i = Input(
            board_dimension=(5, 5),
            initial_position=(1, 1),
            movements=['N', 'N', 'S'],
            walls={(1, 2)})
        x, y, c = GameOrchestrator(i).play()
        self.assertEqual((x, y, c), (1, 0, 1))

    def test_game_with_bumping_on_edge(self):
        i = Input(
            board_dimension=(5, 5),
            initial_position=(0, 0),
            movements=['S', 'W', 'S'],
            walls={})
        x, y, c = GameOrchestrator(i).play()
        self.assertEqual((x, y, c), (0, 0, 0))
