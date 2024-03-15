x, y = 0, 0
dx = 0
dy = 1
while (cmd := input()) != 'СТОП':
    if cmd == '':
        x += dx
        y += dy
    if cmd == '':
        if dx == 0 and dy == 1:
            dx = 1
            dy = 0
        if dx == 1 and dy == 0:
            dx = 0
            dy = -1
    if cmd == ''

print(x, y)