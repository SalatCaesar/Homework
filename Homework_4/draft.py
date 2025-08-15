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

n = 7   # Можно попоробовать удалять элемент с индексом, а потом создавать новый список начиная с элемента индекс +1
krug = list(range(1,n+1))
print(krug)


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
start_index = 2  # Начинаем с третьего элемента (индекс 2)

for i in range(len(my_list)):
    index = (start_index + i) % len(my_list)
    print(my_list[index])