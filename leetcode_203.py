# Remove Linked List Elements
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
    def removeElements(self, head, val: int):
        p = head
        temp = None
        while p is not None:
            if p.val == val:
                if temp is None:
                    p = p.next
                    head = p
                else:
                    p = p.next
                    temp.next = p
            else:
                temp = p
                p = p.next
        return head


head = createLLFromList([6, 6])
printList(head)
s = Solution()
head1 = s.removeElements(head, val=6)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([1, 2, 6, 3, 4, 5, 6, 7, 6])
printList(head)
s = Solution()
head1 = s.removeElements(head, val=6)
printList(head1) if head1 is not None else print("List is empty")


head = createLLFromList([6, 6, 6, 1, 2, 6, 3, 4, 5, 6, 7, 6])
printList(head)
s = Solution()
head1 = s.removeElements(head, val=6)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([])
printList(head)
s = Solution()
head1 = s.removeElements(head, val=6)
printList(head1) if head1 is not None else print("List is empty")


head = createLLFromList([7])
printList(head)
s = Solution()
head1 = s.removeElements(head, val=7)
printList(head1) if head1 is not None else print("List is empty")
