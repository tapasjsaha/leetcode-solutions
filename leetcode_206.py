# Reverse Linked List
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
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            fast, slow = head.next, None
            while head.next:
                head.next = slow
                slow = head
                head = fast
                fast = fast.next
            head.next = slow
        return head


#head = createLLFromList([1, 2, 3])
head = createLLFromList([1, 2, 3, 4, 5, 6, 7])
printList(head)
s = Solution()
head1 = s.reverseList(head)
printList(head1) if head1 is not None else print("List is empty")


"""
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            fast, newhead, slow = head.next, head, None
            while newhead.next:
                newhead.next = slow
                slow = newhead
                newhead = fast
                fast = fast.next
            newhead.next = slow
        return newhead
"""