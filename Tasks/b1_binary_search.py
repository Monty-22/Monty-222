from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    arr_sort = sorted(arr)
    while arr_sort:
      N = len(arr_sort) - 1
      el = arr[int(N/2)]
      if el == elem:
          return arr_sort.index(el)
      if el < elem:
          arr_sort = arr_sort[arr_sort.index(el):]
      if el > elem:
          arr_sort = arr_sort[:arr_sort.index(el)]
    return None





