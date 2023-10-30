from utils import cpu_bound_fn, timeit

nums = [30] * 100


@timeit
def main():
    result = [cpu_bound_fn(num) for num in nums]


if __name__ == "__main__":
    main()

"""
...
os.getpid()=74219 | threading.get_ident()=8474747008
os.getpid()=74219 | threading.get_ident()=8474747008
os.getpid()=74219 | threading.get_ident()=8474747008
fn.__name__='main' args=() kwargs={} took 17.0262 seconds
"""