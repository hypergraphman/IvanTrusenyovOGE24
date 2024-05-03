res = 0
while ' ' not in (sound := input()):
    num = int(input())
    if len(sound) == num:
        res += 1
print(res)