'''Напишите декоратор retry_backoff(retries, base_delay) c экспоненциальной паузой base_delay * 2**attempt.'''

import functools
import time

def retry_backoff(retries: int, base_delay: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i == retries - 1:
                        raise
                    time.sleep(base_delay*2**i)
        return wrapper
    return decorator