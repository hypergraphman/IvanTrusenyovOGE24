num = int(input())
d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10
if d1 != 0 and d2 != 0 and d3 != 0:
    if d1 == d2 == d3:
        print(3)
    elif d1 == d2 or d2 == d3 or d1 == d3:
        print(2)
    else:
        print(d1 * d2 * d3)
else:
    print(max(d1, d2, d3))