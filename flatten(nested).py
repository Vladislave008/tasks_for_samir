def flatten(nested) -> list:
    from collections.abc import Iterable
    ''' Функция итерируется по всем объектам из nested, \
        углубляясь на уровень ниже при вложенности и поднимаясь назад после окончания вложенности '''
    if not isinstance(nested, Iterable):
        raise Exception('Bad input')
    res = []
    all_iterators = [iter(nested)] # Список итераторов, изначально состоит из итератора на весь nested
    while all_iterators: # До тех пор, пока есть по чему итерироваться
        try:
            iterator = all_iterators[-1] # Работаем с самой глубокой вложенностью на данный момент (крайний итератор)
            cur = next(iterator) 
            if isinstance(cur, Iterable):
                all_iterators.append(iter(cur)) # Попался очередной итерируемый объект
            else:
                res.append(cur) 
        except StopIteration: # Очередной итерируемый объект пройден (генерируется методом __next__ под капотом next'а)
            all_iterators.pop() # Удаляем итератор пройденного объекта, продолжаем работу на крайнем итераторе
    return res

# Примеры использования
nested = (1,2,[3,4],5,[6,7,(8,9,10)])
print(flatten(nested))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(flatten([]))
# []
print(flatten(52))
# Exception: Bad input