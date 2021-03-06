# simple tools to time algorithm execution and verify output

import math
from timeit import timeit
import itertools
import copy


# python does a little of this with scientific notation but I like the unit notation
# standard time modules are a little frustrating, strftime() being the only thing coming close
# this was really fun to code. 
def format_time(duration: float, precision=5):
    """converts timeit output to SI (and sanctioned non-SI) units

    Args:
        duration (float): to convert
        precision (int): digits to round to

    Returns:
        str: (d* hh mm ss)|(ms|μs|...|ys)
    """
    if duration == 0.0: return '0.0s'

    # switch from SI units for large values. it's not a seamless transition
    # divmod preserves duration's type,
    # annoyingly necessitating casting floats already equal to ints
    if duration >= 60:
        time_str = ''
        if duration >= 3600:
            if duration >= 86400:
                days, duration = divmod(duration, 86400)
                time_str += f"{int(days)}d "
            hours, duration = divmod(duration, 3600)
            time_str += f"{int(hours)}h "
        minutes, seconds = divmod(duration, 60)
        time_str += f'{int(minutes)}m {round(seconds, precision)}s'
        return time_str

    duration_digits = math.log(duration, 10)

    magnitude = math.floor(duration_digits)
    magnitude -= magnitude % 3 # comes from log(1000,10)

    # packing -precision inside abs fixes the case where 1 <= duration < 60
    rounding_digits = abs(math.ceil(duration_digits) - precision) + magnitude

    # this would probably be faster with structural pattern matching
    magnitudes = {0:'s', -3:'ms', -6:'μs', -9:'ns', -12:'ps', -15:'fs', -18:'as', -21:'zs', -24:'ys'}
    unit = magnitudes[magnitude]

    return str(round(duration * 10**-magnitude, rounding_digits)) + unit


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

    Time: O(loops)
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
                    print(f"function {fn.__name__}: Passed")
                else:
                    print(f"function {fn.__name__}: Failed.",
                          f"Expected {repr(classifier)}: {type(classifier)}")
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

            duration = format_time(timeit(timeit_statement, globals=timeit_namespace, number=loops))
            print(f"    Time over {loops} iteration{suffix}: {duration}")
        return duration
    return inner


# i'm feeling like an interface between calling and executing could remove duplicate code,
# or at least make it more readable.
# checking skip_print/unpack_data only needs to happen once, but it'd bloat this whale of a function even harder
# TODO: timeit.Timer().autorange enables loops=None, dropping the param entirely
# it's O(data), but because the function is O(data*fns*log(fns)*loops), it's basically nothing
def batch(fns, args, classifiers=None, loops=100000, skip_print=False, nested_args=True):
    """prints function(s) output and runtime over args 

    Args:
        fns (Option[iterable[function], function]): to evaluate
        args (iterable): of points as function arg(s)
        classifiers (iterable): to verify fn output correctness.
            type(args[i]) = type(classifiers[i]).
            len(classifiers) = len(args). Defaults to None
        loops (int, optional): for runtime calc,
            per function per arg. Defaults to 100000.
        skip_print (bool, optional): ing output? Defaults to False.
        unpack_args (bool, optional): TODO

    Time: O(args*fns*log(fns)*loops)

    Returns: results: list[tuple(   args[i], [result,fn,output,correctness]   )]
    """
    # support for evaluating a single function/method
    # i prefer it to batch(*fns, args=None, ...) because args isn't optional,
    # and i think it's more intuitive than batch(args, *fns, ...).
    # i might change this, but i settled on this after awhile
    if callable(fns):
        fns = [fns]

    # many algs will mutate input in-place,
    # preserving a copy helps print output, and lets us mutate data
    # just packing everything in a compound data type rather than perform tedious islices
    if not nested_args:
        data = [[elem] for elem in args]
    else:
        data = copy.deepcopy(args)

    if not skip_print:
        suffix = 's' if loops > 1 else ''
        print(f"\nRuntimes over {loops} loop{suffix}: ")

    results = []
    # categorize the results by datapoint instead of by function
    # makes comparing algorithm efficiency much smoother
    if classifiers is not None:
        for point, classifier in zip(data, classifiers, strict=True):
            point_results = []

            # do this before timing; point might be mutated
            if not skip_print:
                print(f"    Point {repr(point)}: {type(point)}:")

            for fn in fns:
                # store fn(point) outside of timeit
                output = fn(*point)
                # here's the execution
                duration = timeit("fn(*point)", number=loops, globals={"fn":fn, "point":point})
                fn_result = (duration, fn.__name__, output, output == classifier)
                point_results.append(fn_result)

            # printing the output
            if not skip_print:

                for duration, fn_name, output, correctness in sorted(point_results):
                    individual = format_time(duration/loops)
                    duration = format_time(duration)

                    if correctness:
                        print(f"        Function {fn_name} ***Passed*** in {individual}/loop ({duration}):\n",
                        f"           Received {output}: {type(output)}")
                    else:
                        print(f"        Function {fn_name} ***Failed*** in {individual}/loop ({duration}):\n",
                        f"           Received {output}: {type(output)}\n",
                        f"           Expected {classifier}: {type(classifier)}")

            results.append( (point, point_results) )

    # same as above but without classification
    else:
        for point in data:
            point_results = []
            for fn in fns:
                # timeit_statement = f"{fn.__name__}(*_{hex(id(point))})"
                output = fn(*point)
                duration = timeit("fn(*point)", number=loops, globals={"fn":fn, "point":point})
                fn_result = (duration, fn.__name__, output)
                point_results.append(fn_result)

            if not skip_print:
                print(f"    Point {repr(point)}:")
                for duration, fn_name, output in point_results:
                    print(f"        {fn_name} yielded {output} in {format_time(duration)}")

            results.append( (point, point_results) )

    return results


# timeit operates in its own namespace. this is a huge
# (but necessary) headache for timing accuracy,
# but you can import another namespace with its globals param.
# this requires all calling functions to import their globals() as an arg.
# i've circumvented this by making a dict to pass as a namespace to timeit.
# it's maybe easier to conceptualize this as timeit's __init__ method?

# a previous version used timeit's setup param to import calling modules
# into timeit's namespace by examining the stack.
# that ended up being really slow, and it required calling modules
# to hide code behind "if __name__ == '__main__'" statements anyway.
# i think, ideally, timeit could just pull vars from memory with
# memoryview() or some ctypes pointer tricks
