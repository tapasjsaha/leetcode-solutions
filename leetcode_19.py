# Remove Nth Node From End of List
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
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        fast = head
        cnt = 1
        while fast.next:
            cnt += 1
            fast = fast.next
        if cnt == n:
            head = head.next
        else:
            fast = slow = head
            for i in range(n):
                fast = fast.next
            while fast.next:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
        return head


head = createLLFromList([1])
printList(head)
s = Solution()
head1 = s.removeNthFromEnd(head, n=1)
printList(head1) if head1 is not None else print("List is empty")



head = createLLFromList([1, 2, 3, 4, 5])
printList(head)
s = Solution()
head1 = s.removeNthFromEnd(head, n=2)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([1, 2, 3])
printList(head)
s = Solution()
head1 = s.removeNthFromEnd(head, n=1)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([1, 2, 3, 4, 5])
printList(head)
s = Solution()
head1 = s.removeNthFromEnd(head, n=5)
printList(head1) if head1 is not None else print("List is empty")

