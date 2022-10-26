from typing import List


def swap(el_1, el_2):
    temp = el_2
    el_2 = el_1   # том 1 стр 543
    el_1 = temp
    return el_1, el_2


def sort(container: List[int]) -> List[int]:

    while True:
        count = 0
        for i in range(len(container) - 1):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = swap(container[i], container[i + 1])
                count += 1
        if count == 0:
            break

    return container

if __name__ == "__main__":
    list_ = [10, 17, 3, 58, 44, 100, 91, 400, 555, 0, 76]
    sort(list_)
    print(list_)
