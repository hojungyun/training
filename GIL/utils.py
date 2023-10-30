import os
import threading
from functools import wraps
import time


def timeit(fn):
    @wraps(fn)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"{fn.__name__=} {args=} {kwargs=} took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


def cpu_bound_fn(num):
    print(f"{os.getpid()=} | {threading.get_ident()=}")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total
