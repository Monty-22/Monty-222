from typing import Union, Sequence
from copy import deepcopy

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    cost_routers = [[0, 0]]
    for i in range(len(stairway) - 1):
        cost_1 = deepcopy(cost_routers)
        cost_2 = deepcopy(cost_routers)

        for j in range(len(cost_1) - 1):
            cost_1[j][0] += 1
            cost_1[j][1] += stairway[i]
            cost_2[j][0] += 2
            cost_2[j][1] += stairway[i + 1]
        cost_routers = cost_1 + cost_2
        print(f"{cost_routers}")
    print(stairway)
    print(cost_routers)
    costes = []
    for i in range(len(cost_routers) - 1):
        costes.append(cost_routers[i][1])
    x = min(costes)
    print(x)
    return x
