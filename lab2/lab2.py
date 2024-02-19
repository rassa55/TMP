import math

class Pythagorean:

    def find_pythagorean_triplets_iterative(self, N: int):
        """
        Функция для нахождения троек чисел Пифагора.

        Args:
        - N: int, верхняя граница для поиска троек чисел Пифагора.

        Returns:
        - list: Список троек чисел Пифагора, удовлетворяющих условиям.
        """
        if N < 1:
            raise ValueError("N должно быть больше или равно 1")

        triplets = []
        for a in range(1, N+1):
            for b in range(a, N+1):
                c = math.sqrt(a**2 + b**2)
                if c.is_integer() and 1 <= c <= N:
                    triplets.append((a, b, int(c)))

        if not triplets:
            raise ValueError("Нет троек пифагора для данного N")
        return triplets

if __name__ == "__main__":
    try:
        Pythagorean = Pythagorean()
        N = int(input("Введите N: "))
        pythagorean_triplets = Pythagorean.find_pythagorean_triplets_iterative(N=N)
        print("Тройки чисел Пифагора:")
        for triplet in pythagorean_triplets:
            print(triplet)
    except ValueError as ve:
        print(f"Ошибка: {ve}")