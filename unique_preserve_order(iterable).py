def unique_preserve_order(iterable) -> list:
    '''Удаляет дубликаты с сохранением порядка элементов'''
    from collections.abc import Iterable
    if not isinstance(iterable, Iterable):
        raise Exception('Bad input')
    processed = set()   # проверка на наличие элемента в set() будет быстрее, чем проверка в результирующем list(), 
                        # потому что поиск в set'е реализуется через хеш-таблицу, а не итеративно
    res = []
    for elem in iterable:
        if elem not in processed:
            res.append(elem)
            processed.add(elem)
    return res

# Использование
data = [5,5,8,3,1,2,2,50,100,3]
print(unique_preserve_order(data))  # [5, 8, 3, 1, 2, 50, 100]