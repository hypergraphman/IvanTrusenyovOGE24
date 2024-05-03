# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
pre = 1
cur = 1
p_n = 2
n = int(input())
while n > cur:
    p_n += 1
    num = pre
    pre = cur
    cur = num + pre
if cur == n:
    print(p_n)
else:
    print('НЕТ')