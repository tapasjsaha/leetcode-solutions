# Rotate List

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


class Solution:
    def rotateRight(self, head: [ListNode], k: int) -> [ListNode]:
        start, n = head, 0
        while start:
            n += 1
            start = start.next
        if n == 0:
            return head
        else:
            k = k % n
            if k == 0:
                return head
            else:
                fast = head
                for _ in range(k):
                    fast = fast.next
                slow = head
                while fast.next:
                    fast = fast.next
                    slow = slow.next
                fast.next = head
                head = slow.next
                slow.next = None
                return head



l1 = createLLFromList([1, 2, 3, 4, 5, 6, 7, 8])
l2 = createLLFromList([1, 2, 3, 4])
l3 = createLLFromList([])
printList(l1)
printList(l2)
printList(l3)
s = Solution()
head=s.rotateRight(l1, k=3)
printList(head)
head = s.rotateRight(l2, k=1)
printList(head)
head = s.rotateRight(l3, k=4)
printList(head)

l2 = createLLFromList([1, 2, 3, 4])
printList(l2)
head = s.rotateRight(l2, k=4)
printList(head)

l2 = createLLFromList([1, 2, 3, 4])
printList(l2)
head = s.rotateRight(l2, k=6)
printList(head)

l2 = createLLFromList([1, 2, 3, 4])
printList(l2)
head = s.rotateRight(l2, k=0)
printList(head)