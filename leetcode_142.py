# Linked List Cycle II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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

# Floyed's algorithm

class Solution:
    def detectCycle(self, head: []) -> []:
        if head is None:
            return None
        else:
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    break
            if not fast or not fast.next:
                return None
            # Once cycle is detected start again from head. both the pointers will meet at starting of the cycle
            if slow == fast:
                while head != fast:
                    fast = fast.next
                    head = head.next
                return head


head = createLLFromList([1, 2])
printList(head)
s = Solution()
print(s.detectCycle(head))

head = createLLFromList([1, 2, 3, 4, 5, 6, 7])
printList(head)
s = Solution()
print(s.detectCycle(head))

head = createCyclicLLFromList([1, 2, 3, 4, 5, 6, 7], 2)
# printList(head)
s = Solution()
print(s.detectCycle(head))
