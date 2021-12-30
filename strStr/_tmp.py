
candidates = [2,3,9,234]
candidates_set = set(candidates)

def candidate_factorize(candidates, quotient, factors=None, factor_detected=True):
    if factors is None:
        factors = []

    for candidate in candidates:
        if quotient % candidate == 0:
            factors.append(candidate)
            candidate_factorize(candidates, quotient/candidate, factors=factors, factor_detected=True)
            return

    # return all factors + result to save timevbv
    factors.append(n)
    return factors

print(candidate_factorize(candidates,82))