#n1 = 'qweq'
#a1 = ({i:n1.count(i) for i in [*n1]})
#
#n2 = 'qweqw'
#c2 = str()
#for i2 in range(len(n2)):
#    c2 += n2[i2] + '_' + str(n2[0:i2+1].count(n2[i2]))
#
#
#
#
#
#
#t = [('Мартин', 5, 'Алексей', 'Егоров'),
#         ('Фродо', 3, 'Анна', 'Самохина'),
#         ('Вася', 4, 'Алексей', 'Егоров')]
#for i in range(len(t)):
#    d = t[i]
#    c = {(d[0], d[1]):(d[2], d[3]) for n in d}
#    print(c)
o1 = dict.fromkeys(['а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т'], 1)
o2 = dict.fromkeys(['д', 'к', 'л', 'м', 'п', 'у'], 2)
o3 = dict.fromkeys(['б', 'г', 'ь', 'я'], 3)
o4 = dict.fromkeys(['й', 'ы'], 4)
o5 = dict.fromkeys(['ж', 'з', 'х', 'ц', 'ч'], 5)
o8 = dict.fromkeys(['ф', 'ш', 'э', 'ю'], 8)
o10 = dict.fromkeys(['щ'], 10)
o15 = dict.fromkeys(['ъ'], 15)
o_all = {**o1, **o2, **o3, **o4, **o5, **o8, **o10, **o15}
#print(o_all)

s = 'струт'
l = list(s)
w = 0
print(l)
for i in range(len(l)):
    f = l[i]
    w += int(o_all[f])
print(w)