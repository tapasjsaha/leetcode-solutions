# Merge In Between Linked Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1, a: int, b: int, list2):
        res = list1
        i, ath, bth = 0, res, res
        while i < a-1:
            ath = ath.next
            i += 1
        i = 0
        while i < b:
            bth = bth.next
            i += 1
        ath.next = list2
        while ath.next:
            ath = ath.next
        ath.next = bth.next
        return res


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLLFromList(lst):
    if lst:
        anode = ListNode(val=lst[0])
        head = anode
        p = head
        for l in lst[1:]:
            anode = ListNode(val=l)
            p.next = anode
            p = p.next
        return head
    else:
        return None


def printList(head):
    if head is None:
        print("List is empty")
    else:
        p = head
        while p.next:
            print(p.val, "--> " if p.next is not None else "", end="")
            p = p.next
        print(p.val)


list1 = createLLFromList([0, 1, 2, 3, 4, 5])
list2 = createLLFromList([1000000, 1000001, 1000002])
printList(list1)
printList(list2)
s = Solution()
head1 = s.mergeInBetween(list1, 3, 4, list2)
printList(head1) if head1 is not None else print("List is empty")
