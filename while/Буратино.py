coast = int(input())
n = 1
res = 0
while coast > n:
    n *= 10
    res += 1
print(res)