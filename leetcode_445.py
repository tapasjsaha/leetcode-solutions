# Add Two Numbers II

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
    def addTwoNumbers(self, l1: [], l2: []) -> []:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        # print(s1, s2)

        head = None
        carry = 0
        while True:
            n1 = s1.pop() if s1 else 0
            n2 = s2.pop() if s2 else 0
            total = n1 + n2 + carry
            if total == 0 and not s1 and not s2:
                break
            else:
                carry = total // 10
                total = total % 10
                node = ListNode(val=total, next=head)
                head = node

        if head is None:
            head = ListNode()

        return head


l1 = createLLFromList([2, 4, 3])
l2 = createLLFromList([9, 6, 4])
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

l1 = createLLFromList([6, 4, 5, 0, 4, 4, 9, 4, 1])
l2 = createLLFromList([3, 8, 8, 0, 3, 0, 1, 4, 8])
printList(l1)
printList(l2)
s = Solution()
head1 = s.addTwoNumbers(l1, l2)
printList(head1)
