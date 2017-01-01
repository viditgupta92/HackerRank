#!/bin/python3

# import sys
# import math
#
# n,p = input().strip().split(' ')
# n,p = [int(n),int(p)]
# a = [int(a_temp) for a_temp in input().strip().split(' ')]
# # your code goes here
# b = []
# for i in range(len(a)):
#     num = math.ceil(a[i]/p)
#     while(num in b):
#         num += 1
#     b.append(num)
# print(sum(b))

#!/bin/python3

import sys
import math
import collections


n,p = input().strip().split(' ')
n,p = [int(n),int(p)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
# your code goes here
dict = collections.OrderedDict()
total = 0
for i in range(n):
    num = math.ceil(a[i]/p)
    if num not in dict:
        dict[num] = 1
    else:
        dict[num] += 1
for k,v in dict.items():
    if v != 1:
        diff = v - 1
        dict[k] = 1
        if k+1 not in dict:
            dict[k+1] = v-1
        else:
            dict[k+1] += v-1

# for k,v in dict.items():
#     if v == 1:
#         total += k
#     else:
#         total += ((v/2)*(k + (k + v - 1)))
print(sum(dict.keys()))