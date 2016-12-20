#!/bin/python3

import sys

n = int(input().strip())
i = 0
j = 0
bin = []
num = []
ctr = 0
while n > 0:
    bin.append(int(n % 2))
    n = int(n/2)
for i in range(0,len(bin)):
    if bin[i] == 1:
        ctr += 1
    else:
        num.append(ctr)
        ctr = 0
if bin[i-1] == 1:
    num.append(ctr)
print(max(num))
