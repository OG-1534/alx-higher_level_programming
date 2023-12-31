#!/usr/bin/python3


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    number = 0
    total = 0
    digits = {'X': 10, 'V': 5, 'I': 1, 'M': 1000, 'D': 500, 'C': 100, 'L': 50}
    for i in reversed(roman_string):
        number = digits[i]
        total += number if total < number * 5 else -number
    return total
