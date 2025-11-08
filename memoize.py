'''Собственная версия memoize для чистых функций c ограничением размера кэша.'''

import functools

def memoize(cache_size: int):
    def decorator(func):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple(kwargs.items())
            if key in cache:
                return cache[key]
            if len(cache) >= cache_size:
                first_key = next(iter(cache))
                cache.pop(first_key)
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        return wrapper
    return decorator