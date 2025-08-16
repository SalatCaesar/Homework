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
l4 = 1
krug = list(range(1,n4+1))
print(krug)
g4 = []
for i4 in range(n4-l4):  # Попробую по очереди добавлять в конец пустого списка значения из начального
    g4.append(i4+l4+1)
for i5 in range(l4):
    g4.append(i5+1)
print(g4)

print()

h = 7
k = 3
lst = list(range(1, h + 1))  # Создаём список людей в круге с порядковыми номерами
nlst = []  # Создаём пустой список, в котором жертва всегда будет последней
i = len(range(len(lst)))  # Создаём переменную с количеством людей в круге
while i > k:  # Пока количество людей в круге больше, чем шаг убийства, нам не надо переходить в начало списка при выборе жертвы
    nlst += lst[k:]  # Срез от жертвы до конца круга
    nlst += lst[:k]  # Срез от начала круга до жертвы включительно
    del nlst[-1]  # Убиваем жертву
    lst = nlst  # Список для выбора жертвы изменился, новый строить надо от этого
    nlst = []  # Очищаем список для выбора жертвы
    i = len(range(len(lst)))  # Новое количество людей
while i > 1:  # А вот когда количество людей становится не больше шага, то начинаем переходить при выборе в начало круга
    nlst += lst[k % i:]  # Срез от жертвы до конца круга
    nlst += lst[:k % i]  # Срез от начала круга до жертвы включительно
    del nlst[-1]  # Убиваем жертву
    lst = nlst  # Список для выбора жертвы изменился, новый строить надо от этого
    nlst = []  # Очищаем список для убийства
    i = len(range(len(lst)))  # Записываем длину списка
print(str(lst))

print()

tpl = (1, 1, 1, 2, 2, 2, 3, 3, 3, 3)
print(tpl[3])
numb = '('
for i in range(3):
    numb = (numb + str(tpl[i]))
print(numb)
numb += ') '
for i in range(3,6):
    numb = (numb + str(tpl[i]))
print(numb)
numb += '-'
for i in range(6,10):
    numb = (numb + str(tpl[i]))
print(numb)