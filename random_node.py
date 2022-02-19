import random


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    def __iter__(self):
        yield self.next

class Solution:
    def __init__(self, head):
        self.head = head
    def solve(self):
        selection = None
        for idx,elem in enumerate(head,start=1)
            if random.uniform(0,idx) < 1:
                selection = elem
        return selection