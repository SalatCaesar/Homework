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

q2 = 12345
q2 = str(q2)
w2 = 0
print(type(q2))
for i in q2:
    w2 += int(i)
print(w2)
