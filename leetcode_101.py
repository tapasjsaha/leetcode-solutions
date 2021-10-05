# Symmetric Tree

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


# Symmetric Tree
class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        def compare(root1: [TreeNode], root2: [TreeNode]):
            if not root1 and not root2:
                return True
            elif root1 and root2 and (root1.val == root2.val) and compare(root1.right, root2.left) and compare(root1.left, root2.right):
                return True
            else:
                return False

        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        elif compare(root.right, root.left):
            return True
        else:
            return False


T = TreeNode()
root = T.buildFromList([1, 2, 2, 3, 4, 4, 3])
s = Solution()
print(s.isSymmetric(root))

T = TreeNode()
root = T.buildFromList([1, 2, 2, 'null', 3, 'null', 3])
s = Solution()
print(s.isSymmetric(root))

T = TreeNode()
root = T.buildFromList([1, 2, 2, 2, 'null', 2])
s = Solution()
print(s.isSymmetric(root))
