r = int(input())
v = int(input())
a = int(input())
t = 0
while r > 0:
    r = r - v - a * t
    t += 1
print(t)