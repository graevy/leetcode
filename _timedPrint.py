from timeit import timeit


# you'll want to read the timeit.timeit documentation before reading this file

# TODO: optionally check outputs against a correct output?
# TODO: support for functions with more than 1 param, or class obj params
# (add class obj params to timeitNamespace)
def timedPrint(data, *funcs, n=10000):
    """prints function(s) output and runtime over datapoints 

    Args:
        data (iterable): a container of data
        *funcs (tuple): functions to check for datapoints with
        n (int, optional): number of iterations (for runtime calc)
                           per datapoint per function. Defaults to 10000.
    """
    suffix = '' if n==1 else 's'

    # see timeitNamespace explanation at end of file
    timeitNamespace = {}
    for func in funcs:
        timeitNamespace[func.__name__] = func

    for point in data:
        results = []
        print(f"Runtimes for datapoint {point} over {n} iteration{suffix}:")

        # the timing process, saving all output
        for func in funcs:
            # timeit basically runs exec(timeitStatement)
            timeitStatement = f"{func.__name__}({repr(point)})"
            duration = timeit(timeitStatement, number=n, globals=timeitNamespace)
            duration = round(duration, 5)
            results.append((duration, func.__name__, func(point)))

        # formatting and sorting the output
        for duration, funcName, output in sorted(results):
            print(f"    {funcName} yielded {output} in {duration} seconds")

    return results


# this might benefit from a number kwarg for timeit looping,
# but it's meant for short and presumably fast snippets
def timed(func):
    """decorator wrapper for timing function runtime in-file

    Args:
        func (function): to time
    """
    def inner(*args, **kwargs):
        # see timeitNamespace explanation at end of file
        timeitNamespace = {}
        timeitNamespace[func.__name__] = func
        timeitNamespace['args'] = args
        timeitNamespace['kwargs'] = kwargs
        # timeit basically runs exec(timeitStatement)
        timeitStatement = func.__name__+"(*args, **kwargs)"

        # begin printing
        # TODO: if i ever check correctness, it should be printed here
        print(f"Function {func.__name__}:")

        # sometimes the i/o is too verbose for my terminal, so i cut it off
        argList = str(list(args) + list(kwargs.items()))
        if len(argList) > 50:
            print(f"    Input:    {argList[:50]} ...")
        else:
            print(f"    Input:    {argList}")

        output = str(func(*args, **kwargs))
        if len(output) > 50:
            print(f"    Output:    {output[:50]} ...")
        else:
            print(f"    Output:    {output}")

        # print the (rounded) time
        print(f"""    Relative execution time: {
            round(timeit(timeitStatement, globals=timeitNamespace), 5)
            }""")

    return inner

# timeit operates in its own namespace. this is a huge
# (but necessary) headache to achieve greater timing accuracy.
# but you can import another namespace with its globals() param.
# this requires all calling functions to import their globals() as an arg.
# i've circumvented this by making a dict to pass as a namespace to timeit.
# it's maybe easier to conceptualize this as timeit's __init__ method

# a previous version used timeit's setup param to import calling modules
# into timeit's namespace by examining the stack.
# that ended up being really slow, and it required calling modules
# to hide code behind "if __name__ == '__main__'" statements anyway.
# i think, ideally, timeit could just pull functions from memory with
# memoryview() tricks, but i don't think that's universally reproducible.
