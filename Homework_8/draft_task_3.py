def segment(a, b):
    try:
        s = sum(a) + sum(b)
        return s
    except TypeError as e:
        return str(e)[::-1]

print(segment(('a', 2), (2, 4)))