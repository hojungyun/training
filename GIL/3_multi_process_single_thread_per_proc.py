from concurrent.futures import ProcessPoolExecutor
from utils import cpu_bound_fn, timeit

nums = [30] * 100


@timeit
def main():
    executor = ProcessPoolExecutor(max_workers=10)
    result = list(executor.map(cpu_bound_fn, nums))


if __name__ == "__main__":
    main()

"""
...
os.getpid()=83759 | threading.get_ident()=8474747008
os.getpid()=83756 | threading.get_ident()=8474747008
os.getpid()=83761 | threading.get_ident()=8474747008
Function main() {} Took 2.5419 seconds
"""
