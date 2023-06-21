# Task 1. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать "больше" или "меньше" после каждой попытки.

from random import randint

num = randint(0, 1000)
i = 0
TRIES = 10
guess = input(f'Try to guess a number between 0 and 1000 inclusive. You have {TRIES} tries:  ')

while i <= TRIES - 1:
    if i == TRIES - 1:
        print(f"Sorry, you don't have any attempts left. Guessed number was {num}")
        break
    elif not guess.isdigit():
        guess = input('incorrect input, please, try again: ')
        continue
    else:
        guess = int(guess)
        if guess < 0 or guess > 1000:
            guess = input('Number should be between 0 and 1000, please, try again: ')
            continue
        elif guess > num:
            i += 1
            guess = input(f'Guessed number is smaller, try again. You have {TRIES - i} tries left: ')
            continue
        elif guess < num:
            i += 1
            guess = input(f'Guessed number is greater, try again. You have {TRIES - i} tries left: ')
            continue
        elif guess == num:
            print('Bravo, you guessed the right number!')
            break

# Task 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с
# суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с
# такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.


def side_length(side_number):
    side = input(f'Please, input side {side_number} length: ')
    while not side.isdigit():
        side = input('Incorrect input, please try again: ')
    side = int(side)
    return side


a = side_length('1')
b = side_length('2')
c = side_length('3')

if a > b + c or b > a + c or c > a + b:
    print('such triangle cannot not exist')
else:
    print('This is', end=' ')
    if a == b == c:
        print('equilateral triangle')
    elif a == b or a == c or b == c:
        print('isosceles triangle')
    else:
        print('versatile triangle')

# Task 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч

MIN_VALUE = 0
MAX_VALUE = 100000
num = input('input number: ')

while True:
    if num.isdigit():
        num = int(num)
        if MIN_VALUE < num <= MAX_VALUE:
            break
        else:
            num = input('incorrect input, please, try again: ')
    else:
        num = input('incorrect input, please, try again: ')

MAX_RANGE = int(num ** 0.5)
check = False
for i in range(2, MAX_RANGE + 1):
    if num % i == 0:
        print('not prime number')
        break
    elif i == MAX_RANGE:
        print('prime number')

