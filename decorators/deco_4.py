def many_runs(runs):
    def run(func):
        def wrapper(*args, **kwargs):
            for _ in range(runs):
                func(*args, **kwargs)
        return wrapper
    return run


@many_runs(5)
def func(*args, **kwargs):
    print(args, kwargs)
    return sum(args)
