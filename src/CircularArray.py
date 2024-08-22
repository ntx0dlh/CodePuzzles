#!/bin/python3
import os

"""
This code puzzle was provided by HackerRank: https://www.hackerrank.com/challenges/circular-array-rotation/problem

The puzzle asks someone to write a function
"""

def circularArrayRotation(a: list[int], k: int, queries: list[int]) -> list[int]:
    """
    This function rotates values in an array, by the amount "k."  Then it returns various members of the rotated array.
    The various members that will be returned are passed in the queries parameter.
    :param a: list[int] - Beginning array that will be rotated to some degree.
    :param k: int - The amount degrees of rotation to apply, where 1 degree takes a number from the right and moves it
              to the left.
    :param queries: list[int] - An array of values contained in a, by index, used to verify that things are in the right
                    place.
    :returns: list[int] - All the items in queries, as indexes, with their corresponding values.
    """
    new_k = k % len(a)
    b = a[-new_k:] + a[:-new_k]
    return [b[i] for i in queries]


if __name__ == '__main__':
    n = 3
    k = 2
    q = 3
    a = [1, 2, 3]
    queries = [0, 1, 2]
    assert circularArrayRotation(a, k, queries), [2, 3, 1]
