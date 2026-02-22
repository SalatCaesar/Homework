import pytest
from datetime import datetime

@pytest.fixture(scope='class')
def data_class():
    print('Дата теста:' + datetime.now().strftime('%d.%m'))


@pytest.fixture(scope='function', autouse=True)
def data_func(request):
    if request.node.fspath.basename == 'test_task_4.py' and request.node.name == 'test_02':
        print('Начало теста:' + datetime.now().strftime('%H:%M:%S'))
    yield
    if request.node.fspath.basename == 'test_task_4.py' and request.node.name == 'test_02':
        print('Конец теста:' + datetime.now().strftime('%H:%M:%S'))
