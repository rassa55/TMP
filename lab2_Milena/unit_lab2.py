import unittest
import io
import time
from unittest.mock import patch
from contextlib import redirect_stdout
from lab2_1 import print_sequence
from lab2_2 import sequence_recursive

class TestPrintSequence(unittest.TestCase):
    @patch('builtins.input', return_value='3')
    def test_print_sequence(self, mock_input):
        fake_out = io.StringIO()
        with redirect_stdout(fake_out):
            print_sequence(3)
        output = fake_out.getvalue().strip()
        start_time = time.perf_counter()
        self.assertEqual(output, 'Член 1: 1\nЧлен 2: 2\nЧлен 3: 4')

        with self.assertRaises(ValueError):
            print_sequence(-5)
        end_time = time.perf_counter()
        print(f"Время выполнения теста print_sequence: {end_time - start_time} секунд")

    def test_sequence_recursive(self):
        start_time = time.perf_counter()
        self.assertEqual(sequence_recursive(1), 1)
        self.assertEqual(sequence_recursive(2), 2)
        self.assertEqual(sequence_recursive(3), 4)
        self.assertEqual(sequence_recursive(4), 8)
        self.assertEqual(sequence_recursive(50), 562949953421312)

        with self.assertRaises(ValueError):
            print_sequence(-5)

        end_time = time.perf_counter()
        print(f"Время выполнения теста sequence_recursive: {end_time - start_time} секунд")

if __name__ == '__main__':
    unittest.main()