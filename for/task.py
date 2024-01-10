a1 = len(input())
a2 = len(input())
a3 = len(input())
if a1 > a2:
    a1, a2 = a2, a1
if a2 > a3:
    a2, a3 = a3, a2
if a1 > a2:
    a1, a2 = a2, a1
if a2 - a1 == a3 - a2:
    print('YES')
else:
    print('NO')