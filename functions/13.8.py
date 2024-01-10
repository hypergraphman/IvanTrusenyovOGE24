def is_valid_password(s):
    if s.count(':') != 2:
        return False
    a, b, c = s.split(':')
    if a != a[::-1]:
        return False
    b = int(b)
    if b == 1:
        return False
    for d in range(2, int(b ** 0.5) + 1):
        if b % d == 0:
            return False
    c = int(c)
    return c % 2 == 0



print(is_valid_password('1231:7:22'))