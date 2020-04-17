from functools import wraps


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrap


@memo
def fib(n):
    if n <= 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(10))
