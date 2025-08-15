q = (5, 5, 5)
w = sorted(q)
print(w)
if w[2] >= w[0] + w[1]:
    print('Не треугольник')
else:
    if w[0] == w[1] == w[2]:
        print('Равносторонний')
    else:
        if w[0] == w[1] or w[1] == w[2] or w[1] == w[2]:
            print('Равнобедренный')
        else:
            print('Обычный')

print()

q1 = [
    [[1,2,4], [5,6,7]],
    [[], [1,2,3]],
    [[8,7,6], [2,6,0,]]
]
t1=[]
for w1 in q1:
    for e1 in w1:
        for r1 in e1:
            t1.append(r1)
t1 = sorted(t1)
print(t1)

print()

q2 = 12345
q2 = str(q2)
w2 = 0
print(type(q2))
for i in q2:
    w2 += int(i)
print(w2)

print()

num = 999
strnum = str(num)
v = 1
p = None
z = 0
if len(strnum) > 1:
    while p != 1:
        for i in strnum:
            v *= int(i)
        p = (len(str(v)))
        strnum = str(v)
        z = z + 1
        v = 1
else:
    z = 0
print(z)

print()

n4 = 7   # Можно попоробовать удалять элемент с индексом, а потом создавать новый список начиная с элемента индекс +1
l4 = 3
krug = list(range(1,n4+1))
print(krug)
g4 = []
for i4 in range(n4-l4):  # Попробую по очереди добавлять в конец пустого списка значения из начального
    g4.append(i4+l4)
for i5 in range(n4-l4):
    g4.append(i5+1)
print(g4)