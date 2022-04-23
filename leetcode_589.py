# N-ary Tree Preorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root) -> [int]:
        self.res = []

        def dfs(node):
            if not node:
                return
            else:
                self.res.append(node.val)
                for child in node.children:
                    dfs(child)

        dfs(root)
        return self.res

    # Accepted solution
    # def preorder(self, root) -> [int]:
    #     res = []
    #     if not root:
    #         return res
    #     else:
    #         stack = [root]
    #         while stack:
    #             node = stack.pop()
    #             res.append(node.val)
    #             for n in node.children[::-1]:
    #                 stack.append(n)
    #     return res
