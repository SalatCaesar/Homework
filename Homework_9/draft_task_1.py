# Можно улучшить:
# 1. ПРочитать подробнее про str.translate(). Выглядит, что это может прям много очень

table = str.maketrans('','','1234567890')

with open(r'test_file\task1_data.txt', 'r', encoding='utf-8') as file:
    file = file.read()
print(file)

res = file.translate(table)

with open(r'test_file\task1_answer.txt', 'w', encoding='utf-8') as file:
    file.write(res)