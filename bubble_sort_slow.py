#!/usr/bin/env python3
from random import randrange

list_of_ints = []
for _ in range(10_000):
    list_of_ints.append(randrange(-1000, 1000))


def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i-1]:
                a[i-1], a[i] = a[i], a[i-1]


bubble_sort(list_of_ints)
