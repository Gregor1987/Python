import random


def write_file(string_count: int, filename: str):
    filename = filename + '.txt'
    with open(filename, 'a', encoding='utf-8') as f:
        for i in range(string_count):
            print(f'{random.randint(-1000, 1000)}|{random.uniform(-1000.00, 1000.00)}', file=f)


write_file(10, 'new_file')
