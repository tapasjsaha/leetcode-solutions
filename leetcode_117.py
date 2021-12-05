# Populating Next Right Pointers in Each Node II
"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            prev = None
            for i in range(len(queue)):
                node = queue.pop(0)
                node.next = prev
                prev = node
                queue.append(node.right)
                queue.append(node.left)
        return root




#        if not root:
#            return root
#
#        current = root
#        while current.left or current.right:
#            temp = current
#            while current:
#                if current.left:
#                    if current.right:
#                        current.left.next = current.right
#                    elif current.next and current.next.left:
#                        current.left.next = current.next.left
#                    elif current.next and current.next.right:
#                        current.left.next = current.next.right
#                    else:
#                        current.left.next = None
#                if current.right:
#                    if current.next and current.next.left:
#                        current.right.next = current.next.left
#                    elif current.next and current.next.right:
#                        current.right.next = current.next.right
#                    else:
#                        current.right.next = None
#                current = current.next
#            current = temp.left if temp.left else temp.right
#        return root




