"""
This functions will load the input resources.
Loading resources can be source of errors so we use typing and NamedTuple to facilitate the development and testing.
"""
import logging
import os
from typing import List, NamedTuple, Set, Tuple

from util.exception import InputFormatException

LOG = logging.getLogger(__name__)

CoordType = Tuple[int, int]
MovesType = List[str]
WallsType = Set[CoordType]

Input = NamedTuple("Input", [("board_dimension", CoordType),
                             ("initial_position", CoordType),
                             ("movements", MovesType), ("walls", WallsType)])
Resources = NamedTuple("Resources", [("input_data", Input)])


def load_input(filename) -> Input:
    """
    Load a file relative to the root folder
    :return: a NamedTuple input_data of type Input
    """
    file = os.path.join(os.path.dirname(__file__), "..", filename)

    def process_moves(line: str, line_number: int) -> MovesType:
        try:
            moves = list(line.strip())
            if any(p not in ['S', 'E', 'N', 'W'] for p in moves):
                LOG.error("wrong move format in: %s", moves)
                raise InputFormatException(
                    "wrong move format in: {}".format(moves))
            return moves
        except Exception as e:
            LOG.error(
                "line number %s, with content:'%s' has a bad coord format",
                line_number, line.strip())
            raise InputFormatException(str(e))

    def process_coord(line: str, line_number: int) -> CoordType:
        try:
            split_coord = line.strip().split(' ')
            return (int(split_coord[0]), int(split_coord[1]))
        except Exception as e:
            LOG.error(
                "line number %s, with content:'%s' has a bad moves format",
                line_number, line.strip())
            raise InputFormatException(str(e))

    with open(file, "rt", encoding="utf8") as f:
        board_dimension = process_coord(f.readline(), 1)
        initial_position = process_coord(f.readline(), 2)
        movements = process_moves(f.readline(), 3)
        walls = set(
            process_coord(line, i) for i, line in enumerate(f, start=4))

    LOG.debug("Loaded board_dimension: %s", board_dimension)
    LOG.debug("Loaded initial_position: %s", initial_position)
    LOG.debug("Loaded movements: %s", movements)
    LOG.debug("Loaded walls: %s", walls)
    return Input(
        board_dimension=board_dimension,
        initial_position=initial_position,
        movements=movements,
        walls=walls)


def load(input_filename="input.txt"):
    return Resources(input_data=load_input(input_filename))
