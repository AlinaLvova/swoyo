# Решение тестового задания

В этом репозитории представлено решение для трех задач:

1. Поиск Простых Чисел в Диапазоне (prime_numbers)
Функция prime_numbers(low, high) позволяет находить простые числа в заданном диапазоне и возвращает их список, отсортированный по возрастанию.

2. Статистика Текста (text_stat)
Функция text_stat(filename) рассчитывает статистику содержимого текстового файла. Статистика включает частоту использования каждой буквы латинского или кириллического алфавита, количество слов в тексте, количество абзацев в тексте, долю слов, в которых встречается конкретная буква, и количество слов, в которых одновременно встречаются буквы обоих алфавитов.

3. Перевод Римских Чисел в Целые Числа (roman_numerals)
Функция roman_numerals_to_int(roman_numeral) выполняет перевод числа из римской нотации в десятичную целочисленную нотацию и возвращает результат в формате int.

Каждая из этих функций предоставляет решение для своей конкретной задачи и имеет документацию, описывающую ее входные параметры, выходные данные и способ использования.

## Использование

Для использования функций, вы можете импортировать их в свой Python-скрипт, как показано в примерах в каждой документации:

```python
from prime_numbers import prime_numbers

result = prime_numbers(10, 50)
print(result)  # Выведет список простых чисел в диапазоне [10, 50]
```

```python
from text_stat import text_stat

filename = 'sample.txt'
stats = text_stat(filename)
print(stats)
```

```python
from roman_numerals import roman_numerals_to_int

result = roman_numerals_to_int("XII")
print(result) 
```

## Зависимости

Решения задач не требуют использования сторонних библиотек и основаны на стандартных возможностях Python.

## Обратная Связь

Если у вас есть вопросы, предложения или замечания по решениям задач, пожалуйста, свяжитесь со мной. Ваши отзывы важны и помогают сделать эти решения лучше.

Автор: Lvova Alina

Контакт: <lvov.alina@yandex.ru>
