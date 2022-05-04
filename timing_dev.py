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

    # categorize the results by datapoint instead of by function
    # this simplifies comparing algorithm runtime, and neatens classification
    res = []
    for point in data:
        point_res = []
        for fn in fns:
            # store result outside of timeit
            output = fn(*point)
            # bulk of the runtime
            duration = timeit("fn(*point)", number=loops,
                globals={"fn":fn, "point":point})
            fn_res = [duration, fn, output]
            point_res.append(fn_res)
        res.append(point_res)
        # res is e.g. [['212.053ns', quicksort, [1,3,5,8]], ['253.782ns', failsort, [1,5,3,8]]]

    # TODO: combine this loop with the printing loop?
    # the whole flow of control with these loops and classifiers is pretty garbage
    # i'm thinking this function is a good target for OOP -- point could just be a class
    if classifiers is not None:
        if len(args) != len(classifiers):
            raise Exception("len(args) != len(classifiers)")

        for idx, (_,_,output) in enumerate(res):
            res[idx].append(output == classifiers[idx])

    if not skip_print:
        suffix = 's' if loops > 1 else ''
        print(f"\nRuntimes over {loops} loop{suffix}: ")

        for idx, point_res in enumerate(res):
            if classifiers is not None:
                duration, fn, output = point_res
            else:
                duration, fn, output, success = point_res

            input = args[idx]
            print(f"    Point {repr(input)}: {type(input)}:")

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

    return res
