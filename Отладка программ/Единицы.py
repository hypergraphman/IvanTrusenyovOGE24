num = int(input())
dw = 0

while num > 2**dw:
    dw += 1
print(num - 2**dw - 1)