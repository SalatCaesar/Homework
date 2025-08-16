lst = [0 ,1, 0, 2, 0, 3, 0]
p = lst.count(0)
for i in range(p):
    lst.remove(0)
print(lst)
for i in range(p):
    lst.append(0)
print(lst)