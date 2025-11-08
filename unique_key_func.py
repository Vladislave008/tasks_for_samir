'''Реализуйте unique_by(iterable, key) — возвращает элементы, уникальные по key-функции, сохраняя порядок.'''

def unique_by(iterable, key):
    seen = set()
    for elem in iterable:
        if key(elem) not in seen:
            yield elem
            seen.add(key(elem))
            
# for elem in unique_by([{"id": 1}, {"id": 2}, {"id": 1}], lambda x: x["id"]): print(elem)
# {'id': 1}
# {'id': 2}