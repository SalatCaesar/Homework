# Можно улучшить:
# 1. Добавить инпут
# 2. Убрать импорт коллекции и сделать через for
# 3. Фамилию и имя переделать что ли
from collections import Counter
class PersonInfo:
    def __init__(self, fio, age, *deps):
        self.fio = fio
        self.age = age
        self.deps = deps
    def short_name(self):
       return f"{self.fio[self.fio.find(' ')+1:]} {self.fio[:1]}."
    def path_deps(self):
        road = self.deps[0]
        for i in self.deps[1:]:
            road += f" --> {i}"
        return road
    def new_salary(self):
        d = sum([i[1] for i in Counter((''.join(self.deps))).most_common(3)])
        salary = 1337 * self.age * d
        return salary
first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
print(PersonInfo.short_name(first_person))
print(PersonInfo.path_deps(first_person))
print(PersonInfo.new_salary(first_person))