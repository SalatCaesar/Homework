# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
from task_2 import all_division


@pytest.mark.usefixtures('data_class')
class TestTask2:
    def test_01(self):
        assert all_division(10, 2, 5, 2) == 0.5

    def test_02(self):
        with pytest.raises(ZeroDivisionError):
            all_division(1, 2, 1, 0)

    def test_03(self):
        with pytest.raises(TypeError):
            all_division(3, 2, 's')

    def test_04(self):
        assert all_division(-1, 5, -1, -1) == -0.2

    def test_05(self):
        assert all_division(5) == 5