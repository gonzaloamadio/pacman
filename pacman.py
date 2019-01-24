"""
This module if the entry point for the pacman game.

"""

__author__ = "Pierre Caserta"

import argparse
import logging
from typing import Tuple

import util.logger
from app.game_orchestrator import GameOrchestrator
from resources.resource_loader import load

util.logger.setup()

LOG = logging.getLogger(__name__)


def pacman(input_filename) -> Tuple[int, int, int]:
    """ Use this function to format your input/output arguments. Be sure not change the order of the output arguments.
    Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.

    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """
    result = (-1, -1, 0)
    try:
        resources = load(input_filename=input_filename)
        LOG.debug("Parsed input data: %s", resources.input_data)
        game = GameOrchestrator(resources.input_data)
        result = game.play()
        # return final_pos_x, final_pos_y, coins_collected
    except Exception as e:
        LOG.error(str(e))
    return result


if __name__ == "__main__":
    # pylint: disable=invalid-name
    parser = argparse.ArgumentParser(
        description="Run the pacman application",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "-i",
        "--input-filename",
        dest="input_filename",
        help=
        "Input file name for the pacman (this file need to be on resources folder)"
    )
    parser.set_defaults(input_filename='input.txt')
    args = parser.parse_args()
    LOG.debug("Args received: %s", args)
    final_x_position, final_y_position, total_coins = pacman(
        args.input_filename)
    print("# finalXposition, finalYposition, totalCoins")
    print("return {} {} {}".format(final_x_position, final_y_position,
                                   total_coins))
