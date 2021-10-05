# Binary Tree Level Order Traversal

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


class Solution:
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


T = TreeNode()
root = T.buildFromList([3, 9, 20, 'null', 'null', 15, 7])
s = Solution()
print(s.levelOrder(root))

T = TreeNode()
root = T.buildFromList([])
s = Solution()
print(s.levelOrder(root))

T = TreeNode()
root = T.buildFromList([1])
s = Solution()
print(s.levelOrder(root))

T = TreeNode()
root = T.buildFromList([1, 2, 3, 4, 5, 6, 7, 8, 9])
s = Solution()
print(s.levelOrder(root))
