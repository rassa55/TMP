import math

class Pythagorean_recursive:

    def find_pythagorean_triplets_recursive(self, N: int, a=1, b=1, triplets=None):
        """
        Функция для нахождения троек чисел Пифагора с помощью рекурсии.

        Args:
        - N: int, верхняя граница для поиска троек чисел Пифагора.
        - a: int, текущее значение a.
        - b: int, текущее значение b.
        - triplets: list, текущий список троек чисел Пифагора.

        Returns:
        - list: Список троек чисел Пифагора, удовлетворяющих условиям.
        """
        if triplets is None:
            triplets = []

        if N < 1:
            raise ValueError("N должно быть больше или равно 1")

        if a > N:
            return triplets

        if b > N:
            return self.find_pythagorean_triplets_recursive(N, a + 1, a + 1, triplets)

        c = math.sqrt(a ** 2 + b ** 2)
        if c.is_integer() and 1 <= c <= N:
            triplets.append((a, b, int(c)))
        result = self.find_pythagorean_triplets_recursive(N, a, b + 1, triplets)
        if not result:
            raise ValueError("Нет троек пифагора для данного N")
        return result

if __name__ == "__main__":
    try:
        Pythagorean = Pythagorean_recursive()
        N = int(input("Введите N: "))
        pythagorean_triplets = Pythagorean.find_pythagorean_triplets_recursive(N=N)
        print("Тройки чисел Пифагора:")
        for triplet in pythagorean_triplets:
            print(triplet)
    except ValueError as ve:
        print(f"Ошибка: {ve}")
