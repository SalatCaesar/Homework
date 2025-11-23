# Можно улучшить:
# 1. Прочитать подробнее про str.translate(). Выглядит, что это может прям много очень
# 2. Добавить удаления файла с ответом после сравнения с эталоном

table = str.maketrans('','','1234567890')

with open(r'test_file\task1_data.txt', 'r', encoding='utf-8') as file:
    file = file.read()
print(file)

res = file.translate(table)

with open(r'test_file\task1_answer.txt', 'w', encoding='utf-8') as file:
    file.write(res)