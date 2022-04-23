# Intersection of Two Linked Lists
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        if headA is None or headB is None:
            return None
        else:
            d = {}
            nodeA = headA
            while nodeA:
                d[nodeA] = 1
                nodeA = nodeA.next
            nodeB = headB
            while nodeB:
                if nodeB in d:
                    return nodeB
                nodeB = nodeB.next
            return None


s = Solution()
b = ListNode(2)
a = ListNode(1)
a.next = b
print(s.getIntersectionNode(a, b))


