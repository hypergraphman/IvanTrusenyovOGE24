n = int(input())
if n == 0:
    n += 50
elif n > 70:
    n = n
elif 0 < n <= 30:
    n = int(n * 1.5)
elif 30 < n <= 70:
    n = int(n * 1.1)
print(n)