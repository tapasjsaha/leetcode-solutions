# Reorder List
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
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """ Determine the midpoint of the list"""
        fast, slow, l1_end = head, head, head
        head2 = None
        count = 1
        while fast.next:
            count += 1
            l1_end = slow
            slow = slow.next
            fast = fast.next
            if fast.next:
                count += 1
                fast = fast.next

        """If list is more than 2 elements end the first half of the list 
           and reverse second half of the list"""
        if count > 2:
            l1_end.next = None
            head2 = slow
            if head2.next is None:
                pass
            else:
                nf, ns = head2.next, None
                while head2.next:
                    head2.next = ns
                    ns = head2
                    head2 = nf
                    nf = nf.next
                head2.next = ns

        """If second list is not empty, start merger of the two lists into the first one"""
        if head2:
            head1 = head
            while head1 and head2:
                temp1, temp2 = head1.next, head2.next
                head1.next = head2
                head2.next = temp1
                if temp1 and temp2:
                    head1, head2 = temp1, temp2
                else:
                    head1, head2.next = temp1, temp2
        return None



head = createLLFromList([1, 2, 3, 4, 5, 6, 7])
printList(head)
s = Solution()
s.reorderList(head)
printList(head)


print("---------------------------")
head = createLLFromList([1, 2, 3, 4, 5, 6, 7, 8])
printList(head)
s = Solution()
s.reorderList(head)
printList(head)

print("---------------------------")
head = createLLFromList([10])
printList(head)
s = Solution()
s.reorderList(head)
printList(head)

print("---------------------------")
head = createLLFromList([1, 2])
printList(head)
s = Solution()
s.reorderList(head)
printList(head)

print("---------------------------")
head = createLLFromList([1, 2, 3])
printList(head)
s = Solution()
s.reorderList(head)
printList(head)
