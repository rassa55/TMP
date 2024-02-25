def print_sequence(n: int):
    if n <= 0:
        raise ValueError("N должно быть больше или равно 1")
    for i in range(n):
        print(f"Член {i + 1}: {2**i}")

print("Задана последовательность: 1; 2; 4; 8; 16; 32; 64, ….")
n = int(input("Введите число элементов "))
print_sequence(n)
print("Формула: a_n = 2 * a_(n-1)")
