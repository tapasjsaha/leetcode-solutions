# Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: [int]) -> [TreeNode]:
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(val=nums[0])
        else:
            mid = len(nums) // 2
            tr = TreeNode(val=nums[mid], left=self.sortedArrayToBST(nums[:mid]),
                            right=self.sortedArrayToBST(nums[mid + 1:]))
            return tr

    def levelOrder(self, root: [TreeNode]) -> [[int]]:
        res = []
        if root:
            stack = [root]
            while stack:
                level = []
                for i in range(len(stack)):
                    node = stack.pop(0)
                    if node:
                        level.append(node.val)
                        if node.left:
                            stack.append(node.left)
                        if node.right:
                            stack.append(node.right)
                res.append(level)
        return res

s = Solution()
tr = s.sortedArrayToBST(nums=[-10, -3, 0, 5, 9])
print(s.levelOrder(tr))
