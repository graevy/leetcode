class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked(l):
    previous = None
    for elem in reversed(l):
        elem = ListNode(elem, previous)
        previous = elem
    return previous