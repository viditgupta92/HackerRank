N = int(input().strip())
a = [int(each) for each in input().strip().split(' ')]
a.sort()
length = len(a)
lst = []
smallest_diff = max(a)
lst = []
for i in range(length-1):
    for j in range(i+1,length,1):
        diff = a[j] - a[i]
        if diff < smallest_diff:
            lst = []
            smallest_diff = diff
            lst.append(a[i])
            lst.append(a[j])
        elif diff == smallest_diff:
            lst.append(a[i])
            lst.append(a[j])
for ind, val in enumerate(lst):
    print(val, end= " ")
