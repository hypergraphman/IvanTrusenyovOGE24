n = int(input())
for i in range(n):
    for _ in range(n // 2 + 1 - abs(n // 2 - i)):
        print('*', end='')
    print()

for i in range(1, (n + 1) // 2 + 1):
    print('*' * i)
for i in range((n + 1) // 2 - 1, 0, -1):
    print('*' * i)