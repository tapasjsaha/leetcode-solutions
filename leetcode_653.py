# Two Sum IV - Input is a BST

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


# Two Sum IV - Input is a BST
class Solution:
    def findTarget(self, root: [TreeNode], k: int) -> bool:
        def inOrder(node: [TreeNode], valueSet):
            res = []
            if not node:
                return False
            elif k - node.val in valueSet:
                return True
            else:
                valueSet.add(node.val)
                return inOrder(node.left, valueSet) or inOrder(node.right, valueSet)
        return inOrder(root, set())


T = TreeNode()
root = T.buildFromList([5, 3, 6, 2, 4, 'null', 7])
s = Solution()
print(s.findTarget(root, k=11))
print(s.findTarget(root, k=9))

T = TreeNode()
root = T.buildFromList([5, 3, 6, 2, 4, 'null', 7])
s = Solution()
print(s.findTarget(root, k=28))

T = TreeNode()
root = T.buildFromList([2, 1, 3])
s = Solution()
print(s.findTarget(root, k=4))

T = TreeNode()
root = T.buildFromList([2, 1, 3])
s = Solution()
print(s.findTarget(root, k=1))

T = TreeNode()
root = T.buildFromList([2, 1, 3])
s = Solution()
print(s.findTarget(root, k=3))
