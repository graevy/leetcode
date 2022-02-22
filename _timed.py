# simple tools to time algorithm execution and verify output

from timeit import timeit


# python does a little of this with scientific notation but I like the unit notation
def format_duration(duration: float):
    """converts float timing data to SI units

    Args:
        duration (float): to convert

    Returns:
        str: duration in SI units
    """
    if duration > 60.0:
        mins, seconds = divmod(f, 60.0)
        return f"{mins}m {round(seconds)}s"
    if duration * 10**6 < 1.0:
            if duration * 10**9 < 1.0:
                return f"{duration * 10**12}ps"
        return f"{duration * 10**9}ns"
    if duration * 10**3 < 1.0:
        return f"{duration * 10**6}μs"
    if duration < 1.0:
        return f"{duration * 10**3}ms"
    return f"{duration}s"


# this has become more useful than batch
# still best to use batch for bulk comparisons
def timed(fn):
    """timeit decorator wrapper

    RESERVED KWARGS:
    loops (int, for timeit loops),
    skip_print (bool, to skip console output), 
    classify, and classifier (bool and any, to check output against)

    Args:
        fn (function): to time

    Runtime: O(loops)
    """
    def inner(*args, loops=100000, skip_print=False, classify=False, classifier=None, **kwargs):
        # see timeit_namespace explanation at end of file
        timeit_namespace = {fn.__name__:fn, 'args':args, 'kwargs':kwargs}
        # timeit basically does exec(timeit_statement)
        timeit_statement = fn.__name__+"(*args, **kwargs)"

        # begin printing
        if not skip_print:
            # run function once for output
            output = fn(*args, **kwargs)

            # checking correctness. i opted for 2 vars incase output is None, False, etc
            if classify:
                if output == classifier:
                    print(f"function {fn.__name__}: SUCCESS")
                else:
                    print(f"function {fn.__name__}: FAILURE. "+\
                          f"Expected type {type(classifier)}: {repr(classifier)}")
            else:
                print(f"function {fn.__name__}:")

            # sometimes the output is too verbose for my terminal, so i cut it off here
            param_str = repr(list(args) + list(kwargs.items()))
            if len(param_str) > 50:
                print(f"    Input:     {param_str[:50]} ...")
            else:
                print(f"    Input:     {param_str}")

            output = repr(output)
            if len(output) > 50:
                print(f"    Output:    {output[:50]} ...")
            else:
                print(f"    Output:    {output}")

            # print the (rounded) time
            suffix = 's' if loops != 1 else ''

            duration = format_duration(timeit(timeit_statement, globals=timeit_namespace, number=loops))
            print(f"    Execution time over {loops} iteration{suffix}: {duration}s")
        return duration
    return inner


def batch(data, fns, loops=100000, skip_print=False, classify=False, classifiers=None, unpack_data=False):
    """prints function(s) output and runtime over datapoints 

    Args:
        data (list): of points as function input
        fns (iterable[function]): to evaluate
        loops (int, optional): of iterations (for runtime calc)
                           per datapoint per function. Defaults to 100000.
        skip_print (bool, optional): skip printing output? Defaults to False.
        classify (bool, optional): check output correctness against
                            the last member of each data point? Defaults to false.
        unpack_data (bool, optional): for fn(*point) instead of fn(point)

    Runtime: O(data*fns*loops)
    """
    # see timeit_namespace explanation at end of file
    timeit_namespace = {fn.__name__:fn for fn in fns}

    results = []
    # categorize the results by datapoint instead of by function
    # makes comparing algorithm efficiency much smoother
    for point in data:
        point_results = []

        # checking classify/unpack_data only needs to happen once, but it would duplicate so much code
        if classify:
            for fn, classifier in zip(fns, classifiers, strict=True):
                # timeit basically runs exec(timeit_statement)
                if not unpack_data:
                    timeit_statement = f"{fn.__name__}({repr(point)})"
                else:
                    timeit_statement = f"{fn.__name__}(*{repr(point)}"
                # this is where the calculation actually happens
                duration = format_duration(timeit(timeit_statement, number=loops, globals=timeit_namespace))
                # to get the function output, just run it again
                # not ideal for slow algs.
                output = fn(point)
                fn_result = [duration, fn.__name__, output, output == classifier]
                point_results.append(fn_result)

        # same as above minus output == classifier in fn_result
        else:
            for fn in fns:
                timeit_statement = f"{fn.__name__}(*{repr(point)}" if unpack_data else f"{fn.__name__}({repr(point)})"
                duration = format_duration(timeit(timeit_statement, number=loops, globals=timeit_namespace))
                point_results.append([duration, fn.__name__, fn(point)])

        # (sorted by duration)
        results.append( (point, sorted(point_results)) )

        # printing the output
        if not skip_print:
            suffix = 's' if loops != 1 else ''
            print(f"Runtimes for datapoint {point} over {loops} iteration{suffix}:")
            if classify:
                # key sorts by the last element (correctness) instead of the first (duration)
                for duration, fn_name, output, correctness in sorted(point_results, key=lambda x: x[-1], reverse=True):
                    print(f"    {correctness}: {fn_name} yielded {output} in {duration} seconds")
            else:
                for duration, fn_name, output in point_results:
                    print(f"    {fn_name} yielded {output} in {duration} seconds")

    return results


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
# i think, ideally, timeit could just pull vars from memory with
# memoryview() or some ctypes pointer tricks
