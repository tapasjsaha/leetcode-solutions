# Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addNode(self, val):
        a = ListNode(val)
        p = self
        while p.next is not None:
            p = p.next
        p.next = a


class Solution:
    def buildLinkList(self, lst):
        head = ListNode(lst[0])
        for i in lst[1:]:
            head.addNode(i)
        return head


    def getDecimalValue(self, head: ListNode) -> int:
        dec = 0

        while head.next:
            dec = (dec * 2) + head.val
            head = head.next
        dec = (dec * 2) + head.val

        return dec


s = Solution()
head = s.buildLinkList([1, 0, 1, 0, 1, 1])
print(s.getDecimalValue(head))
