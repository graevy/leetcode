def prime_factorize(candidates, n, out=None):
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
            