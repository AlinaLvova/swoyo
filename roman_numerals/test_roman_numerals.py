import unittest
from roman_numerals import roman_numerals_to_int

class TestRomanNumeralsConversion(unittest.TestCase):
    def test_roman_numerals_to_int(self):
        self.assertEqual(roman_numerals_to_int("III"), 3)
        self.assertEqual(roman_numerals_to_int("IV"), 4)
        self.assertEqual(roman_numerals_to_int("IX"), 9)
        self.assertEqual(roman_numerals_to_int("LVIII"), 58)
        self.assertEqual(roman_numerals_to_int("MCMXCIV"), 1994)
        self.assertEqual(roman_numerals_to_int("XLII"), 42)
        self.assertEqual(roman_numerals_to_int("xlii"), 42)
        self.assertEqual(roman_numerals_to_int("MMXXI"), 2021)
        self.assertEqual(roman_numerals_to_int("MMMDCCCLXXXVIII"), 3888)
        
    def test_invalid_roman_numerals(self):
        self.assertIsNone(roman_numerals_to_int("XLIXIV"))
        self.assertIsNone(roman_numerals_to_int("IIII"))    # Неверная форма для 4
        self.assertIsNone(roman_numerals_to_int("ILIXIV"))  # Неверная форма для 4
        self.assertIsNone(roman_numerals_to_int("IC"))    # Неверная форма для 99
        self.assertIsNone(roman_numerals_to_int("LL"))    # Неверная форма для 50
        self.assertIsNone(roman_numerals_to_int("VV"))    # Неверная форма для 10
        
    def test_empty_roman_numeral(self):
        self.assertEqual(roman_numerals_to_int(""), 0)  # Пустая строка представляет 0

    def test_whitespace_roman_numeral(self):
        # Тесты с пробелами в римском числе
        self.assertIsNone(roman_numerals_to_int("VII  X"))
        self.assertIsNone(roman_numerals_to_int("  IX  IV  "))

    def test_dot_separator(self):
        # Тест с использованием точки для разделения символов
        self.assertIsNone(roman_numerals_to_int("X.II.III"))
        
if __name__ == '__main__':
    unittest.main()
