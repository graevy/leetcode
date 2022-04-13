def batch(fns, args, classifiers=None, loops=100000, skip_print=False, nested_args=False):
    """prints function(s) output and runtime over args 

    Args:
        fns (Union[iterable[function], function]): to evaluate
        args (Union[list, tuple]): of points as function arg(s)
        classifiers (Union[list, tuple]): to verify fn output correctness.
            type(args[i]) = type(classifiers[i]).
            len(classifiers) = len(args). Defaults to None
        loops (int, optional): for runtime calc,
            per function per arg. Defaults to 100000.
        skip_print (bool, optional): ing output? Defaults to False.
        nested_args (bool, optional): if True, functions unpack arg's elements
            e.g. print([1,2,3]) -> print(*[1,2,3]). Defaults to False.

    Time: O(args*fns*log(fns)*loops)

    Returns: results: TODO [[result,fn,output,correctness]]
    """
    if classifiers is not None:
        if len(args) != len(classifiers):
            raise Exception("len(args) != len(classifiers)")

    # support for evaluating a single function/method
    # i prefer it to batch(*fns, args=None, ...) because args isn't optional,
    # and i think it's more intuitive than batch(args, *fns, ...).
    # i might change this, but i settled on this after awhile
    if callable(fns):
        fns = [fns]

    # many algs will mutate input in-place,
    # preserving an input copy simplifies printing i/o
    # packing args makes for simpler code re:unpacking
    if not nested_args:
        data = [[elem] for elem in args]
    else:
        data = copy.deepcopy(args)

    results = []
    # categorize the results by datapoint instead of by function
    # this simplifies comparing algorithm runtime, and neatens classification
    for idx, point in enumerate(data):
        point_results = []
        for fn in fns:
            # store result outside of timeit
            output = fn(*point)
            # here's the execution
            duration = timeit("fn(*point)", number=loops,
                globals={"fn":fn, "point":point})
            fn_result = [duration, fn, output]
            point_results.append(fn_result)

        results.append( (point, point_results) )

    # TODO: combine this loop with the printing loop?
    if classifiers is not None:
        for idx, point_result in enumerate(results):
            output, classifier = point_result[-1], classifiers[idx]
            point_result.append(output == classifier)

    if not skip_print:
        suffix = 's' if loops > 1 else ''
        print(f"\nRuntimes over {loops} loop{suffix}: ")

        for idx, point_result in enumerate(results):
            input = args[idx]
            print(f"    Point {repr(input)}: {type(input)}:")

            for duration, fn, output in sorted(point_result):
                # individual loop duration
                individual = format_time(duration/loops)
                # total loop duration
                duration = format_time(duration)
                # printing tools
                output_str = f"{output}: {type(output)}"
                header = f"        Function {fn.__name__}"

                if classifiers is not None:
                    classifier = classifiers[idx]

                    if success:
                        print(header, f"***Passed*** in {individual} per loop ({duration}):\n",
                        f"           Received {output_str}")
                    else:
                        print(header, f"***Failed*** in {individual} per loop ({duration}):\n",
                        f"           Received {output_str}\n",
                        f"           Expected {classifier}: {type(classifier)}")
                else:
                    print(header, f"yielded {output_str} in {individual} per loop ({duration})")

    return results