#!/bin/python3

import sys
import math

n,p = input().strip().split(' ')
n,p = [int(n),int(p)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
# your code goes here
b = []
for i in range(len(a)):
    num = math.ceil(a[i]/p)
    while(num in b):
        num += 1
    b.append(num)
print(sum(b))

