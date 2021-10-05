# Remove Duplicates from Sorted List II
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
        root = ListNode(val=None, next=head)
        slow = root
        fast = head.next if head else None  # slow and fast should be two nodes apart
        curr_val = head.val if head else None
        remove_flag = False
        while fast:
            if fast.val != curr_val and not remove_flag:
                curr_val = fast.val
                slow = slow.next
            elif fast.val == curr_val:
                remove_flag = True
            else:
                remove_flag = False
                curr_val = fast.val
                slow.next = fast
            fast = fast.next

        if remove_flag:               # if last node is duplicate
            slow.next = fast

        return root.next


head = createLLFromList([1, 2, 3, 3, 4, 4, 5])
printList(head)
s = Solution()
head1 = s.deleteDuplicates(head)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([1, 1, 1, 2, 3, 3, 4, 4, 5])
printList(head)
s = Solution()
head1 = s.deleteDuplicates(head)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([1, 2, 3, 3, 4, 4, 5, 6, 6])
printList(head)
s = Solution()
head1 = s.deleteDuplicates(head)
printList(head1) if head1 is not None else print("List is empty")

head = createLLFromList([])
printList(head)
s = Solution()
head1 = s.deleteDuplicates(head)
printList(head1) if head1 is not None else print("List is empty")