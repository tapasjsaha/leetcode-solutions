# Merge Two Sorted Lists
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
    def mergeTwoLists(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        head = ListNode()
        temp = head
        while True:
            if not l1 and not l2:
                break
            elif not l1 and l2:
                head.next = l2
                break
            elif l1 and not l2:
                head.next = l1
                break
            else:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next
        return temp.next


l1 = createLLFromList([1, 2, 4, 6])
printList(l1)
l2 = createLLFromList([2, 3, 4, 5, 7])
printList(l2)
s = Solution()
head1 = s.mergeTwoLists(l1, l2)
printList(head1) if head1 is not None else print("List is empty")

print("----------------------------------------------------------------")

l1 = createLLFromList([1, 2, 4, 6])
printList(l1)
l2 = createLLFromList([])
printList(l2)
s = Solution()
head1 = s.mergeTwoLists(l1, l2)
printList(head1) if head1 is not None else print("List is empty")

print("----------------------------------------------------------------")

l1 = createLLFromList([])
printList(l1)
l2 = createLLFromList([2, 3, 4, 5, 7])
printList(l2)
s = Solution()
head1 = s.mergeTwoLists(l1, l2)
printList(head1) if head1 is not None else print("List is empty")

print("----------------------------------------------------------------")

l1 = createLLFromList([])
printList(l1)
l2 = createLLFromList([])
printList(l2)
s = Solution()
head1 = s.mergeTwoLists(l1, l2)
printList(head1) if head1 is not None else print("List is empty")
