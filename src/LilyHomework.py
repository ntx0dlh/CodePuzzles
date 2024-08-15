#!/bin/python3
"""
This code puzzle was provided by HackerRank: https://www.hackerrank.com/challenges/circular-array-rotation/problem

My solution is not fast enough for the HackerRank environment, but it is more accurate than the top, accepted solutions.
I read the articles, and discussions, and the top-rated ones solve the issue by sorting the array forwards, and
backwards, then simply counting the differences.  These solutions can result in incorrect results, because it is
possible for a single swap to put two numbers into the right place at the same time, which can result in fewer swaps
than there are total differences.  That is why I kept my solution as-is, and I am publishing it here.  I also notified
HackerRank about the discrepancy.
"""


def get_max(max_arr: list[int], left: int) -> [int, int]:
    """
    This function takes an array, and returns the highest-index occurrence of the max value in the array.
    :param max_arr: list[int] - This is the array from which the user wants to find the max value.
    :param left: Integer -  As the program goes along, the passed array gets smaller and smaller, shrinking from the
                 outer sides.  This parameter tells how many values on the left were cut off before passing the current
                 array.
    :return: [int, int] - First value is the max value from the array.  Second value is the highest index of that value
             from the array.  That would be first value, if there is only one, but the highest index if there is more
             than one.
    """
    arr = max_arr[::-1]  # Reverse the array
    # Max value, but highest index, since the array has been reversed.  This is necessary if there are duplicate values.
    val = max(arr)
    idx = len(arr) - arr.index(val) - 1 + left
    return val, idx


def get_min(min_arr: list[int], left: int) -> [int, int]:
    """
    This function takes an array, and returns the highest-index occurrence of the max value in the array.
    :param min_arr: list[int] - This is the array from which the user wants to find the min value.
    :param left: Integer -  As the program goes along, the passed array gets smaller and smaller, shrinking from the
                 outer sides.  This parameter tells how many values on the left were cut off before passing the current
                 array.
    :return: [int, int] - First value is the min value from the array.  Second value is the highest index of that value
             from the array.  That would be first value, if there is only one, but the highest index if there is more
             than one.
    """
    arr = min_arr[::-1]  # Reverse the array
    # Min value, but highest index, since the array has been reversed.  This is necessary if there are duplicate values.
    val = min(arr)
    idx = len(arr) - arr.index(val) - 1 + left
    return val, idx


def sort_desc(desc_arr: list[int]) -> [list[int], int]:
    """
    This function sorts an array in descending order, and counts the number of swaps needed to reorder the array.
    :param desc_arr: List[int] - This is the array that needs to be sorted.
    :return: [list[int], int] - The first value is the sorted array.  The second value is the number of swaps that were
             required.
    """
    swaps = 0
    stop = len(desc_arr) // 2
    left = 0
    right = -1
    rp = None  # rp has to start as None in order to go all the way to the end of the array.
    """
    This loop goes through the array making swaps, and shrinking the array from the outside, in.  Once the outer part of
    the array is sorted, those values are ignored until the end of the loop.
    """
    while left < stop:
        mi, mi_idx = get_min(desc_arr[left:rp], left)  # Min value and index
        ma, ma_idx = get_max(desc_arr[left:rp], left)  # Max value and index
        if not desc_arr[left] == ma:  # Swap the max value with whatever is currently in its place.
            swap = desc_arr[left]
            desc_arr[left] = ma
            desc_arr[ma_idx] = swap
            mi_idx = mi_idx if mi_idx != left else ma_idx  # If the min value just got swapped, update its index
            swaps += 1
        if not desc_arr[right] == mi:  # Swap the min value with whatever is currently in its place.
            swap = desc_arr[right]
            desc_arr[right] = mi
            desc_arr[mi_idx] = swap
            swaps += 1
        # Shrink the array by one from each end.
        left += 1
        right -= 1
        rp = right + 1
    return desc_arr, swaps


def sort_asc(asc_arr: list[int]) -> [list[int], int]:
    """
    This function sorts an array in ascending order, and counts the number of swaps needed to reorder the array.
    :param asc_arr: List[int] - This is the array that needs to be sorted.
    :return: [list[int], int] - The first value is the sorted array.  The second value is the number of swaps that were
             required.
    """
    swaps = 0
    stop = len(asc_arr) // 2
    left = 0
    right = -1
    rp = None  # rp has to start as None in order to go all the way to the end of the array.
    """
    This loop goes through the array making swaps, and shrinking the array from the outside, in.  Once the outer part of
    the array is sorted, those values are ignored until the end of the loop.
    """
    while left < stop:
        mi, mi_idx = get_min(asc_arr[left:rp], left)  # Min value and index
        ma, ma_idx = get_max(asc_arr[left:rp], left)  # Max value and index
        if not asc_arr[left] == mi:  # Swap the max value with whatever is currently in its place.
            swap = asc_arr[left]
            asc_arr[left] = mi
            asc_arr[mi_idx] = swap
            ma_idx = ma_idx if ma_idx != left else mi_idx  # If the min value just got swapped, update its index
            swaps += 1
        if not asc_arr[right] == ma:  # Swap the min value with whatever is currently in its place.
            swap = asc_arr[right]
            asc_arr[right] = ma
            asc_arr[ma_idx] = swap
            swaps += 1
        # Shrink the array by one from each end.
        left += 1
        right -= 1
        rp = right + 1
    return asc_arr, swaps


def lilysHomework(arr: list[int]) -> int:
    """
    This function determines whether it is fewer swaps to sort an array in ascending or descending order, and reports
    how many swaps will be the lower number.
    :param arr: list[int] - The array to find the cheapest sortation path for.
    :param n: int - The length of the array.
    :return: int - The lowest number of swaps needed to sort the array.
    """
    arr1, swaps1 = sort_asc(arr.copy())
    arr2, swaps2 = sort_desc(arr.copy())
    print(f"arr: {arr}, arr1: {arr1}, arr2: {arr2}, swaps1: {swaps1}: swaps2: {swaps2}")
    return min(swaps1, swaps2)


if __name__ == '__main__':
    n = 12
    ary = [10, 1000, 42, 96, 85, 0, 18, 999, 500, 33, 42, 42]
    result = lilysHomework(ary)
    print(result)
