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
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        if head is None:
            return head
        else:
            fast = slow = head
            while fast.next is not None:
                fast = fast.next
                if slow.val == fast.val:
                    slow.next = fast.next
                else:
                    slow = slow.next
        return head


head = createLLFromList([1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7])
printList(head)
s = Solution()
head1 = s.deleteDuplicates(head)
printList(head1) if head1 is not None else print("List is empty")