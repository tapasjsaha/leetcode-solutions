# N-ary Tree Level Order Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> [[int]]:
        res = []
        queue = [root] if root else None
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.children:
                    queue.extend(node.children)
            res.append(level)

        return res
