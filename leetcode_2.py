# Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        #res, r, p, q, c = None, None, l1, l2, 0
        p, q, c = l1, l2, 0
        res = ListNode(val=None)
        r = res
        while p or q or c:
            if p:
                c += p.val
                p = p.next
            if q:
                c += q.val
                q = q.next
            anode = ListNode(val=c % 10)
            c = c // 10
            r.next = anode
            r = r.next
        return res.next


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


l1 = createLLFromList([2, 4, 3])
l2 = createLLFromList([5, 6, 4])
printList(l1)
printList(l2)
s = Solution()
head1 = s.addTwoNumbers(l1, l2)
printList(head1)

l1 = createLLFromList([0])
l2 = createLLFromList([0])
printList(l1)
printList(l2)
s = Solution()
head1 = s.addTwoNumbers(l1, l2)
printList(head1)

l1 = createLLFromList([9, 9, 9, 9, 9, 9, 9])
l2 = createLLFromList([9, 9, 9, 9])
printList(l1)
printList(l2)
s = Solution()
head1 = s.addTwoNumbers(l1, l2)
printList(head1)

# Version 1
# res, r, p, q, c = None, None, l1, l2, 0
# while p is not None or q is not None:
#    a = p.val if p is not None else 0
#    b = q.val if q is not None else 0
#    s = a + b + c
#    c = s // 10
#    s = s % 10
#    p = p.next if p is not None else p
#    q = q.next if q is not None else q
#    anode = ListNode(val=s)
#    if res is None:
#        res = anode
#        r = anode
#    else:
#        r.next = anode
#        r = r.next
# if c == 0:
#    pass
# else:
#    anode = ListNode(val=c)
#    r.next = anode
# return res
