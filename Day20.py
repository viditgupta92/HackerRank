#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
numSwaps = 0
for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] =t
            numSwaps += 1
print("Array is sorted in %d swaps" %(numSwaps))
print("First element: %d" %(a[0]))
print("Last element: %d" %(a[len(a)-1]))
