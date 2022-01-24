from typing import Optional


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# second try. first shot would accidentally drop remainders
# the looping slows it down a lot, but it scales well
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        remainder = 0
        threads = [l1,l2]

        while threads or remainder == 1:
            remainder, digit = divmod(sum(node.val for node in threads) + remainder, 10)
            result.append(ListNode(digit))

            threads = [node for node in threads if node.next is not None]
            threads = [node.next for node in threads]

        previous = None
        for node in result[::-1]:
            node.next = previous
            previous = node

        return result[0]

def make_linked_list(l: list):
    previous = None
    for idx,elem in enumerate(l[::-1]):
        l[idx] = ListNode(elem)
        l[idx].next = previous
        previous = l[idx]
    return l[::-1]

# x = make_linked_list([3,0,7])
# y = make_linked_list([5,8,9,2,4])
# print(Solution().addTwoNumbers(l1=x[0],l2=y[0]))

# a = make_linked_list([2,4,3])
# b = make_linked_list([5,6,4])
# print(Solution().addTwoNumbers(l1=a[0], l2=b[0]))

a = make_linked_list([9,9,9,9,9,9,9])
b= make_linked_list([9,9,9,9])
print(Solution().addTwoNumbers(l1=a[0], l2=b[0]))