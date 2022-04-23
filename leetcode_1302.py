# Deepest Leaves Sum

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
    def deepestLeavesSum(self, root: [TreeNode]) -> int:
        self.maxDepth = -1
        self.maxDepthNodes = []

        def helper(node, depth):
            if node:
                if depth < self.maxDepth:
                    helper(node.left, depth + 1)
                    helper(node.right, depth + 1)
                elif depth == self.maxDepth:
                    self.maxDepthNodes.append(node.val)
                    helper(node.left, depth + 1)
                    helper(node.right, depth + 1)
                else:
                    self.maxDepth = depth
                    self.maxDepthNodes = [node.val]
                    helper(node.left, depth + 1)
                    helper(node.right, depth + 1)

        helper(root, 0)
        return sum(self.maxDepthNodes)


tree = TreeNode()
root = tree.buildFromList([1, 2, 3, 'null', 'null', 4, 5])
#print(root)
s = Solution()
print(s.deepestLeavesSum(root))

tree = TreeNode()
root = tree.buildFromList([1, 2, 3, 4, 5, 'null', 6, 7, 'null', 'null', 'null', 'null', 8])
#print(root)
s = Solution()
print(s.deepestLeavesSum(root))

root = tree.buildFromList([6, 7, 8, 2, 7, 1, 3, 9, 'null', 1, 4, 'null', 'null', 'null', 5])
print(s.deepestLeavesSum(root))

root = tree.buildFromList([])
print(s.deepestLeavesSum(root))

root = tree.buildFromList([6])
print(s.deepestLeavesSum(root))
