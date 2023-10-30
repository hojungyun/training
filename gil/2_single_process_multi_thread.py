from concurrent.futures import ThreadPoolExecutor
from gil.utils import cpu_bound_fn, timeit

nums = [30] * 100


@timeit
def main():
    executor = ThreadPoolExecutor(max_workers=10)
    result = list(executor.map(cpu_bound_fn, nums))


if __name__ == "__main__":
    main()

"""
...
os.getpid()=74318 | threading.get_ident()=6392344576
os.getpid()=74318 | threading.get_ident()=6325039104
os.getpid()=74318 | threading.get_ident()=6375518208
Function main() {} Took 17.6252 seconds
"""
