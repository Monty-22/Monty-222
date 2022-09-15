from typing import Union, Sequence
from copy import deepcopy

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    stairway.sort()
    cost = 0
    for i in range(0, len(stairway), 2):
        cost += stairway[i]
    print(cost)
    return cost
