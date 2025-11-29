# Можно улучшить:
# 1. Да вообще нельзя

def memorize(function):
    # todo Здесь нужно написать код
    mem = dict()
    def wrapper(*args):
        if args not in mem:
            mem[args] = function(*args)
        return mem[args], mem
    return wrapper
# todo Здесь ничего изменять не нужно!
@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2)/2