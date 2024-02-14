s1 = input()
s2 = input()
s3 = input()
if s1 < s2:
    s1, s2 = s2, s1
if s2 < s3:
    s2, s3 = s3, s2
if s1 < s2:
    s1, s2 = s2, s1
print(f'{s1}, {s2}, {s3}.')