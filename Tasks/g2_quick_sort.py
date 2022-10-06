import random
from typing import List


def sort(container: List[int]) -> List[int]:
    if len(container) <= 0:
        return container
    else:
        pivot = random.choice(container)
        left = []
        right = []
        equal = []
        for elem in container:
            if elem < pivot:
                left.append(elem)
            elif elem > pivot:
                right.append(elem)
            else:
                equal.append(elem)
        return sort(left) + equal + sort(right)


if __name__ == "__main__":
    list_ = [10, 17, 3, 58, 44, 100, 91, 400, 555, 0, 76]
    list_ = sort(list_)
    print(list_)





