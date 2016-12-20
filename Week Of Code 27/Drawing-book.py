#!/bin/python3

import sys

n = int(input().strip())
p = int(input().strip())
# your code goes here
diff = n - p
if diff < p:
    steps = int(diff/2)
else:
    steps = (p-1)/2
print(steps)
