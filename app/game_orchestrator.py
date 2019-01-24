import logging
from typing import Tuple

from app.board import Board
from app.the_pacman import ThePacman
from util.exception import PositionException

LOG = logging.getLogger(__name__)


class GameOrchestrator:
    def __init__(self, input_data):
        """
        Create the board.
        Make sure the initial_position is a valid move
        Add the initial_position to the path_history and set coins to 0
        """
        self.board = Board(*input_data.board_dimension, input_data.walls)
        if self.board.is_valid_move(*input_data.initial_position):
            self.the_pacman = ThePacman(*input_data.initial_position)
        else:
            raise PositionException(
                "The pacman can not be placed at the location: {}".format(
                    input_data.initial_position))
        self.movements = input_data.movements
        self.path_history = {input_data.initial_position}
        self.coins = 0

    def play(self) -> Tuple[int, int, int]:
        """
        play loop over the list of movements and execute them
        For each move, it check if it is a valid one
        For each valid move it will record the past history and compute the collected coins
        'return': "a tuple of [int, int, int] representing position x, y, and collected coins at the end of the game"
        """
        for move in self.movements:
            if self.board.is_valid_move(*self.the_pacman.move(move).coord()):
                self.the_pacman = self.the_pacman.move(move)
                coord = self.the_pacman.coord()
                if coord not in self.path_history:
                    LOG.debug("%s is not in path history: %s", coord,
                              self.path_history)
                    self.coins = self.coins + 1
                    LOG.debug("The number of coins is now: %s", self.coins)
                    self.path_history.add(coord)
        coord = self.the_pacman.coord()
        return (coord[0], coord[1], self.coins)
