import timeit

def printall(data, *funcs):
    for func in funcs:
        print(func.__name__)
        for point in data:
            print(f"{point}: {func(point)}")
        print("")
    print("")

setup = r"""
def printall(data, *funcs):
    for func in funcs:
        for point in data:
            print(f"{point}: {func(point)}")
        print("")
    print("")
    """
main = "printall(data, *funcs)"

def timed(func):
    print(timeit.timeit(stmt=func.__name__, setup="", number=100, globals=globals()))
