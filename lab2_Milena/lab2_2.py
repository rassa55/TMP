def sequence_recursive(n):
    if n <= 0:
        raise ValueError("N должно быть больше или равно 1")
    if n == 1:
        return 1
    else:
        return 2 * sequence_recursive(n-1)

print("Задана последовательность: 1; 2; 4; 8; 16; 32; 64, ….")

n = int(input("Введите число элементов "))
for i in range(1, n+1):
    print(f"Член {i}: {sequence_recursive(i)}")

print("Формула: a_n = 2 * a_(n-1)")