# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('arg1', [pytest.param((1, 2, 5, 7), marks=pytest.mark.smoke), pytest.param((1, -1, 2), marks=pytest.mark.skip('Да кому это нужно')), (0, 2, 4, 5), (1, 's', 2), (1, 0, 5)], ids=['positive', 'NegativeNumber', 'Zero', 'TypeError', 'ZeroDivisionError'])
def test_01(arg1):
    try:
        all_division(*arg1)
    except TypeError as e:
        assert type(e) == TypeError
    except ZeroDivisionError as e:
        assert type(e) == ZeroDivisionError