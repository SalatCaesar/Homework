# Можно улучшить:
# 1. Добавить инпут, а потом создать из этого кортеж

def treatment_sum(our_tuple):
    try:
        if len(our_tuple) > 2:
            raise Exception ('Много данных')
        result = our_tuple[0] + our_tuple[1]
        return result
    except TypeError:
        return 'Нельзя сложить эти данные'
    except IndexError:
        return 'Недостаточно данных'

