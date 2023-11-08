import random


def run_from_csv(func):
    def wrapper(file_name):



def generate_csv(file_name):
    with open(f'{file_name}.csv', 'w', encoding='utf-8', newline='') as f:
        for _ in range(random.randint(100, 1000)):
            print(f'{random.randint(-100, 100)}, {random.randint(-100, 100)}, {random.randint(-100, 100)}', file=f)


def square(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x_1 = (-b + d ** 0.5) / (2 * a)
        x_2 = (-b - d ** 0.5) / (2 * a)
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return - (b / 2 * a)
    else:
        return 'корней нет'

