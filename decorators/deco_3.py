import json
from os.path import isfile


def save_to_json(func):
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


@save_to_json
def func(*args, **kwargs):
    return sum(args)


func(1, 2, 6, 8, 5, a=5, b=8)