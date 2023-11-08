import json
from os.path import isfile
import random
from functools import wraps


def save_to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isfile(f'{func.__name__}.json'):
            with open(f'{func.__name__}.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                data[result] = [args, kwargs]
        else:
            data = {result: [args, kwargs]}
        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    return wrapper


def check_data(func):
    @wraps(func)
    def wrapper(answer, attempts_number):
        if not (1 <= answer <= 100):
            answer = random.randint(1, 100)
        if not (1 <= attempts_number <= 10):
            attempts_number = random.randint(1, 10)
        func(answer, attempts_number)
    return wrapper


def many_runs(runs):
    def run(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(runs):
                func(*args, **kwargs)
        return wrapper
    return run


@many_runs(2)
@save_to_json
@check_data
def guessing_game(answer, attempts):
    for _ in range(attempts):
        guess = int(input('input number\n'))
        if guess == answer:
            print('correct')
            return
        elif guess > answer:
            print('lower')
        else:
            print('greater')


guessing_game(random.randint(0, 1000), random.randint(0, 100))
