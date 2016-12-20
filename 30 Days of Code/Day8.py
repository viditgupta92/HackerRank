# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
phone = collections.OrderedDict()
num = int(input())
for i in range(0, num):
    temp = input().split()
    phone[temp[0]] = temp[1]
for i in range(0, num):
    name = str(input())
    if name in phone:
        print(name,"=",phone[name],sep="")
    else:
        print("Not found")