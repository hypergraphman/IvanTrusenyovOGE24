n = int(input())
m = int(input())
res = 0
while (num := int(input())) != 0:
    if num == 1:
        res += n
    else:
        res -= m
print(res)