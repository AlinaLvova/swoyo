import argparse
from is_roman_number import is_roman_number

def roman_numerals_to_int(roman_numeral):
    roman_str = roman_numeral.upper()

    if len(roman_str) == 0:
        return 0

    if not is_roman_number(roman_str):
        return None

    arabic_values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman_symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    result = 0
    i = len(arabic_values) - 1
    pos = 0

    while i >= 0 and pos < len(roman_str):
        if roman_str[pos:pos + len(roman_symbols[i])] == roman_symbols[i]:
            result += arabic_values[i]
            pos += len(roman_symbols[i])
        else:
            i -= 1

    return result

def main():
    parser = argparse.ArgumentParser(description="Convert Roman numerals to integers.")
    parser.add_argument("roman_numeral", nargs='?', default='', help="The Roman numeral to convert (default: 0).")
    args = parser.parse_args()

    roman_numeral = args.roman_numeral
    integer_value = roman_numerals_to_int(roman_numeral)

    if integer_value is not None:
        print(f"Римское число {roman_numeral} соответствует целому числу {integer_value}")
    else:
        print("Ошибка в римской нотации.")

if __name__ == "__main__":
    main()