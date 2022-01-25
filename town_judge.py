# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

#     The town judge trusts nobody.
#     Everybody (except for the town judge) trusts the town judge.
#     There is exactly one person that satisfies properties 1 and 2.

# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2

# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3

# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1

 

# Constraints:

#     1 <= n <= 1000
#     0 <= trust.length <= 104
#     trust[i].length == 2
#     All the pairs of trust are unique.
#     ai != bi
#     1 <= ai, bi <= n


# this first solution works. it could use less memory without the Person class, or by implementing __slots__
# i ended up not needing to use sets for each person object's trust counts. they could just be integers.
class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n==1 and not trust:
            return 1

        class Person:
            def __init__(self, number: int, trusts: set, trusted_bys: set):
                self.number = number
                self.trusts = trusts
                self.trusted_bys = trusted_bys

        people = {}
        for citizen, trustee in trust:
            if citizen not in people:
                people[citizen] = Person(number=citizen, trusts=set((trustee,)), trusted_bys=set())
            else:
                people[citizen].trusts.add(trustee)
            if trustee not in people:
                people[trustee] = Person(trustee, set(), set((citizen,)))
            else:
                people[trustee].trusted_bys.add(citizen)
        
        potential_judges = []
        for citizen in people.values():
            if len(citizen.trusted_bys) == n - 1:
                if len(citizen.trusts) == 0:
                    potential_judges.append(citizen)
        
        if len(potential_judges) == 1:
            return potential_judges[0].number
        else:
            return -1
