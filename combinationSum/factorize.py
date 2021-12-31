def str_str(candidates, target):
    if len(candidates) == 0:
        return 0
    out = []
    candidates_set = set(candidates)

def prime_factorize(candidates, n, out=None):
    global candidates_set
    if out is None:
        out = []
    for elem in candidates:
        if type(n/elem) is int and n/elem in candidates_set:
            out.append(elem)
            prime_factorize(n/elem)
    return out

    for elem in candidates:
        if elem > target:
            continue
        if target % elem in candidates_set:
            