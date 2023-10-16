import re
from collections import defaultdict

def text_stat(filename):
    try:
        # Открываем файл и читаем его содержимое
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        # Проверка на пустоту файла
        if not text:
            return {
                'letter_frequencies': {},
                'word_amount': 0,
                'paragraph_amount': 0,
                'bilingual_word_amount': 0
            }

        # Разделение текста на абзацы. Пусть абзац это переход на новую строку.
        paragraphs = re.split(r'\n(?!\s*\n)', text)
        paragraph_amount = len(paragraphs)

        # Разделение текста на слова с учётом дефисов, @ и точек. Цифра считается словом.
        words = re.findall(r'\b[А-Яа-яA-Za-z0-9]+(?:[-._@][А-Яа-яA-Za-z0-9]+)*\b', text)
        word_amount = len(words)

        # Создаем словарь для подсчета частоты букв
        letter_count = defaultdict(int)
        bilingual_word_count = 0

        # Создаем массив для подсчета частоты букв с одним попаданием буквы в слове
        letter_freq_count = defaultdict(int)

        for word in words:
            # Проверяем, содержит ли слово буквы из обоих алфавитов
            has_latin = bool(re.search(r'[a-zA-Z]', word))
            has_cyrillic = bool(re.search(r'[а-яА-Я]', word))

            if has_latin and has_cyrillic:
                bilingual_word_count += 1

            # Флаги для отслеживания букв в слове
            letter_flag = defaultdict(bool)

            for letter in word:
                if letter.isalpha():
                    letter_count[letter.lower()] += 1
                    if not letter_flag[letter.lower()]:
                        letter_flag[letter.lower()] = True
                        letter_freq_count[letter.lower()] += 1

        # Рассчитываем долю слов, в которых встречается конкретная буква
        letter_percentages = {}
        for letter, count in letter_freq_count.items():
            percentage = round(count / word_amount * 100, 2)
            letter_percentages[letter] = (letter_count[letter], percentage)

        # Создаем словарь с результатами
        result = {
            'letter_frequencies': letter_percentages,
            'word_amount': word_amount,
            'paragraph_amount': paragraph_amount,
            'bilingual_word_amount': bilingual_word_count
        }

        return result

    except FileNotFoundError:
        return {'error': 'Файл не найден'}
    except Exception as e:
        return {'error': str(e)}

# Пример использования функции
if __name__ == "__main__":
    filename = 'test_files/example_text_file.txt'
    stats = text_stat(filename)
    if 'error' in stats:
        print(stats['error'])
    else:
        print("Частота букв: ", stats['letter_frequencies'])
        print("Количество слов: ", stats['word_amount'])
        print("Количество абзацев: ", stats['paragraph_amount'])
        print("Количество слов с использованием букв из обоих алфавитов: ", stats['bilingual_word_amount'])
