# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_01():
    assert all_division(10, 2, 5, 2) == 0.5

@pytest.mark.acceptance
def test_02():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 2, 1, 0)

@pytest.mark.acceptance
def test_03():
    with pytest.raises(TypeError):
        all_division(3, 2, 's')

def test_04():
    assert all_division(-1, 5, -1, -1) == -0.2

def test_05():
    assert all_division(5) == 5