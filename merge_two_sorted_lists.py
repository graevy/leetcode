# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# totally misread this problem, built a list instead of a linked list
# oh well. this thing is pretty fast but ugly. no compound conditionals.
# i wonder what the time savings is on that
class Solution:
    def mergeTwoLists(self, list1, list2):

        res = []

        def exhaust_linked_list(to_exhaust, output=res):
            while to_exhaust is not None:
                output.append(to_exhaust.val)
                to_exhaust = to_exhaust.next

        # this is basically all setup code, ensuring that both lists are actually populated
        # and creating the big,small vars
        if list1:
            if list2:
                if list1.val >= list2.val:
                    big, small = list1, list2
                else:
                    big, small = list2, list1
            else:
                exhaust_linked_list(list1)
        elif list2:
            exhaust_linked_list(list2)
        else:
            return res

        while True:
            if small is None:

                if big is None:
                    return res

                exhaust_linked_list(big)
                return res

            elif big is None:
                exhaust_linked_list(small)

            if small.val > big.val:
                small, big = big, small

            res.append(small.val)
            small = small.next


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

a = list_to_linked([1,3,5,7,50])
b = list_to_linked([0,2,4,6])
c = ListNode()
print(Solution().mergeTwoLists(a,b))