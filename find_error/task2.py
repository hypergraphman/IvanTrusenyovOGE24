mx = -10 ** 10
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s = x
        if x > mx:
            mx = x
print(s)
print(mx)