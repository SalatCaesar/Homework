f = open(r'test_file\task1_data.txt', 'r', encoding='utf-8')
z = f.readlines()
f.close()
r = str()
for i in z:
    r += i.translate(str.maketrans('', '', '0123456789'))
f = open(r'test_file\task1_answer.txt', 'w+', encoding='utf-8')
f.writelines(r)
print(*f)