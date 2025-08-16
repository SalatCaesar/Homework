n = 7
k = 3
res = 0
for i in range(1, n + 1):
    res = (res + k) % i
    print(res)
print(res+1)