# Sum of Left Leaves
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
    def sumOfLeftLeaves(self, root: [TreeNode]) -> int:
        self.total = 0

        def helper(node, flag):
            if node:
                if node.left or node.right:
                    helper(node.left, True)
                    helper(node.right, False)
                elif flag:
                    self.total += node.val

        helper(root, False)
        return self.total



tree = TreeNode()
s = Solution()
root = tree.buildFromList([3, 9, 20, 'null', 'null', 15, 7])
print(s.sumOfLeftLeaves(root))

root = tree.buildFromList([1])
print(s.sumOfLeftLeaves(root))
