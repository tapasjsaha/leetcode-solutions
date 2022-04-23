# Construct Binary Tree from Preorder and Inorder Traversal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> [TreeNode]:
        if not preorder or not inorder:
            return None
        elif len(preorder) == 1:
            return TreeNode(val=preorder[0])
        else:
            root_val = preorder[0]
            root_indx = inorder.index(root_val)
            inorder_left = inorder[:root_indx]
            inorder_right = inorder[root_indx + 1:]
            preorder_left = preorder[1:len(inorder_left) + 1]
            preorder_right = preorder[len(inorder_left) + 1:]
            tr = TreeNode(val=root_val, left=self.buildTree(preorder_left, inorder_left),
                          right=self.buildTree(preorder_right, inorder_right))
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
tr = s.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
print(s.levelOrder(tr))
