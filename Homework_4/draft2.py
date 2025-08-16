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