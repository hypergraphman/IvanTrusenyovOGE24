mn1 = mn2 = float('inf')
mx1 = mx2 = -float('inf')
while (n := int(input())) != 0:
    if n > mx1:
        mx2 = mx1
        mx1 = n
    elif n > mx2:
        mx2 = n

    if n < mn1:
        mn2 = mn1
        mn1 = n
    elif n < mn2:
        mn2 = n
print(mx1 + mx2)
print(mn1 + mn2)