# Можно улучшить:
# 1. Подумать над split и join, может как-то сократить
# 2. Проверить sorted, как-то сомнительно

with open('test_file/task_3.txt', 'r', encoding='utf-8') as file:
    file = [i.strip() for i in file.readlines()]
    file = ','.join(file)
    file = file.split(',,')
    three_most_expensive_purchases = []
    for i in file:
        i = [int(n) for n in i.split(',')]
        purch = sum(i)
        three_most_expensive_purchases.append(purch)
    three_most_expensive_purchases = sum(sorted(three_most_expensive_purchases)[-3:])
    print(three_most_expensive_purchases)