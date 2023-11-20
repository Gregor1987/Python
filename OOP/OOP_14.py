from collections import deque as deq
import json
from datetime import datetime as dt


class Factorial:
    def __init__(self, k):
        self.history_number = deq(maxlen=k)
        self.history_value = deq(maxlen=k)

    def __call__(self, number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        self.history_number.append(number)
        self.history_value.append(result)
        return result

    def get_history(self):
        return {i: j for i, j in zip(self.history_number, self.history_value)}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(f'{dt.now()}.json'.replace(':', ''), 'w', encoding='utf-8') as f:
            json.dump(self.get_history(), f, indent=2)


with Factorial(4) as f:
    print(f(5))
    print(f(4))
    print(f(20))
    print(f(7))
    print(f(6))
    # print(f.get_history())
