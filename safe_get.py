'''Safe get: Напишите функцию safe_get(d, path, default=None) 
которая возвращает d[a][b][c]... по списку ключей path, не кидая исключение при отсутствии.'''

def safe_get(d: dict, path: list, default=None):
    cur = d
    for key in path:
        if not isinstance(cur, dict) or key not in cur.keys():
            return default
        cur = cur[key]
    return cur

# print(safe_get({'a': {'b': 3}}, ['a', 'b']))
# 3

# print(safe_get({'a': {'b': [1,1]}}, ['a', 'b']))
# [1, 1]

# print(safe_get({'a': {'b': [1,1]}}, ['a', 'b', 'c']))
# None