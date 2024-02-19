import unittest
import time
from lab2 import Pythagorean
from lab2_1 import Pythagorean_recursive

Pythagorean = Pythagorean()
Pythagorean_recursive = Pythagorean_recursive()

class TestPythagoreanTriplets(unittest.TestCase):

    def test_find_pythagorean_triplets(self):
        start_time = time.time()
        # Проверяем, что функция возвращает ожидаемый результат для N = 5
        expected_result_N5 = [(3, 4, 5)]
        self.assertEqual(Pythagorean.find_pythagorean_triplets_iterative(N=5), expected_result_N5)

        # Проверяем, что функция возвращает ожидаемый результат для N = 10
        expected_result_N10 = [(3, 4, 5), (6, 8, 10)]
        self.assertEqual(Pythagorean.find_pythagorean_triplets_iterative(N=10), expected_result_N10)

        expected_result_N40 = [
            (3, 4, 5),
            (5, 12, 13),
            (6, 8, 10),
            (7, 24, 25),
            (8, 15, 17),
            (9, 12, 15),
            (10, 24, 26),
            (12, 16, 20),
            (12, 35, 37),
            (15, 20, 25),
            (15, 36, 39),
            (16, 30, 34),
            (18, 24, 30),
            (20, 21, 29),
            (21, 28, 35),
            (24, 32, 40),
        ]
        self.assertEqual(Pythagorean.find_pythagorean_triplets_iterative(40), expected_result_N40)

        # Проверяем, что функция обрабатывает ошибку при N = 2 (нет троек)
        with self.assertRaises(ValueError):
            Pythagorean.find_pythagorean_triplets_iterative(N=2)

        # Проверяем, что функция обрабатывает ошибку при N = 0
        with self.assertRaises(ValueError):
            Pythagorean.find_pythagorean_triplets_iterative(N=0)

        # Проверяем, что функция обрабатывает ошибку при N < 0
        with self.assertRaises(ValueError):
            Pythagorean.find_pythagorean_triplets_iterative(N=-5)
        end_time = time.time()
        print(f"Время выполнения теста find_pythagorean_triplets: {end_time - start_time} секунд")

    # @unittest.skip("Время выполнения теста find_pythagorean_triplets_recursive слишком велико")
    def test_find_pythagorean_triplets_recursive(self):
        start_time = time.time()
        # Тестирование для N = 5
        expected_result_N5 = [(3, 4, 5)]
        self.assertEqual(Pythagorean_recursive.find_pythagorean_triplets_recursive(5), expected_result_N5)

        # Тестирование для N = 10
        expected_result_N10 = [(3, 4, 5), (6, 8, 10)]
        self.assertEqual(Pythagorean_recursive.find_pythagorean_triplets_recursive(10), expected_result_N10)

        expected_result_N40 = [
            (3, 4, 5),
            (5, 12, 13),
            (6, 8, 10),
            (7, 24, 25),
            (8, 15, 17),
            (9, 12, 15),
            (10, 24, 26),
            (12, 16, 20),
            (12, 35, 37),
            (15, 20, 25),
            (15, 36, 39),
            (16, 30, 34),
            (18, 24, 30),
            (20, 21, 29),
            (21, 28, 35),
            (24, 32, 40),
        ]
        self.assertEqual(Pythagorean_recursive.find_pythagorean_triplets_recursive(40), expected_result_N40)

        # Тестирование для N = 2 (нет троек)
        with self.assertRaises(ValueError):
            Pythagorean.find_pythagorean_triplets_iterative(N=2)

        # Тестирование для N = 0 (вызов исключения)
        with self.assertRaises(ValueError):
            Pythagorean_recursive.find_pythagorean_triplets_recursive(2)

        # Тестирование для N < 0 (вызов исключения)
        with self.assertRaises(ValueError):
            Pythagorean_recursive.find_pythagorean_triplets_recursive(-5)
        end_time = time.time()
        print(f"Время выполнения теста find_pythagorean_triplets_recursive: {end_time - start_time} секунд")


if __name__ == '__main__':
    unittest.main()