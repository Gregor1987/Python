# Task 1. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = input('input number: ')
while not num.isdigit():
    num = input('incorrect input, try again: ')
num = int(num)
print(hex(num)[2::])
DIVISOR = 16
hex_dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c',
            13: 'd', 14: 'e', 15: 'f'}
res = ''
while num != 0:
    res = hex_dict[num % DIVISOR] + res
    num //= DIVISOR
print(res)

# Task 2. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import math
import fractions

frac_1 = input('Input first fraction: ')
frac_2 = input('Input second fraction: ')

a_1, b_1 = int(frac_1[:frac_1.find('/')]), int(int(frac_1[frac_1.find('/') + 1:]))
a_2, b_2 = int(frac_2[:frac_2.find('/')]), int(int(frac_2[frac_2.find('/') + 1:]))

sum_denominator = math.lcm(b_1, b_2)
new_numerator_1 = a_1 * (sum_denominator / b_1)
new_numerator_2 = a_2 * (sum_denominator / b_2)
sum_numerator = int(new_numerator_1 + new_numerator_2)

print(f'Sum of fractions = {sum_numerator}/{sum_denominator}')

mult_numerator = a_1 * a_2
mult_denominator = b_1 * b_2

print(f'Product of fractions = {mult_numerator}/{mult_denominator}')

f_1 = fractions.Fraction(a_1, b_1)
f_2 = fractions.Fraction(a_2, b_2)
print(f_1 + f_2)
print(f_1 * f_2)
