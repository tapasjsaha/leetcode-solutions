# Swap Nodes in Pairs
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

# Swap Nodes in Pairs
class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return head
        elif head and head.next:
            dummy = ListNode()
            dummy.next = head
            first, second = dummy.next, dummy.next.next
            temp = second.next
            dummy.next = second
            second.next = first
            first.next = self.swapPairs(temp)
            return dummy.next
        else:
            return head

head = createLLFromList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
printList(head)
s = Solution()
head1 = s.swapPairs(head)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([1, 2, 3, 4])
printList(head)
s = Solution()
head1 = s.swapPairs(head)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([])
printList(head)
s = Solution()
head1 = s.swapPairs(head)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([1])
printList(head)
s = Solution()
head1 = s.swapPairs(head)
printList(head1) if head1 is not None else print("List is empty")