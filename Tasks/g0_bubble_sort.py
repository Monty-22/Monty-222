from typing import List


def swap (el_1, el_2):
    temp = el_2
    el_2 = el_1
    el_1 = temp
    print(temp)


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    while True:
        count = 0
        for i in range(len(container) - 1):
            if container[i] > container[i + 1]:
                swap(container[i], container[i + 1])
                count += 1
        if count == 0:
            break

    return container

if __name__ == "__main__":
    list = [ 10, 17, 3, 58, 44, 100]
    sort(list)
    print(list)
