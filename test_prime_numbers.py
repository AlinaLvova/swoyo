import unittest
from prime_numbers import prime_numbers, is_prime

class TestPrimeNumbers(unittest.TestCase):
    def test_prime_numbers_with_valid_input(self):
        self.assertEqual(prime_numbers(10, 50), [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
        self.assertEqual(prime_numbers(2, 20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(prime_numbers(2, 2), [2])

    def test_prime_numbers_with_invalid_input(self):
        self.assertEqual(prime_numbers(20, 10), [])
        self.assertEqual(prime_numbers(0, 10), [2, 3, 5, 7])
        self.assertEqual(prime_numbers(1, 10), [2, 3, 5, 7])

    def test_prime_numbers_with_negative_input(self):
        # Тестирование на отрицательных числах в диапазоне
        self.assertEqual(prime_numbers(-10, 10), [2, 3, 5, 7])
        self.assertEqual(prime_numbers(-50, -10), [])
        self.assertEqual(prime_numbers(-10, -5), [])
        
    def test_prime_numbers_with_large_values(self):
        # Тестирование на больших значениях
        self.assertEqual(prime_numbers(1000, 1100), [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097])
        
    def test_prime_numbers_with_boundary_values(self):
        # Тестирование на граничных значениях
        self.assertEqual(prime_numbers(0, 10), [2, 3, 5, 7])
        self.assertEqual(prime_numbers(1, 1), [])
        self.assertEqual(prime_numbers(10, 11), [11])
        self.assertEqual(prime_numbers(11, 12), [11])
        self.assertEqual(prime_numbers(20, 10), [])
        
    def test_prime_numbers_with_empty_range(self):
        # Тестирование на пустом диапазоне
        self.assertEqual(prime_numbers(5, 4), [])
        self.assertEqual(prime_numbers(7, 7), [7])
        
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))

if __name__ == '__main__':
    unittest.main()
