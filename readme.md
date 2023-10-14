# Простые числа в заданном диапазоне

Реализация функции по поиску простых числе prime_numbers(low, high), где low и high – нижняя и верхняя границы диапазона, в котором надо найти эти числа. Функция должна возвращает список с числами, отсортированными по возрастанию.

Функция корректно обрабатывает некорректное значение аргументов, возвращая пустой список

Алгоритм является оптимизированным методом проверки чисел на простоту. Важные особенности этого алгоритма:

* Исключение чисел, меньших или равных 1, сразу же возвращает False.
* Проверка чисел до корня из числа, что уменьшает количество делителей для проверки.
* Использование оптимизированного метода проверки делителей для чисел, которые не делятся на 2 или 3. Мы проверяем делители, находящиеся на шагах 6 относительно друг друга, что позволяет уменьшить количество проверок.

Этот алгоритм более эффективен, чем простой перебор делителей от 2 до n-1, так как уменьшает количество проверок и исключает числа, которые являются точными кратными 2 и 3. Он хорошо подходит для поиска простых чисел в заданном диапазоне.

Для запуска тестов:
```python
python -m unittest test_prime_numbers.py
