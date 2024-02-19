import unittest
from lab1 import calculate_formula

class TestFormula(unittest.TestCase):

    def test_calculate_formula(self):
        # Тестирование для x = 2, k = 3, a = 4, b = 5
        self.assertAlmostEqual(calculate_formula(2, 3, 4, 5), 8.74,  places=2)

        # Тестирование для x = 0, k = 0, a = 0, b = 0
        self.assertAlmostEqual(calculate_formula(0, 0, 0, 0), float('inf'))

        # Тестирование для x = -1, k = -1, a = -1, b = -1
        self.assertAlmostEqual(calculate_formula(-1, -1, -1, -1), -7.94, places=2)

        # Тестирование для x = 'a', k = 'b', a = 'c', b = 'd'
        with self.assertRaises(ValueError):
            calculate_formula('a', 'b', 'c', 'd')

        # Тестирование для x = 2, k = 3, a = 0, b = 0
        self.assertEqual(calculate_formula(2, 3, 0, 0), float('inf'))

if __name__ == '__main__':
    unittest.main()