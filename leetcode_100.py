# Same Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: [], q: []) -> bool:
        def helper(x, y):
            if x is None and y is None:
                return True
            elif p is not None and q is not None:
                if x.val == y.val and helper(x.left, y.left) and helper(x.right, y.right):
                    return True
                else:
                    return False
            else:
                return False

        return helper(p, q)

