x = int(input())
month = (x + 19) // 20
day = (x % 20 - 1) % 20
month = str(month)
day = str(day)
print('Месяц', month + ',', "день", day + '.')