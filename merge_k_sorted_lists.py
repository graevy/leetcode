# 23. Merge k Sorted Lists
# Hard

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

 

# Constraints:

#     k == lists.length
#     0 <= k <= 104
#     0 <= lists[i].length <= 500
#     -104 <= lists[i][j] <= 104
#     lists[i] is sorted in ascending order.
#     The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


# first actual leetcode hard submission!
# this was the most annoying thing in the world to solve, because i wrote the alg in about 5 minutes
# but the empty list return cases kept ruining the submissions, i think like 4 times? fool me once...
# this is a misclassified medium problem complicated by the fact that
# leetcode's python linked list implementation is really vague.
# the method parameter type hint uses capitalises list, typeerroring by default...

# you'd think (if n=m*k) it's a brute linearithmic alg.
# but python's default sorting algorithm is tim peters' timsort, the quicksort alg optimized for
# pre-sorted data runs, which is just the contents of each sorted linked list in order
# so it becomes linear for small k. accordingly this was 60th percentile in speed and 90th in memory
# without timsort, to achieve O(n), i'd have to maintain some list metadata,
# to take advantage of linked list constant insertion speed.
# probably why it's great on memory and medium on speed?
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # first, flatten all the linked lists, preserving sorting heaps(?)
        res = []
        for l in lists:
            while l:
                res.append(l)
                l = l.next
        res.sort(key=lambda node: node.val)
        # this part attaches the list nodes very elegantly
        previous = None
        for node in reversed(res):
            node.next = previous
            previous = node
        return res[0] if res else None


def to_linked_list(l):
    previous = None
    for elem in reversed(l):
        elem = ListNode(elem)
        elem.next = previous
        previous = elem
    return previous



data =  [
                [[1,2,3],[4,5,6],[7,8,9]],
                [[12,2,4,5],[8,2,5,1,786],[0,-5,8,2,4,7,23,-67,32,754,2,2**50]],
                [[]], []
        ]

data = [[to_linked_list(l) for l in point] for point in data]

results = [Solution().mergeKLists(point) for point in data]
for idx,res in enumerate(results, start=1):
    print(f"result {idx}:")
    while res:
        print(res.val)
        res = res.next