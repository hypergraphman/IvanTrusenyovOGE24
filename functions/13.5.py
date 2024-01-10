def is_password_good(password):
    if len(password) < 8:
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.islower() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    return True

# считываем данные
n = input()

# вызываем функцию
print(is_password_good(n))