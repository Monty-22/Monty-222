from typing import List
import random
import timeit


def quick_sort(container: List[int]) -> List[int]:

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
        return quick_sort(left) + equal + quick_sort(right)


def bubble_sort(container: List[int]) -> List[int]:
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(container) - 1):
                if container[i] > container[i + 1]:
                    container[i], container[i + 1] = container[i + 1], container[i]
                    swapped = True
        return container


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


def merge_sort(container: List[int]) -> List[int]:

    if len(container) == 1:
        return container

    index_ = len(container) // 2
    left = merge_sort(container[:index_])
    right = merge_sort(container[index_:])

    return merge(left, right)


def insertion_sort(container: List[int]) -> List[int]:
    for i in range(1, len(container)):
        temp = container[i]
        j = i - 1
        while j >= 0 and temp < container[j]:
            container[j + 1] = container[j]
            j = j - 1
        container[j + 1] = temp
    return container




if __name__ == "__main__":
    list_ = []
    for i in range(100):
        list_.append(random.randint(0, 100))



    list_q = quick_sort(list_)
    print(list_q)
    list_m = merge_sort(list_)
    print(list_m)
    list_i = insertion_sort(list_)
    print(list_i)
    list_b = bubble_sort(list_)
    print(list_b)
    print("\n" * 2)



    for i in range(10**6):
        list_.append(random.randint(13, 25))
    start_time_q = timeit.default_timer()
    quick_sort(list_)
    time_quick = timeit.default_timer() - start_time_q
    print(f"время выполнения quick_sort => {time_quick}")

    start_time_m = timeit.default_timer()
    merge_sort(list_)
    time_merge = timeit.default_timer() - start_time_m
    print(f"время выполнения merge_sort => {time_merge}")

    start_time_b = timeit.default_timer()
    bubble_sort(list_)
    time_bubble = timeit.default_timer() - start_time_b
    print(f"время выполнения bubble_sort => {time_bubble}")

    start_time_i = timeit.default_timer()
    insertion_sort(list_)
    time_insertion = timeit.default_timer() - start_time_i
    print(f"время выполнения insertion_sort => {time_insertion}")

    start_time_b = timeit.default_timer()
    bubble_sort(list_)
    time_bubble = timeit.default_timer() - start_time_b
    print(f"время выполнения bubble_sort => {time_bubble}")

    """Результыаты тестов для массива из 10**3 чисел:
       время выполнения quick_sort => 0.0012432999938027933
       время выполнения merge_sort => 0.012940399996296037
       время выполнения insertion_sort => 0.09498260000691516
       время выполнения bubble_sort => 9.640000644139946e-05
       
       Для 10**4 :
       время выполнения quick_sort => 0.008022100002563093
       время выполнения merge_sort => 0.10052210000139894
       время выполнения insertion_sort => 4.484122000001662
       время выполнения bubble_sort => 0.0007111000013537705
       
       Для 10**5 :
       время выполнения quick_sort => 0.053295699995942414
       время выполнения merge_sort => 0.6740831999995862
       время выполнения insertion_sort => 383.67376630000217
       время выполнения bubble_sort => 0.017217500004335307
       
       Для 10**6 :
       время выполнения quick_sort => 0.3785219000055804
       время выполнения merge_sort => 6.739290100005746
       insertion_sort и bubble_sort не справились с заданием
       за 3-и часа.
       """