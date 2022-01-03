target = 13
candidates = [2,3,4,234]

candidates_copy = candidates.copy()

append_list = []
output = []
for candidate_copy in candidates_copy:
    for candidate in candidates:
        if target % candidate == 0:
            output.append(append_list + )


# def candidate_factorize(candidates, dividend, factors=None, factor_detected=True):
#     if factors is None:
#         factors = []

#     for candidate in candidates:
#         if dividend % candidate == 0:
#             factors.append(candidate)
#             candidate_factorize(candidates, dividend/candidate, factors=factors, factor_detected=True)
#             return

#     # return all factors + result to save time
#     factors
#     return (factors, dividend)

# def is_factorable(target, candidates):
#     output = []
#     history = []
#     target_to_factor = target
#     while target_to_factor > candidate1:
#         if target_to_factor % candidate2 == 0:
#             history.append(candidate2)
#             output.append(history)
#             history.clear()
#         else:
#             target_to_factor -= candidate
#             history.append(candidate)
#     return False

print(candidate_factorize(candidates,82))

# notes
# i used 3 examples for determining algorithm success:
# 1: 13, [2,3,4]. -> [[2,2,2,2,2,3],[2,2,3,3,3],[3,3,3,4],[2,3,4,4]]
# 2: 7, [2,3]     -> [[2,2,3]]
# 3: 10, [2,5]    -> [[2,2,2,2,2],[5,5]]

# the steps of the algorithm
# 1. search for combinations via target % candidate
# 2. subtract a candidate from target. save it to a list. search again, appending that list to each hit
# 3. repeat until candidate empty