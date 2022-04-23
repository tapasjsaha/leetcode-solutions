# Reverse Nodes in k-Group
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


# Reverse Nodes in k-Group
class Solution:
    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:

        def helper(node):
            pointer = ListNode(val=None, next=node)
            counter = 0
            for i in range(k):
                if pointer.next:
                    pointer = pointer.next
                    counter += 1
                else:
                    break
            if counter == k:
                res_node = reverseList(node, helper(pointer.next))
                return res_node
            else:
                return node

        def reverseList(head, next_part):
            prev, curr = next_part, head
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        if not head:
            return None
        elif k == 1:
            return head
        else:
            dummy_head = ListNode(next=helper(head))
            return dummy_head.next


head = createLLFromList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
printList(head)
s = Solution()
head1 = s.reverseKGroup(head, k=5)
printList(head1) if head1 is not None else print("List is empty")


head = createLLFromList([1, 2, 3])
printList(head)
s = Solution()
head1 = s.reverseKGroup(head, k=4)
printList(head1) if head1 is not None else print("List is empty")