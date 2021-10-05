# Binary Tree Preorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def buildFromList(self, lst):  # [1,null,2,3]
        if not lst:
            return None
        else:
            val = lst.pop(0)
            root = TreeNode(val)
            queue = [root]
            while lst and queue:
                node = queue.pop(0)
                val = lst.pop(0)
                if val != 'null':
                    anode = TreeNode(val)
                    node.left = anode
                    queue.append(anode)
                else:
                    node.left = None
                if lst:
                    val = lst.pop(0)
                    if val != 'null':
                        anode = TreeNode(val)
                        node.right = anode
                        queue.append(anode)
                    else:
                        node.right = None
            return root

# Binary Tree Preorder Traversal
class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> [int]:
        # Iterative method
        res = []
        if root is None:
            return res
        else:
            stack = [root]
            while stack:
                current = stack.pop()
                res.append(current.val)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
            return res

    # def preorderTraversal(self, root: [TreeNode]) -> [int]:
    #     # Recursive method
    #     res = []
    #     if root is None:
    #         return res
    #     else:
    #         lft = self.preorderTraversal(root.left)
    #         rgt = self.preorderTraversal(root.right)
    #         res.append(root.val)
    #         res.extend(lft)
    #         res.extend(rgt)
    #         return res


T = TreeNode()
root = T.buildFromList([1, 'null', 2, 3])
s = Solution()
print(s.preorderTraversal(root))

T = TreeNode()
root = T.buildFromList([])
s = Solution()
print(s.preorderTraversal(root))

T = TreeNode()
root = T.buildFromList([1])
s = Solution()
print(s.preorderTraversal(root))

T = TreeNode()
root = T.buildFromList([1, 2])
s = Solution()
print(s.preorderTraversal(root))

T = TreeNode()
root = T.buildFromList([1, 'null', 2])
s = Solution()
print(s.preorderTraversal(root))
