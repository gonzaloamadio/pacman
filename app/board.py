"""
The Board just has a width, a height and some walls.
The Board can only tell if a move is valid or invalid
"""

import logging

LOG = logging.getLogger(__name__)


class Board:
    def __init__(self, x, y, walls):
        self.x = x
        self.y = y
        self.walls = walls
        LOG.debug("The board is %s by %s and the walls are %s", self.x, self.y,
                  self.walls)

    def height(self):
        return self.y

    def width(self):
        return self.x

    def is_valid_move(self, x, y):
        """
        Check if you can move to the x, y location
        Moving to a wall is not allowed
        Moving out of the board is not allowed
        """
        is_in = x >= 0 and x < self.x and y >= 0 and y < self.y
        LOG.debug("is_in for values (%s,%s) is: %s", x, y, is_in)
        is_wall = (x, y) in self.walls
        LOG.debug("is_wall for values (%s,%s) is: %s", x, y, is_wall)
        is_valid = is_in and not is_wall
        LOG.debug("is_valid for values (%s,%s) is: %s", x, y, is_valid)
        return is_valid
