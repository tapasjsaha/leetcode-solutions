# Maximum Twin Sum of a Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: []) -> int:
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        stack = []
        node = head
        ans, i = 0, 1
        while i <= n // 2:
            stack.append(node.val)
            node = node.next
            i += 1

        while i <= n:
            x = stack.pop()
            x += node.val
            ans = max(ans, x)
            node = node.next
            i += 1

        return ans


head = ListNode(val=1)
head.next = ListNode(val=100000)
s = Solution()
print(s.pairSum(head))
