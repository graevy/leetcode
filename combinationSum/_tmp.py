target = 13
candidates = [2,3,4,234]

candidates_copy = candidates.copy()

append_list = []
output = []
while target > min(candidates):
    # for candidate_copy in candidates_copy:
    for candidate in candidates:
        if target % candidate == 0:
            output.append(append_list + [candidate for _ in range(target//candidate)])
        target -= candidate
        append_list.append(candidate)

def recur():
    out=[]
    for candidate in candidates:
        if target % candidate == 0:
            out.append([candidate for _ in range(target//candidate)])




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
#     while target > candidate1:
#         if target % candidate2 == 0:
#             history.append(candidate2)
#             output.append(history)
#             history.clear()
#         else:
#             target -= candidate
#             history.append(candidate)
#     return False


# notes
# i used 3 examples for determining algorithm success. 7 as a target is basic, and 10 has slight variations.
# 13 is complex, with solutions involving 3 separate candidates:

# 1: 7, [2,3]     -> [[2,2,3]]
# 2: 10, [2,3]    -> [[2,2,2,2,2],[2,2,3,3]]
# 3: 13, [2,3,4]. -> [[2,2,2,2,2,3],[2,2,3,3,3],[3,3,3,4],[2,2,2,3,4],[2,3,4,4]]

# the steps of the algorithm
# 1. search for combinations via target % candidate
# 2. subtract a candidate from target. save it to a list. search again, appending that list to each hit
# 3. repeat until candidate empty
# this solution creates lots of duplicate entries