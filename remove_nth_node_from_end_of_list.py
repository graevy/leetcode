# 19. Remove Nth Node From End of List
# Medium

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:

# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:

# Input: head = [1], n = 1
# Output: []

# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

 

# Constraints:

#     The number of nodes in the list is sz.
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz

 

# Follow up: Could you do this in one pass?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # banged this out. doesn't bounds-check. immediately decided to extend the ListNode class instead
    def removeNthFromEnd(self, head, n: int):
        res = head
        stack = []
        while head:
            stack.append(head)
            head = head.next
        stack[-(n+1)].next = stack[-(n-1)]
        return res

    # proper breadcrumbs strategy
    def better(self, head, n):
        prev = None
        current = head

        # in a single pass, traverse the list and drop the crumbs
        while current:
            current.prev = prev
            prev = current
            current = current.next

        # walk back and excise the target node
        for _ in range(n):
            current = current.prev

        current.prev.next = current.next

        return head

    # O(sz) space could be improved on with a queue of length n
    def queue(self, head, n):

        from collections import deque

        q = deque()
        # to excise the nth-from-last node, we need to get the node before it
        # if n == 1, and the linked list is [5,6,7,8,9],
        # 8 needs to be removed by setting 7.next to 9, meaning we need to view 3 = n + 2 entries
        nplus2 = n + 2
        prev = None
        current = head

        while current:
            current.prev = prev
            q.append(current)
            if len(q) > nplus2:
                q.popleft()
            prev = current
            current = current.next

        # horrifying
        q.popleft().next = q.popleft().next

        return head


import linkedlist
import timing

l = linkedlist.list_to_linked([5,8,23,34,2,7,8])
timing.batch(Solution().queue, [[l,2]])