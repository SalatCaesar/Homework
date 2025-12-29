import string
import random


def g_r_n():
    while True:
        yield ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 15))) + ' ' + ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 15)))
b = g_r_n()


print(type(b))
print(next(b))
print(next(b))
print(next(b))
