a = int(input())
b = int(input())
op = input()
res = None
if op == '+':
    res = a + b
elif op == '-':
    res = a - b
elif op == '*':
    res = a * b
elif op == '/':
    if b != 0:
        res = a / b
    else:
        res = 'Делить на ноль нельзя'
else:
    res = 'Неверная операция'
print(res)