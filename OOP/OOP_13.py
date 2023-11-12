from collections import deque as deq


class Factorial:
    def __init__(self, k):
        self.history = deq(maxlen=k)

    def __call__(self, number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        self.history.append({number: result})
        return result

    def get_history(self):
        return self.history


f = Factorial(5)
print(f(5))
print(f(4))
print(f(20))
print(f(7))
print(f(6))
print(f.get_history())
