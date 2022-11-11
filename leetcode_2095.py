# Delete the Middle Node of a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: []) -> []:
        fast = head
        l = 0
        while fast:
            l += 1
            fast = fast.next

        mid = l // 2
        if mid == 0:
            head = None
        else:
            fast = head
            l = 0
            while l < mid - 1:
                l += 1
                fast = fast.next

            fast.next = fast.next.next

        return head

