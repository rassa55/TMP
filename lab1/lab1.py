import numpy as np

def calculate_formula(x, k, a, b):
    try:
        x, k, a, b = float(x), float(k), float(a), float(b)  # Преобразуем входные значения в числа
    except ValueError:
        raise ValueError("Неправильный тип данных")  # Возвращаем строку, если ввод не является числом

    if a + b == 0:
        return float('inf')  # Избегаем деления на ноль

    result = np.cbrt(((10 ** 3) * abs(x * k)) / (a + b))
    return result

if __name__ == "__main__":
    x, k, a, b = input("Введите четыре числа через пробел: ").split()
    print(f"Вы ввели числа: x = {x}, k = {k}, a = {a}, b = {b}")
    result = calculate_formula(x, k, a, b)
    if isinstance(result, str):
        print(result)
    else:
        print(f"Результат вычисления формулы: {round(result, 2)}")