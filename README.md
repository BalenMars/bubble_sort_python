# bubble_sort_python

This is to demonstrate the speed of two different ways for coding a bubble sort in python. The two codes generate a 10,000 integers exactly the same way, only they differ in how they loop through them. 

The code in bubble_sort_slow.py is taken from the wonderful book, Effective Python by Brett Slatkin, and the second bubble_sort_fast.py, I wrote it myself to demonstrate the difference. The algorithm of the latter, basically, does not loop through the entire list again and again, but leave the parts that have already been found. The list, this way, shrinks with each loop making the code fast and faster. 

[![Build Status](https://travis-ci.com/BalenMars/bubble_sort_python.svg?branch=main)](https://travis-ci.com/BalenMars/bubble_sort_python)

Execution time comparison:

> bubble_sort_slow.py
```
real	0m10,965s
user	0m10,961s
sys	0m0,004s
```

> bubble_sort_fast.py
```
real	0m6,785s
user	0m6,780s
sys	0m0,004s
```
