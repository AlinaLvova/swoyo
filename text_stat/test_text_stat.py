import unittest
from text_stat import text_stat

class TestTextStat(unittest.TestCase):
    def test_invalid_file(self):
        filename = 'test_files/non_existent_file.txt'
        result = text_stat(filename)
        self.assertIn('error', result)

    def test_empty_file(self):
        filename = 'test_files/empty_file.txt'
        result = text_stat(filename)
        self.assertEqual(result['letter_frequencies'], {})
        self.assertEqual(result['word_amount'], 0)
        self.assertEqual(result['paragraph_amount'], 0)
        self.assertEqual(result['bilingual_word_amount'], 0)
        self.assertNotIn('error', result)

    def test_whitespace_file(self):
        filename = 'test_files/whitespace_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)
        self.assertEqual(result['letter_frequencies'], {})
        self.assertEqual(result['word_amount'], 0)
        self.assertEqual(result['paragraph_amount'], 1)
        self.assertEqual(result['bilingual_word_amount'], 0)

    def test_only_latin_characters(self):
        filename = 'test_files/latin_characters_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)
        self.assertEqual(result['paragraph_amount'], 1)
        self.assertEqual(result['word_amount'], 12)
        self.assertEqual(result['letter_frequencies']['i'], (6, round(6/12*100,2)))
        self.assertEqual(result['letter_frequencies']['n'], (6, round(4/12*100,2)))
        self.assertEqual(result['letter_frequencies']['t'], (8, round(8/12*100,2)))
        self.assertEqual(result['bilingual_word_amount'], 0)

    def test_only_cyrillic_characters(self):
        filename = 'test_files/cyrillic_characters_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)
        self.assertEqual(result['paragraph_amount'], 1)
        self.assertEqual(result['word_amount'], 11)
        self.assertEqual(result['letter_frequencies']['в'], (2, round(2/11*100,2)))
        self.assertEqual(result['letter_frequencies']['о'], (6, round(5/11*100,2)))
        self.assertEqual(result['bilingual_word_amount'], 0)

    def test_bilingual_words(self):
        filename = 'test_files/bilingual_words_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)
        self.assertEqual(result['paragraph_amount'], 2)
        self.assertEqual(result['word_amount'], 2)
        self.assertEqual(result['bilingual_word_amount'], 2)

    def test_special_characters_and_numbers(self):
        filename = 'test_files/special_characters_and_numbers_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)
        self.assertEqual(result['word_amount'], 17)

    def test_multiple_paragraphs(self):
        filename = 'test_files/hyphenated_words_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)    
        self.assertEqual(result['word_amount'], 41)
  
    def test_multiple_paragraphs(self):
        filename = 'test_files/multiple_paragraphs_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)
        self.assertEqual(result['paragraph_amount'], 7)

    def test_single_word_file(self):
        filename = 'test_files/single_word_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)
        self.assertEqual(result['paragraph_amount'], 1)
        self.assertEqual(result['word_amount'], 1)
        self.assertEqual(result['letter_frequencies']['t'], (2, round(1/1*100,2)))
        self.assertEqual(result['letter_frequencies']['e'], (2, round(1/1*100,2)))
        self.assertEqual(result['letter_frequencies']['l'], (1, round(1/1*100,2)))
        self.assertEqual(result['letter_frequencies']['r'], (1, round(1/1*100,2)))
        self.assertEqual(result['bilingual_word_amount'], 0)

    def test_duplicate_words(self):
        filename = 'test_files/duplicate_words_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)
        self.assertEqual(result['word_amount'], 5)
        self.assertEqual(result['letter_frequencies']['t'], (2, round(2/5*100,2)))
        self.assertEqual(result['letter_frequencies']['w'], (2, round(2/5*100,2)))
        self.assertEqual(result['letter_frequencies']['e'], (3, round(3/5*100,2)))
        self.assertEqual(result['bilingual_word_amount'], 0)

    def test_mixed_case_letters(self):
        filename = 'test_files/mixed_case_letters_file.txt'
        result = text_stat(filename)
        self.assertNotIn('error', result)
        self.assertEqual(result['word_amount'], 8)
        self.assertEqual(result['letter_frequencies']['m'], (2, round(2/8*100,2)))
        self.assertEqual(result['letter_frequencies']['s'], (4, round(4/8*100,2)))
        self.assertEqual(result['letter_frequencies']['l'], (4, round(4/8*100,2)))
        self.assertEqual(result['letter_frequencies']['t'], (4, round(2/8*100,2)))
        self.assertEqual(result['bilingual_word_amount'], 0)
    
if __name__ == '__main__':
    unittest.main()
