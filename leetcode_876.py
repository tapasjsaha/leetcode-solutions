# Middle of the Linked List
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
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        slow_head = fast_head = head
        if slow_head is not None:
            flag = True
            while flag:
                if fast_head.next is not None:
                    fast_head = fast_head.next
                    slow_head = slow_head.next
                else:
                    flag = False
                if fast_head.next is not None:
                    fast_head = fast_head.next
                else:
                    flag = False
        return slow_head


head = createLLFromList([1, 2, 3, 4, 5])
printList(head)
s = Solution()
head1 = s.middleNode(head)
printList(head1) if head1 is not None else print("List is empty")


head = createLLFromList([1, 2, 3, 4, 5, 6])
printList(head)
s = Solution()
head1 = s.middleNode(head)
printList(head1) if head1 is not None else print("List is empty")


head = createLLFromList([1])
printList(head)
s = Solution()
head1 = s.middleNode(head)
printList(head1) if head1 is not None else print("List is empty")