import random


def check_data(func):
    def wrapper(answer, attempts_number):
        if not (1 <= answer <= 100):
            answer = random.randint(1, 100)
        if not (1 <= attempts_number <= 10):
            attempts_number = random.randint(1, 10)
        func(answer, attempts_number)
    return wrapper


@check_data
def guessing_game(answer, attempts_number):
    def attempts():
        for _ in range(attempts_number):
            guess = int(input('input number'))
            if guess == answer:
                print('correct')
                return
            elif guess > answer:
                print('lower')
            else:
                print('greater')
    return attempts


guessing_game(100, 5000)
