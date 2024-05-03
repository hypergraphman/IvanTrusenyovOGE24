part = int(input())
rt = 2 * part
ser = part / 3
spirt = part / 8
start = cur = rt + ser + spirt
hour = 0
while start / 2 < cur:
    rt *= 0.99
    spirt *= 0.995
    cur = rt + ser + spirt
    hour += 1
print(hour, cur)
