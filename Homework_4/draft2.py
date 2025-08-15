num = 4
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