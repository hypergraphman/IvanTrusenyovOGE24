from math import inf

n = int(input())
a = [int(input()) for _ in range(n)]
mx = -inf
mx_i = None
for i in range(len(a)):
    if a[i] > mx:
        mx = a[i]
        mx_i = i
del a[mx_i]
mn = inf
mn_i = None
for i in range(len(a)):
    if a[i] < mn:
        mn = a[i]
        mn_i = i
del a[mn_i]
print(a)
print(mx, mn)