prev = int(input())
k = 0
while n := int(input()):
    if n > prev:
        k += 1
    prev = n
print(k)