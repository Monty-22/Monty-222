from typing import List


def merge(left, right):
    result = []
    i = j = r = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        r += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def sort(container: List[int]) -> List[int]:

    if len(container) == 1:
        return container

    index_ = len(container) // 2
    left = sort(container[:index_])
    right = sort(container[index_:])

    return merge(left, right)


if __name__ == "__main__":

    list_ = [10, 17, 3, 58, 44, 100, 19, 40, 21, 66, 55, 32, 49, 9, 2, 45]

    list_ = sort(list_)
    print(list_)
