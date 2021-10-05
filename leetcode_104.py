# Maximum Depth of Binary Tree

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


# Maximum Depth of Binary Tree
class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        # Recursive method
        if not root:
            return 0
        else:
            lh = self.maxDepth(root.left)
            rh = self.maxDepth(root.right)
            return 1 + max(lh, rh)

    #def maxDepth(self, root: [TreeNode]) -> int:
    #    # Iterative method
    #    level = 0
    #    if root:
    #        queue = [root]
    #        while queue:
    #            level += 1
    #            for i in range(len(queue)):
    #                node = queue.pop(0)
    #                if node.left:
    #                    queue.append(node.left)
    #                if node.right:
    #                    queue.append(node.right)
    #    return level


T = TreeNode()
root = T.buildFromList([3, 9, 20, 'null', 'null', 15, 7])
s = Solution()
print(s.maxDepth(root))

T = TreeNode()
root = T.buildFromList([1, 'null', 2])
s = Solution()
print(s.maxDepth(root))

T = TreeNode()
root = T.buildFromList([])
s = Solution()
print(s.maxDepth(root))

T = TreeNode()
root = T.buildFromList([0])
s = Solution()
print(s.maxDepth(root))

T = TreeNode()
root = T.buildFromList([1, 2, 3, 4, 5, 6, 7, 'null', 9])
s = Solution()
print(s.maxDepth(root))
