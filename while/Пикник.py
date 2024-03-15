dice = int(input())
nums = []
k = 1
while k <= dice:
    if dice % k == 0:
        print(k)
    k += 1