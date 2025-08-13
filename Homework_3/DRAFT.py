from itertools import count

n = [1, 2, 3, 4, 5]
n[0], n[-1] = n[-1], n[0]
print(n)
print(len(n))