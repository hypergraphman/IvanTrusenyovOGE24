prev = int(input())
current = int(input())
k = 0
while (next := int(input())) != -1:
    if prev < current > next:
        k += 1
    prev = current
    current = next
print(k)