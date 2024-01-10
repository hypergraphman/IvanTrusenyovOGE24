def get_factors(num):
    s = 0
    for i in range(1, 10801):
        if num % i == 0:
            s += 1
    return s

# считываем данные
n = 5

# вызываем функцию
print(get_factors(n))