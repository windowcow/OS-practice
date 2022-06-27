from __future__ import generators
from email import generator
import time
from types import GeneratorType
a = (x * x for x in range(10))

print(type(a))


def generator_example():
    for i in range(10):
        print("yield 전:", i)

        if i % 2 == 0:
            yield i
            print("yield 후:", i)


c = generator_example()
d = map(lambda l: l * l, [1, 2, 3, 4, 5])

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
