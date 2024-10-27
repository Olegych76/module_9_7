def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        if num < 2:
            return f'Некорректное использование функции'
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                return f'Сумма данных трёх чисел ({num}) - число составное'
        return f'Сумма данных трёх чисел ({num}) - число простое'
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(0, 0, 1))
print(sum_three(0, 1, 1))
print(sum_three(1, 3, 6))
