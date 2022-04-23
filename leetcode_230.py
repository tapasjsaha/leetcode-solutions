# Kth Smallest Element in a BST
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        res = []

        def inorder(node):
            if k > len(res):
                if node.left:
                    inorder(node.left)
                res.append(node.val)
                if node.right:
                    inorder(node.right)
            else:
                return

        inorder(root)
        return res[k-1]


a = TreeNode(val=1)
b = TreeNode(val=2,left=a)
c = TreeNode(val=4)
d = TreeNode(val=3, left=b, right=c)
e = TreeNode(val=6)
root = TreeNode(val=5, left=d, right=e)

s = Solution()
print(s.kthSmallest(root, k=2))


