import pytest
import task_2


@pytest.mark.smoke
def test_01():
    assert task_2.all_division(10, 2, 5, 2) == 0.5

@pytest.mark.acceptance
def test_02():
    with pytest.raises(ZeroDivisionError):
        task_2.all_division(1, 2, 1, 0)

@pytest.mark.acceptance
def test_03():
    with pytest.raises(TypeError):
        task_2.all_division(3, 2, 's')

def test_04():
    assert task_2.all_division(-1, 5, -1, -1) == -0.2

def test_05():
    assert task_2.all_division(5) == 5



