from typing import List

def merge (container_1, container_2):
    result = []
    for i in range(len(container_1) - 1):
        if container_1[i] < container_2[i]:
            result.append(container_1[i])
            container_1.remove(container_1[i])
        if container_2[i] < container_1[i]:
            result.append(container_2[i])
            container_2.remove(container_2[i])
        else:
            result.append(container_1[i])
            container_1.remove(container_1[i])
            result.append(container_2[i])
            container_2.remove(container_2[i])
    return result


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) == 1:
        return container

    index_ = len(container) // 2
    left = sort(container[:index_])
    right = sort(container[index_:])

    return merge(left, right)


if __name__ == "__main__":

    list_= [10, 17, 3, 58, 44, 100, 19, 40, 21, 66, 55, 32, 49, 9, 2, 45]

    sort(list_)
    print(list_)
