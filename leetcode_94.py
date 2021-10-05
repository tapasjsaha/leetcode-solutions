# Binary Tree Inorder Traversal

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


# Binary Tree Inorder Traversal
class Solution:
    # # Recursive method
    # def inorderTraversal(self, root: [TreeNode]) -> [int]:
    #     res = []
    #     if root is None:
    #         return res
    #     else:
    #         lft = self.inorderTraversal(root.left)
    #         rgt = self.inorderTraversal(root.right)
    #         res.extend(lft)
    #         res.append(root.val)
    #         res.extend(rgt)
    #         return res

    def inorderTraversal(self, root: [TreeNode]) -> [int]:
        # Iterative method
        res = []
        if root is None:
            return res
        else:
            stack = []
            current = root
            while current or stack:
                if current and current.left:
                    stack.append(current)
                    current = current.left
                elif current:
                    res.append(current.val)
                    if current.right:
                        current = current.right
                    else:
                        current = None
                elif stack:
                    current = stack.pop()
                    res.append(current.val)
                    current = current.right
        return res


T = TreeNode()
root = T.buildFromList([2, 3, 'null', 1])
s = Solution()
print(s.inorderTraversal(root))

T = TreeNode()
root = T.buildFromList([1, 2, 3, 4, 5, 6, 7, 'null', 9])
s = Solution()
print(s.inorderTraversal(root))

T = TreeNode()
root = T.buildFromList([1, 'null', 2, 3])
s = Solution()
print(s.inorderTraversal(root))

T = TreeNode()
root = T.buildFromList([])
s = Solution()
print(s.inorderTraversal(root))

T = TreeNode()
root = T.buildFromList([1])
s = Solution()
print(s.inorderTraversal(root))

T = TreeNode()
root = T.buildFromList([1, 2])
s = Solution()
print(s.inorderTraversal(root))

T = TreeNode()
root = T.buildFromList([1, 'null', 2])
s = Solution()
print(s.inorderTraversal(root))
