from timeit import timeit
import inspect

# def printall(data, *funcs):
#     for func in funcs:
#         print(func.__name__)
#         for point in data:
#             print(f"{point}: {func(point)}")
#         print("")
#     print("")


# TODO: optionally check outputs against a correct function?
def timedPrint(data, *funcs, n=1000):
    """prints function(s) output and runtime over datapoints 

    Args:
        data (iterable): a container of data
        n (int, optional): number of iterations (for runtime calc) per datapoint per function. Defaults to 1.
    """
    suffix = '' if n==1 else 's'

    # this is a pretty weird portion
    # so, timeit operates in its own namespace unless you pass
    # another namespace into it via its globals parameter. this is awkward
    # (all function calls to timedPrint would have to have globals=globals() as a kwarg)
    # instead, inspecting the stack frames can get you the module name,
    # and timeit can import the calling module with its setup parameter.
    # inspect.stack() output was changed in python 3.5
    # if this function ever breaks, changed output is probably why

    # inspect.stack()[1] is the FrameInfo object of the calling function,
    # inspect.stack()[1][1] is the file path of the module containing that function
    filePathOfCallingModuleFunction = inspect.stack()[1][1]
    moduleName = inspect.getmodulename(filePathOfCallingModuleFunction)

    setup = f"import {moduleName}"

    for point in data:
        results = []
        print(f"Runtimes for datapoint {point} over {n} iteration{suffix}:")

        for func in funcs:
            statement = f"{moduleName}.{func.__name__}({repr(point)})"
            duration = timeit(stmt=statement, setup=setup, number=n)

            results.append((duration, func.__name__, func(point)))

        for duration, funcName, output in sorted(results):
            print(f"    {funcName} yielded {output} in {duration} seconds")




# if returnOutput:
#     points = {}
#     for point in data:
#         points[point] = {}
#         for func in funcs:
#             statement = f"{moduleName}.{func.__name__}({point})"
#             duration = timeit(stmt=statement, setup=setup, number=n)
#             points[point][func] = duration
#     return points
# else:
#     for point in data:
#         print(f"Runtimes for {point} over {n} iteration{suffix}:")
#         results = []
#         for func in funcs:
#             statement = f"{moduleName}.{func.__name__}({point})"
#             duration = timeit(stmt=statement, setup=setup, number=n)
#             results.append((duration, func.__name__, func(point)))
#         for duration, funcName, output in sorted(results):
#             print(f"    {funcName} yielded {output} in {duration} seconds")
