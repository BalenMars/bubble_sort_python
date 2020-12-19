#!/usr/bin/env python3
from random import randrange

list_of_ints = []
for _ in range(10_000):
    list_of_ints.append(randrange(-1000, 1000))


def bubble_sort(k):
    for i in range(len(k), 0, -1):
        for j in range(i-1):
            if k[j] > k[j+1]:
                k[j+1], k[j] = k[j], k[j+1]


bubble_sort(list_of_ints)





