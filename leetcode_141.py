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


def createCyclicLLFromList(lst, pos):
    if lst:
        anode = ListNode(val=lst[0])
        head = anode
        now = 0
        p = head
        for l in lst[1:]:
            if now == pos:
                temp = anode
            else:
                now += 1
            anode = ListNode(val=l)
            p.next = anode
            p = p.next
        p.next = temp
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
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        else:
            slow = fast = head
            while fast.next is not None:
                slow = slow.next
                fast = fast.next
                if fast.next:
                    fast = fast.next
                else:  # Already reached the end
                    return False
                if slow == fast:
                    return True
            return False


head = createLLFromList([1, 2])
printList(head)
s = Solution()
print(s.hasCycle(head))

head = createLLFromList([1, 2, 3, 4, 5, 6, 7])
printList(head)
s = Solution()
print(s.hasCycle(head))

head = createCyclicLLFromList([1, 2, 3, 4, 5, 6, 7], 2)
# printList(head)
s = Solution()
print(s.hasCycle(head))
