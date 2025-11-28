# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
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

assert three_most_expensive_purchases == 202346