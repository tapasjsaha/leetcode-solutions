# Subtree of Another Tree

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


# Subtree of Another Tree
class Solution:
    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        def isEqualtree(root: [TreeNode], subRoot: [TreeNode]):
            if not root and not subRoot:
                return True
            elif not root and subRoot:
                return False
            elif root and not subRoot:
                return False
            elif root.val == subRoot.val and isEqualtree(root.left, subRoot.left) and isEqualtree(root.right, subRoot.right):
                return True
            else:
                return False

        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root and not subRoot:
            return False
        elif root.val == subRoot.val:
            if isEqualtree(root.left, subRoot.left) and isEqualtree(root.right, subRoot.right):
                return True
            else:
                if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
                    return True
                else:
                    return False
        else:
            if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
                return True
            else:
                return False


T = TreeNode()
root = T.buildFromList([3, 4, 5, 1, 2])
subRoot = T.buildFromList([4, 1, 2])
s = Solution()
print(s.isSubtree(root, subRoot))
