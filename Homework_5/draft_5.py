#n1 = 'qweq'
#a1 = ({i:n1.count(i) for i in [*n1]})
#
#n2 = 'qweqw'
#c2 = str()
#for i2 in range(len(n2)):
#    c2 += n2[i2] + '_' + str(n2[0:i2+1].count(n2[i2]))


t = [('Мартин', 5, 'Алексей', 'Егоров'),
         ('Фродо', 3, 'Анна', 'Самохина'),
         ('Вася', 4, 'Алексей', 'Егоров')]
# d = {(i[0],i[1]):(i[2],i[3]) for i in t}
# print(d)


def transform_cats_data(cats_data):
    """
    Преобразует данные о котах и владельцах в оптимизированный формат.

    Args:
        cats_data: список кортежей (кличка, возраст, имя, фамилия)

    Returns:
        строка с данными, сгруппированными по владельцам
    """
    # Создаем словарь для группировки данных по владельцам
    owners_dict = {}

    # Заполняем словарь данными
    for cat_name, age, first_name, last_name in cats_data:
        owner_key = (first_name, last_name)
        if owner_key not in owners_dict:
            owners_dict[owner_key] = []
        owners_dict[owner_key].append((cat_name, age))

    # Формируем результат
    result_lines = []
    for (first_name, last_name), cats in owners_dict.items():
        # Формируем строку с информацией о котах
        cats_info = []
        for cat_name, age in cats:
            cats_info.append(f"{cat_name}, {age}")

        # Добавляем строку для текущего владельца
        result_lines.append(f"{first_name} {last_name}: {'; '.join(cats_info)}")

    # Объединяем все строки с переносами
    return '\n'.join(result_lines)


#o1 = dict.fromkeys(['а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т'], 1)
#o2 = dict.fromkeys(['д', 'к', 'л', 'м', 'п', 'у'], 2)
#o3 = dict.fromkeys(['б', 'г', 'ь', 'я'], 3)
#o4 = dict.fromkeys(['й', 'ы'], 4)
#o5 = dict.fromkeys(['ж', 'з', 'х', 'ц', 'ч'], 5)
#o8 = dict.fromkeys(['ф', 'ш', 'э', 'ю'], 8)
#o10 = dict.fromkeys(['щ'], 10)
#o15 = dict.fromkeys(['ъ'], 15)
#o_all = {**o1, **o2, **o3, **o4, **o5, **o8, **o10, **o15}
#print(o_all)
#
#s = 'струт'
#l = list(s)
#w = 0
#print(l)
#for i in range(len(l)):
#    f = l[i]
#    w += int(o_all[f])
#print(w)