import random
import json


def run_from_csv(func):
    def wrapper(file_name):
        res_dict = {}
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                a, b, c = line.strip().split(',')
                result = func(int(a), int(b), int(c))
                res_dict.update((result, [a, b, c]))
        return res_dict
    return wrapper


def save_to_json(func):
    def wrapper(file_name, data):
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    return wrapper


def generate_csv(file_name):
    with open(f'{file_name}.csv', 'w', encoding='utf-8', newline='') as f:
        for _ in range(random.randint(100, 1000)):
            print(f'{random.randint(-100, 100)}, {random.randint(-100, 100)}, {random.randint(-100, 100)}', file=f)


def square(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x_1 = (-b + d ** 0.5) / (2 * a)
        x_2 = (-b - d ** 0.5) / (2 * a)
        return [(-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)]
    elif d == 0:
        return - (b / 2 * a)
    else:
        return 'корней нет'

