# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500


def solve(target, candidates):
    result = []
    candidates.sort()
    def dfs(remainder, stack):
        # if this condition is met, stack sums up to target
        if remainder == 0:
            result.append(stack)
            return

        # this for loop does all the work
        for candidate in candidates:
            # if candidate > remainder, stack + [candidate] > target; the loop can be broken because candidates is sorted
            if candidate > remainder:
                break
            # if stack is empty, we can shortcut checking candidate < stack[-1] and go straight to dfs. we also know there is a stack[-1]
            # if candidate < stack[-1], it's already been visited, because candidates is sorted
            if stack and candidate < stack[-1]:
                continue
            else:
                dfs(remainder-candidate, stack + [candidate])

    dfs(target,[])
    return result

print(solve(13,[2,3,4]))


# notes
# i used 3 examples for determining algorithm success. 7 as a target is basic, and 10 has slight variations.
# 13 is complex, with solutions involving 3 separate candidates:

# 1: 7, [2,3]     -> [[2,2,3]]
# 2: 10, [2,3]    -> [[2,2,2,2,2],[2,2,3,3]]
# 3: 13, [2,3,4]. -> [[2,2,2,2,2,3],[2,2,3,3,3],[3,3,3,4],[2,2,2,3,4],[2,3,4,4]]

# first solution was linearithmic for case 1:
# 1. search for combinations via target % candidate
# 2. subtract a candidate from target. save it to a list. search again, appending that list to each hit
# 3. repeat until candidates empty

# it failed case 2, and couldn't touch case 3. eventually i realized modulo couldn't solve most cases
# i implemented a quadratic? recursion algorithm