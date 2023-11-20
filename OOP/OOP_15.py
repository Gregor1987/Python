from collections import deque as deq


class Factorial:
    def __init__(self, stop, start=1, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.result = 1
        for i in range(1, start):
            self.result *= i

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            for i in range(1, self.stop):
                self.result *= self.start
                self.start += self.step
            return self.result
        else:
            raise StopIteration


for i in Factorial(start=1, stop=5, step=2):
    print(i)

