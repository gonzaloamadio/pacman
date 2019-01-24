"""
The Pacman can move without restriction.
The constraint of moving to a valid position is more a concern of the game orchestrator
This way this class is easily testable
"""

from typing import Tuple


class ThePacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'S': return self.modify_location(0, -1)
        elif direction == 'N': return self.modify_location(0, 1)
        elif direction == 'W': return self.modify_location(-1, 0)
        elif direction == 'E': return self.modify_location(1, 0)

    def coord(self) -> Tuple[int, int]:
        return (self.x, self.y)

    def modify_location(self, dx, dy):
        return ThePacman(self.x + dx, self.y + dy)
