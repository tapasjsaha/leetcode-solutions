# Balanced Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        self.balanced = True

        def dfs(node):
            if not node:
                return 0
            elif not node.left and not node.right:
                return 1
            else:
                l = dfs(node.left)
                r = dfs(node.right)
                diff = abs(l - r)
                hight = max(l, r)
                if diff > 1:
                    self.balanced = False
                return hight + 1

        rootBalanced = dfs(root)

        return self.balanced